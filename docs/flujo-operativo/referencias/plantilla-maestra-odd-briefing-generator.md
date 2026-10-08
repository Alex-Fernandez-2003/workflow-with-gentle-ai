# PLANTILLA MAESTRA DE PROMPT — GENTLE AI ODD BRIEFING GENERATOR

> Esta plantilla está diseñada para preparar un **ODD Execution Brief** detallado antes de entregar una HU, feature, bugfix, refactor, migración o cambio a Pi / Gentle Shell.
>
> ODD es implícito. No hace falta seleccionar un modo.
>
> Puedes eliminar cualquier sección que no aplique. La intención es conservar contexto y rigor, no llenar boilerplate.

---

# 0. INSTRUCCIÓN DE TRABAJO

Quiero que prepares un **ODD Execution Brief pre-ejecución** para Pi / Gentle Shell.

NO implementes código.

NO modifiques archivos.

NO ejecutes tests/builds.

NO inventes detalles del repositorio.

NO predefinas el plan técnico definitivo cuando dependa de inspeccionar el código.

Tu responsabilidad es organizar con precisión:

- intent;
- scope;
- non-goals;
- sources of truth;
- business rules;
- acceptance;
- constraints;
- approved decisions;
- known context;
- material uncertainty;
- verification expectations;
- permanent documentation expectations;
- Git/delivery authorization;
- stop conditions.

Pi será responsable de:

- explorar el repositorio real;
- derivar archivos/símbolos involucrados;
- decidir el diseño técnico compatible con el código actual;
- derivar work units;
- identificar runners/comandos reales;
- decidir si el trabajo es small o substantial;
- crear tracking durable sólo si corresponde;
- implementar;
- verificar con evidencia observada.

---

# 1. PROYECTO

Nombre:

`[NOMBRE DEL PROYECTO]`

Descripción:

`[DESCRIPCIÓN GENERAL]`

Repositorio:

`[URL, SI APLICA]`

Rama canónica esperada:

`[develop | main | otra]`

Tipo:

`[Académico | Personal | Producción | MVP | Investigación | Otro]`

Estado actual relevante:

`[RESUMEN]`

Contexto de entrega:

`[Sprint / HU / demo / feria / producción / mantenimiento / otro]`

---

# 2. IDENTIFICADOR DEL CAMBIO

Tipo:

`[HU | Feature | Bugfix | Refactor | Migration | Maintenance | Documentation | Otro]`

Identificador:

`[HU-XXX / nombre-feature / issue / etc.]`

Nombre:

`[NOMBRE DESCRIPTIVO]`

Una HU completa puede seguir siendo una unidad vertical de trabajo.

No separar automáticamente frontend/backend como features distintas si forman un único resultado funcional.

---

# 3. OBJETIVO

Quiero lograr:

`[RESULTADO PRINCIPAL]`

Resultado final esperado:

`[CÓMO DEBE QUEDAR EL SISTEMA]`

Motivo:

`[POR QUÉ IMPORTA]`

Problema actual:

`[QUÉ FALLA / FALTA / SE QUIERE CAMBIAR]`

---

# 4. ALCANCE AUTORIZADO

Está autorizado modificar lo necesario dentro de:

- `[ÁREA / FLUJO / CAPACIDAD]`
- `[ÁREA / FLUJO / CAPACIDAD]`
- `[ÁREA / FLUJO / CAPACIDAD]`

También está autorizado:

- `[REFACTOR ACOTADO, SI APLICA]`
- `[MIGRACIÓN, SI APLICA]`
- `[DOCUMENTACIÓN, SI APLICA]`

Regla de scope:

Un hallazgo fuera de este alcance NO autoriza su implementación.

Si Pi detecta una dependencia fuera de alcance necesaria para cumplir el objetivo, debe reportarla y preservar la barrera de decisión humana cuando expanda materialmente el scope.

---

# 5. NON-GOALS / FUERA DE ALCANCE

NO incluir:

- `[EXCLUSIÓN 1]`
- `[EXCLUSIÓN 2]`
- `[FEATURE FUTURA]`
- `[MÓDULO QUE NO DEBE TOCARSE]`

