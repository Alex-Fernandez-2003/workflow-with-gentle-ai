# Checklist Maestra Universal para Proyectos Universitarios de Software v4

## Propósito

Esta checklist sirve para desarrollar y documentar un proyecto universitario de software desde una idea o problema inicial hasta su validación, implementación y presentación final.

Debe funcionar indistintamente cuando el proyecto tenga como objetivo:

- una empresa u organización concreta;
- una institución pública o privada;
- una comunidad;
- una población objetivo;
- un segmento de usuarios;
- un producto dirigido al mercado;
- un problema social;
- un proyecto experimental o académico;
- un prototipo, MVP o producto funcional.

> **Principio fundamental:** primero se comprende y demuestra el problema; después se diseña la solución.

> **Regla de evidencia:** nunca presentar entrevistas, encuestas, usuarios, métricas, pruebas, resultados o validaciones simuladas como si fueran reales.

> **Principio de trazabilidad:** toda decisión importante debería poder rastrearse hacia una necesidad, requisito, regla, historia, diseño, implementación, prueba o evidencia según corresponda.

> **Principio de legibilidad:** un artefacto no está bien únicamente porque sea técnicamente correcto; también debe poder comprenderse en el medio real de entrega. Si un diagrama se vuelve ilegible al insertarlo en el informe, debe simplificarse, dividirse o acompañarse con vistas de detalle.

> **Principio de fuente editable:** cuando un artefacto visual se genera desde una fuente editable —PlantUML, Mermaid, draw.io, BPMN u otra— conservar la fuente y el render de forma sincronizada.

> **Principio de mínima duplicación:** cada información debe tener una fuente principal. Otros documentos pueden resumirla o referenciarla, pero no deberían mantener copias completas que evolucionen de manera independiente.

> **Principio de evolución controlada:** cuando cambie comportamiento, alcance, arquitectura, datos o estados, revisar también los documentos, diagramas, pruebas y trazabilidad afectados.

---

# 0. Cómo utilizar esta checklist

## 0.1 Identificar la modalidad del proyecto

- [ ] Identificar si existe una organización/empresa objetivo.
- [ ] Identificar si existe una población o comunidad objetivo.
- [ ] Identificar si se trata de un producto para usuarios potenciales sin cliente específico.
- [ ] Identificar si el proyecto responde principalmente a una consigna académica.
- [ ] Identificar si existe un cliente, sponsor, docente o contraparte que deba aprobar decisiones.
- [ ] Identificar quién representa legítimamente las necesidades del proyecto.

## 0.2 Clasificar cada elemento

Cuando sea necesario, marcar elementos como:

- [ ] **Obligatorio:** necesario para cualquier proyecto.
- [ ] **Académico:** exigido por la asignatura.
- [ ] **Si aplica:** necesario únicamente según el proyecto.
- [ ] **Pendiente de validar:** propuesta todavía no confirmada.
- [ ] **No aplica:** revisado y descartado con justificación.

## 0.3 Regla frente a la consigna académica

- [ ] Obtener la consigna oficial.
- [ ] Obtener rúbrica o lista de cotejo.
- [ ] Identificar formato de entrega.
- [ ] Identificar entregables obligatorios.
- [ ] Identificar diagramas obligatorios.
- [ ] Identificar técnicas obligatorias.
- [ ] Identificar cantidades obligatorias.
- [ ] Identificar tecnologías obligatorias, si existen.
- [ ] Identificar fecha y modalidad de entrega.
- [ ] Registrar las exigencias académicas como restricciones.
- [ ] No convertir recomendaciones genéricas en requisitos de la materia.
- [ ] No inventar evidencia para satisfacer una rúbrica.

---

# 1. Preparación y gobierno del proyecto

## 1.1 Ficha básica

- [ ] Nombre del proyecto.
- [ ] Nombre corto.
- [ ] Tipo de proyecto.
- [ ] Asignatura.
- [ ] Docente.
- [ ] Carrera/programa.
- [ ] Periodo académico.
- [ ] Integrantes.
- [ ] Roles del equipo.
- [ ] Organización objetivo, si existe.
- [ ] Población objetivo, si existe.
- [ ] Sponsor/contraparte, si existe.
- [ ] Repositorio.
- [ ] Espacio documental.
- [ ] Tablero de trabajo.
- [ ] Fecha de inicio.
- [ ] Fecha de entrega.
- [ ] Duración disponible.
- [ ] Versión/baseline documental.

## 1.2 Objetivo de la entrega

- [ ] Determinar qué debe quedar terminado.
- [ ] Determinar qué puede quedar únicamente diseñado.
- [ ] Determinar qué debe quedar implementado.
- [ ] Determinar qué debe quedar validado.
- [ ] Determinar qué evidencia será necesaria.

## 1.3 Convenciones

- [ ] Convención de nombres de archivos.
- [ ] Convención para IDs.
- [ ] Convención para diagramas.
- [ ] Convención para versiones.
- [ ] Convención para ramas/commits, si aplica.
- [ ] Ubicación oficial de cada documento.
- [ ] Definir una única fuente de verdad para requisitos y backlog.
- [ ] Definir una fuente principal por tipo de información para evitar duplicaciones divergentes.
- [ ] Definir convención para fuentes editables y renders de diagramas.
- [ ] Utilizar el mismo nombre base para fuente y render cuando sea posible.
- [ ] Definir cómo identificar diagramas globales y diagramas por módulo.
- [ ] Definir cuándo un archivo queda reemplazado/superseded y cómo retirar referencias antiguas.
- [ ] Definir formato para registrar archivos creados/modificados por historia o cambio, si el equipo lo necesita.

---

# 2. Estructura documental

Una estructura de referencia puede ser:

```text
proyecto/
├── README.md
│
├── docs/
│   ├── 00-ficha-proyecto.md
│   ├── 01-contexto-y-diagnostico.md
│   ├── 02-relevamiento.md
│   ├── 03-hallazgos-y-necesidades.md
│   ├── 04-objetivos-y-propuesta-valor.md
│   ├── 05-alcance-y-mvp.md
│   ├── 06-srs.md
│   │
│   ├── requirements/
│   │   ├── requisitos-funcionales.md
│   │   ├── requisitos-no-funcionales.md
│   │   └── reglas-negocio.md
│   │
│   ├── 07-product-backlog.md
│   │
│   ├── historias/
│   │   ├── README.md
│   │   └── HU-XXX-....md
│   │
│   ├── 08-scrum-y-refinamiento.md
│   │
│   ├── sprints/
│   │   ├── README.md
│   │   ├── sprint-XX.md
│   │   ├── sprint-XX-review.md
│   │   └── sprint-XX-retrospectiva.md
│   │
│   ├── 09-ux-y-flujos.md
│   │
│   ├── puml/                    # si se utiliza PlantUML
│   │   └── ...
│   ├── images/                  # renders, capturas o figuras
│   │   └── ...
│   │
│   ├── 10-arquitectura.md
│   │
│   ├── adr/
│   │   └── ADR-XXX-....md
│   │
│   ├── 11-modelo-datos.md
│   │
│   ├── database/
│   │   └── ...
│   │
│   ├── 12-seguridad-y-riesgos.md
│   ├── 13-pruebas-y-validacion.md
│   ├── 14-trazabilidad.md
│   ├── 15-plan-desarrollo.md
│   │
│   ├── handoffs/                # si existen entregas entre equipos/capas
│   │   └── ...
│   │
│   ├── openspec/                # si se utiliza especificación de cambios
│   │   ├── specs/
│   │   └── changes/
│   │
│   ├── evidence/
│   │   ├── relevamiento/
│   │   ├── historias/
│   │   ├── pruebas/
│   │   └── ...
│   │
│   └── 16-informe-final.md
│
├── frontend/
├── backend/
├── database/                    # si el proyecto la necesita en ejecución
├── scripts/                     # si aplica
├── tests/                       # tests transversales, si aplica
└── ...
```

La estructura concreta puede variar. Para diagramas se puede utilizar, por ejemplo:

```text
docs/
├── diagrams/
│   ├── src/
│   └── rendered/
```

o bien una separación específica por herramienta:

```text
docs/
├── puml/
└── images/
```

Lo importante es conservar claramente la **fuente editable** y el **render consumido por la documentación**, preferentemente con el mismo nombre base.

- [ ] Adaptar la estructura a la materia.
- [ ] Eliminar carpetas innecesarias.
- [ ] No mencionar entregables inexistentes.
- [ ] Separar fuentes editables de renders cuando corresponda.
- [ ] Evitar guardar múltiples versiones huérfanas del mismo artefacto.
- [ ] Definir dónde viven las evidencias de relevamiento, implementación y pruebas.
- [ ] Definir dónde viven Sprint Review y Retrospective si la metodología las requiere.
- [ ] Mantener rutas relativas estables y comprensibles.

---

# 3. Contexto del proyecto

## 3.1 Contexto general

- [ ] Describir el dominio del problema.
- [ ] Describir dónde ocurre.
- [ ] Describir a quién afecta.
- [ ] Describir el proceso, comportamiento o situación actual.
- [ ] Identificar alternativas actuales.
- [ ] Identificar herramientas actualmente utilizadas.
- [ ] Identificar datos disponibles.
- [ ] Identificar restricciones conocidas.
- [ ] Identificar factores económicos relevantes.
- [ ] Identificar factores sociales relevantes.
- [ ] Identificar factores tecnológicos relevantes.
- [ ] Identificar factores regulatorios relevantes, si aplica.

## 3.2 Si existe empresa u organización objetivo

- [ ] Nombre y tipo de organización.
- [ ] Actividad principal.
- [ ] Área involucrada.
- [ ] Proceso involucrado.
- [ ] Responsable del proceso.
- [ ] Usuarios operativos.
- [ ] Responsables de decisión.
- [ ] Sistemas existentes.
- [ ] Restricciones internas.
- [ ] Políticas relevantes.
- [ ] Datos disponibles.
- [ ] Persona autorizada para validar necesidades.

