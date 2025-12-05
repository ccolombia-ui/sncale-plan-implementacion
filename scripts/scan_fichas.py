#!/usr/bin/env python3
"""
Scan local ficha HTML files and compare extracted financial fields against L5 unitary totals.
Outputs:
 - output/scan_fichas_report.csv : per-file extraction
 - output/scan_fichas_summary.md : mermaid summary and aggregated stats

Run from repo root: python scripts\scan_fichas.py
"""
import re
import json
import os
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
TABLA_L5 = ROOT / 'TABLAS_L5_RESUMEN_NACIONAL.json'
OUTDIR = ROOT / 'output'
OUTDIR.mkdir(exist_ok=True)

SEARCH_DIRS = [
    ROOT / 'fichas_l5',
    ROOT / 'output' / 'fichas_html',
    ROOT / 'output' / 'fichas_cale_teorico',
]
# also include mirrored output folders in parent workspace (c:\guezarel\output)
ALT_OUT = ROOT.parent / 'output'
if ALT_OUT.exists():
    SEARCH_DIRS.append(ALT_OUT / 'fichas_html')
    SEARCH_DIRS.append(ALT_OUT / 'fichas_cale_teorico')


NUM_RE = re.compile(r"([\d\.,]{3,})")
FIELD_PATTERNS = {
    'capex': re.compile(r'capex[^\d\n\r]{0,30}([\d\.,]+)', re.I),
    'opex_anual': re.compile(r'opex[^a-zA-Z0-9\n\r]{0,40}anual[^\d\n\r]{0,30}([\d\.,]+)', re.I),
    'opex_mes': re.compile(r'opex[^\d\n\r]{0,30}mes[^\d\n\r]{0,30}([\d\.,]+)', re.I),
    'opex_any': re.compile(r'opex[^\d\n\r]{0,30}([\d\.,]+)\s*(?:anual|year|/año|/año)?', re.I),
    'capacidad_anual': re.compile(r'(?:capacidad|evaluaciones)[^\d\n\r]{0,40}(?:anual|anuales)?[^\d\n\r]{0,30}([\d\.,]+)', re.I),
}

def parse_number(s: str):
    if not s:
        return None
    s2 = s.strip().replace('.', '').replace(',', '')
    try:
        return int(s2)
    except Exception:
        try:
            return float(s2)
        except Exception:
            return None

def extract_fields(text: str):
    res = {}
    for name, pat in FIELD_PATTERNS.items():
        m = pat.search(text)
        if m:
            num = parse_number(m.group(1))
            res[name] = num
    # normalize: prefer explicit opex_anual, fallback to opex_any
    if 'opex_anual' not in res and 'opex_any' in res:
        res['opex_anual'] = res['opex_any']
    return res

def find_html_files():
    files = []
    for d in SEARCH_DIRS:
        if d.exists():
            for p in d.rglob('*.html'):
                files.append(p)
    return sorted(files)

def load_l5():
    # try primary location
    if TABLA_L5.exists():
        with open(TABLA_L5, 'r', encoding='utf-8') as f:
            return json.load(f)
    # fallback: try parent workspace folder (c:\guezarel)
    alt = ROOT.parent / 'TABLAS_L5_RESUMEN_NACIONAL.json'
    if alt.exists():
        print('INFO: loading L5 from', alt)
        with open(alt, 'r', encoding='utf-8') as f:
            return json.load(f)
    print('WARNING: TABLAS_L5_RESUMEN_NACIONAL.json not found at', TABLA_L5, 'or', alt)
    return {}

