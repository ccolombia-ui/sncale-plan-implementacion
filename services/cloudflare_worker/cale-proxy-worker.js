/**
 * Cloudflare Worker - Proxy Seguro para Google Sheets
 *
 * Este worker actúa como proxy entre el frontend y Google Sheets API,
 * manteniendo las credenciales del Service Account seguras.
 *
 * Deploy en: https://workers.cloudflare.com/
 */

// ============================================================================
// CONFIGURACIÓN - REEMPLAZAR CON TUS VALORES
// ============================================================================

const SERVICE_ACCOUNT = {
  // Copiar de tu archivo JSON del service account
  client_email: "TU_SERVICE_ACCOUNT_EMAIL@proyecto.iam.gserviceaccount.com",

  // Copiar TODO el private_key del JSON (incluir BEGIN y END)
  private_key: `-----BEGIN PRIVATE KEY-----
TU_PRIVATE_KEY_AQUI_MULTIPLES_LINEAS
-----END PRIVATE KEY-----`
};

const SPREADSHEET_ID = "1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU";

// Configuración de hojas
const SHEETS_CONFIG = {
  nodos: {
    range: "'197 Nodos'!A2:Z198",
    columns: {
      centro_id: 0,
      tipo_centro: 1,
      codigo_dane: 2,
      municipio: 3,
      departamento: 4,
      latitud: 5,
      longitud: 6,
      categoria_cale: 7,
      demanda_estimada_anual: 8,
      padre_jerarquico: 22,
      distancia_padre_km: 23,
      nivel_jerarquico: 24
    }
  },
  municipios: {
    range: "'Asignación Municipal 1122'!A2:J1123",
    columns: {
      codigo_dane: 0,
      municipio: 1,
      departamento: 2,
      latitud: 3,
      longitud: 4,
      nodo_cale_id: 5,
      nodo_cale_municipio: 6,
      nodo_cale_categoria: 7,
      distancia_km: 8,
      metodo: 9
    }
  }
};

// ============================================================================
// MANEJADOR PRINCIPAL
// ============================================================================

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  // Headers CORS para permitir acceso desde cualquier dominio
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };

  // Manejar preflight OPTIONS
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      headers: corsHeaders
    });
  }

  // Solo permitir GET
  if (request.method !== 'GET') {
    return new Response('Method not allowed', {
      status: 405,
      headers: corsHeaders
    });
  }

  try {
    const url = new URL(request.url);
    const sheet = url.searchParams.get('sheet') || 'nodos';

    // Validar parámetro sheet
    if (!SHEETS_CONFIG[sheet]) {
      return jsonResponse(
        { error: 'Invalid sheet parameter. Use: nodos or municipios' },
        400,
        corsHeaders
      );
    }

    // Obtener token de acceso
    const token = await getAccessToken();

    // Llamar a Google Sheets API
    const data = await fetchSheetData(token, SHEETS_CONFIG[sheet].range);

    // Parsear datos según el tipo de hoja
    const parsed = parseSheetData(data.values, SHEETS_CONFIG[sheet].columns, sheet);

    // Retornar datos con caché
    return jsonResponse(
      {
        sheet: sheet,
        range: SHEETS_CONFIG[sheet].range,
        count: parsed.length,
        data: parsed,
        timestamp: new Date().toISOString()
      },
      200,
      {
        ...corsHeaders,
        'Cache-Control': 'public, max-age=3600', // Cache 1 hora
        'CDN-Cache-Control': 'max-age=3600'
      }
    );

  } catch (error) {
    console.error('Error:', error);

    return jsonResponse(
      {
        error: error.message,
        timestamp: new Date().toISOString()
      },
      500,
      corsHeaders
    );
  }
}

// ============================================================================
// FUNCIONES DE GOOGLE SHEETS API
// ============================================================================

