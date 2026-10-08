# Renderizar el documento

El PDF se genera desde la fuente LaTeX incluida. Las vistas PNG son imágenes independientes porque GitHub no inserta las páginas de un PDF enlazado como vistas previas.

## Requisitos

- Python 3.10 o posterior; el renderer usa únicamente la biblioteca estándar.
- `pdflatex`, `pdftotext` y `pdftoppm` disponibles en `PATH`.

El script comprueba estas herramientas y se detiene con un mensaje claro si falta alguna. No instala herramientas ni dependencias.

## Comandos

Desde la raíz del repositorio:

```bash
python scripts/render_document.py --help
python scripts/render_document.py --output-dir docs/flujo-operativo/rendered
```

El segundo es el comando canónico y reemplaza los cuatro artefactos enlazados por el README. Para verificar sin tocar las vistas previas del repositorio, ejecútalo con un directorio temporal nuevo en `--output-dir`. Las rutas relativas de salida se resuelven desde el directorio actual; la fuente LaTeX se localiza respecto al script.

## Detección y publicación

1. Compila con `pdflatex` al menos tres veces, hasta que `.aux`, `.toc` y `.out` se estabilicen, con un máximo de seis pasadas. Las referencias sin resolver o inestables detienen el proceso.
2. Extrae el texto del PDF con `pdftotext` y detecta por separado las páginas físicas del diagrama general y del ciclo UX. El ciclo UX requiere un conjunto de etiquetas de sus nodos; su encabezado por sí solo en el índice o en una sección textual no cuenta. Cada detector requiere una única página coincidente: una coincidencia ausente o duplicada produce `RenderError`.
3. Renderiza con `pdftoppm` la portada, la página general y la página UX. Comprueba las firmas PDF/PNG y que los cuatro archivos temporales estén completos antes de empezar a copiarlos.
4. Conserva la preparación y los auxiliares en el directorio temporal del sistema. Publica únicamente un PDF y tres PNG; no guarda auxiliares ni logs en el repositorio.

## Artefactos actuales

- PDF: [`flujo-operativo-proyectos-universitarios-alex.pdf`](flujo-operativo/rendered/flujo-operativo-proyectos-universitarios-alex.pdf) (30 páginas físicas).
- Portada: `portada.png`.
- Diagrama general, página física 9: [`diagrama-flujo-operativo-pagina-09.png`](flujo-operativo/rendered/diagrama-flujo-operativo-pagina-09.png).
- Ciclo de referencias visuales UX, página física 13: [`diagrama-ciclo-referencias-visuales-pagina-13.png`](flujo-operativo/rendered/diagrama-ciclo-referencias-visuales-pagina-13.png).

Los nombres de los dos diagramas incluyen la página física detectada y pueden cambiar si cambia la paginación. El renderer no es un validador de enlaces Markdown: no comprueba, reescribe ni repara enlaces del README o de esta guía. Actualiza manualmente las rutas documentadas después de revisar los nuevos artefactos. Tampoco borra automáticamente PNG numerados antiguos; retira una vista obsoleta manualmente sólo después de verificar sus reemplazos y corregir las referencias.

Un fallo de compilación, selección de páginas, renderizado o validación de artefactos ocurre antes de copiar las salidas y no publica archivos nuevos parciales. La copia final no es transaccional ante una interrupción del sistema. Los avisos no fatales de LaTeX de la última pasada se muestran en terminal; no se conserva un registro de compilación.