NO hacer:

- refactors globales no relacionados;
- rediseños no solicitados;
- reemplazos de librerías sin necesidad confirmada;
- migraciones destructivas no autorizadas;
- cambios de contratos no requeridos;
- optimizaciones fuera de scope;
- corrección automática de hallazgos adyacentes.

---

# 6. SOURCES OF TRUTH

Define qué fuente manda para cada dimensión.

## Product / Scope Authority

1. `[DECISIÓN EXPLÍCITA MÁS RECIENTE]`
2. `[HU / BACKLOG / APROBACIÓN]`

## Functional Authority

- `[HU VIGENTE]`
- `[SRS / REQUISITOS]`

## Business Rules

- `[DOCUMENTO / DECISIÓN]`

## Implementation Reality

- `[REPOSITORIO QUE PI DEBE INSPECCIONAR]`
- `[ARCHIVOS REALMENTE CONOCIDOS, SI LOS HAY]`

## Technical / Architecture Authority

- `[ARQUITECTURA / ADR / CONVENCIONES]`

## Visual References

- Referencia editable aprobada: `[URL de página/frame + versión exacta + estado + responsable/fecha]`.
- PNG inicial/mejorado/refinado: `[etapa + viewport + archivo/enlace]`; son referencias intermedias, no el master editable.
- Fuentes realmente consultadas: `[owner/repo + rama/commit + rutas + assets]` o `[no disponible / límite de acceso]`.
- Guía canónica del procedimiento: [Flujo de referencias visuales UX](../../ux/flujo-referencias-visuales.md); este briefing sólo enlaza y resume la referencia necesaria para esta HU.

## Conflict Rule

Ejemplo:

`Si un mockup contradice una decisión funcional explícitamente aprobada, prevalece la decisión funcional.`

`Si documentación y código difieren, Pi debe distinguir intended behavior de current implementation en lugar de asumir que uno describe al otro.`

Las reglas funcionales aprobadas prevalecen ante cualquier conflicto visual. Para diseño, identidad/assets oficiales y tokens/kit del proyecto, junto con el master editable y las pantallas aprobadas, prevalecen sobre PNG intermedios o referencias inspiracionales. Pi inspecciona por separado el código, contratos y pruebas; ni una imagen ni un frame prueban implementación. Un PNG plano no es editable y un componente de Figma no es un componente frontend.

---

# 7. CONTEXTO FUNCIONAL ACTUAL

Comportamiento actual confirmado:

1. `[COMPORTAMIENTO]`
2. `[COMPORTAMIENTO]`
3. `[COMPORTAMIENTO]`

Actores:

- `[ACTOR / ROL]`
- `[ACTOR / ROL]`

Flujo actual:

`[ACTOR]`
→ `[ACCIÓN]`
→ `[PROCESO]`
→ `[RESULTADO ACTUAL]`

Problemas conocidos:

- `[PROBLEMA]`
- `[PROBLEMA]`

Si algo no está confirmado, indícalo como desconocido y deja que Pi lo establezca mediante repository exploration.

---

# 8. COMPORTAMIENTO OBJETIVO

Después del cambio:

1. `[COMPORTAMIENTO ESPERADO]`
2. `[COMPORTAMIENTO ESPERADO]`
3. `[COMPORTAMIENTO ESPERADO]`

Flujo esperado:

`[ACTOR]`
→ `[ACCIÓN]`
→ `[VALIDACIÓN / REGLA]`
→ `[RESULTADO]`

Comportamiento visible:

`[DESCRIPCIÓN]`

Comportamiento interno obligatorio como invariante:

`[DESCRIPCIÓN SIN INVENTAR DISEÑO]`

---

# 9. REGLAS DE NEGOCIO

Reglas confirmadas:

1. `[REGLA]`
2. `[REGLA]`
3. `[REGLA]`

Validaciones confirmadas:

- `[CAMPO]: [REGLA]`
- `[CAMPO]: [REGLA]`

Invariantes:

- `[INVARIANTE]`
- `[INVARIANTE]`

Casos prohibidos:

- `[CASO]`
- `[CASO]`

