/**
 * Cloudflare Worker - Proxy Seguro para Google Sheets
 * Sistema BIM CALE
 *
 * ✅ CONFIGURADO CON TUS CREDENCIALES REALES
 *
 * INSTRUCCIONES:
 * 1. Copiar TODO este código
 * 2. Ir a https://workers.cloudflare.com/
 * 3. Crear nuevo worker
 * 4. Pegar este código
 * 5. Save and Deploy
 * 6. Copiar la URL del worker
 */

// ============================================================================
// CONFIGURACIÓN - YA ESTÁ LISTA ✅
// ============================================================================

const SERVICE_ACCOUNT = {
  client_email: "aksobhya-googlesheet-806@aksobhya.iam.gserviceaccount.com",
  private_key: `-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCgdxkW9VCqti2s
3qWONwgjtFTaYdkAsJ8i6v2U4hHwoRd627IznJuCQyO2KNGutrK6cZIIBovEbks3
+pj45quT+1RfFlKEqlsG4038lpw57v7AKwUrZGkG2hvKTffWsHyRGITIC83l1ln/
uhl218hnUggDUOo1XHNjCdfslgAOYCjSosMIOTTT6E50Eiglulf51NXUA121gfpE
N6FdNjER0bJrbZASG4OIkXmEdaxBvc7pBvLlJei5V2x3NwYAZYjj6nKQHEw5eukl
kOc4CsQV/hdprmAVR8Tm2nZWt+H4aDy/6I5ygsyjzhaIsvfl0BrDR02sT6buNyRg
/0UtbU/LAgMBAAECggEAFq8PaGvwZdmQFmZ5D+QerfFxp1d6tjrBnE2M4G2e7J3R
NGh3Rg2G/ECifT9C+QhRtsKUSrcmLfQLhRPTaSgurCI02KZOrvtoF86tOR5PYm8z
KxZJyksM/894az5fYUWcrmRBbQgiKLIHEfwMWn0Bkv2JLXLUUQvLMf5zvDmuM1nS
TX5KCF9Ae/+cn6yDx3pXU3MiVdzTqxMlTQRZI3qFMknOPsDmGGNbVlBPjcHSyoHc
MmZILQOVmT5YOR3dCO359Guv5ge69I0Bjine8VHV5RmuXCrWiwaDakSOsM2SHlp9
rdaQgQ96kqqbvbpJHsBkSkzDWX8T82L5vCKU9aPzgQKBgQDL+eqmjOpAhNeVQIdg
Rh1fl2FbI9q+SDdpCPGqP7R/uaMCbr68xk1pNJ98jqKbnqVf1VykWeloH1T1BJEf
RHbAsdzzgSRzFM/c8qobAc17Qo1d7djILje/kPU1Jgy/RvsPi77DjW8ACC5Dg8L4
evbvqWBxqwAsSWatoPaZwD9LSwKBgQDJZD8KEvX0V+evnmuVykABsErkrBCKUYoq
p91GmsJ8XV0Gp4CPJZO5J2zqElguu8DOWJS5TqGiOJttK2/jwWreSln5T9ThPt1c
/b0qp217suo5ogtfutJVT0O3jqORAOhuCLRjE5xXQ1kE2E98TQFKFehOU6u0GzUK
1DJdP5a9gQKBgEbXSEiJvj2kJV9fpuSn1UHCyHwnyqu1VxEymwPe1ihZ56RLpBDZ
6j60mQNgYlcb1SGgb2lhFLAl2ZKzAFfUpk2sOCmV23vgaYS5/pwclynM5l4N4fE8
I/5zMMZBrcGsvDsc9Kbj8v4W2UJ3e3pi8mov8B/qHMhEwdVhhuPFIfZbAoGAfqnp
KCnivapoEsGdwtkwxp8di5NY19YPA2MOvfBqMBP8hUnmhqHItmRAkTu2cLYvvthh
ueblrATUZKY0OlgVIfg7fJ2kM4L5cRo51tD1AB74SAVOCAiVb4hp+9HfuDyM81/Q
LJxR8WRvYae23mQEUpdSw6jGToHqK4RopNNwuIECgYEAqq8cAA+6BtiHZZ/Nfjnq
IdQV9erhing0GUpFT8lsDMjlV2vxhyYZuLifz+hydfY8+s4PzYLwqOfqz/FauRaS
ArKHzgFlhf9viNEHh+tijrXxkZlT2HrB17LoFvvnj7BA+HloSKvRkIxjpjc3Q61/
zU/DE36mP8CX53xHCXSKxX0=
-----END PRIVATE KEY-----`
};

const SPREADSHEET_ID = "1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU";

// Configuración de hojas
const SHEETS_CONFIG = {
  nodos: {
    range: "'arquitectura_red_cale_nacional'!A2:Z198",
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
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  if (request.method !== 'GET') {
    return new Response('Method not allowed', {
      status: 405,
      headers: corsHeaders
    });
  }

  try {
    const url = new URL(request.url);

    // Health check
    if (url.searchParams.has('health')) {
      return jsonResponse({
        status: 'healthy',
        timestamp: new Date().toISOString(),
        sheets_available: Object.keys(SHEETS_CONFIG),
        service_account: SERVICE_ACCOUNT.client_email
      }, 200, corsHeaders);
    }

    const sheet = url.searchParams.get('sheet') || 'nodos';

    if (!SHEETS_CONFIG[sheet]) {
      return jsonResponse(
        { error: 'Invalid sheet parameter. Use: nodos or municipios' },
        400,
        corsHeaders
      );
    }

    const token = await getAccessToken();
    const data = await fetchSheetData(token, SHEETS_CONFIG[sheet].range);
    const parsed = parseSheetData(data.values, SHEETS_CONFIG[sheet].columns, sheet);

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
        'Cache-Control': 'public, max-age=3600',
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
// GOOGLE SHEETS API
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
// AUTENTICACIÓN
// ============================================================================

async function getAccessToken() {
  const jwt = await createJWT();

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

  const header = {
    alg: 'RS256',
    typ: 'JWT'
  };

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

  const key = await importPrivateKey(SERVICE_ACCOUNT.private_key);

  const signature = await crypto.subtle.sign(
    'RSASSA-PKCS1-v1_5',
    key,
    stringToArrayBuffer(signatureInput)
  );

  const signatureB64 = base64UrlEncode(signature);

  return `${signatureInput}.${signatureB64}`;
}

async function importPrivateKey(pem) {
  const pemContents = pem
    .replace(/-----BEGIN PRIVATE KEY-----/, '')
    .replace(/-----END PRIVATE KEY-----/, '')
    .replace(/\s/g, '');

  const binaryDer = atob(pemContents);
  const bytes = new Uint8Array(binaryDer.length);
  for (let i = 0; i < binaryDer.length; i++) {
    bytes[i] = binaryDer.charCodeAt(i);
  }

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
