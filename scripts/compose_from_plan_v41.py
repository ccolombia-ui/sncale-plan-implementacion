#!/usr/bin/env python3
"""
Compose per-CALE unitarios using Plan v4.1 key numbers and L5 satellite unitarios.
Produces output/compose_plan_v41.csv and output/compose_plan_v41.md (mermaid table).

Assumptions:
 - Satellite mix per CALE default: 2 C2, 2 C3, 2 C4, 1 C5 (7 total)
 - CALE-P class totals taken from Plan v4.1 text
 - CALE-T unitarios taken from Plan v4.1
"""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output'
OUT.mkdir(exist_ok=True)

# Plan v4.1 extracted key numbers (COP)
plan = {
    'CALE_T_24q': 243_063_465,
    'CALE_T_16q': 200_646_497,
    # CALE-P class totals (as in Plan v4.1)
    'CALE_P_Clase_I_total': 10_335_549_700,
    'CALE_P_Clase_II_total': 14_406_319_700,
    'CALE_P_Clase_III_total': 6_063_316_700,
    # Sala form especializada
    'sala_form_24q': 45_000_000,
    'sala_form_16q': 30_000_000,
}

# L5 satellite unitarios: corrected per-user note.
# Estas infraestructuras ya están contempladas dentro de CALE-T (243...)
# y además hay ~12 millones COP atribuibles por cada satélite C2..C5.
sat_unit = {
    'C2': 12_000_000,
    'C3': 12_000_000,
    'C4': 12_000_000,
    'C5': 12_000_000,
}

# default satellite mix per CALE (7 total)
sat_mix = { 'C2':2, 'C3':2, 'C4':2, 'C5':1 }

# Behaviour flags - toggle to exclude these OPEX items from ficha comparisons
EXCLUDE_SOFTWARE_RRHH = True
EXCLUDE_ARRENDAMIENTO = True

# Path to L3 tables (we will read opex values per CALE config)
L3_PATH = ROOT / 'TABLAS_L3_CALE_TEORICO.json'
# Optional path to USCO docx (can be outside repo). If present, script will try to extract
# numeric references for USCO per configuration. If not present, USCO column stays empty.
DOCX_USCO_PATH = Path(r"C:\raziel\aktriel\01__min_transporte\02__uscocalemania\draft_3\uscocalemania__v4.docx")

def extract_usco_from_docx(path: Path):
    """Try to extract USCO values for 24q/16q/4q from a Word document.
    Returns a dict like {'24q': value, '16q': value, '4q': value} when found, empty otherwise.
    This function is best-effort: it searches paragraphs for keywords and numbers.
    Requires python-docx (pip install python-docx). If not available or file missing, returns {}.
    """
    res = {}
    try:
        if not path.exists():
            return res
        try:
            import docx
        except Exception:
            # python-docx not installed
            return res
        doc = docx.Document(str(path))
        text = '\n'.join(p.text for p in doc.paragraphs)
        # Candidate patterns: lines mentioning 24q/16q/4q or '24 cubículos' etc.
        patterns = {
            '24q': r'(?i)(24q|24 cub[ií]culos|24 cubiculos)[^\n\d]*([\d\.,]+)',
            '16q': r'(?i)(16q|16 cub[ií]culos|16 cubiculos)[^\n\d]*([\d\.,]+)',
            '4q':  r'(?i)(4q|4 cub[ií]culos|4 cubiculos)[^\n\d]*([\d\.,]+)'
        }
        for k,pat in patterns.items():
            m = re.search(pat, text)
            if m:
                num = m.group(2)
                # normalize number: remove dots/commas and parse
                n = int(re.sub(r'[\.,]', '', num))
                res[k] = n
        # Fallback: find currency-like numbers near 'USCO'
        if not res:
            for m in re.finditer(r'(?i)USCO[^\d\n]*([\d\.,]+)', text):
                num = m.group(1)
                n = int(re.sub(r'[\.,]', '', num))
                # assign to a generic key if not specific
                res.setdefault('usco_generic', n)
    except Exception:
        return {}
    return res

