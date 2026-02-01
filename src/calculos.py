import csv

def cargar_descripciones(ruta):
    descripciones = {}

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            descripciones[fila['item']] = float(fila['valor_unitario'])

    return descripciones


def calcular_total(item, cantidad, descripciones):
    if item not in descripciones:
        raise ValueError(f"Ítem no registrado: {item}")

    return cantidad * descripciones[item]