## 3.3 Si existe población objetivo

- [ ] Definir claramente la población.
- [ ] Determinar características relevantes.
- [ ] Determinar ubicación, si es relevante.
- [ ] Determinar criterios de inclusión/exclusión.
- [ ] Identificar subgrupos importantes.
- [ ] Determinar quién experimenta el problema.
- [ ] Determinar quién usaría la solución.
- [ ] Determinar quién se beneficia aunque no la utilice.
- [ ] Identificar posibles barreras de acceso.
- [ ] Identificar representatividad de la muestra utilizada.
- [ ] Evitar generalizar resultados de una muestra limitada a toda la población.

---

# 4. Stakeholders y actores

## 4.1 Identificación

- [ ] Usuario principal.
- [ ] Usuarios secundarios.
- [ ] Beneficiarios.
- [ ] Cliente, si existe.
- [ ] Sponsor, si existe.
- [ ] Administradores.
- [ ] Responsables operativos.
- [ ] Responsables de decisión.
- [ ] Equipo de desarrollo.
- [ ] Docente/evaluador.
- [ ] Sistemas externos.
- [ ] Entidades regulatorias, si aplican.
- [ ] Personas afectadas indirectamente.

## 4.2 Análisis

Por stakeholder:

- [ ] Interés.
- [ ] Necesidades.
- [ ] Influencia.
- [ ] Poder de decisión.
- [ ] Información que aporta.
- [ ] Riesgos asociados.
- [ ] Expectativas.
- [ ] Forma de participación.
- [ ] Forma de validación.

## 4.3 Diferenciar conceptos

- [ ] No asumir que stakeholder = usuario.
- [ ] No asumir que usuario = cliente.
- [ ] No asumir que beneficiario = actor del sistema.
- [ ] No modelar como actor a quien nunca interactúa con el sistema.

---

# 5. Diagnóstico del problema u oportunidad

## 5.1 Describir la situación actual

- [ ] ¿Qué ocurre actualmente?
- [ ] ¿Quién participa?
- [ ] ¿Cómo funciona hoy?
- [ ] ¿Qué pasos existen?
- [ ] ¿Dónde aparecen dificultades?
- [ ] ¿Qué herramientas se utilizan?
- [ ] ¿Qué información se genera?
- [ ] ¿Dónde se pierde información?
- [ ] ¿Dónde existen retrasos?
- [ ] ¿Dónde aparecen errores?
- [ ] ¿Qué decisiones resultan difíciles?
- [ ] ¿Qué necesidades no están satisfechas?

## 5.2 Problema central

Plantilla:

```text
[Usuario / organización / población] presenta ____________
al intentar _____________________________________________
debido a ________________________________________________
lo que provoca __________________________________________.
```

- [ ] Problema expresado en una frase.
- [ ] No formularlo simplemente como “no existe una app”.
- [ ] No formularlo como ausencia de una tecnología específica.
- [ ] Separar problema de solución.
- [ ] Identificar causas.
- [ ] Identificar efectos.
- [ ] Identificar causa raíz cuando sea posible.
- [ ] Identificar impactos observables.
- [ ] Identificar frecuencia.
- [ ] Identificar severidad.
- [ ] Determinar a quién afecta.

## 5.3 Evidencia del problema

- [ ] Observaciones.
- [ ] Entrevistas.
- [ ] Encuestas.
- [ ] Documentos.
- [ ] Datos existentes.
- [ ] Literatura.
- [ ] Estadísticas.
- [ ] Registros históricos.
- [ ] Evidencia proporcionada por la organización.
- [ ] Evidencia proporcionada por usuarios.

## 5.4 Árbol de problemas — si aporta valor

- [ ] Problema central.
- [ ] Causas directas.
- [ ] Causas indirectas.
- [ ] Efectos directos.
- [ ] Efectos indirectos.
- [ ] Relación causal razonable.
- [ ] Evidencia cuando exista.
- [ ] No agregar causas únicamente para alcanzar una cantidad requerida.

---

# 6. Relevamiento / investigación de necesidades

## 6.1 Objetivos del relevamiento

- [ ] Identificar qué información falta.
- [ ] Formular preguntas de investigación.
- [ ] Definir hipótesis que necesitan validación.
- [ ] Determinar qué decisiones dependerán de los resultados.

## 6.2 Técnicas posibles

Evaluar:

- [ ] Entrevistas.
- [ ] Encuestas/cuestionarios.
- [ ] Observación.
- [ ] Talleres.
- [ ] Focus groups.
- [ ] Análisis documental.
- [ ] Análisis de procesos.
- [ ] Análisis de datos existentes.
- [ ] Benchmarking.
- [ ] Prueba de concepto.
- [ ] Prototipado.
- [ ] Prueba de usabilidad.
- [ ] Revisión bibliográfica.

## 6.3 Selección de técnicas

- [ ] Justificar cada técnica.
- [ ] Relacionarla con una pregunta que debe responder.
- [ ] Identificar participantes.
- [ ] Determinar muestra cuando corresponda.
- [ ] Determinar duración.
- [ ] Determinar medio de aplicación.
- [ ] Determinar cómo se analizarán resultados.
- [ ] Cumplir cantidad mínima únicamente si la materia la exige.

## 6.4 Instrumentos

Por instrumento:

- [ ] Objetivo.
- [ ] Población.
- [ ] Perfil del participante.
- [ ] Preguntas neutrales.
- [ ] Lenguaje comprensible.
- [ ] Preguntas no inductivas.
- [ ] Preguntas abiertas cuando aporten descubrimiento.
- [ ] Evitar solicitar información innecesaria.
- [ ] Evitar datos sensibles no indispensables.
- [ ] Definir método de análisis.
- [ ] Realizar piloto si es razonable.

## 6.5 Ética del relevamiento

- [ ] Informar propósito.
- [ ] Solicitar consentimiento cuando corresponda.
- [ ] Permitir retirarse.
- [ ] Minimizar datos personales.
- [ ] Anonimizar cuando corresponda.
- [ ] Evitar exponer participantes.
- [ ] No manipular resultados.
- [ ] No atribuir citas inexistentes.

## 6.6 Resultados

- [ ] Fecha.
- [ ] Medio.
- [ ] Técnica.
- [ ] Número de participantes.
- [ ] Perfil general.
- [ ] Resultados cuantitativos.
- [ ] Hallazgos cualitativos.
- [ ] Patrones.
- [ ] Excepciones.
- [ ] Limitaciones.
- [ ] Sesgos.
- [ ] Preguntas pendientes.

---

# 7. Consolidación de hallazgos y necesidades

## 7.1 Hallazgos

Asignar identificadores:

```text
H-001
H-002
H-003
```

Por hallazgo:

- [ ] Fuente.
- [ ] Evidencia.
- [ ] Interpretación.
- [ ] Nivel de confianza.
- [ ] Impacto.

## 7.2 Necesidades

Asignar:

```text
N-001
N-002
N-003
```

Por necesidad:

- [ ] Descripción.
- [ ] Usuario/stakeholder.
- [ ] Fuente.
- [ ] Hallazgo asociado.
- [ ] Importancia.
- [ ] Frecuencia.
- [ ] Impacto.
- [ ] Prioridad.
- [ ] Estado de validación.

## 7.3 Clasificación

- [ ] Necesidad de usuario.
- [ ] Necesidad de negocio/organización.
- [ ] Necesidad social.
- [ ] Regla operativa.
- [ ] Necesidad de información.
- [ ] Necesidad técnica.
- [ ] Restricción.

## 7.4 Control

- [ ] No convertir cada sugerencia en requisito.
- [ ] Consolidar necesidades duplicadas.
- [ ] Identificar contradicciones.
- [ ] Registrar necesidades descartadas y motivo.
- [ ] Separar hechos de interpretaciones.

---

# 8. Objetivos del proyecto

## 8.1 Objetivo general

- [ ] Explica qué se pretende lograr.
- [ ] Responde al problema identificado.
- [ ] No se limita a “desarrollar un sistema”.
- [ ] Es coherente con el alcance.

## 8.2 Objetivos específicos

- [ ] Derivan del objetivo general.
- [ ] Son verificables.
- [ ] Cubren análisis cuando corresponde.
- [ ] Cubren diseño cuando corresponde.
- [ ] Cubren implementación cuando corresponde.
- [ ] Cubren validación cuando corresponde.

## 8.3 SMART — cuando sea apropiado

- [ ] Específico.
- [ ] Medible.
- [ ] Alcanzable.
- [ ] Relevante.
- [ ] Temporal.

## 8.4 Indicadores de éxito

- [ ] Definir qué significaría que el proyecto tuvo éxito.
- [ ] Utilizar métricas reales cuando exista baseline.
- [ ] Marcar objetivos numéricos no validados como propuestas.
- [ ] Diferenciar éxito académico, técnico y de usuario.

---

# 9. Solución y propuesta de valor

## 9.1 Árbol de soluciones — si aporta valor

- [ ] Convertir causas relevantes en medios/acciones.
- [ ] Convertir efectos negativos en beneficios esperados.
- [ ] Mantener relación con el diagnóstico.
- [ ] Evitar saltar directamente a funcionalidades.

## 9.2 Visión

```text
Para [usuario/población],
[producto] es [tipo de solución]
que permite [beneficio principal].
A diferencia de [alternativa],
aporta [diferencial].
```

- [ ] Usuario principal.
- [ ] Problema.
- [ ] Beneficio.
- [ ] Diferencial.
- [ ] Sin imponer tecnología innecesaria.

## 9.3 Es / No es / Hace / No hace

- [ ] Es.
- [ ] No es.
- [ ] Hace.
- [ ] No hace.
- [ ] Fuera de alcance.

---

# 10. Alcance y MVP

## 10.1 Alcance