def read_l3_opex():
    """Return a dict with per-config opex sums to optionally exclude.
    Keys: '24q', '16q', '4q' -> total opex to exclude (software+rrhh+arrendamiento if present)
    """
    opex = {'24q':0, '16q':0, '4q':0}
    try:
        with open(L3_PATH, 'r', encoding='utf-8') as lf:
            d = json.load(lf)
        # support both English and Spanish keys
        comps = d.get('components') or d.get('componentes') or {}
        for comp in comps.values():
            codigo = comp.get('codigo','')
            if '24q' in codigo:
                key = '24q'
            elif '16q' in codigo:
                key = '16q'
            elif '4q' in codigo:
                key = '4q'
            else:
                continue
            subtotal = 0
            od = comp.get('opex_detallado', {})
            if EXCLUDE_SOFTWARE_RRHH:
                subtotal += od.get('software', {}).get('total_anual', 0)
                subtotal += od.get('rrhh', {}).get('total_anual', 0)
            if EXCLUDE_ARRENDAMIENTO:
                arr = od.get('servicios', {}).get('arrendamiento', {})
                subtotal += arr.get('costo_anual_cop', 0)
            opex[key] = int(subtotal)
    except Exception:
        # if anything fails, return zeros so behaviour is conservative
        pass
    return opex

L3_OPEX_EXCLUDE = read_l3_opex()

# user-provided rows (from your supplied table)
user = {
    'CALE.n_1+': { 'qty':3, 'unit_usuario': 22_876_959_265, 'total_usuario': 68_630_877_795 },
    'CALE.n_1':  { 'qty':17,'unit_usuario': 17_311_999_565, 'total_usuario': 294_303_992_605 },
    'CALE.n_2**':{ 'qty':16,'unit_usuario': 22_087_585_297, 'total_usuario': 353_401_364_752 },
    'CALE.n_2':  { 'qty':4, 'unit_usuario': 11_206_265_897, 'total_usuario': 44_825_063_588 },
    'CALE.n_3':  { 'qty':16,'unit_usuario': 5_641_306_197, 'total_usuario': 90_260_899_152 }
}

def sat_sum(mix):
    return sum(sat_unit[k]*v for k,v in mix.items())

sat_total = sat_sum(sat_mix)

results = []

# Compute per-config unitarios, optionally excluding opex items read from L3
# CALE.n_1 (24q)
deduct_24q = L3_OPEX_EXCLUDE.get('24q', 0)
unit_n1 = plan['CALE_P_Clase_I_total'] + plan['CALE_T_24q'] + sat_total - deduct_24q
results.append(('CALE.n_1', 17, int(unit_n1), int(unit_n1*17)))

# CALE.n_2** (16q, larger bucket)
deduct_16q = L3_OPEX_EXCLUDE.get('16q', 0)
unit_n2_star = plan['CALE_P_Clase_II_total'] + plan['CALE_T_16q'] + sat_total - deduct_16q
results.append(('CALE.n_2**', 16, int(unit_n2_star), int(unit_n2_star*16)))

# CALE.n_2 (smaller count) - assume half satellite impact (integer)
half_sat = sat_total // 2
unit_n2 = plan['CALE_P_Clase_II_total'] + plan['CALE_T_16q'] + half_sat - deduct_16q
results.append(('CALE.n_2', 4, int(unit_n2), int(unit_n2*4)))

# CALE.n_1+ = CALE.n_1 + CALE.n_2 (unitarios summed)
unit_n1_plus = unit_n1 + unit_n2
results.append(('CALE.n_1+', 3, int(unit_n1_plus), int(unit_n1_plus*3)))

# CALE.n_3 (use Clase III + CALE-T-16q)
unit_n3 = plan['CALE_P_Clase_III_total'] + plan['CALE_T_16q'] - deduct_16q
results.append(('CALE.n_3', 16, int(unit_n3), int(unit_n3*16)))

