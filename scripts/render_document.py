"""Build the personal workflow PDF, cover, and two diagram previews."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from collections.abc import Sequence
from pathlib import Path

REQUIRED_TOOLS = ("pdflatex", "pdftotext", "pdftoppm")
MAX_PASSES = 6
MIN_PASSES = 3
PDF_NAME = "flujo-operativo-proyectos-universitarios-alex.pdf"
COVER_NAME = "portada.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


class RenderError(RuntimeError):
    """A required input, tool, or rendering step failed."""


def source_tex_path() -> Path:
    """Return the editable source path, independent of the caller's cwd."""
    return (
        Path(__file__).resolve().parents[1]
        / "docs"
        / "flujo-operativo"
        / "flujo-operativo-proyectos-universitarios-alex.tex"
    )


def missing_tools() -> list[str]:
    return [tool for tool in REQUIRED_TOOLS if shutil.which(tool) is None]


def _fold_text(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    without_marks = "".join(char for char in decomposed if not unicodedata.combining(char))
    return " ".join(without_marks.split())


def workflow_page_number(pages: Sequence[str]) -> int:
    """Find the physical page containing the workflow diagram, not its old page index."""
    markers = (
        "vista general de mi flujo operativo",
        "descubrimiento y documentacion con la checklist maestra v4",
        "pi + gentle shell",
        "maintainer review / entrega",
    )
    matches = [
        index
        for index, page in enumerate(pages, start=1)
        if all(marker in _fold_text(page) for marker in markers)
    ]
    if len(matches) != 1:
        raise RenderError(
            "No se pudo identificar una única página del diagrama en el texto del PDF "
            f"(coincidencias: {matches or 'ninguna'}). Revise los marcadores del documento."
        )
    return matches[0]


def ux_diagram_page_number(pages: Sequence[str]) -> int:
    """Find the UX diagram from its node labels, not its repeated heading or section text."""
    markers = (
        "ux pilot/figma",
        "propuesta",
        "inicial",
        "png inicial",
        "viewport",
        "chatgpt",
        "github + assets",
        "master",
        "editable aprobado",
        "otras",
        "pantallas",
        "hace falta",
        "refinar",
        "referencias aprobadas",
        "hu/brief/evidencia para pi",
    )
    matches = [
        index
        for index, page in enumerate(pages, start=1)
        if all(marker in _fold_text(page) for marker in markers)
    ]
    if len(matches) != 1:
        raise RenderError(
            "No se pudo identificar una única página del diagrama del ciclo UX "
            f"(coincidencias: {matches or 'ninguna'}). Revise los marcadores del documento."
        )
    return matches[0]


def _run(command: Sequence[str], *, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except OSError as error:
        raise RenderError(f"No se pudo ejecutar {command[0]}: {error}") from error
    if result.returncode != 0:
        detail = (result.stdout + "\n" + result.stderr).strip().splitlines()
        excerpt = "\n".join(detail[-16:])
        raise RenderError(
            f"El comando terminó con código {result.returncode}: {' '.join(command)}"
            + (f"\n{excerpt}" if excerpt else "")
        )
    return result


def _auxiliary_state(build_directory: Path, source_stem: str) -> tuple[tuple[str, bytes | None], ...]:
    extensions = (".aux", ".toc", ".out")
    return tuple(
        (
            extension,
            path.read_bytes() if path.is_file() else None,
        )
        for extension in extensions
        for path in (build_directory / f"{source_stem}{extension}",)
    )


def _compile(source: Path, build_directory: Path) -> tuple[Path, int, str]:
    """Compile until auxiliary references are stable, with at least three passes."""
    previous_state = None
    final_output = ""
    for pass_number in range(1, MAX_PASSES + 1):
        result = _run(
            (
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                f"-output-directory={build_directory}",
                source.name,
            ),
            cwd=source.parent,
        )
        final_output = result.stdout + "\n" + result.stderr
        state = _auxiliary_state(build_directory, source.stem)
        if pass_number >= MIN_PASSES and state == previous_state:
            break
        previous_state = state
    else:
        raise RenderError(
            f"Las referencias no se estabilizaron después de {MAX_PASSES} pasadas de pdfLaTeX."
        )

    unresolved = re.search(
        r"(?:undefined references|Reference `[^`]+(?:'|`) undefined|Rerun to get cross-references right)",
        final_output,
        re.IGNORECASE,
    )
    if unresolved:
        raise RenderError(
            "La compilación terminó, pero quedan referencias sin resolver: "
            + unresolved.group(0)
        )
    pdf_path = build_directory / f"{source.stem}.pdf"
    if not pdf_path.is_file() or not pdf_path.read_bytes().startswith(b"%PDF-"):
        raise RenderError("pdfLaTeX no produjo un PDF válido.")
    return pdf_path, pass_number, final_output


def _make_preview(pdf_path: Path, destination_stem: Path, page_number: int) -> Path:
    _run(
        (
            "pdftoppm",
            "-png",
            "-r",
            "160",
            "-f",
            str(page_number),
            "-l",
            str(page_number),
            "-singlefile",
            str(pdf_path),
            str(destination_stem),
        )
    )
    png_path = destination_stem.with_suffix(".png")
    if not png_path.is_file() or not png_path.read_bytes().startswith(PNG_SIGNATURE):
        raise RenderError(f"pdftoppm no produjo una imagen PNG válida para la página {page_number}.")
    return png_path


def _warnings(output: str) -> list[str]:
    return [
        line.strip()
        for line in output.splitlines()
        if "warning" in line.casefold()
        or line.lstrip().startswith(("Underfull \\hbox", "Overfull \\hbox"))
    ]


def render(
    output_directory: Path,
) -> tuple[Path, Path, Path, Path, int, int, int, list[str]]:
    tools = missing_tools()
    if tools:
        raise RenderError(
            "Faltan herramientas requeridas: " + ", ".join(tools)
            + ". Instale/active TeX Live con pdfLaTeX y Poppler (pdftotext, pdftoppm)."
        )

    source = source_tex_path()
    if not source.is_file():
        raise RenderError(f"No se encontró la fuente LaTeX esperada: {source}")
    if not (source.parent / "assets" / "gpt-icon.jpg").is_file():
        raise RenderError("Falta docs/flujo-operativo/assets/gpt-icon.jpg, requerido por la fuente.")

    output_directory = output_directory.expanduser().resolve()
    with tempfile.TemporaryDirectory(prefix="workflow-render-") as temporary_directory:
        temporary_root = Path(temporary_directory)
        build_directory = temporary_root / "build"
        publish_directory = temporary_root / "publish"
        build_directory.mkdir()
        publish_directory.mkdir()

        pdf_path, passes, compile_output = _compile(source, build_directory)
        extracted_text = _run(("pdftotext", "-enc", "UTF-8", "-layout", str(pdf_path), "-")).stdout
        pages = extracted_text.split("\f")
        page_number = workflow_page_number(pages)
        ux_page_number = ux_diagram_page_number(pages)
        shutil.copyfile(pdf_path, publish_directory / PDF_NAME)
        _make_preview(pdf_path, publish_directory / "portada", 1)

        diagram_name = f"diagrama-flujo-operativo-pagina-{page_number:02d}.png"
        _make_preview(
            pdf_path,
            publish_directory / Path(diagram_name).with_suffix(""),
            page_number,
        )
        ux_diagram_name = (
            f"diagrama-ciclo-referencias-visuales-pagina-{ux_page_number:02d}.png"
        )
        _make_preview(
            pdf_path,
            publish_directory / Path(ux_diagram_name).with_suffix(""),
            ux_page_number,
        )

        expected = (PDF_NAME, COVER_NAME, diagram_name, ux_diagram_name)
        if any(not (publish_directory / name).is_file() for name in expected):
            raise RenderError("No se completaron los cuatro artefactos; no se publicaron archivos.")

        output_directory.mkdir(parents=True, exist_ok=True)
        for name in expected:
            shutil.copyfile(publish_directory / name, output_directory / name)

    warnings = _warnings(compile_output)
    return (
        output_directory / PDF_NAME,
        output_directory / COVER_NAME,
        output_directory / diagram_name,
        output_directory / ux_diagram_name,
        page_number,
        ux_page_number,
        passes,
        warnings,
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compila el flujo operativo personal y publica únicamente el PDF, "
            "la portada y las dos páginas de diagramas detectadas en el texto del PDF."
        )
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        metavar="DIRECTORIO",
        help="directorio de salida; los cuatro artefactos con nombres conocidos se reemplazan",
    )
    arguments = parser.parse_args(argv)
    try:
        (
            pdf,
            cover,
            diagram,
            ux_diagram,
            page_number,
            ux_page_number,
            passes,
            warnings,
        ) = render(Path(arguments.output_dir))
    except RenderError as error:
        print(f"Error de renderizado: {error}", file=sys.stderr)
        return 1

    print(f"PDF: {pdf}")
    print(f"Portada: {cover}")
    print(f"Diagrama (página física {page_number}): {diagram}")
    print(f"Ciclo UX (página física {ux_page_number}): {ux_diagram}")
    print(f"Pasadas de pdfLaTeX: {passes} (referencias estables)")
    if warnings:
        print(f"Avisos LaTeX observados en la última pasada: {len(warnings)}")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("Avisos LaTeX: ninguno detectado")
    print("No se publicaron archivos auxiliares ni registros de compilación.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