- [ ] Incluido.
- [ ] Excluido.
- [ ] Actores incluidos.
- [ ] Procesos incluidos.
- [ ] Datos incluidos.
- [ ] Integraciones incluidas.
- [ ] Restricciones.
- [ ] Supuestos.
- [ ] Dependencias.

## 10.2 MVP

- [ ] Problema principal atendido.
- [ ] Usuario principal.
- [ ] Flujo de valor principal.
- [ ] Funciones mínimas.
- [ ] Resultado esperado.
- [ ] Hipótesis que valida.
- [ ] Métricas de validación.
- [ ] Restricciones.
- [ ] Riesgos.
- [ ] Fuera del MVP.

## 10.3 Control de alcance

Por funcionalidad propuesta:

- [ ] Responde a una necesidad.
- [ ] Aporta al objetivo.
- [ ] Es necesaria para esta entrega.
- [ ] Puede implementarse en tiempo.
- [ ] No pertenece mejor a una versión posterior.

---

# 11. SRS — Especificación de Requisitos

## 11.1 Encabezado

- [ ] Producto.
- [ ] Versión.
- [ ] Propósito.
- [ ] Alcance.
- [ ] Definiciones.
- [ ] Actores.
- [ ] Sistemas externos.
- [ ] Supuestos.
- [ ] Restricciones.
- [ ] Dependencias.
- [ ] Fuera de alcance.

## 11.2 Requisitos funcionales

Formato:

```text
ID: RF-001
Nombre:
Actor:
Fuente:
Necesidad relacionada:
Prioridad:
Estado:
Descripción: El sistema deberá...
Precondiciones:
Entradas:
Procesamiento/reglas:
Resultado esperado:
Excepciones:
Criterios de aceptación:
```

Por RF:

- [ ] ID único.
- [ ] Una capacidad principal.
- [ ] Actor identificado.
- [ ] Fuente.
- [ ] Necesidad relacionada.
- [ ] Prioridad.
- [ ] Entradas.
- [ ] Resultado esperado.
- [ ] Condiciones de éxito.
- [ ] Excepciones relevantes.
- [ ] Verificabilidad.

## 11.3 Requisitos no funcionales

Considerar:

- [ ] Seguridad.
- [ ] Privacidad.
- [ ] Rendimiento.
- [ ] Disponibilidad.
- [ ] Confiabilidad.
- [ ] Recuperabilidad.
- [ ] Usabilidad.
- [ ] Accesibilidad.
- [ ] Compatibilidad.
- [ ] Interoperabilidad.
- [ ] Escalabilidad.
- [ ] Mantenibilidad.
- [ ] Portabilidad.
- [ ] Auditabilidad.
- [ ] Observabilidad.
- [ ] Integridad de datos.

Formato:

```text
ID: RNF-[CAT]-001
Categoría:
Fuente:
Prioridad:
Requisito:
Condición observable:
Método de verificación:
```

- [ ] Evitar términos vagos como “rápido”.
- [ ] Evitar “fácil”.
- [ ] Evitar “amigable”.
- [ ] Evitar “seguro” sin explicar condición.
- [ ] No inventar porcentajes o tiempos.
- [ ] Marcar métricas propuestas como pendientes de validación.

## 11.4 Calidad de requisitos

Por cada requisito:

- [ ] Necesario.
- [ ] Atómico.
- [ ] Claro.
- [ ] No ambiguo.
- [ ] Consistente.
- [ ] Factible.
- [ ] Verificable.
- [ ] Trazable.
- [ ] Priorizado.
- [ ] Independiente de implementación cuando sea posible.

---

# 12. Reglas del dominio / negocio

Asignar:

```text
RN-001
RN-002
```

Por regla:

- [ ] Fuente.
- [ ] Descripción.
- [ ] Condición.
- [ ] Acción/consecuencia.
- [ ] Excepciones.
- [ ] RF relacionados.
- [ ] Casos de prueba relacionados.

Revisar:

- [ ] Rangos.
- [ ] Estados permitidos.
- [ ] Transiciones.
- [ ] Límites.
- [ ] Cálculos.
- [ ] Roles.
- [ ] Permisos.
- [ ] Ownership.
- [ ] Fechas.
- [ ] Duplicados.
- [ ] Validaciones.
- [ ] Políticas de eliminación.
- [ ] Reglas regulatorias.

---

# 13. UX, interacción y accesibilidad

## 13.1 Usuarios

- [ ] Identificar perfiles relevantes.
- [ ] Evitar inventar personas como si fueran resultados reales.
- [ ] Relacionar perfiles con evidencia disponible.
- [ ] Identificar capacidades y limitaciones relevantes.
- [ ] Identificar contexto de uso.

## 13.2 Flujos

- [ ] Flujo principal.
- [ ] Flujos alternativos.
- [ ] Errores.
- [ ] Recuperación.
- [ ] Estados vacíos.
- [ ] Confirmaciones.
- [ ] Feedback al usuario.
- [ ] Separar claramente flujo UX de diagrama de secuencia.
- [ ] Usar swimlanes cuando ayuden a distinguir responsabilidades.
- [ ] Verificar coherencia con reglas de negocio y estados del dominio.
- [ ] Evitar documentar como UX comportamientos internos que el usuario no observa.
- [ ] Relacionar flujos críticos con HU/RF cuando aporte trazabilidad.

## 13.3 Prototipos — si aplica

- [ ] Wireframes.
- [ ] Prototipo navegable.
- [ ] Pantallas clave.
- [ ] Navegación coherente.
- [ ] Estados de error.
- [ ] Estados de carga.
- [ ] Estados sin información.

## 13.4 Accesibilidad

- [ ] Contraste adecuado.
- [ ] Navegación comprensible.
- [ ] Etiquetas claras.
- [ ] No depender únicamente del color.
- [ ] Compatibilidad con teclado cuando aplique.
- [ ] Texto alternativo cuando aplique.
- [ ] Lenguaje adecuado a la población.

---

# 14. Product Backlog

## 14.1 Entrada

Antes de crear historias:

- [ ] Problema entendido.
- [ ] Necesidades identificadas.
- [ ] MVP delimitado.
- [ ] SRS mínimo disponible.
- [ ] Actores conocidos.
- [ ] Reglas principales conocidas.

## 14.2 Épicas

- [ ] Cada épica representa valor.
- [ ] Está relacionada con necesidades/requisitos.
- [ ] Evitar épicas puramente técnicas salvo justificación.
- [ ] No imponer cantidad fija salvo requerimiento académico.

## 14.3 Historias de usuario

```text
Como [rol],
quiero [acción],
para [beneficio].
```

Por historia:

- [ ] ID.
- [ ] Épica.
- [ ] Rol.
- [ ] Acción.
- [ ] Beneficio.
- [ ] Necesidad relacionada.
- [ ] RF/RNF relacionado.
- [ ] Prioridad.
- [ ] Estimación.
- [ ] Dependencias.
- [ ] Criterios de aceptación.

## 14.4 INVEST

- [ ] Independent.
- [ ] Negotiable.
- [ ] Valuable.
- [ ] Estimable.
- [ ] Small.
- [ ] Testable.

## 14.5 Priorización

Puede utilizarse:

- [ ] MoSCoW.
- [ ] Valor vs esfuerzo.
- [ ] Riesgo.
- [ ] Dependencias.
- [ ] Impacto.
- [ ] Prioridad académica.

- [ ] Priorizar MVP.
- [ ] Ordenar dependencias.
- [ ] Identificar historias críticas.
- [ ] No imponer cantidad fija de historias salvo consigna.

---

# 15. Criterios de aceptación

Por historia/requisito:

- [ ] Camino exitoso.
- [ ] Campos obligatorios.
- [ ] Validaciones.
- [ ] Reglas de negocio.
- [ ] Resultado esperado.
- [ ] Flujo alternativo.
- [ ] Errores.
- [ ] Permisos.
- [ ] Límites.
- [ ] Consistencia con SRS.

Formato opcional:

```text
Dado...
Cuando...
Entonces...
```

---

# 16. Definition of Ready

Una historia puede considerarse Ready cuando:

- [ ] Está correctamente redactada.
- [ ] Tiene épica.
- [ ] Tiene RF/RNF asociados cuando corresponda.
- [ ] Tiene fuente o necesidad asociada.
- [ ] Tiene prioridad.
- [ ] Tiene estimación.
- [ ] Tiene criterios de aceptación.
- [ ] Tiene reglas identificadas.
- [ ] Tiene datos identificados.
- [ ] Tiene actores.
- [ ] Tiene precondiciones.
- [ ] Tiene alternativas importantes.
- [ ] Tiene dependencias.
- [ ] Tiene riesgos.
- [ ] Es suficientemente pequeña.
- [ ] No contradice el SRS.
- [ ] No tiene bloqueos críticos.

---

# 17. Definition of Done

Una historia puede considerarse Done cuando:

- [ ] Está implementada.
- [ ] Compila/ejecuta correctamente.
- [ ] Cumple criterios de aceptación.
- [ ] Pasó pruebas previstas.
- [ ] No introduce defectos críticos conocidos.
- [ ] Se revisó el código cuando corresponde.
- [ ] Se actualizó documentación afectada.
- [ ] Se actualizaron diagramas si cambió el diseño.
- [ ] Se actualizaron requisitos si cambió comportamiento.
- [ ] Se actualizó trazabilidad.
- [ ] Existe evidencia verificable.
- [ ] Fue aceptada por quien corresponda.

---

# 18. Refinamiento de historias críticas

Por historia crítica:

- [ ] ID.
- [ ] Objetivo.
- [ ] Beneficio.
- [ ] Actor.
- [ ] Precondiciones.
- [ ] Entradas.
- [ ] Flujo principal.
- [ ] Alternativas.
- [ ] Excepciones.
- [ ] Reglas.
- [ ] Entidades.
- [ ] Integraciones.
- [ ] Riesgos.
- [ ] Dependencias.
- [ ] Criterios.
- [ ] Pruebas esperadas.

