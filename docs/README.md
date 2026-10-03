# Índice de documentación y referencias

Este índice separa la práctica personal descrita en el documento principal, las referencias Gentle AI v4 y el seguimiento operativo de trabajo. Son capas relacionadas, no una única metodología ni fuentes intercambiables.

## Mapa de fuentes

| Ruta | Qué contiene y para qué sirve |
|---|---|
| [Flujo Operativo Personal (PDF)](flujo-operativo/rendered/flujo-operativo-proyectos-universitarios-alex.pdf) | Explicación completa de la adaptación personal: análisis, Sprint 0, UX, preparación de HU, handoff, ejecución ODD y trazabilidad. |
| [Fuente LaTeX editable](flujo-operativo/flujo-operativo-proyectos-universitarios-alex.tex) | Fuente del PDF; conserva el contenido y la atribución del autor. |
| [Icono original del complemento](flujo-operativo/assets/gpt-icon.jpg) | Recurso de portada incluido con autorización expresa del autor. |
| [Checklist Maestra Universal v4](flujo-operativo/referencias/checklist-maestra-universal-proyectos-universitarios-v4.md) | Cobertura para comprender el problema, documentar necesidades, definir requisitos, planificar y verificar proyectos universitarios. |
| [Plantilla del ODD Briefing Generator](flujo-operativo/referencias/plantilla-maestra-odd-briefing-generator.md) | Estructura la intención y las restricciones antes de entregar una HU a Pi; no fija el plan técnico del repositorio. |
| [Vistas previas y PDF generado](flujo-operativo/rendered/) | Entregables visibles del documento: PDF, portada PNG y diagrama PNG. |
| [Guía de renderizado](RENDERING.md) | Herramientas, comando reproducible, selección de página y límites de la generación. |
| [Renderer](../scripts/render_document.py) | Implementación Python estándar que compila y prepara los tres entregables. |

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

- **Entender el flujo personal:** [README del repositorio](../README.md) y PDF, en especial las secciones 4, 8–10 y 12–16.
- **Preparar una HU:** [Checklist](flujo-operativo/referencias/checklist-maestra-universal-proyectos-universitarios-v4.md) → [plantilla](flujo-operativo/referencias/plantilla-maestra-odd-briefing-generator.md) → referencias [01](referencias/gentle-ai-v4/01-gentle-ai-odd-methodology.md) y [02](referencias/gentle-ai-v4/02-odd-conventions-and-standards.md).
- **Distinguir briefing y tracking:** referencia [04](referencias/gentle-ai-v4/04-odd-feature-document-reference.md). El directorio `odd/` corresponde al seguimiento de ejecución cuando se utiliza; no reemplaza requisitos, HU, arquitectura ni evidencia permanente.
- **Reconstruir los renders:** [guía de renderizado](RENDERING.md).

La autorización expresa para publicar el nombre completo del autor y el icono original del complemento no establece por sí sola una licencia general sobre estos u otros materiales. Se preserva la atribución; la inclusión de referencias no implica afiliación ni aval oficial de Gentle AI o de sus autores.
