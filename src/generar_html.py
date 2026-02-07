from datetime import date

html_base = open("templates/recibo.html", encoding="utf-8").read()

filas = """
<tr>
  <td>1</td>
  <td>10/02/2026</td>
  <td>GASTOS MENORES</td>
  <td>DEL 03/09/2025 AL 03/09/2025</td>
  <td>1</td>
  <td>$79.000</td>
</tr>
"""

html_final = html_base \
    .replace("{{ consecutivo }}", "1") \
    .replace("{{ fecha }}", str(date.today())) \
    .replace("{{ centro_costos }}", "DIFICIL") \
    .replace("{{ filas }}", filas)

with open("output/recibo.html", "w", encoding="utf-8") as f:
    f.write(html_final)

print("HTML generado correctamente")

