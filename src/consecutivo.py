import csv
from pathlib import Path

archivo = Path("data/recibos.csv")

if archivo.exists():
    with open(archivo, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
        ultimo = max(int(r['consecutivo']) for r in rows)
else:
    ultimo = 0

nuevo_consecutivo = ultimo + 1
print("Nuevo consecutivo:", nuevo_consecutivo)