async function fetchSheetData(token, range) {
  const apiUrl = `https://sheets.googleapis.com/v4/spreadsheets/${SPREADSHEET_ID}/values/${encodeURIComponent(range)}`;

  const response = await fetch(apiUrl, {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Accept': 'application/json'
    }
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Google Sheets API error: ${response.status} - ${error}`);
  }

  return response.json();
}

function parseSheetData(rows, columns, sheetType) {
  if (!rows || rows.length === 0) {
    return [];
  }

  return rows.map(row => {
    const obj = {};

    for (const [key, index] of Object.entries(columns)) {
      const value = row[index] || '';

      // Convertir tipos según necesidad
      if (key.includes('latitud') || key.includes('longitud')) {
        obj[key] = parseFloat(value.replace(',', '.')) || 0;
      } else if (key.includes('distancia') || key === 'demanda_estimada_anual') {
        obj[key] = parseFloat(value) || 0;
      } else {
        obj[key] = value;
      }
    }

    return obj;
  });
}

// ============================================================================
// AUTENTICACIÓN CON SERVICE ACCOUNT
// ============================================================================

async function getAccessToken() {
  // Crear JWT
  const jwt = await createJWT();

  // Intercambiar JWT por access token
  const tokenResponse = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams({
      grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
      assertion: jwt
    })
  });

  if (!tokenResponse.ok) {
    const error = await tokenResponse.text();
    throw new Error(`Token exchange failed: ${error}`);
  }

  const tokenData = await tokenResponse.json();
  return tokenData.access_token;
}

async function createJWT() {
  const now = Math.floor(Date.now() / 1000);

  // Header
  const header = {
    alg: 'RS256',
    typ: 'JWT'
  };

  // Payload
  const payload = {
    iss: SERVICE_ACCOUNT.client_email,
    scope: 'https://www.googleapis.com/auth/spreadsheets.readonly',
    aud: 'https://oauth2.googleapis.com/token',
    exp: now + 3600,
    iat: now
  };

  const headerB64 = base64UrlEncode(JSON.stringify(header));
  const payloadB64 = base64UrlEncode(JSON.stringify(payload));
  const signatureInput = `${headerB64}.${payloadB64}`;

  // Importar clave privada
  const key = await importPrivateKey(SERVICE_ACCOUNT.private_key);

  // Firmar
  const signature = await crypto.subtle.sign(
    'RSASSA-PKCS1-v1_5',
    key,
    stringToArrayBuffer(signatureInput)
  );

  const signatureB64 = base64UrlEncode(signature);

  return `${signatureInput}.${signatureB64}`;
}

async function importPrivateKey(pem) {
  // Limpiar PEM
  const pemContents = pem
    .replace(/-----BEGIN PRIVATE KEY-----/, '')
    .replace(/-----END PRIVATE KEY-----/, '')
    .replace(/\s/g, '');

  // Decodificar base64
  const binaryDer = atob(pemContents);
  const bytes = new Uint8Array(binaryDer.length);
  for (let i = 0; i < binaryDer.length; i++) {
    bytes[i] = binaryDer.charCodeAt(i);
  }

  // Importar como CryptoKey
  return crypto.subtle.importKey(
    'pkcs8',
    bytes.buffer,
    {
      name: 'RSASSA-PKCS1-v1_5',
      hash: 'SHA-256'
    },
    false,
    ['sign']
  );
}

// ============================================================================
// UTILIDADES
// ============================================================================

function base64UrlEncode(data) {
  let base64;

  if (typeof data === 'string') {
    base64 = btoa(data);
  } else if (data instanceof ArrayBuffer) {
    const bytes = new Uint8Array(data);
    let binary = '';
    for (let i = 0; i < bytes.length; i++) {
      binary += String.fromCharCode(bytes[i]);
    }
    base64 = btoa(binary);
  } else {
    throw new Error('Invalid data type for base64 encoding');
  }

  return base64
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=/g, '');
}

function stringToArrayBuffer(str) {
  const buffer = new ArrayBuffer(str.length);
  const view = new Uint8Array(buffer);
  for (let i = 0; i < str.length; i++) {
    view[i] = str.charCodeAt(i);
  }
  return buffer;
}

function jsonResponse(data, status = 200, additionalHeaders = {}) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      'Content-Type': 'application/json',
      ...additionalHeaders
    }
  });
}

// ============================================================================
// HEALTH CHECK
// ============================================================================

// Endpoint para verificar que el worker está funcionando
// Acceder a: https://tu-worker.workers.dev/?health
addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  if (url.searchParams.has('health')) {
    event.respondWith(new Response(JSON.stringify({
      status: 'healthy',
      timestamp: new Date().toISOString(),
      sheets_available: Object.keys(SHEETS_CONFIG)
    }), {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    }));
  }
});