Decisiones de negocio ya aprobadas NO deben reabrirse salvo contradicción real.

---

# 10. CRITERIOS DE ACEPTACIÓN

El cambio se considera correcto cuando:

1. `[CRITERIO OBSERVABLE]`
2. `[CRITERIO OBSERVABLE]`
3. `[CRITERIO OBSERVABLE]`
4. `[CRITERIO OBSERVABLE]`

Puedes usar MUST / SHOULD / MAY si aporta precisión.

Puedes usar Given / When / Then si aporta claridad.

Ejemplo opcional:

### `[CASO]`

Given `[CONDICIÓN]`  
When `[ACCIÓN]`  
Then `[RESULTADO]`

No uses estas notaciones por ceremonia.

---

# 11. EDGE CASES RELEVANTES

Incluir sólo los que apliquen.

- `[EMPTY STATE]`
- `[NULL / MISSING DATA]`
- `[DUPLICADO]`
- `[INVALID STATE]`
- `[PERMISSION DENIED]`
- `[RETRY]`
- `[CONCURRENCIA]`
- `[REDONDEO]`
- `[FECHA / TIMEZONE]`
- `[LEGACY DATA]`
- `[FALLO PARCIAL]`
- `[OTRO]`

Resultado esperado para cada caso relevante:

`[DESCRIBIR]`

---

# 12. ARQUITECTURA Y STACK CONOCIDOS

Frontend:

- Framework: `[ ]`
- Lenguaje: `[ ]`
- UI: `[ ]`
- Estado/data fetching: `[ ]`
- Convención relevante: `[ ]`

Backend:

- Framework: `[ ]`
- Lenguaje: `[ ]`
- Arquitectura: `[ ]`
- ORM/data access: `[ ]`

Base de datos:

`[ ]`

Auth:

`[ ]`

Integraciones:

`[ ]`

Infra/Deployment:

`[ ]`

Testing conocido:

`[ ]`

IMPORTANTE:

Estos datos son contexto, NO una orden para inventar el diseño.

Pi debe preservar patrones existentes y derivar la implementación real tras inspeccionar el repositorio.

---

# 13. ARCHIVOS / SÍMBOLOS REALMENTE CONOCIDOS

Archivos confirmados:

- `[ruta]`
- `[ruta]`

Componentes/clases/servicios confirmados:

- `[nombre]`

Endpoints confirmados:

- `[METHOD /ruta]`

Tablas/entidades confirmadas:

- `[nombre]`

Contratos/DTOs/interfaces confirmados:

- `[nombre]`

Si no está confirmado:

usar formulaciones como:

`must be confirmed during repository exploration`

o:

`exact implementation location is unresolved`

NO inventar rutas.

---

# 14. CONTRATOS Y DATOS

Entradas conocidas:

- `[DATO]`

Salidas conocidas:

- `[DATO]`

Persistencia esperada:

- `[DATO / REGLA]`

Datos que NO deben persistirse:

- `[DATO]`

Compatibilidad requerida:

- `[CLIENTE / API / DATO LEGACY / VERSIÓN]`

Contrato externo que debe mantenerse:

`[DESCRIPCIÓN]`

Contrato exacto desconocido:

`[QUÉ DEBE CONFIRMAR PI]`

---

# 15. ESTADOS Y TRANSICIONES

Estados relevantes:

- `[ESTADO]`

Transiciones válidas:

`[A] -> [B]`

Transiciones inválidas:

`[X] -> [Y]`

Guards/reglas:

- `[REGLA]`

No obligar a crear enums/estado nuevo si el repositorio ya modela esto de otra forma.

---

# 16. CONCURRENCIA / ATOMICIDAD / IDEMPOTENCIA

¿Puede haber operaciones simultáneas?

`[Sí | No | Desconocido]`

Casos relevantes:

- doble submit;
- doble confirmación;
- retry;
- dos usuarios editando;
- stock concurrente;
- batch parcial;
- asignación simultánea;
- otro.

Invariante esperado:

`[QUÉ DEBE SER ATÓMICO / CONSISTENTE]`

NO inventar locks/transacciones concretas.

Pi debe elegir el mecanismo compatible con la arquitectura actual.

