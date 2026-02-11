# Caja Menor

Sistema para gestionar caja menor por obra. Ahora puedes trabajar tanto por línea de comandos como desde una interfaz gráfica ligera para usuarios operativos.

## Novedades destacadas

- ✅ **Interfaz gráfica ligera (GUI)** en `ui/index.html`.
- ✅ **Compatibilidad total con CLI** para usuarios técnicos.
- ✅ Flujo guiado para:
  - registrar movimientos,
  - consultar consecutivo,
  - generar recibo HTML,
  - convertir recibo a PDF,
  - revisar resumen por centro de costos.

## Estructura del proyecto

- `src/`: scripts de la lógica principal.
- `data/`: archivos CSV con la información de movimientos, recibos e ítems.
- `templates/`: plantilla HTML usada para generar el recibo.
- `output/`: archivos generados (HTML/PDF).
- `ui/`: interfaz gráfica de apoyo para operación diaria.

## Requisitos

- Python 3.10+ (o equivalente).
- Dependencias adicionales:
  - `weasyprint` para generar PDF (`src/generar_pdf.py`).
  - `num2text` para convertir totales a letras (`src/recibo.py`).

Instalación de dependencias (ejemplo):

```bash
pip install weasyprint num2text
```

## Datos de entrada

Los scripts leen y escriben en los CSV de `data/`:

- `data/descriciones.cvs`: listado de ítems y valor unitario. Se usa en `src/calculos.py`.
- `data/movimientos.csv`: movimientos registrados (fecha, obra, ítem, cantidad, valor unitario, total).
- `data/recibos.csv`: consecutivo y metadatos del recibo.

Asegúrate de que los encabezados de los CSV coincidan con los que se esperan en cada script.

## Uso por interfaz gráfica (recomendado para usuario final)

1. Abre el archivo `ui/index.html` en tu navegador.
2. Usa el asistente para preparar comandos de registro de movimientos.
3. Ejecuta los comandos desde tu terminal en la raíz del proyecto.
4. Utiliza los botones de “Operaciones rápidas” para copiar comandos frecuentes.

> Nota: la GUI está pensada como panel operativo y no reemplaza la ejecución de Python en terminal.

## Uso por línea de comandos (CLI)

### 1. Calcular totales y registrar movimientos

El módulo `src/movimientos.py` registra un movimiento en `data/movimientos.csv` y retorna el total.
Ejemplo en un script interactivo:

```python
from calculos import cargar_descripciones
from movimientos import registrar_movimiento

descripciones = cargar_descripciones('data/descriciones.cvs')

registro_total = registrar_movimiento(
    obra='OBRA 1',
    item='ALIMENTACION 12000',
    cantidad=2,
    descripciones=descripciones,
)

print(registro_total)
```

### 2. Obtener el consecutivo de recibo

```bash
python src/consecutivo.py
```

El script imprime el próximo consecutivo disponible según `data/recibos.csv`.

### 3. Generar recibo HTML

```bash
python src/generar_html.py
```

Esto crea `output/recibo.html` usando la plantilla `templates/recibo.html`.

### 4. Convertir HTML a PDF

```bash
python src/generar_pdf.py
```

Genera `output/recibo.pdf` a partir del HTML.

### 5. Resumen por centro de costos

```bash
python src/resumen.py
```

Imprime el total agrupado por centro de costos tomando los datos en `data/recibos.csv`
y `data/movimientos.csv`.

## Notas

- Los scripts actuales asumen rutas relativas (ejecuta los comandos desde la raíz del proyecto).
- Revisa los CSV de ejemplo en `data/` para entender los formatos esperados.
- Consulta `CHANGELOG.md` para revisar versiones y cambios recientes.