---

# 19. Modelado del sistema

> Crear diagramas porque explican algo, no únicamente para aumentar el número de entregables.

## 19.1 Estrategia de modelado

Antes de crear diagramas:

- [ ] Identificar los diagramas obligatorios según consigna/rúbrica.
- [ ] Identificar diagramas adicionales que realmente aportan comprensión.
- [ ] Determinar qué pregunta responde cada diagrama.
- [ ] Diferenciar vistas de negocio, análisis, diseño, datos, arquitectura, UX y despliegue.
- [ ] Identificar qué diagramas serán principales y cuáles complementarios.
- [ ] Identificar el documento principal donde se mostrará cada diagrama.
- [ ] Evitar repetir la misma imagen en múltiples documentos sin necesidad.
- [ ] Evitar dos diagramas que pretendan explicar exactamente lo mismo.
- [ ] Mantener trazabilidad con RF/HU/reglas cuando corresponda.
- [ ] Planificar la legibilidad antes de intentar representar “todo” en una sola imagen.
- [ ] Definir si conviene una vista global + vistas por módulo.
- [ ] Determinar formato fuente y formato render.
- [ ] Definir convención de nombres por tipo y alcance.

Ejemplo de nomenclatura:

```text
diagrama-casos-uso-compras.puml
diagrama-casos-uso-compras.png

diagrama-clases-dominio-general.puml
diagrama-clases-inventario.puml
```

## 19.2 Modelo de contexto

- [ ] Sistema central.
- [ ] Actores humanos.
- [ ] Sistemas externos.
- [ ] Límites.
- [ ] Entradas.
- [ ] Salidas.
- [ ] Integraciones.
- [ ] Responsabilidades externas al sistema.
- [ ] No modelar detalles internos innecesarios en una vista de contexto.

## 19.3 Diagramas de actividad / negocio

Utilizar cuando exista un proceso, flujo de valor o comportamiento procedural que se beneficie de esta vista.

- [ ] Inicio y fin claramente identificados.
- [ ] Actividades ordenadas.
- [ ] Decisiones con condiciones comprensibles.
- [ ] Caminos alternativos coherentes.
- [ ] Paralelismo correctamente representado cuando exista.
- [ ] Swimlanes cuando ayuden a separar responsabilidades.
- [ ] Coherencia con alcance.
- [ ] Coherencia con requisitos.
- [ ] Coherencia con reglas de negocio.
- [ ] No confundir un diagrama de actividad con uno de secuencia.
- [ ] Si representa negocio, evitar introducir detalles técnicos innecesarios.

## 19.4 Diagramas de casos de uso — si aplica

Por caso de uso/modelo:

- [ ] Actor principal.
- [ ] Actores secundarios.
- [ ] Objetivo observable para el actor.
- [ ] Precondiciones cuando se documente especificación textual.
- [ ] Flujo principal cuando se documente especificación textual.
- [ ] Alternativas.
- [ ] Postcondiciones.
- [ ] Alineación con RF/HU.
- [ ] `include`/`extend` utilizados correctamente.
- [ ] El sistema no aparece como actor de sí mismo.
- [ ] No convertir cada operación interna del sistema en caso de uso.
- [ ] No convertir cada RF automáticamente en un óvalo.
- [ ] Agrupar por dominio/módulo cuando una vista global pierda legibilidad.
- [ ] Mantener una vista global únicamente si sigue siendo útil.
- [ ] Evitar exceso de líneas cruzadas.
- [ ] Mantener actores y permisos coherentes con SRS.

Regla práctica:

> Si para leer el diagrama hay que hacer zoom extremo, seguir decenas de líneas cruzadas o reducir el texto hasta volverlo ilegible, dividirlo por áreas funcionales.

## 19.5 Diagramas de clases

- [ ] Clases relevantes.
- [ ] Responsabilidades.
- [ ] Atributos relevantes.
- [ ] Operaciones solo si aportan valor.
- [ ] Relaciones.
- [ ] Multiplicidades.
- [ ] Composición cuando corresponda.
- [ ] Agregación solo cuando tenga semántica útil.
- [ ] Herencia solo cuando tenga sentido.
- [ ] No confundir pantalla con entidad.
- [ ] No confundir tabla con clase automáticamente.
- [ ] Diferenciar modelo conceptual UML del modelo físico de persistencia.
- [ ] No utilizar un DER como sustituto de un diagrama de clases.
- [ ] Evitar copiar todas las columnas físicas de la base de datos.
- [ ] Crear una vista general del dominio cuando aporte orientación.
- [ ] Crear vistas por módulo cuando la vista completa pierda legibilidad.
- [ ] Mantener coherencia entre vista global y vistas de detalle.
- [ ] Mantener coherencia con modelo de datos e implementación cuando exista.

## 19.6 Diagramas de estados

Crear únicamente para entidades o procesos con un ciclo de vida significativo.

- [ ] Entidad/proceso modelado claramente identificado.
- [ ] Estado inicial.
- [ ] Estados finales cuando correspondan.
- [ ] Estados permitidos.
- [ ] Transiciones válidas.
- [ ] Evento/acción que provoca cada transición.
- [ ] Guardas/condiciones cuando sean necesarias.
- [ ] Transiciones prohibidas coherentes con reglas de negocio.
- [ ] Estados coinciden con SRS.
- [ ] Estados coinciden con reglas de negocio.
- [ ] Estados coinciden con modelo de datos.
- [ ] Estados coinciden con implementación si ya existe.
- [ ] Separar máquinas de estados independientes.
- [ ] No crear un “mega diagrama de estados del sistema” únicamente para centralizar.
- [ ] No crear estados artificiales para cumplir una cantidad de diagramas.

## 19.7 Diagramas de secuencia

Seleccionar flujos críticos o representativos, no necesariamente cada CRUD.

- [ ] Actor.
- [ ] Interfaz/frontera.
- [ ] Controlador/API.
- [ ] Servicio/caso de uso.
- [ ] Dominio cuando aporte valor.
- [ ] Persistencia.
- [ ] Sistema externo cuando corresponda.
- [ ] Canal realtime/mensajería cuando corresponda.
- [ ] Validaciones.
- [ ] Errores.
- [ ] Alternativas mediante `alt` cuando corresponda.
- [ ] Opcionales mediante `opt` cuando corresponda.
- [ ] Respuesta final.
- [ ] Cambios de estado importantes cuando aporten comprensión.
- [ ] Efectos transaccionales importantes.
- [ ] Coherencia con flujo UX.
- [ ] Coherencia con requisitos y reglas.
- [ ] No confundir flujo UX con secuencia.
- [ ] Evitar detalles internos que no aporten al objetivo de la vista.

## 19.8 Diagramas de componentes

- [ ] Componentes/módulos principales.
- [ ] Responsabilidades.
- [ ] Dependencias.
- [ ] Interfaces.
- [ ] Comunicación.
- [ ] Sistemas/servicios externos cuando corresponda.
- [ ] Persistencia mostrada con el nivel de detalle adecuado.
- [ ] Coherencia con arquitectura documentada.
- [ ] Coherencia con ADR.
- [ ] No confundir componente con clase.
- [ ] No confundir componente con pantalla.
- [ ] No confundir componente con tabla.
- [ ] Separar frontend/backend u otros subsistemas cuando una única vista se congestione.

## 19.9 Diagramas de despliegue

- [ ] Nodos/hosts.
- [ ] Entornos reales o planificados.
- [ ] Componentes/artefactos desplegados.
- [ ] Base de datos.
- [ ] Comunicación entre nodos.
- [ ] Protocolos relevantes.
- [ ] Contenedores cuando formen parte real del despliegue.
- [ ] Diferenciar desarrollo, pruebas, demo y producción cuando aporte valor.
- [ ] No inventar infraestructura no confirmada.
- [ ] No exponer IP, credenciales, tokens o secretos.
- [ ] Coherencia con documentación de despliegue/operación.

## 19.10 Modelo entidad-relación y vistas de datos

Cuando el proyecto use persistencia relacional:

- [ ] Entidades/tablas principales.
- [ ] PK.
- [ ] FK.
- [ ] Relaciones.
- [ ] Cardinalidades.
- [ ] Cabeceras/detalles.
- [ ] Catálogos.
- [ ] Tablas puente cuando correspondan.
- [ ] Coherencia con el modelo relacional documentado.
- [ ] Diferenciar DER de diagrama de clases UML.
- [ ] Evitar una imagen global ilegible.
- [ ] Dividir por dominios cuando sea necesario.
- [ ] Mantener una vista global si aporta orientación.

## 19.11 Referencias visuales complementarias

Pueden conservarse cuando aporten contexto aunque no sean el artefacto principal exigido por la materia:

- [ ] Árbol de problemas.
- [ ] Árbol de soluciones.
- [ ] Flujos UX.
- [ ] BPMN.
- [ ] DFD.
- [ ] C4 / arquitectura de contexto o contenedores.
- [ ] Mapas de navegación.
- [ ] Wireframes.
- [ ] Mockups.
- [ ] ER.
- [ ] Otros modelos específicos del dominio.

Para cada uno:

- [ ] Está claramente identificado su propósito.
- [ ] No se presenta como sustituto incorrecto de otro tipo de diagrama.
- [ ] Tiene relación con una decisión, requisito o documento concreto.
- [ ] Aporta información real y no únicamente decoración.
- [ ] Su ubicación documental tiene sentido.
- [ ] No duplica innecesariamente otro artefacto.

## 19.12 Gobierno y calidad de diagramas

### Identidad y nombres

- [ ] El nombre del archivo identifica el tipo de diagrama.
- [ ] El nombre identifica su alcance cuando existen varios del mismo tipo.
- [ ] El título interno coincide con el propósito.
- [ ] Fuente y render utilizan preferentemente el mismo nombre base.
- [ ] No quedan referencias al nombre anterior después de un rename.

### Fuente y render

