/**
 * CALE Data Loader - Carga datos desde Cloudflare Worker Proxy
 * Sistema BIM CALE
 *
 * Este módulo carga datos de nodos y municipios desde un proxy seguro
 * en Cloudflare Workers que usa Service Account authentication.
 */

const CALE_DATA_CONFIG = {
    // URL del Cloudflare Worker Proxy
    PROXY_URL: 'https://cale-proxy.ccolombia.workers.dev',

    // Configuración de cache
    CACHE_TTL: 60 * 60 * 1000, // 1 hora en milisegundos
    CACHE_KEY_NODOS: 'cale_nodos_proxy_v1',
    CACHE_KEY_MUNICIPIOS: 'cale_municipios_proxy_v1',

    // Health check interval (opcional)
    HEALTH_CHECK_INTERVAL: 5 * 60 * 1000 // 5 minutos
};

/**
 * Loader principal para datos CALE
 */
class CALEDataLoader {
    constructor(config = CALE_DATA_CONFIG) {
        this.config = config;
        this.healthStatus = null;
    }

    /**
     * Verifica el health del proxy
     */
    async checkHealth() {
        try {
            const response = await fetch(`${this.config.PROXY_URL}?health`);
            if (!response.ok) {
                throw new Error(`Health check failed: ${response.status}`);
            }

            const health = await response.json();
            this.healthStatus = {
                ...health,
                checked_at: Date.now()
            };

            console.log('✓ Proxy health check:', health);
            return health;

        } catch (error) {
            console.error('❌ Proxy health check failed:', error);
            this.healthStatus = {
                status: 'error',
                error: error.message,
                checked_at: Date.now()
            };
            throw error;
        }
    }

    /**
     * Carga nodos CALE (197 centros)
     * @param {boolean} forceRefresh - Forzar recarga sin cache
     * @returns {Promise<Array>} Array de nodos
     */
    async cargarNodos(forceRefresh = false) {
        try {
            // Intentar cargar desde cache
            if (!forceRefresh) {
                const cached = this._getFromCache(this.config.CACHE_KEY_NODOS);
                if (cached) {
                    console.log(`✓ Nodos cargados desde cache (${cached.length} centros)`);
                    return cached;
                }
            }

            // Cargar desde proxy
            console.log('📥 Cargando nodos desde proxy...');
            const url = `${this.config.PROXY_URL}?sheet=nodos`;
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            const result = await response.json();

            if (result.error) {
                throw new Error(result.error);
            }

            const nodos = result.data;
            console.log(`✓ Cargados ${nodos.length} nodos CALE`);

            // Guardar en cache
            this._saveToCache(this.config.CACHE_KEY_NODOS, nodos);

            return nodos;

        } catch (error) {
            console.error('❌ Error cargando nodos:', error);

            // Intentar fallback a cache expirado
            const cached = localStorage.getItem(this.config.CACHE_KEY_NODOS);
            if (cached) {
                console.warn('⚠️ Usando cache expirado como fallback');
                const { data } = JSON.parse(cached);
                return data;
            }

            throw error;
        }
    }

    /**
     * Carga municipios (1,122 municipios con asignación a nodos)
     * @param {boolean} forceRefresh - Forzar recarga sin cache
     * @returns {Promise<Array>} Array de municipios
     */
    async cargarMunicipios(forceRefresh = false) {
        try {
            // Intentar cargar desde cache
            if (!forceRefresh) {
                const cached = this._getFromCache(this.config.CACHE_KEY_MUNICIPIOS);
                if (cached) {
                    console.log(`✓ Municipios cargados desde cache (${cached.length} municipios)`);
                    return cached;
                }
            }

            // Cargar desde proxy
            console.log('📥 Cargando municipios desde proxy...');
            const url = `${this.config.PROXY_URL}?sheet=municipios`;
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            const result = await response.json();

            if (result.error) {
                throw new Error(result.error);
            }

            const municipios = result.data;
            console.log(`✓ Cargados ${municipios.length} municipios`);

            // Guardar en cache
            this._saveToCache(this.config.CACHE_KEY_MUNICIPIOS, municipios);

            return municipios;

        } catch (error) {
            console.error('❌ Error cargando municipios:', error);

            // Intentar fallback a cache expirado
            const cached = localStorage.getItem(this.config.CACHE_KEY_MUNICIPIOS);
            if (cached) {
                console.warn('⚠️ Usando cache expirado como fallback');
                const { data } = JSON.parse(cached);
                return data;
            }

            throw error;
        }
    }

    /**
     * Limpia el cache
     */
    limpiarCache() {
        localStorage.removeItem(this.config.CACHE_KEY_NODOS);
        localStorage.removeItem(this.config.CACHE_KEY_MUNICIPIOS);
        console.log('✓ Cache limpiado');
    }

    /**
     * Obtiene info del cache
     */
    getCacheInfo() {
        const nodosCache = localStorage.getItem(this.config.CACHE_KEY_NODOS);
        const municipiosCache = localStorage.getItem(this.config.CACHE_KEY_MUNICIPIOS);

        const info = {
            nodos: null,
            municipios: null
        };

        if (nodosCache) {
            const { data, timestamp } = JSON.parse(nodosCache);
            const age = Date.now() - timestamp;
            const timeLeft = this.config.CACHE_TTL - age;
            info.nodos = {
                count: data.length,
                age_ms: age,
                time_left_ms: timeLeft,
                is_valid: timeLeft > 0
            };
        }

        if (municipiosCache) {
            const { data, timestamp } = JSON.parse(municipiosCache);
            const age = Date.now() - timestamp;
            const timeLeft = this.config.CACHE_TTL - age;
            info.municipios = {
                count: data.length,
                age_ms: age,
                time_left_ms: timeLeft,
                is_valid: timeLeft > 0
            };
        }

        return info;
    }

    // ========================================================================
    // Métodos privados
    // ========================================================================

    /**
     * Obtiene datos desde cache si son válidos
     * @private
     */
    _getFromCache(cacheKey) {
        const cached = localStorage.getItem(cacheKey);
        if (!cached) return null;

        try {
            const { data, timestamp } = JSON.parse(cached);
            const age = Date.now() - timestamp;

            if (age < this.config.CACHE_TTL) {
                const timeLeft = this.config.CACHE_TTL - age;
                const secondsLeft = Math.round(timeLeft / 1000);
                console.log(`✓ Cache válido por ${secondsLeft} segundos`);
                return data;
            }

            console.log('⚠️ Cache expirado');
            return null;

        } catch (error) {
            console.error('Error leyendo cache:', error);
            return null;
        }
    }

    /**
     * Guarda datos en cache
     * @private
     */
    _saveToCache(cacheKey, data) {
        try {
            const cacheData = {
                data: data,
                timestamp: Date.now()
            };
            localStorage.setItem(cacheKey, JSON.stringify(cacheData));
            console.log(`✓ Datos guardados en cache (${data.length} items)`);
        } catch (error) {
            console.warn('⚠️ No se pudo guardar en cache:', error);
        }
    }
}

// Exportar para uso en HTML
if (typeof window !== 'undefined') {
    window.CALEDataLoader = CALEDataLoader;
    window.CALE_DATA_CONFIG = CALE_DATA_CONFIG;
}

// Exportar para módulos ES6
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { CALEDataLoader, CALE_DATA_CONFIG };
}