# write CSV
csv_path = OUT / 'compose_plan_v41.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
    w = csv.writer(cf)
    w.writerow(['Categoria','Qty','Unitario_compuesto','Total_compuesto','Unit_usuario','Total_usuario','Delta_usuario_vs_compuesto'])
    for cat,qty,unit,total in results:
        u_user = user.get(cat, {}).get('unit_usuario','')
        t_user = user.get(cat, {}).get('total_usuario','')
        delta = ''
        if isinstance(t_user, int):
            delta = t_user - total
        w.writerow([cat, qty, unit, total, u_user, t_user, delta])

# write mermaid md
md_path = OUT / 'compose_plan_v41.md'
with open(md_path, 'w', encoding='utf-8') as mf:
    mf.write('# Composed units from Plan v4.1\n\n')
    mf.write('```mermaid\n')
    mf.write('table\n')
    mf.write('  "Categoria" | "Qty" | "Unit_compuesto" | "Total_compuesto" | "Unit_usuario" | "Total_usuario" | "Delta_vs_compuesto"\n')
    for cat,qty,unit,total in results:
        u_user = user.get(cat, {}).get('unit_usuario','')
        t_user = user.get(cat, {}).get('total_usuario','')
        delta = ''
        if isinstance(t_user, int):
            delta = t_user - total
        # Excluir software y talento humano de las fichas: estos rubros se usan
        # exclusivamente desde Anexo A (OPEX). Si las fichas contienen esos
        # unitarios, deben restarse antes de comparar con Anexo A.
        mf.write(f'  "{cat}" | "{qty}" | "{unit:,}" | "{total:,}" | "{u_user:,}" | "{t_user:,}" | "{delta:,}"\n')
    mf.write('```\n')

print('Wrote', csv_path, md_path)

# ---- Generar Anexo A (OPEX consolidado por configuración L3)
anexo_path = OUT / 'anexo_a_opex.csv'
def generate_anexo_a():
    rows = []
    try:
        with open(L3_PATH, 'r', encoding='utf-8') as lf:
            d = json.load(lf)
        comps = d.get('components') or d.get('componentes') or {}
        for comp in comps.values():
            codigo = comp.get('codigo', '')
            # map config to plan values
            if '24q' in codigo:
                plan_val = plan['CALE_P_Clase_I_total'] + plan['CALE_T_24q']
            elif '16q' in codigo:
                plan_val = plan['CALE_P_Clase_II_total'] + plan['CALE_T_16q']
            elif '4q' in codigo:
                plan_val = plan['CALE_P_Clase_III_total'] + plan['CALE_T_16q']
            else:
                continue

            ficha_opex_anual = comp.get('valor_total_opex_anual') or comp.get('resumen_financiero', {}).get('opex_anual_total') or 0

            # usco: not available in repo; leave empty for manual fill
            usco_val = ''

            # tthh_anexoA (mensual) from rrhh total_anual
            rrhh_anual = comp.get('opex_detallado', {}).get('rrhh', {}).get('total_anual', 0)
            tthh_mensual = int(rrhh_anual // 12) if rrhh_anual else 0

            # platec_anexoA (mensual) from software total_anual
            software_anual = comp.get('opex_detallado', {}).get('software', {}).get('total_anual', 0)
            platec_mensual = int(software_anual // 12) if software_anual else 0

            rows.append((codigo, int(ficha_opex_anual), int(plan_val), usco_val, tthh_mensual, platec_mensual))
    except Exception:
        pass

    with open(anexo_path, 'w', newline='', encoding='utf-8') as af:
        w = csv.writer(af)
        w.writerow(['tipo_cale_l3','ficha_actual_opex_anual','plan.41_valor','usco','tthh_anexoA_mensual','platec_anexoA_mensual'])
        for r in rows:
            w.writerow(r)

generate_anexo_a()
print('Wrote', anexo_path)