---

# 17. MIGRACIÓN / DATA SAFETY

¿Se espera cambio persistente?

`[Sí | No | Desconocido]`

Si aplica, considerar:

- existing records;
- defaults;
- nullability;
- backfill;
- backward compatibility;
- partial deployment;
- rollout ordering;
- destructive change risk;
- rollback;
- validation old/new data.

Requisitos concretos:

`[DESCRIBIR]`

No inventar nombre de migration ni comando.

---

# 18. SEGURIDAD / PERMISOS

Roles:

- `[ROL]`

Acciones permitidas:

- `[ROL]` → `[ACCIÓN]`

Acciones prohibidas:

- `[ROL]` MUST NOT `[ACCIÓN]`

Datos sensibles:

`[NINGUNO / DESCRIPCIÓN GENERAL]`

Requisitos:

- `[AUTORIZACIÓN]`
- `[PRIVACIDAD]`
- `[AUDITORÍA, SI APLICA]`

No incluir secretos/tokens/credenciales.

---

# 19. UX / VISUAL / RESPONSIVE

Si aplica:

Vista actual:

`[DESCRIPCIÓN]`

Vista objetivo:

`[DESCRIPCIÓN]`

Referencias visuales:

- `[IMAGEN / ZIP / FIGMA]`

Referencia maestra editable aprobada (frame/versión exacta, responsable y fecha):

`[URL / DESCONOCIDA / NO APLICA]`

PNG inicial/mejorado y viewport(s):

`[ETAPA + ARCHIVO/ENLACE + VIEWPORT / DESCONOCIDO / NO APLICA]`

Mobile:

`[EXPECTATIVA]`

Tablet:

`[EXPECTATIVA]`

Desktop:

`[EXPECTATIVA]`

Estados visuales relevantes:

- loading;
- empty;
- error;
- success;
- disabled;
- inactive;
- permission denied;
- otro.

Reglas de preservación:

- `[NO MODIFICAR DESKTOP]`
- `[MANTENER INTERACCIONES]`
- `[ACCESIBILIDAD]`

Las referencias visuales no crean features que no estén autorizadas. La [guía UX](../../ux/flujo-referencias-visuales.md) es la fuente del procedimiento completo; aquí sólo se identifican las referencias y límites de esta HU. Distingue capas editables de componentes reutilizables y de componentes frontend; Pi debe verificar el código de forma independiente.

---

# 20. DECISIONES YA APROBADAS

Estas decisiones son autoridad del briefing:

1. `[DECISIÓN]`
2. `[DECISIÓN]`
3. `[DECISIÓN]`

Rationale, si importa:

- `[DECISIÓN]`: `[MOTIVO]`

No volver a preguntar lo ya decidido.

---

# 21. MATERIAL UNCERTAINTY

No quiero preguntas genéricas.

## BLOCKING

- `[DECISIÓN SIN LA CUAL NO SE PUEDE CONTINUAR]`

## RESEARCH REQUIRED

- `[ALGO QUE PI PUEDE RESOLVER INSPECCIONANDO REPO/DOCS]`

## HUMAN DECISION REQUIRED

- `[DECISIÓN DE PRODUCTO / RIESGO / SCOPE]`

## NON-BLOCKING

- `[INCERTIDUMBRE MENOR]`

Si una duda puede resolverse de forma segura mediante repository exploration, no me preguntes antes de intentarlo.

---

# 22. ASSUMPTION CHECK DE ALTO IMPACTO

¿Existe una hipótesis incierta que, si es falsa, cambiaría materialmente la implementación?

`[No | Sí: describir]`

Si sí, se permite como máximo una comprobación independiente/read-only útil.

No crear reviewer chains.

No ampliar scope.

---

# 23. TEST / VERIFICATION CONTEXT

Infraestructura de tests conocida:

- Unit: `[Sí / No / Desconocido]`
- Application: `[Sí / No / Desconocido]`
- Integration: `[Sí / No / Desconocido]`
- E2E: `[Sí / No / Desconocido]`

Runners/comandos realmente confirmados:

- `[COMANDO EXACTO]`

Entorno E2E conocido:

