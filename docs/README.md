# Índice de documentación y referencias

Este índice distingue cuatro capas relacionadas, no intercambiables: el flujo universitario personal (Checklist y documento operativo), el procedimiento visual UX con su prompt autónomo, las referencias/plantilla ODD de handoff y el tracking operacional `odd/`. La guía visual complementa el flujo personal; no sustituye requisitos, la Checklist v4 ni el briefing de una HU.

## Mapa de fuentes

| Ruta | Qué contiene y para qué sirve |
|---|---|
| [Flujo Operativo Personal (PDF)](flujo-operativo/rendered/flujo-operativo-proyectos-universitarios-alex.pdf) | Explicación completa de la adaptación personal: análisis, Sprint 0, UX, preparación de HU, handoff, ejecución ODD y trazabilidad. |
| [Fuente LaTeX editable](flujo-operativo/flujo-operativo-proyectos-universitarios-alex.tex) | Fuente del PDF; conserva el contenido y la atribución del autor. |
| [Icono original del complemento](flujo-operativo/assets/gpt-icon.jpg) | Recurso de portada incluido con autorización expresa del autor. |
| [Checklist Maestra Universal v4](flujo-operativo/referencias/checklist-maestra-universal-proyectos-universitarios-v4.md) | Cobertura para comprender el problema, documentar necesidades, definir requisitos, planificar y verificar proyectos universitarios; referencia upstream preservada. |
| [Ciclo personal de referencias visuales UX](ux/flujo-referencias-visuales.md) | Procedimiento canónico: propuesta UX Pilot → PNG → mejora contextual de ChatGPT → reconstrucción editable y aprobación humana → pantallas coherentes; refinamiento posterior opcional. |
| [Plantilla autónoma para ChatGPT](ux/plantilla-chatgpt-mejora-referencias-visuales.md) | Prompt copiable para pedir el PNG mejorado y declarar con honestidad el acceso real a GitHub, documentación y assets; no reemplaza la guía visual. |
| [Plantilla del ODD Briefing Generator](flujo-operativo/referencias/plantilla-maestra-odd-briefing-generator.md) | Estructura la intención, las fuentes y las restricciones antes de entregar una HU a Pi; no fija el plan técnico del repositorio. |
| [Vistas previas y PDF generado](flujo-operativo/rendered/) | [PDF (30 páginas)](flujo-operativo/rendered/flujo-operativo-proyectos-universitarios-alex.pdf), [portada PNG](flujo-operativo/rendered/portada.png), [diagrama general (página física 9)](flujo-operativo/rendered/diagrama-flujo-operativo-pagina-09.png) y [ciclo UX (página física 13)](flujo-operativo/rendered/diagrama-ciclo-referencias-visuales-pagina-13.png). |
| [Guía de renderizado](RENDERING.md) | Herramientas, comando reproducible, selección de página y límites de la generación. |
| [Renderer](../scripts/render_document.py) | Implementación Python estándar que compila y prepara los cuatro entregables: PDF, portada y ambas vistas de diagramas. |

## Referencias Gentle AI v4

Los cinco documentos de esta carpeta explican conceptos y ejemplos de referencia; no describen la práctica personal completa de Alex.

| Documento | Uso de lectura |
|---|---|
| [00 — System Instructions](referencias/gentle-ai-v4/00-gpt-system-instructions.md) | Rol y límites del complemento que prepara el ODD Execution Brief. |
| [01 — ODD Methodology](referencias/gentle-ai-v4/01-gentle-ai-odd-methodology.md) | Modelo de responsabilidades y flujo conceptual de Organic Driven Development. |
| [02 — ODD Conventions and Standards](referencias/gentle-ai-v4/02-odd-conventions-and-standards.md) | Criterios para redactar handoffs claros, acotados y basados en evidencia. |
| [03 — ODD Briefing Example](referencias/gentle-ai-v4/03-odd-briefing-example.md) | Ejemplo extendido de una HU vertical; no es un plan universal ni una tarea de este repositorio. |
| [04 — ODD Feature Document Reference](referencias/gentle-ai-v4/04-odd-feature-document-reference.md) | Diferencia entre el brief previo y el ledger operativo que Pi puede mantener si el trabajo es sustancial. |

## Rutas rápidas

- **Entender el flujo personal:** [README del repositorio](../README.md) y [PDF operativo](flujo-operativo/rendered/flujo-operativo-proyectos-universitarios-alex.pdf), en especial las secciones 4, 8–10 y 12–16.
- **Preparar la referencia visual:** [guía UX](ux/flujo-referencias-visuales.md) → [prompt autónomo de ChatGPT](ux/plantilla-chatgpt-mejora-referencias-visuales.md) → reconstrucción editable y aprobación en UX Pilot/Figma → vínculo/versionado en la HU.
- **Preparar una HU para Pi:** [Checklist v4](flujo-operativo/referencias/checklist-maestra-universal-proyectos-universitarios-v4.md) → [plantilla ODD](flujo-operativo/referencias/plantilla-maestra-odd-briefing-generator.md) → referencias [01](referencias/gentle-ai-v4/01-gentle-ai-odd-methodology.md) y [02](referencias/gentle-ai-v4/02-odd-conventions-and-standards.md). La referencia visual complementa la HU y no autoriza funciones.
- **Distinguir briefing y tracking:** referencia [04](referencias/gentle-ai-v4/04-odd-feature-document-reference.md). El directorio `odd/` corresponde al seguimiento de ejecución cuando se utiliza; no reemplaza requisitos, HU, arquitectura ni evidencia permanente.
- **Reconstruir los renders:** [guía de renderizado](RENDERING.md).

La autorización expresa para publicar el nombre completo del autor y el icono original del complemento no establece por sí sola una licencia general sobre estos u otros materiales. Se preserva la atribución; la inclusión de referencias no implica afiliación ni aval oficial de Gentle AI o de sus autores.
