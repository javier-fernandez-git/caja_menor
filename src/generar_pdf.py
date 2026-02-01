from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from recibo import cargar_movimientos, total_recibo, total_en_letras
import csv

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('recibo.html')

with open('data/recibos.csv', newline='', encoding='utf-8') as f:
    recibo = list(csv.DictReader(f))[0]

movimientos = cargar_movimientos()

html_render = template.render(
    **recibo,
    movimientos=movimientos,
    total=total_recibo(movimientos),
    total_letras=total_en_letras(movimientos)
)

HTML(string=html_render).write_pdf('output/recibos/recibo_5.pdf')