`[Windows / Linux / CI / navegador / desconocido]`

Limitaciones conocidas:

- `[Docker unavailable]`
- `[Chromium no disponible en esta máquina]`
- `[otro]`

Fallos preexistentes conocidos:

- `[EVIDENCIA]`

NO inferir comandos no confirmados.

---

# 24. TEST-FIRST EXPECTATION

Para cambios de comportamiento con un test:

- meaningful;
- runnable;
- deterministic;
- con resultado esperado claro;

favorecer durante ejecución:

RED
→ GREEN
→ REFACTOR

No exigir RED artificial si:

- no existe runner aplicable;
- el cambio es documentación;
- el test sería no determinista/no significativo;
- el entorno falla antes de probar el comportamiento.

En ese caso usar verificación proporcional y documentar la razón.

---

# 25. VERIFICATION EXPECTATIONS

Evidencia esperada según lo que realmente aplique:

- `[unit tests]`
- `[application tests]`
- `[integration tests]`
- `[API verification]`
- `[typecheck]`
- `[lint]`
- `[build]`
- `[E2E]`
- `[manual QA]`
- `[responsive]`
- `[screenshots]`
- `[DB state]`
- `[logs]`
- `[migration check]`
- `[authorization/security]`
- `[backward compatibility]`

No anticipar PASS.

Si un check no puede ejecutarse, Pi debe reportarlo honestamente:

- BLOCKED;
- UNAVAILABLE;
- NOT RUN;
- SKIPPED;

con razón.

---

# 26. DOCUMENTACIÓN PERMANENTE

Documentos que deben actualizarse si la implementación cambia su verdad:

- `[docs/historias/HU-XXX.md]`
- `[docs/requirements/...]`
- `[docs/architecture/...]`
- `[docs/adr/...]`
- `[API docs]`
- `[README/deployment docs]`
- `[otro]`

No generar documentación irrelevante por ceremonia. Enlazar el master editable y su aprobación en la HU/documentación UX vigente cuando sean relevantes; no copiar el procedimiento entero ni crear referencias divergentes.

La documentación permanente NO se reemplaza por tracking operacional ODD.

---

# 27. EVIDENCE EXPECTATIONS

Evidencia requerida:

- `[capturas]`
- `[manifest]`
- `[logs]`
- `[test output]`
- `[API evidence]`
- `[migration evidence]`
- `[manual checklist]`
- Para UX, si aplica: `[frame/versión editable + responsable/fecha de aprobación; PNG por etapa/viewport; fuentes, repo/rama/commit, rutas y assets realmente consultados; límites y pendientes]`.

No afirmar acceso a GitHub/archivos ni editabilidad que no se haya comprobado. Una captura plana no es evidencia de diseño editable ni de implementación frontend.

Resolución/tamaño/formato requerido, si aplica:

`[ ]`

Ubicación esperada, sólo si está confirmada:

`[ ]`

No inventar evidencia ni marcarla como existente antes de producirla.

---

# 28. GIT / DELIVERY AUTHORIZATION

Completar cada permiso independientemente.

| Operación | Autorización | Notas |
| --- | --- | --- |
| Branch creation/switching | `[ALLOWED / NOT ALLOWED / ASK]` | `[ ]` |
| Worktree creation | `[ALLOWED / NOT ALLOWED / ASK]` | `[ ]` |
| Local commits | `[ALLOWED / NOT ALLOWED / ASK]` | `[ ]` |
| Push | `[ALLOWED / NOT ALLOWED / ASK]` | `[ ]` |
| PR creation | `[ALLOWED / NOT ALLOWED / ASK]` | `[ ]` |
| Merge | `[ALLOWED / NOT ALLOWED / ASK]` | `[ ]` |
| Rebase | `[ALLOWED / NOT ALLOWED / ASK]` | `[ ]` |
| Force push | `[ALLOWED / NOT ALLOWED]` | `[ ]` |
| Destructive Git operations | `[ALLOWED / NOT ALLOWED]` | `[ ]` |
| Deployment | `[ALLOWED / NOT ALLOWED / ASK]` | `[ ]` |

Regla:

`Local commits: ALLOWED` NO implica `Push: ALLOWED`.