- [ ] Existe fuente editable cuando el artefacto es generado.
- [ ] Existe render cuando la documentación necesita una imagen.
- [ ] El render corresponde a la versión actual de la fuente.
- [ ] No quedan renders antiguos después de renombrar.
- [ ] No existen fuentes sin render cuando este es requerido.
- [ ] No existen renders generados huérfanos sin fuente, salvo excepción documentada.

### Legibilidad

- [ ] Se probó el diagrama al tamaño real del documento final.
- [ ] No requiere zoom extremo.
- [ ] El texto es legible.
- [ ] Las relaciones se distinguen.
- [ ] No hay cruces excesivos.
- [ ] Si es demasiado grande, se evaluó dividirlo.
- [ ] Si se divide, se evaluó conservar una vista general de orientación.
- [ ] Cada imagen mantiene suficiente resolución.

### Integración documental

- [ ] Tiene un documento principal.
- [ ] Tiene contexto antes/después de la figura.
- [ ] Tiene título o descripción.
- [ ] Se referencia su fuente editable cuando corresponde.
- [ ] No se incrusta repetidamente en documentos donde bastaría un enlace.
- [ ] La documentación explica qué representa y qué no representa.

### Coherencia transversal

- [ ] Coincide con requisitos.
- [ ] Coincide con reglas de negocio.
- [ ] Coincide con backlog/HU.
- [ ] Coincide con UX.
- [ ] Coincide con arquitectura.
- [ ] Coincide con datos.
- [ ] Coincide con implementación si ya existe.
- [ ] Coincide con pruebas/validaciones cuando corresponda.

## 19.13 Matriz de cobertura de modelado

Una matriz simple ayuda a controlar el conjunto sin obligar a crear diagramas innecesarios:

| Artefacto | ¿Aplica? | Obligatorio por materia | Fuente editable | Render | Documento principal | Legible | Actualizado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Contexto | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Actividad / negocio | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Casos de uso | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Clases | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Estados | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Secuencia | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Componentes | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Despliegue | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| ER | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| C4 / contenedores | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Flujo UX | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| BPMN / DFD / otro | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |

---

# 20. Arquitectura

## 20.1 Drivers arquitectónicos

- [ ] Requisitos funcionales críticos.
- [ ] Seguridad.
- [ ] Rendimiento.
- [ ] Escalabilidad.
- [ ] Disponibilidad.
- [ ] Integraciones.
- [ ] Restricciones tecnológicas.
- [ ] Tiempo disponible.
- [ ] Experiencia del equipo.

## 20.2 Diseño

- [ ] Componentes principales.
- [ ] Responsabilidades.
- [ ] Dependencias.
- [ ] Comunicación.
- [ ] Persistencia.
- [ ] Interfaces externas.
- [ ] Manejo de errores.
- [ ] Configuración.
- [ ] Vista lógica de alto nivel cuando aporte valor.
- [ ] Vista de componentes cuando aporte valor.
- [ ] Vista de contenedores/C4 cuando aporte valor.
- [ ] Vista de despliegue cuando aplique.
- [ ] Límites entre módulos.
- [ ] Dependencias permitidas y prohibidas.
- [ ] Coherencia entre diagramas arquitectónicos y estructura real del proyecto.

## 20.3 Decisiones arquitectónicas importantes

Registrar:

```text
ADR-001
Decisión:
Contexto:
Alternativas:
Decisión elegida:
Razón:
Consecuencias:
```

- [ ] No elegir tecnologías únicamente por moda.
- [ ] Registrar restricciones impuestas por la materia.
- [ ] Diferenciar requisito de preferencia técnica.

---

# 21. Datos y persistencia

## 21.1 Entidades

- [ ] Entidades principales.
- [ ] Detalles.
- [ ] Catálogos.
- [ ] Historiales.
- [ ] Auditoría.
- [ ] Eventos.
- [ ] Propósito de cada entidad.
- [ ] Diferenciar entidades de dominio de tablas físicas cuando sea relevante.

## 21.2 Modelo entidad-relación — si aplica

- [ ] Entidades/tablas principales representadas.
- [ ] PK.
- [ ] FK.
- [ ] Cardinalidades.
- [ ] Relaciones identificables.
- [ ] Tablas puente cuando correspondan.
- [ ] Cabecera/detalle correctamente representado.
- [ ] Catálogos correctamente relacionados.
- [ ] Coherencia con el esquema documentado.
- [ ] Diferenciar ER de diagrama de clases UML.
- [ ] Legibilidad al tamaño de entrega.
- [ ] Dividir el ER si la vista completa resulta ilegible.
- [ ] Mantener una vista general si aporta orientación.

## 21.3 Modelo relacional

Por tabla:

- [ ] Nombre.
- [ ] Propósito.
- [ ] PK.
- [ ] FK.
- [ ] Campos obligatorios.
- [ ] Campos opcionales.
- [ ] Tipos.
- [ ] Unique.
- [ ] Checks.
- [ ] Índices.
- [ ] Defaults.
- [ ] Estados.
- [ ] Política de eliminación/desactivación.
- [ ] Campos de auditoría cuando correspondan.
- [ ] Snapshot histórico cuando una operación deba preservar valores del momento.

## 21.4 Diccionario de datos

Por campo:

- [ ] Nombre.
- [ ] Descripción.
- [ ] Tipo.
- [ ] Longitud.
- [ ] PK/FK.
- [ ] Nullability.
- [ ] Default.
- [ ] Restricciones.
- [ ] Valores permitidos.
- [ ] Ejemplo si aporta claridad.
- [ ] Unidad de medida cuando corresponda.
- [ ] Semántica temporal cuando corresponda.

## 21.5 Integridad

- [ ] Evitar registros huérfanos.
- [ ] Evitar duplicados cuando corresponda.
- [ ] Validar rangos.
- [ ] Validar estados.
- [ ] Validar fechas.
- [ ] Definir eliminación.
- [ ] Definir historial.
- [ ] Mantener consistencia cabecera/detalle.
- [ ] Mantener atomicidad en operaciones relacionadas cuando corresponda.
- [ ] Evitar estados parciales después de fallos.
- [ ] Definir restricciones reforzadas por base de datos cuando aporten seguridad.

## 21.6 Coherencia requisitos ↔ datos

- [ ] Rangos del SRS coinciden con restricciones.
- [ ] Estados coinciden.
- [ ] Listas controladas coinciden.
- [ ] Permisos coinciden.
- [ ] El modelo permite responder las consultas requeridas.
- [ ] El modelo soporta los flujos críticos.
- [ ] Los diagramas de clases y ER no se contradicen.
- [ ] Los diagramas de estados coinciden con valores persistidos.
- [ ] Los datos históricos necesarios no se pierden por sobrescritura.

---

# 22. Integraciones y APIs — si aplica

Por integración:

- [ ] Sistema externo.
- [ ] Propósito.
- [ ] Dirección del flujo.
- [ ] Datos intercambiados.
- [ ] Autenticación.
- [ ] Autorización.
- [ ] Formato.
- [ ] Validación.
- [ ] Manejo de errores.
- [ ] Timeouts.
- [ ] Reintentos.
- [ ] Disponibilidad esperada.
- [ ] Dependencias.
- [ ] Datos sensibles involucrados.

Por endpoint relevante:

- [ ] Método.
- [ ] Ruta.
- [ ] Entrada.
- [ ] Salida.
- [ ] Errores.
- [ ] Permisos.
- [ ] Requisito relacionado.

---

# 23. Seguridad y privacidad

## 23.1 Identidad y acceso

- [ ] ¿Requiere autenticación?
- [ ] Roles definidos.
- [ ] Permisos definidos.
- [ ] Principio de mínimo privilegio.
- [ ] Ownership de datos.
- [ ] Sesiones protegidas.
- [ ] Recuperación de acceso, si aplica.

## 23.2 Datos

- [ ] Identificar datos personales.
- [ ] Identificar datos sensibles.
- [ ] Minimizar recopilación.
- [ ] Limitar exposición.
- [ ] Definir retención.
- [ ] Definir eliminación.
- [ ] Proteger secretos.
- [ ] No guardar secretos en repositorio.
- [ ] Cifrado cuando corresponda.
- [ ] Auditoría cuando corresponda.

## 23.3 Riesgos

- [ ] Entrada maliciosa.
- [ ] Escalada de privilegios.
- [ ] Acceso indebido.
- [ ] Filtración de datos.
- [ ] Pérdida de datos.
- [ ] Dependencias inseguras.
- [ ] Configuraciones inseguras.

---

# 24. Analítica, indicadores o DSS — únicamente si aporta valor

Antes de incluirlo:

- [ ] ¿Existe una decisión que deba apoyarse?
- [ ] ¿Existe una pregunta real que responder?
- [ ] ¿Existen los datos necesarios?
- [ ] ¿El usuario necesita indicadores?
- [ ] ¿Un dashboard es realmente útil?
- [ ] ¿Un reporte sería suficiente?
- [ ] ¿No aplica? Documentar la decisión y omitir.

Por indicador:

- [ ] Nombre.
- [ ] Pregunta.
- [ ] Usuario.
- [ ] Datos requeridos.
- [ ] Fórmula.
- [ ] Periodicidad.
- [ ] Filtros.
- [ ] Visualización.
- [ ] Umbral, si existe.
- [ ] Acción o decisión que permite.
- [ ] Requisito relacionado.

- [ ] No crear KPIs únicamente porque “el proyecto necesita dashboard”.
- [ ] No mostrar datos que el sistema no puede obtener.

---

# 25. Estrategia de pruebas

## 25.1 Plan

- [ ] Qué se probará.
- [ ] Qué no se probará.
- [ ] Responsables.
- [ ] Ambiente.
- [ ] Datos de prueba.
- [ ] Criterios de entrada.
- [ ] Criterios de salida.

## 25.2 Tipos posibles

