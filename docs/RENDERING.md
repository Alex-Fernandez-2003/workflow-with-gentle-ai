# Renderizar el documento

El PDF se genera desde la fuente LaTeX incluida; las imágenes del README son PNG independientes porque GitHub no inserta un PDF enlazado como vista previa.

## Requisitos

- Python 3.10 o posterior (el renderer usa únicamente la biblioteca estándar).
- `pdflatex`, `pdftotext` y `pdftoppm` disponibles en `PATH`.

El script comprueba estas herramientas y se detiene con un mensaje claro si falta alguna. No instala herramientas ni dependencias.

## Comandos

Desde la raíz del repositorio:

```bash
python scripts/render_document.py --help
python scripts/render_document.py --output-dir docs/flujo-operativo/rendered
```

El segundo es el comando canónico de reconstrucción y reemplaza los entregables con los mismos nombres que enlaza el README. Para verificar sin tocar las vistas previas revisadas, pasa un directorio temporal nuevo a `--output-dir`. Una ruta relativa de salida se resuelve desde el directorio actual; la fuente LaTeX, en cambio, se localiza respecto al script.

## Qué hace y qué publica

1. Compila con `pdflatex` al menos tres veces y hasta que `.aux`, `.toc` y `.out` se estabilicen, con un máximo de seis pasadas. Una referencia sin resolver o referencias que no se estabilizan detienen el proceso.
2. Extrae el texto del PDF con `pdftotext` y localiza la página que contiene el título y los marcadores del diagrama. No presupone que el diagrama seguirá en la página 8.
3. Renderiza la portada y esa página con `pdftoppm`. Comprueba las firmas PDF/PNG antes de publicar.
4. Mantiene los auxiliares y la preparación en el directorio temporal del sistema. Copia sólo un PDF y dos PNG cuando todas las etapas terminan; no guarda logs en el repositorio.

Nombres actuales:

- `flujo-operativo-proyectos-universitarios-alex.pdf`
- `portada.png`
- `diagrama-flujo-operativo-pagina-08.png` (el número corresponde a la página física detectada en esta versión)

Si la fuente mueve el diagrama, la salida incluirá el nuevo número físico. Actualiza entonces el enlace de vista previa del README; el script no borra automáticamente imágenes numeradas antiguas. El ajuste de ancla de página incluido en la fuente distingue la portada del índice y evita destinos PDF duplicados; no cambia el contenido del flujo.

Un fallo de compilación, selección o renderizado ocurre antes de copiar los entregables, así que no deja salidas nuevas parciales. Los avisos no fatales de LaTeX de la última pasada se muestran en terminal; no se conserva un registro de compilación.