def main():
    l5 = load_l5()
    files = find_html_files()
    print(f'Found {len(files)} HTML fichas to scan')

    report_rows = []
    totals = {'capex_found':0, 'opex_anual_found':0, 'files_with_zero':0, 'files_missing':0}

    for p in files:
        txt = p.read_text(encoding='utf-8', errors='ignore')
        fields = extract_fields(txt)
        capex = fields.get('capex')
        opex = fields.get('opex_anual') or fields.get('opex_mes')
        capacidad = fields.get('capacidad_anual')

        missing = []
        if capex is None:
            missing.append('capex')
        if opex is None:
            missing.append('opex')
        if capacidad is None:
            missing.append('capacidad')

        zeros = []
        if capex == 0:
            zeros.append('capex')
        if opex == 0:
            zeros.append('opex')

        if zeros:
            totals['files_with_zero'] += 1
        if missing:
            totals['files_missing'] += 1

        try:
            file_ref = str(p.relative_to(ROOT))
        except Exception:
            file_ref = str(p)
        report_rows.append({
            'file': file_ref,
            'capex': capex or '',
            'opex_anual': opex or '',
            'capacidad_anual': capacidad or '',
            'zeros': ';'.join(zeros),
            'missing': ';'.join(missing)
        })

        if capex:
            try:
                totals['capex_found'] += int(capex)
            except Exception:
                pass
        if opex:
            try:
                totals['opex_anual_found'] += int(opex)
            except Exception:
                pass

    # write CSV
    csv_path = OUTDIR / 'scan_fichas_report.csv'
    with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
        writer = csv.DictWriter(cf, fieldnames=['file','capex','opex_anual','capacidad_anual','zeros','missing'])
        writer.writeheader()
        for r in report_rows:
            writer.writerow(r)

    # prepare mermaid summary
    md_path = OUTDIR / 'scan_fichas_summary.md'
    with open(md_path, 'w', encoding='utf-8') as mf:
        mf.write('# Scan fichas summary\n\n')
        mf.write('## Totals\n\n')
        mf.write(f'- Files scanned: {len(files)}\n')
        mf.write(f'- Files with zero fields: {totals["files_with_zero"]}\n')
        mf.write(f'- Files with missing fields: {totals["files_missing"]}\n')
        mf.write(f'- CAPEX found (sum of parsed values): {totals["capex_found"]:,}\n')
        mf.write(f'- OPEX anual found (sum of parsed values): {totals["opex_anual_found"]:,}\n')
        if l5.get('consolidado_nacional'):
            capex_l5 = l5['consolidado_nacional']['financiero'].get('capex_total_red')
            opex_l5 = l5['consolidado_nacional']['financiero'].get('opex_anual_total_red')
            mf.write(f'- CAPEX L5 (reference): {capex_l5:,}\n')
            mf.write(f'- OPEX anual L5 (reference): {opex_l5:,}\n')

        mf.write('\n## Mermaid table (resumen)\n\n')
        mf.write('```mermaid\n')
        mf.write('table\n')
        mf.write('  "Métrica" | "Valor"\n')
        mf.write(f'  "Files escaneados" | "{len(files)}"\n')
        mf.write(f'  "Files con campos = 0" | "{totals["files_with_zero"]}"\n')
        mf.write(f'  "Files con campos faltantes" | "{totals["files_missing"]}"\n')
        mf.write(f'  "CAPEX parseado (suma)" | "{totals["capex_found"]:,}"\n')
        mf.write(f'  "OPEX anual parseado (suma)" | "{totals["opex_anual_found"]:,}"\n')
        if l5.get('consolidado_nacional'):
            mf.write(f'  "CAPEX L5 (referencia)" | "{capex_l5:,}"\n')
            mf.write(f'  "OPEX anual L5 (referencia)" | "{opex_l5:,}"\n')
            # discrepancy
            disc_capex = ''
            try:
                disc_capex = totals['capex_found'] - int(capex_l5 or 0)
            except Exception:
                disc_capex = ''
            mf.write(f'  "Diferencia CAPEX (parseado - L5)" | "{disc_capex:,}"\n')
        mf.write('```\n')

    print('\nReport written:')
    print(' -', csv_path)
    print(' -', md_path)

if __name__ == '__main__':
    main()