- [ ] Unitarias.
- [ ] Integración.
- [ ] Sistema.
- [ ] End-to-end.
- [ ] Aceptación.
- [ ] Usabilidad.
- [ ] Seguridad.
- [ ] Rendimiento.
- [ ] Compatibilidad.
- [ ] Accesibilidad.
- [ ] Regresión.

## 25.3 Caso de prueba

```text
ID: CP-001
Requisito:
Historia:
Precondiciones:
Datos:
Pasos:
Resultado esperado:
Resultado obtenido:
Estado:
Evidencia:
```

- [ ] Cada requisito importante tiene forma de comprobarse.
- [ ] Cada criterio de aceptación puede verificarse.
- [ ] Los fallos quedan registrados.
- [ ] Los defectos corregidos vuelven a probarse.

---

# 26. Trazabilidad integral

Cadena recomendada:

```text
Problema / oportunidad
        ↓
Hallazgo / evidencia
        ↓
Necesidad
        ↓
Objetivo
        ↓
RF / RNF / regla
        ↓
Épica / historia / caso de uso
        ↓
UX / modelo / API / datos
        ↓
Implementación
        ↓
Prueba
        ↓
Evidencia
        ↓
Resultado / validación
```

## 26.1 Matriz

Por elemento:

- [ ] Problema relacionado.
- [ ] Hallazgo.
- [ ] Necesidad.
- [ ] Requisito.
- [ ] Historia.
- [ ] Modelo.
- [ ] Componente.
- [ ] Prueba.
- [ ] Evidencia.
- [ ] Estado.

## 26.2 Validaciones

- [ ] Todo RF tiene fuente.
- [ ] Todo RF responde a una necesidad.
- [ ] Toda HU importante responde a un requisito.
- [ ] Toda funcionalidad del MVP aparece en requisitos/backlog.
- [ ] Toda regla crítica aparece en pruebas.
- [ ] Todo requisito implementado tiene evidencia.
- [ ] No existen historias “huérfanas” sin justificación.
- [ ] No existen funcionalidades implementadas accidentalmente fuera del alcance.

---

# 27. Gestión de riesgos

Crear registro:

```text
R-001
Riesgo:
Causa:
Probabilidad:
Impacto:
Prioridad:
Mitigación:
Contingencia:
Responsable:
Estado:
```

Considerar:

- [ ] Alcance.
- [ ] Tiempo.
- [ ] Personas.
- [ ] Tecnología.
- [ ] Datos.
- [ ] Integraciones.
- [ ] Seguridad.
- [ ] Dependencias.
- [ ] Disponibilidad de participantes.
- [ ] Cambios de requerimientos.
- [ ] Falta de evidencia.
- [ ] Restricciones académicas.

- [ ] Revisar riesgos periódicamente.
- [ ] No confundir riesgo con problema ya ocurrido.

---

# 28. Ética e impacto

Especialmente importante con poblaciones objetivo:

- [ ] Identificar posibles daños.
- [ ] Identificar grupos vulnerables.
- [ ] Evaluar sesgos.
- [ ] Evitar discriminación.
- [ ] Evaluar exclusión digital.
- [ ] Evaluar accesibilidad.
- [ ] Evaluar uso indebido.
- [ ] Evaluar consecuencias de errores.
- [ ] Proteger privacidad.
- [ ] Evitar decisiones automatizadas injustificadas.
- [ ] Definir supervisión humana cuando corresponda.

---

# 29. Plan de implementación

## 29.1 Preparación

- [ ] Repositorio creado.
- [ ] README.
- [ ] Convenciones.
- [ ] Entorno.
- [ ] Dependencias.
- [ ] Configuración.
- [ ] Variables de entorno.
- [ ] Datos iniciales.
- [ ] Estrategia de ramas si aplica.
- [ ] Automatizaciones básicas de calidad si aplican.
- [ ] Responsables o ownership técnico identificados cuando aporte valor.

## 29.2 Iteraciones

- [ ] Ordenar historias.
- [ ] Identificar dependencias.
- [ ] Identificar camino crítico.
- [ ] Seleccionar primera iteración.
- [ ] Definir objetivo de iteración.
- [ ] Identificar entregable incremental.
- [ ] Definir capacidad aproximada del equipo.
- [ ] Evitar comprometer trabajo sin dependencias resueltas.
- [ ] Mantener separación entre trabajo comprometido y backlog futuro.

## 29.3 Tablero

Estados sugeridos — adaptar a la metodología real:

- [ ] Backlog.
- [ ] Ready.
- [ ] In Progress.
- [ ] Blocked, si aporta valor.
- [ ] Review.
- [ ] Testing, si el equipo utiliza una etapa separada.
- [ ] Done.

- [ ] Cada columna tiene significado claro.
- [ ] No crear columnas que el equipo no utilizará.
- [ ] Los estados del tablero coinciden con la Definition of Ready/Done.
- [ ] Los bloqueos visibles tienen causa y responsable de seguimiento.

## 29.4 Gestión de Sprint — si se utiliza Scrum

### Sprint Planning

- [ ] Sprint Goal definido.
- [ ] Historias comprometidas identificadas.
- [ ] Dependencias revisadas.
- [ ] Capacidad del equipo considerada.
- [ ] Responsables/coordinación definidos sin convertir Scrum en asignación rígida.
- [ ] Riesgos del Sprint identificados.
- [ ] Criterio de revisión al final del Sprint definido.

### Durante el Sprint

- [ ] Tablero actualizado.
- [ ] Bloqueos registrados.
- [ ] Cambios de alcance del Sprint justificados.
- [ ] Evidencia de avance mantenida.
- [ ] Documentación afectada actualizada junto con la implementación.

### Sprint Review

- [ ] Incremento identificado.
- [ ] HUs terminadas verificadas.
- [ ] HUs incompletas explicitadas.
- [ ] Feedback de PO/stakeholder registrado cuando exista.
- [ ] No registrar aprobación ficticia.
- [ ] Cambios al Product Backlog derivados de la review registrados.

### Sprint Retrospective

- [ ] Qué salió bien.
- [ ] Qué no salió bien.
- [ ] Problemas técnicos.
- [ ] Problemas de proceso.
- [ ] Problemas de comunicación.
- [ ] Problemas de herramientas/Git cuando correspondan.
- [ ] Deuda documental identificada.
- [ ] Acciones de mejora concretas.
- [ ] Decisiones realmente acordadas diferenciadas de simples propuestas.
- [ ] Lecciones trasladables al siguiente Sprint.

---

# 30. Ready to Sprint / Ready to Develop

Antes de programar:

- [ ] El problema está comprendido.
- [ ] Existe evidencia suficiente.
- [ ] Los usuarios están identificados.
- [ ] El alcance está definido.
- [ ] Fuera de alcance está definido.
- [ ] El MVP está delimitado.
- [ ] Los requisitos iniciales están baselined.
- [ ] Las reglas principales están claras.
- [ ] Las historias iniciales cumplen DoR.
- [ ] Los criterios de aceptación existen.
- [ ] Las dependencias están identificadas.
- [ ] Los riesgos principales están identificados.
- [ ] Los datos necesarios están definidos.
- [ ] La arquitectura mínima está definida.
- [ ] Las integraciones importantes están identificadas.
- [ ] La primera iteración está priorizada.
- [ ] Se sabe cómo probar lo primero que se construirá.
- [ ] La primera línea de código puede escribirse sin rehacer el análisis principal.

---

# 31. Seguimiento durante el desarrollo

## 31.1 En cada iteración

- [ ] Actualizar tablero.
- [ ] Revisar prioridades.
- [ ] Revisar riesgos.
- [ ] Registrar decisiones.
- [ ] Actualizar requisitos afectados.
- [ ] Actualizar trazabilidad.
- [ ] Actualizar diagramas relevantes.
- [ ] Registrar defectos.
- [ ] Mantener evidencias.
- [ ] Validar incrementos.
- [ ] Revisar documentación afectada por cambios de comportamiento.
- [ ] Revisar si cambió algún estado, relación, endpoint o flujo.
- [ ] Verificar que el render de diagramas siga sincronizado con su fuente.

## 31.2 Control de documentación por historia/cambio

Cuando una HU o cambio modifique el sistema:

- [ ] Identificar documentos afectados.
- [ ] Identificar diagramas afectados.
- [ ] Identificar requisitos/reglas afectados.
- [ ] Identificar pruebas afectadas.
- [ ] Identificar trazabilidad afectada.
- [ ] Registrar archivos creados/modificados si el equipo utiliza Manifest o mecanismo equivalente.
- [ ] No cerrar la HU con documentación conocida como desactualizada.

## 31.3 Revisión de integración

- [ ] Cambios integrados sobre una baseline actualizada.
- [ ] Conflictos resueltos sin perder documentación válida.
- [ ] Referencias a archivos verificadas después de renames/moves.
- [ ] No quedan duplicados accidentales por conflictos de Git.
- [ ] Se revisa `diff` antes de integrar cuando sea posible.
- [ ] Evidencias continúan apuntando a archivos existentes.

---

# 32. Gestión de cambios

Ante un cambio:

- [ ] Identificar origen.
- [ ] Registrar razón.
- [ ] Determinar impacto en problema/necesidad.
- [ ] Revisar SRS.
- [ ] Revisar RF/RNF.
- [ ] Revisar backlog.
- [ ] Revisar criterios.
- [ ] Revisar arquitectura.
- [ ] Revisar datos.
- [ ] Revisar UML.
- [ ] Revisar pruebas.
- [ ] Revisar plazo.
- [ ] Revisar riesgos.
- [ ] Revisar documentación de Sprint si el cambio afecta compromiso/resultado.
- [ ] Revisar OpenAPI/contratos si aplica.
- [ ] Revisar diagramas de estados si cambia un ciclo de vida.
- [ ] Revisar clases/ER si cambia el modelo.
- [ ] Revisar secuencias/UX si cambia un flujo.
- [ ] Revisar componentes/despliegue si cambia arquitectura.
- [ ] Actualizar trazabilidad.
- [ ] Registrar decisión importante en ADR/log de cambios.
- [ ] Retirar referencias a artefactos superseded.
- [ ] Regenerar renders derivados.
- [ ] Versionar nueva baseline cuando corresponda.

