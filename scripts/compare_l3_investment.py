#!/usr/bin/env python3
"""
Compute per-instance unitarios for L3 configurations by summing component totals
and compare against user-provided investment table and L5 reference.

Outputs:
 - output/compare_l3_investment.csv
 - output/compare_l3_investment.md (mermaid table)
"""
import json
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
TABLA_L3 = ROOT / 'TABLAS_L3_OFICIALES.json'
TABLA_L5 = ROOT.parent / 'TABLAS_L5_RESUMEN_NACIONAL.json'
OUT = ROOT / 'output'
OUT.mkdir(exist_ok=True)

if not TABLA_L3.exists():
    print('ERROR: TABLAS_L3_OFICIALES.json not found at', TABLA_L3)
    raise SystemExit(1)

with open(TABLA_L3, 'r', encoding='utf-8') as f:
    l3 = json.load(f)

# load L5 reference if available
l5 = {}
if TABLA_L5.exists():
    with open(TABLA_L5, 'r', encoding='utf-8') as f:
        l5 = json.load(f)

# user-provided table (from your message) - unitarios and totals
user_table = {
    'CALE.n_1+': {
        'qty': 3,
        'unit_usuario': 22876959265,
        'total_usuario': 68630877795
    },
    'CALE.n_1': {
        'qty': 17,
        'unit_usuario': 17311999565,
        'total_usuario': 294303992605
    },
    'CALE.n_2**': {
        'qty': 16,
        'unit_usuario': 22087585297,
        'total_usuario': 353401364752
    },
    'CALE.n_2': {
        'qty': 4,
        'unit_usuario': 11206265897,
        'total_usuario': 44825063588
    },
    'CALE.n_3': {
        'qty': 16,
        'unit_usuario': 5641306197,
        'total_usuario': 90260899152
    }
}

def compute_unit_from_components(config):
    # compute per-base unitario by summing component.valor_total_cop / cantidad_base
    components = config.get('components', [])
    qty_base = config.get('cantidad_base', 0)
    qty_var = config.get('cantidad_variante', 0)

    unit_base = 0
    unit_var = 0
    for c in components:
        vt = c.get('valor_total_cop', 0) or 0
        cb = c.get('cantidad_base', 0) or 0
        cv = c.get('cantidad_variante', 0) or 0
        # if valor_total_cop seems to be total for base counts, allocate per base
        if cb and qty_base:
            unit_base += vt / qty_base
        elif cv and qty_var:
            unit_var += vt / qty_var
        else:
            # fallback: use valor_unitario_cop as per-instance contribution
            unit_base += c.get('valor_unitario_cop', 0) or 0
    return unit_base, unit_var

rows = []
for cfg in l3.get('configuraciones', []):
    title = cfg.get('titulo')
    nivel = cfg.get('nivel')
    # map nivel to category label used by user
    # simple mapping heuristics
    label = None
    if 'cale_n1' in nivel:
        # distinguish variant plus
        if cfg.get('cantidad_variante', 0):
            label = 'CALE.n_1+'
        else:
            label = 'CALE.n_1'
    elif 'cale_n2' in nivel:
        # decide between n2** and n2
        if cfg.get('cantidad_variante', 0) >= 16:
            label = 'CALE.n_2**'
        else:
            label = 'CALE.n_2'
    elif 'cale_n3' in nivel:
        label = 'CALE.n_3'
    else:
        label = nivel

    unit_base, unit_var = compute_unit_from_components(cfg)
    # fallback to valorizacion total if available
    val = cfg.get('valorizacion', {})
    total_cop = val.get('total_cop', 0) or 0
    qty_base = cfg.get('cantidad_base') or 0
    qty_var = cfg.get('cantidad_variante') or 0
    per_base_from_total = (total_cop / qty_base) if qty_base else 0

    # prefer per_base_from_total if present
    unit_official = per_base_from_total or unit_base

    rows.append({
        'label': label,
        'titulo': title,
        'qty_base': qty_base,
        'qty_var': qty_var,
        'unit_official': int(unit_official),
        'unit_base_calc': int(unit_base),
        'unit_var_calc': int(unit_var),
    })

# aggregate and compare to user table
csv_path = OUT / 'compare_l3_investment.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.writer(cf)
    writer.writerow(['Categoria','Qty','Unitario_L3_oficial','Total_L3_oficial','Unitario_usuario','Total_usuario','Delta_usuario_vs_L3'])
    for r in rows:
        cat = r['label']
        qty = user_table.get(cat, {}).get('qty', r['qty_base'] or r['qty_var'])
        unit_l3 = r['unit_official']
        total_l3 = int(unit_l3 * qty)
        u_user = user_table.get(cat, {}).get('unit_usuario', '')
        t_user = user_table.get(cat, {}).get('total_usuario', '')
        delta = ''
        if isinstance(t_user, int) or isinstance(t_user, float):
            delta = int(t_user - total_l3)
        writer.writerow([cat, qty, unit_l3, total_l3, u_user, t_user, delta])

# write mermaid md
md_path = OUT / 'compare_l3_investment.md'
with open(md_path, 'w', encoding='utf-8') as mf:
    mf.write('# Compare L3 investment\n\n')
    mf.write('```mermaid\n')
    mf.write('table\n')
    mf.write('  "Categoría" | "Qty" | "Unit_L3_oficial" | "Total_L3_oficial" | "Unit_usuario" | "Total_usuario" | "Delta_vs_L3"\n')
    for r in rows:
        cat = r['label']
        qty = user_table.get(cat, {}).get('qty', r['qty_base'] or r['qty_var'])
        unit_l3 = r['unit_official']
        total_l3 = int(unit_l3 * qty)
        u_user = user_table.get(cat, {}).get('unit_usuario', '')
        t_user = user_table.get(cat, {}).get('total_usuario', '')
        delta = ''
        if isinstance(t_user, int) or isinstance(t_user, float):
            delta = int(t_user - total_l3)
        # format numbers safely (u_user/t_user may be empty)
        def fmt(x):
            try:
                return f"{int(x):,}"
            except Exception:
                return str(x)
        mf.write('  "{}" | "{}" | "{}" | "{}" | "{}" | "{}" | "{}"\n'.format(
            cat, qty, fmt(unit_l3), fmt(total_l3), fmt(u_user), fmt(t_user), fmt(delta)
        ))
    mf.write('```\n')

print('Wrote', csv_path, md_path)
