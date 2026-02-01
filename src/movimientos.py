import csv
from datetime import date
from calculos import calcular_total

def registrar_movimiento(obra, item, cantidad, descripciones):
    total = calcular_total(item, cantidad, descripciones)

    with open('data/movimientos.csv', 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([
            date.today(),
            obra,
            item,
            cantidad,
            descripciones[item],
            total
        ])

    return total