---

# 33. Validación de la solución

## 33.1 Validación funcional

- [ ] Cumple requisitos.
- [ ] Cumple historias.
- [ ] Cumple reglas.
- [ ] Cumple criterios de aceptación.

## 33.2 Validación con usuarios/stakeholders

- [ ] Identificar quién valida.
- [ ] Definir objetivo de validación.
- [ ] Preparar tareas.
- [ ] Registrar observaciones.
- [ ] Registrar dificultades.
- [ ] Registrar satisfacción cuando sea pertinente.
- [ ] Registrar cambios sugeridos.
- [ ] Diferenciar opinión de evidencia.

## 33.3 Validación del impacto

- [ ] Comparar con problema inicial.
- [ ] Revisar métricas de éxito.
- [ ] Identificar beneficios observados.
- [ ] Identificar beneficios todavía hipotéticos.
- [ ] Identificar limitaciones.

---

# 34. Despliegue y operación — si aplica

- [ ] Ambiente de desarrollo.
- [ ] Ambiente de pruebas.
- [ ] Ambiente de producción/demo.
- [ ] Configuración documentada.
- [ ] Variables seguras.
- [ ] Migraciones.
- [ ] Seeds.
- [ ] Backups.
- [ ] Logs.
- [ ] Monitoreo.
- [ ] Manejo de errores.
- [ ] Procedimiento de recuperación.
- [ ] Manual de instalación.
- [ ] Manual de uso cuando corresponda.

---

# 35. Evidencias

Organizar evidencia de:

- [ ] Relevamiento.
- [ ] Consentimientos cuando corresponda.
- [ ] Resultados.
- [ ] Requisitos.
- [ ] Backlog.
- [ ] Tablero.
- [ ] Diagramas y modelos.
- [ ] Fuentes editables de diagramas cuando corresponda.
- [ ] Prototipos.
- [ ] Implementación.
- [ ] Commits.
- [ ] Pruebas.
- [ ] Validaciones.
- [ ] Sprint Review cuando corresponda.
- [ ] Retrospectivas/lecciones aprendidas cuando corresponda.
- [ ] Resultados.
- [ ] Presentación.

Control:

- [ ] La evidencia realmente corresponde al proyecto.
- [ ] Tiene fecha cuando sea relevante.
- [ ] Es legible.
- [ ] No contiene información sensible innecesaria.
- [ ] No se utilizan capturas únicamente como decoración.
- [ ] No se marca como implementado algo únicamente documentado.
- [ ] No se marca como validado algo únicamente implementado.
- [ ] Cada captura está asociada a una HU, requisito, prueba o validación cuando corresponda.
- [ ] Los nombres/rutas de evidencia son estables.
- [ ] No existen capturas huérfanas importantes sin explicación.

---

# 36. Calidad documental

## 36.1 Calidad general

- [ ] Terminología consistente.
- [ ] IDs consistentes.
- [ ] Nombres consistentes.
- [ ] Versiones consistentes.
- [ ] No existen nombres de proyectos antiguos.
- [ ] No existen textos de plantilla sin reemplazar.
- [ ] No existen enlaces rotos.
- [ ] No existen imágenes faltantes.
- [ ] No existen archivos mencionados que no estén incluidos.
- [ ] No existen requisitos contradictorios.
- [ ] No existen métricas inventadas.
- [ ] No existen entrevistas inventadas.
- [ ] No existen resultados inventados.
- [ ] No existen tecnologías impuestas sin razón.
- [ ] Tablas legibles.
- [ ] Figuras legibles.
- [ ] Diagramas explicados.
- [ ] Ortografía revisada.
- [ ] Referencias correctamente citadas.
- [ ] Documentos con propósito claro.
- [ ] No existen secciones “pendiente” que ya hayan sido resueltas en documentación posterior.
- [ ] No existen duplicaciones extensas que puedan divergir entre sí.
- [ ] La documentación refleja el estado actual conocido, no únicamente la planificación inicial.
- [ ] Información histórica válida se distingue del current-state.

## 36.2 Auditoría automatizable del repositorio

Siempre que sea posible, realizar búsquedas globales o scripts para comprobar:

- [ ] Referencias Markdown a archivos inexistentes.
- [ ] Imágenes referenciadas inexistentes.
- [ ] Fuentes de diagramas referenciadas inexistentes.
- [ ] Renders generados sin fuente editable equivalente, cuando debería existir.
- [ ] Fuentes editables sin render requerido.
- [ ] Nombres antiguos después de renames.
- [ ] Archivos duplicados por conflictos o copias accidentales.
- [ ] Artefactos huérfanos no referenciados que podrían ser obsoletos.
- [ ] Placeholders (`TODO`, `TBD`, `Pendiente`) no intencionales.
- [ ] IDs duplicados de RF/RN/HU/ADR/riesgos.
- [ ] Rutas con diferencias de mayúsculas/minúsculas.
- [ ] Extensiones duplicadas o nombres erróneos.
- [ ] Capturas referenciadas desde la HU equivocada.
- [ ] Estados de trazabilidad evidentemente desactualizados.
- [ ] HUs de Sprint que no coinciden con backlog/sprint plan.
- [ ] Archivos superseded todavía referenciados.

> Un archivo no referenciado no es automáticamente incorrecto: puede ser histórico, evidencia o fuente auxiliar. Revisar antes de eliminar.

## 36.3 Calidad de diagramas y figuras

- [ ] Cada diagrama tiene propósito claro.
- [ ] Cada diagrama tiene fuente editable cuando corresponde.
- [ ] El render está actualizado.
- [ ] Fuente y render utilizan nombres coherentes.
- [ ] El diagrama es legible al tamaño real de entrega.
- [ ] No hay texto microscópico por intentar mostrar demasiada información.
- [ ] Los diagramas grandes fueron divididos cuando era necesario.
- [ ] Las vistas divididas mantienen coherencia entre sí.
- [ ] No se confunde flujo UX con secuencia.
- [ ] No se confunde ER con clases.
- [ ] No se confunde contenedores/C4 con despliegue UML.
- [ ] No se presenta un diagrama parcial como si cubriera todo el sistema.
- [ ] Cada imagen insertada tiene contexto.
- [ ] Las figuras complementarias se conservan cuando aportan valor.

## 36.4 Auditoría de coherencia transversal

Comprobar explícitamente:

- [ ] Problema ↔ hallazgos.
- [ ] Hallazgos ↔ necesidades.
- [ ] Necesidades ↔ requisitos.
- [ ] Requisitos ↔ reglas.
- [ ] Requisitos ↔ backlog/HU.
- [ ] HU ↔ criterios.
- [ ] HU ↔ UX.
- [ ] HU/RF ↔ casos de uso.
- [ ] Reglas/estados ↔ diagramas de estados.
- [ ] Flujos ↔ diagramas de secuencia.
- [ ] Dominio ↔ diagramas de clases.
- [ ] Clases ↔ ER/datos.
- [ ] Arquitectura ↔ componentes.
- [ ] Arquitectura ↔ despliegue.
- [ ] Implementación ↔ documentación current-state.
- [ ] Pruebas ↔ requisitos/HU.
- [ ] Evidencias ↔ pruebas/validación.
- [ ] Sprint ↔ historias realmente realizadas.

---

# 37. Informe final

Según la materia, considerar:

- [ ] Portada.
- [ ] Resumen ejecutivo.
- [ ] Introducción.
- [ ] Contexto.
- [ ] Problema.
- [ ] Justificación.
- [ ] Objetivos.
- [ ] Metodología.
- [ ] Relevamiento.
- [ ] Resultados.
- [ ] Necesidades.
- [ ] Alcance.
- [ ] MVP.
- [ ] Requisitos.
- [ ] Backlog.
- [ ] UX.
- [ ] UML.
- [ ] Arquitectura.
- [ ] Modelo de datos.
- [ ] Implementación.
- [ ] Pruebas.
- [ ] Validación.
- [ ] Resultados.
- [ ] Limitaciones.
- [ ] Riesgos.
- [ ] Conclusiones.
- [ ] Trabajo futuro.
- [ ] Bibliografía.
- [ ] Anexos.

---

# 38. Checklist final antes de entregar

## 38.1 Consigna

- [ ] Todos los puntos de la rúbrica están cubiertos.
- [ ] Formato correcto.
- [ ] Extensión correcta.
- [ ] Nombre correcto.
- [ ] Fecha correcta.
- [ ] Integrantes correctos.

## 38.2 Contenido

- [ ] Problema claro.
- [ ] Evidencia clara.
- [ ] Usuarios/población claros.
- [ ] Objetivos claros.
- [ ] Alcance claro.
- [ ] Requisitos claros.
- [ ] MVP claro.
- [ ] Backlog coherente.
- [ ] Diagramas coherentes.
- [ ] Datos coherentes.
- [ ] Seguridad considerada.
- [ ] Pruebas realizadas.
- [ ] Resultados documentados.
- [ ] Limitaciones reconocidas.
- [ ] Conclusiones responden a objetivos.

## 38.3 Coherencia transversal

- [ ] Problema → necesidades.
- [ ] Necesidades → requisitos.
- [ ] Requisitos → MVP.
- [ ] MVP → backlog.
- [ ] Backlog → UML.
- [ ] UML → arquitectura.
- [ ] Arquitectura → datos.
- [ ] Historias → implementación.
- [ ] Requisitos → pruebas.
- [ ] Pruebas → evidencia.
- [ ] Evidencia → conclusiones.

## 38.4 Archivos