No asumir permiso faltante.

---

# 29. REVIEW CONFIGURATION

Política:

`Respect existing runtime/user review configuration.`

El briefing NO debe activar/desactivar review mode.

Expectativa adicional, si existe:

`[ ]`

Un resultado de review NO autoriza commit, push, PR, merge ni deploy.

---

# 30. STOP CONDITION / MAINTAINER REVIEW

Stop condition:

`[Ninguna especial | Maintainer Review | Otra]`

Ejemplo habitual:

Detenerse cuando:

- implementación esté completa dentro del scope;
- applicable checks estén ejecutados;
- unavailable checks estén documentados;
- documentación/evidencia esté actualizada;
- commits locales estén listos sólo si fueron autorizados.

Estado esperado:

`IMPLEMENTATION + APPLICABLE CHECKS COMPLETE — PENDING MAINTAINER REVIEW`

Antes de revisión NO:

- push;
- PR;
- merge;
- deployment;

salvo autorización explícita distinta.

---

# 31. DELIVERY / WORK-UNIT PREFERENCES

No predefinir la lista exacta de work units.

Preferencias conocidas:

- mantener HU como unidad vertical: `[Sí / No]`
- favorecer commits por work unit si están autorizados: `[Sí / No / Dejar a runtime]`
- preferencia de PR: `[Single / Chained / Decidir después de explorar]`

Heurística:

~400 authored changed lines puede ser una referencia de reviewability/delivery, no un hard cap ni acceptance criterion.

Pi decide límites reales después de explorar.

---

# 32. MULTI-MACHINE / ENVIRONMENT CONSTRAINTS

Si aplica:

Máquina/OS actual:

`[Windows / Linux Mint / otro]`

Checks permitidos aquí:

- `[ ]`

Checks diferidos a otra máquina/CI:

- `[ ]`

Docker:

`[Disponible / No disponible / Parcial]`

Browser/E2E:

`[ ]`

No tratar limitaciones ambientales como fallo funcional del cambio sin evidencia.

---

# 33. LEGACY / HISTORICAL INPUT

Si existen documentos históricos del proyecto:

- `[ruta / descripción]`

Úsalos como input de decisiones/requisitos cuando sigan vigentes.

No los migres/elimine automáticamente.

Si contradicen decisiones actuales:

- conservar historia;
- usar decisión actual como autoridad correspondiente;
- reportar discrepancia cuando importe.

---

# 34. REQUISITOS PARA EL EXECUTION HANDOFF

El briefing final debe instruir a Pi, adaptándolo al caso concreto, a:

1. usar ODD;
2. inspeccionar primero el repositorio;
3. reconciliar brief + repo + documentación vigente;
4. derivar el plan técnico del repositorio real;
5. no inventar implementación;
6. preservar patrones existentes;
7. respetar scope y non-goals;
8. reportar hallazgos fuera de scope;
9. clasificar small vs substantial después de explorar;
10. crear `odd/tasks/<feature>.md` sólo si el trabajo resulta substantial;
11. mantener mirror project-scoped en Engram cuando esté disponible;
12. reconciliar memoria + feature doc + repo al reanudar;
13. derivar work units reales;
14. usar test-first cuando sea aplicable;
15. usar verificación proporcional cuando no;
16. mantener evidencia honesta;
17. actualizar documentación permanente relevante;
18. respetar permisos Git/delivery;
19. respetar review mode existente;
20. detenerse en Maintainer Review si está configurado.

---

# 35. REGLA FINAL DE SALIDA

Genera únicamente un documento:

# ODD Execution Brief

No conviertas esta plantilla en 35 secciones obligatorias.

Selecciona y organiza sólo las secciones relevantes.

No pierdas información importante por intentar resumir demasiado.

Normaliza redundancias.

Preserva decisiones exactas.

Si hay contradicción real:

1. identifica las fuentes;
2. aplica la autoridad correspondiente;
3. si sigue requiriendo decisión humana, clasifícala como HUMAN DECISION REQUIRED;
4. no inventes una resolución.

La simplificación debe eliminar ceremonia, NO contexto ni rigor.
