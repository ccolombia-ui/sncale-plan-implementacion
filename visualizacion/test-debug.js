const TIPOS_CONFIG = [
    {
        tipo_id: 'L3.CALE.n_1',
        nombre: 'CALE Metropolitano',
        categoria: 'Cat.A+',
        color: '#E63946',
        icono: '🔴',
        cantidad: 20
    }
];

async function test() {
    try {
        const response = await fetch('../data/nodos_completos_mapa.json');
        const data = await response.json();
        
        const NODOS_DATA = data.nodos || {};
        console.log('Total nodos en JSON:', Object.keys(NODOS_DATA).length);
        
        // Buscar por tipo_id exacto
        const nodosTipo = Object.values(NODOS_DATA).filter(n => n.tipo_id === 'L3.CALE.n_1');
        console.log(`Nodos con tipo_id 'L3.CALE.n_1': ${nodosTipo.length}`);
        console.log('Nodos encontrados:', nodosTipo.map(n => `${n.nodo_id}: ${n.nombre}`).join(', '));
        
        // Verificar otros tipos
        const tiposUnicos = [...new Set(Object.values(NODOS_DATA).map(n => n.tipo_id))];
        console.log('Tipos únicos en el JSON:', tiposUnicos);
        
    } catch (error) {
        console.error('Error:', error);
    }
}

test();