- [ ] Todo archivo mencionado existe.
- [ ] Todo enlace funciona.
- [ ] Todo diagrama es legible.
- [ ] Toda imagen tiene contexto.
- [ ] Toda fuente editable requerida existe.
- [ ] Todo render requerido existe.
- [ ] Fuente y render corresponden a la misma versión.
- [ ] No quedan nombres antiguos después de renames.
- [ ] No quedan renders obsoletos importantes.
- [ ] No quedan archivos superseded todavía enlazados.
- [ ] No quedan imágenes huérfanas relevantes sin explicación.
- [ ] Repositorio accesible cuando corresponda.
- [ ] PDF final abre correctamente.
- [ ] Las figuras siguen legibles dentro del PDF final.
- [ ] No quedan comentarios internos.
- [ ] No quedan placeholders.

---

# 39. Cierre del proyecto

- [ ] Comparar resultado con objetivo general.
- [ ] Evaluar objetivos específicos.
- [ ] Enumerar requisitos terminados.
- [ ] Enumerar requisitos pendientes.
- [ ] Registrar alcance realmente implementado.
- [ ] Registrar defectos conocidos.
- [ ] Registrar limitaciones.
- [ ] Registrar deuda técnica relevante.
- [ ] Registrar riesgos pendientes.
- [ ] Registrar recomendaciones futuras.
- [ ] Registrar lecciones aprendidas.
- [ ] Preparar entrega final reproducible.

---

# 40. Orden recomendado para comenzar desde cero

1. [ ] Leer consigna y rúbrica.
2. [ ] Identificar entregables y diagramas obligatorios.
3. [ ] Crear ficha del proyecto.
4. [ ] Identificar organización/población objetivo.
5. [ ] Identificar stakeholders.
6. [ ] Comprender situación actual.
7. [ ] Formular problema.
8. [ ] Buscar evidencia.
9. [ ] Diseñar relevamiento.
10. [ ] Aplicar técnicas reales.
11. [ ] Analizar resultados.
12. [ ] Consolidar hallazgos.
13. [ ] Consolidar necesidades.
14. [ ] Formular objetivos.
15. [ ] Definir visión de solución.
16. [ ] Delimitar alcance.
17. [ ] Definir MVP.
18. [ ] Redactar SRS.
19. [ ] Redactar RF.
20. [ ] Redactar RNF.
21. [ ] Definir reglas del dominio.
22. [ ] Revisar calidad de requisitos.
23. [ ] Crear trazabilidad inicial.
24. [ ] Diseñar flujos/UX.
25. [ ] Crear épicas.
26. [ ] Crear historias.
27. [ ] Crear criterios de aceptación.
28. [ ] Priorizar.
29. [ ] Revisar INVEST.
30. [ ] Definir DoR.
31. [ ] Refinar historias críticas.
32. [ ] Definir estrategia de modelado.
33. [ ] Crear modelos de contexto/negocio necesarios.
34. [ ] Crear casos de uso necesarios.
35. [ ] Crear diagramas de clases necesarios.
36. [ ] Crear diagramas de estados necesarios.
37. [ ] Crear secuencias de flujos críticos.
38. [ ] Diseñar arquitectura.
39. [ ] Crear diagramas de componentes cuando aporten valor.
40. [ ] Diseñar despliegue cuando aplique.
41. [ ] Diseñar datos y ER.
42. [ ] Revisar coherencia entre todos los modelos.
43. [ ] Revisar legibilidad de diagramas en tamaño real.
44. [ ] Revisar seguridad y privacidad.
45. [ ] Definir integraciones/APIs.
46. [ ] Definir analítica únicamente si aporta valor.
47. [ ] Definir estrategia de pruebas.
48. [ ] Revisar riesgos.
49. [ ] Definir plan de iteraciones/Sprints.
50. [ ] Alcanzar Ready to Develop.
51. [ ] Implementar incrementalmente.
52. [ ] Probar.
53. [ ] Mantener trazabilidad.
54. [ ] Mantener documentación y diagramas sincronizados.
55. [ ] Realizar Sprint Review / validación incremental cuando corresponda.
56. [ ] Realizar retrospectiva y aplicar mejoras cuando corresponda.
57. [ ] Validar con usuarios/stakeholders.
58. [ ] Evaluar resultados.
59. [ ] Documentar limitaciones.
60. [ ] Consolidar evidencias.
61. [ ] Ejecutar auditoría documental y de referencias.
62. [ ] Preparar informe.
63. [ ] Revisar rúbrica punto por punto.
64. [ ] Verificar legibilidad del PDF/entrega final.
65. [ ] Presentar.
66. [ ] Registrar cierre y lecciones aprendidas.

---

# 41. Regla maestra de calidad

Antes de considerar terminado el proyecto, debería ser posible responder claramente:

- [ ] **¿Qué problema se está resolviendo?**
- [ ] **¿Qué evidencia demuestra que existe?**
- [ ] **¿A quién afecta?**
- [ ] **¿Qué necesita esa persona, organización o población?**
- [ ] **¿Por qué esta solución responde a esa necesidad?**
- [ ] **¿Qué está dentro y fuera del alcance?**
- [ ] **¿Qué debe hacer exactamente el sistema?**
- [ ] **¿Qué condiciones de calidad debe cumplir?**
- [ ] **¿De dónde salió cada requisito?**
- [ ] **¿Cómo se transforma cada requisito en diseño e implementación?**
- [ ] **¿Cómo se comprueba que funciona?**
- [ ] **¿Qué evidencia demuestra que se cumplió?**
- [ ] **¿Qué limitaciones siguen existiendo?**
- [ ] **¿Qué diagrama o modelo explica cada aspecto importante del sistema?**
- [ ] **¿Los diagramas siguen siendo legibles, actuales y coherentes con la documentación?**
- [ ] **¿Existe una fuente editable para los artefactos generados que deban mantenerse?**
- [ ] **¿La documentación diferencia correctamente planificación, estado actual e información histórica?**
- [ ] **¿Puede identificarse qué cambió en cada iteración y por qué?**

Si alguna de estas preguntas importantes no puede responderse con documentación o evidencia, el proyecto todavía tiene una brecha que debe revisarse.

---

# 42. Matriz maestra de artefactos y mantenimiento

Esta matriz puede utilizarse como control final o como inventario vivo. No obliga a crear todos los artefactos: permite marcar **No aplica** con justificación.

| Artefacto | Estado | Fuente principal | Fuente editable | Render/entregable | Documento principal | Relación con requisitos/HU | Última revisión |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Consigna/rúbrica | ☐ |  | N/A |  |  | N/A |  |
| Contexto/diagnóstico | ☐ |  | N/A |  |  |  |  |
| Relevamiento/evidencia | ☐ |  | N/A |  |  |  |  |
| SRS | ☐ |  | N/A |  |  |  |  |
| RF/RNF/RN | ☐ |  | N/A |  |  |  |  |
| Product Backlog | ☐ |  | N/A |  |  |  |  |
| Historias de usuario | ☐ |  | N/A |  |  |  |  |
| Flujo UX | ☐ |  |  |  |  |  |  |
| Actividad / negocio | ☐ |  |  |  |  |  |  |
| Casos de uso | ☐ |  |  |  |  |  |  |
| Clases | ☐ |  |  |  |  |  |  |
| Estados | ☐ |  |  |  |  |  |  |
| Secuencia | ☐ |  |  |  |  |  |  |
| Componentes | ☐ |  |  |  |  |  |  |
| Despliegue | ☐ |  |  |  |  |  |  |
| ER | ☐ |  |  |  |  |  |  |
| C4/contenedores | ☐ |  |  |  |  |  |  |
| ADR | ☐ |  | N/A |  |  |  |  |
| Modelo de datos | ☐ |  | N/A |  |  |  |  |
| APIs/OpenAPI | ☐ |  |  |  |  |  |  |
| Plan de pruebas | ☐ |  | N/A |  |  |  |  |
| Evidencias de pruebas | ☐ |  | N/A |  |  |  |  |
| Trazabilidad | ☐ |  | N/A |  |  |  |  |
| Sprint/iteración | ☐ |  | N/A |  |  |  |  |
| Review | ☐ |  | N/A |  |  |  |  |
| Retrospectiva | ☐ |  | N/A |  |  |  |  |
| Informe final | ☐ |  | N/A |  |  | N/A |  |

## 42.1 Estados sugeridos

- [ ] No iniciado.
- [ ] En elaboración.
- [ ] Pendiente de validar.
- [ ] Validado.
- [ ] Implementado/documentado.
- [ ] Desactualizado.
- [ ] Superseded.
- [ ] No aplica.

## 42.2 Regla para artefactos superseded

Cuando un artefacto sea sustituido:

- [ ] Confirmar cuál es el reemplazo oficial.
- [ ] Actualizar todas las referencias.
- [ ] Regenerar renders.
- [ ] Retirar el artefacto antiguo de la documentación current-state.
- [ ] Conservarlo como histórico únicamente si existe una razón.
- [ ] Evitar que dos artefactos parezcan simultáneamente canónicos.
- [ ] Verificar que no queden imágenes o enlaces huérfanos.

## 42.3 Auditoría final sugerida

Antes de entregar o cerrar una versión:

- [ ] Ejecutar búsqueda global de nombres antiguos.
- [ ] Ejecutar búsqueda global de placeholders.
- [ ] Verificar enlaces.
- [ ] Verificar pares fuente/render.
- [ ] Verificar legibilidad de diagramas.
- [ ] Verificar trazabilidad.
- [ ] Verificar estados de Sprint/HU.
- [ ] Verificar coherencia de roles y permisos.
- [ ] Verificar coherencia de estados del dominio.
- [ ] Verificar coherencia clases ↔ ER ↔ datos.
- [ ] Verificar coherencia UX ↔ secuencia.
- [ ] Verificar arquitectura ↔ componentes ↔ despliegue.
- [ ] Verificar pruebas ↔ evidencia.
- [ ] Revisar que no se haya inventado evidencia o validación.

