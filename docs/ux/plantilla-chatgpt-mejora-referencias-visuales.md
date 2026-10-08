# Plantilla autónoma: mejora de referencias visuales con ChatGPT

Usa esta plantilla para pedir una **imagen PNG mejorada**, no sólo una crítica escrita. No presupone un stack, una conexión a GitHub, una función de generación de imágenes ni una conversión automática a Figma. Completa los campos entre corchetes, elimina lo que no aplique y adjunta el PNG de entrada. En modo B, adjunta también el master aprobado y la pantalla actual.

**Procedimiento relacionado:** [Flujo personal de referencias visuales para UX](flujo-referencias-visuales.md). Esta plantilla se puede copiar y usar sin leer ese documento; las reglas esenciales están incluidas aquí.

## Cómo usarla (fuera del prompt)

1. Elige **un solo modo**: A para establecer la primera referencia fundacional; B para mejorar una pantalla posterior con un master visual ya aprobado.
2. Completa sólo lo que conoces. No inventes una rama, commit, ruta, regla, marca ni capacidad de herramienta.
3. Adjunta el PNG actual y los assets/referencias autorizados. En B, adjunta también el master vigente y confirma su versión.
4. Copia el contenido completo de **Prompt para copiar** en el chat. Si la conexión o generación de imágenes no está disponible, exige que se declare la limitación, no una simulación.
5. La reconstrucción editable posterior se hace en UX Pilot/Figma y requiere revisión y aprobación humana; este prompt no la realiza.

---

## Prompt para copiar

Actúa como especialista en diseño de interfaces y mejora visual de referencias PNG para este proyecto. Debes respetar la función y marca aprobadas y devolver como resultado principal **una imagen PNG realmente generada o editada**, adecuada al viewport indicado. No basta con describir cambios, escribir una especificación, proponer un prompt de imagen o devolver sólo análisis. Si en este chat no tienes una capacidad real para generar/adjuntar el PNG, dilo claramente y no finjas que existe un archivo.

No presupongas acceso a GitHub, archivos, Figma, internet, herramientas externas ni generador de imágenes. Usa únicamente conexiones y archivos que efectivamente estén disponibles en esta conversación. No edites el repositorio, no escribas HTML/CSS/React u otro código, y no entregues un archivo de diseño editable: el resultado aquí es el PNG. La reconstrucción editable se hará después en UX Pilot/Figma, usando las capacidades disponibles en la versión real, y una persona deberá comprobarla y aprobarla.

### 1. Modo de trabajo

El modo seleccionado es **[MODO A — PRIMERA REFERENCIA FUNDACIONAL / MODO B — MEJORA POSTERIOR CON MASTER APROBADO]**.

- **Modo A:** mejora la pantalla inicial a partir de la función, rol, marca y contexto confirmados. Es una propuesta de referencia, no un master aprobado automáticamente. No inventes un sistema de marca si faltan datos.
- **Modo B:** mejora sólo la pantalla actual adjunta para su objetivo específico. Usa el master adjunto como referencia visual aprobada, preserva su identidad y componentes, y adapta la composición al objetivo de esta pantalla. No la conviertas en una copia del layout del master. Si el master/versión no está disponible o no se identifica, informa la limitación y no declares consistencia verificada.

### 2. Datos del proyecto y fuentes disponibles

- Nombre del proyecto: [NOMBRE]
- Tipo de proyecto: [ACADÉMICO / PERSONAL / PRODUCTO / OTRO]
- Descripción breve: [DESCRIPCIÓN]
- Propietario/equipo responsable: [NOMBRE U ORGANIZACIÓN / DESCONOCIDO]
- Repositorio GitHub: [URL / NO HAY / NO SÉ]
- Referencia que se desea consultar: [OWNER/REPO Y RAMA O COMMIT / DESCONOCIDA]
- Si no conozco rama o commit: [DEJAR SIN INVENTAR; INDICAR QUE SE USE Y REGISTRE LA REFERENCIA QUE REALMENTE SEA ACCESIBLE]
- Documentos o extractos adjuntos: [LISTA / NINGUNO]
- Enlaces y otras referencias: [LISTA / NINGUNO]
- Límite de contexto o exclusiones de privacidad: [DESCRIBIR / NINGUNO]

La conexión de GitHub y la lectura del repositorio son **condicionales**. Si puedes acceder, confirma qué repositorio y referencia (rama/commit) viste realmente, y registra las rutas exactas relevantes que consultaste. Si no puedes, indícalo y trabaja sólo con adjuntos, texto proporcionado y referencias visibles. No afirmes haber leído el repositorio, no inventes rutas ni contenido, no pidas credenciales y no reproduzcas secretos o datos personales.

Si hay un repositorio grande, realiza una inspección **acotada y significativa**: lee los README pertinentes y los archivos suficientes para entender la pantalla, sus convenciones y assets. Busca sólo lo que exista y resulte relevante, por ejemplo: documentación HU/CA/reglas/UX; arquitectura del frontend; componentes UI y kit; tokens CSS; tema Tailwind únicamente si existe; paleta, tipografías, layouts, navegación, logo/iconos/ilustraciones/fotografías; pantallas relacionadas y reglas visuales. No exijas ni leas el repositorio entero, no supongas una estructura/directorio, y registra qué pudiste y qué no pudiste consultar.

### 3. Pantalla y objetivo

- Modo: [A / B]
- Nombre o identificador de la pantalla: [NOMBRE / ID]
- Historia de usuario (HU): [ID Y TEXTO / NO DISPONIBLE]
- Estado de la HU: [BORRADOR / APROBADA / OTRO]
- Rol o audiencia: [ROL / DESCONOCIDO]
- Objetivo de la pantalla: [QUÉ NECESITA LOGRAR LA PERSONA]
- Estado de interfaz: [INICIAL / CARGA / VACÍO / ERROR / ÉXITO / OTRO]
- PNG actual adjunto: [NOMBRE / NO DISPONIBLE]
- Master aprobado adjunto (obligatorio para verificar modo B): [NOMBRE + VERSIÓN / NO DISPONIBLE / NO APLICA]
- Otras pantallas relacionadas: [LISTA / NINGUNA]

### 4. Separa intención funcional, composición, marca y contenido

No mezcles una preferencia estética con una regla funcional. Usa esta clasificación:

**A. Estructura y función aprobadas**
- Información que debe aparecer: [LISTA]
- Acciones/interacciones autorizadas y su propósito: [LISTA]
- Reglas de negocio, permisos y restricciones: [LISTA]
- Campos, estados, relaciones o validaciones confirmados: [LISTA]
- Elementos funcionales que se deben conservar exactamente: [LISTA]
- Fuera de alcance: [LISTA]

**B. Composición y experiencia buscadas**
- Jerarquía visual: [DESCRIPCIÓN]
- Distribución/layout: [DESCRIPCIÓN]
- Navegación, formularios, tablas, tarjetas o controles pertinentes: [DESCRIPCIÓN]
- Problemas concretos que se quieren mejorar: [LISTA]
- Elementos estéticos que se deben preservar: [LISTA]

**C. Branding e identidad**
- Logo oficial y variante autorizada adjunta: [ARCHIVO / NO DISPONIBLE]
- Paleta aprobada/tokens conocidos: [VALORES/ARCHIVO / DESCONOCIDO]
- Tipografías aprobadas: [NOMBRES/ARCHIVO / DESCONOCIDO]
- Iconos, ilustraciones o fotografías autorizados: [ARCHIVOS / NINGUNO]
- Guía/kit/componentes de marca: [FUENTE / NO DISPONIBLE]
- Recursos obligatorios: [LISTA]
- Recursos prohibidos o que no deben modificarse: [LISTA]

**D. Datos de muestra**
- Datos ficticios permitidos: [VALORES / INDICAR “USAR EJEMPLOS NEUTROS”]
- Datos que no deben aparecer: [LISTA]

Trata todo dato inventado como muestra; nunca lo presentes como registro real, evidencia real ni contenido confirmado del proyecto. Si un label, acción, estado, marca o dato no está confirmado, no lo hagas pasar por cierto.

### 5. Archivos, PNG y viewports

- PNG inicial a mejorar: [ADJUNTO / NOMBRE]
- Resolución o dimensiones solicitadas: [ANCHO × ALTO / DESCONOCIDA]
- Orientación y relación de aspecto: [VERTICAL / HORIZONTAL / CUADRADA / OTRA]
- Tipo de vista: [DESKTOP / TABLET / MOBILE / OTRA]
- Viewport(s) que se necesitan: [LISTA CON DIMENSIONES SI SE CONOCEN]
- En modo B, master y versión exacta: [ARCHIVO/FRAME/LINK/FECHA / NO APLICA]
- Preservar: [ELEMENTOS Y DETALLES]
- Mejorar: [ELEMENTOS Y DETALLES]
- No cambiar o incluir: [ELEMENTOS PROHIBIDOS]
- Otros assets de referencia adjuntos: [LISTA]

Genera una imagen por viewport sólo si fueron solicitados y hay información suficiente para diferenciarlos. No presentes una imagen de escritorio como prueba de adaptación móvil/tablet.

### 6. Jerarquía de autoridad

Aplica estas prioridades al resolver decisiones, sin borrar conflictos relevantes:

1. **Función:** decisiones funcionales explícitamente aprobadas prevalecen sobre la interpretación visual; después se respetan la HU, los criterios de aceptación (CA), el SRS y las reglas vigentes. La pantalla no amplía estos límites.
2. **Marca:** identidad oficial y assets aprobados prevalecen sobre tokens/kit del proyecto; tokens/kit prevalecen sobre el master; el master prevalece sobre PNG intermedios o referencias inspiracionales. Respeta la forma, geometría y proporciones exactas del logo: no lo reinterpretes, deformes, reemplaces ni combines con una marca ajena.
3. **Pantalla:** objetivo funcional de esta vista > estructura UX aprobada > referencia PNG > mejoras estéticas compatibles.
4. **Contexto técnico:** el código/documentación que realmente logres consultar informa sobre el contexto actual, pero una maqueta no prueba que una función esté implementada. Pi deberá inspeccionar independientemente código, contratos, pruebas y documentación antes de implementar.

Si un conflicto material de función, permiso, marca o alcance no puede resolverse con las fuentes autorizadas, haz una pregunta breve y concreta **antes de producir el PNG**. No reabras decisiones ya aprobadas por preferencias estéticas. Para incertidumbres visuales menores, elige una alternativa compatible y declara brevemente la suposición.

### 7. Cambios visuales permitidos y límites

Dentro de las restricciones aprobadas, puedes mejorar libremente la estética, consistencia, jerarquía, distribución, legibilidad, contraste, uso del espacio, alineación, tipografía disponible, navegación visual, formularios, tablas, tarjetas, estados, adaptación al viewport e integración con componentes/tokens existentes. En modo B, alinea los patrones compartidos con el master vigente sin forzar su composición en una tarea distinta.

**No hagas ninguno de estos cambios o afirmaciones:**

- no inventes funciones, acciones, módulos, enlaces, permisos, roles, campos de dominio, estados, reglas ni información;
- no elimines, renombres o alteres contenido/función aprobados; no cambies el significado de labels;
- no alteres proporción, geometría, colores aprobados ni identidad del logo, no lo sustituyas ni uses branding de terceros no autorizado;
- no presentes datos ficticios como reales ni afirmes que una pantalla/función ya está implementada;
- no digas que el PNG es un diseño editable, un componente de Figma, una instancia de kit o un componente real de frontend;
- no afirmes acceso, lectura, conexión, compatibilidad o fidelidad de assets que no hayas comprobado;
- no generes variantes o refinamientos repetidos sin una necesidad concreta;
- no sacrifiques legibilidad para decorar ni introduzcas texto borroso, duplicado, recortado o distorsionado.

### 8. Control visual antes de entregar

Antes de devolver el archivo, revisa la imagen al tamaño solicitado:

- corresponde al objetivo, rol, función, contenido y estado de la pantalla;
- conserva todas las acciones e información obligatorias sin añadir otras;
- no tiene elementos cortados, texto deformado/ilegible, etiquetas inventadas, duplicados, alineaciones accidentales ni inconsistencias de espaciado;
- la tipografía es legible; los colores/contraste y la jerarquía son razonables; la composición no oculta información;
- el logo/assets usados son los adjuntos o verificados, sin alteraciones ni sustituciones; si no hay un asset oficial, no inventes uno;
- utiliza componentes/patrones existentes sólo si su existencia se confirmó, y no los presentes como frontend implementado;
- se ha respetado cada viewport solicitado y no se atribuye validación a viewports no generados.

Una PNG estática **no permite certificar por sí sola** accesibilidad, navegación por teclado, semántica, interacción, responsive completo, comportamiento real, contraste en todos los contextos ni conformidad del frontend. Indica explícitamente las verificaciones que no pueden hacerse desde la imagen; no afirmes cumplimiento ni fidelidad perfecta.

### 9. Salida solicitada

**Salida primaria:** adjunta/produce el PNG mejorado real para el viewport y resolución/aspecto solicitados. La imagen debe ser el resultado principal, no sustituida por análisis textual. Si necesitas más de una variante solicitada, identifícalas por vista/viewport. Si no puedes generar o adjuntar el PNG aquí, informa esa limitación en vez de fabricar una ruta o archivo.

**Salida secundaria, breve:** acompaña el PNG con:

1. Cambios visuales principales y qué elementos funcionales se preservaron.
2. Evidencia concreta del contexto que realmente consultaste: owner/repositorio y rama/commit accesibles, rutas leídas y assets/referencias usados. Si no hubo acceso, indica “no verificado/no disponible” y qué adjuntos/texto usaste.
3. Supuestos visuales menores y límites/contradicciones que persisten; indica qué no puede certificarse desde la imagen.
4. Para modo B, si pudiste contrastar de verdad contra el master adjunto y su versión; no declares consistencia verificada si no estaba disponible.

No entregues HTML, CSS, React, código del repositorio ni un diseño editable como sustituto del PNG solicitado. No afirmes que la reconstrucción posterior en Figma ya ocurrió. El paso siguiente es reconstruir la imagen con capas editables/componentes según corresponda en la versión disponible de UX Pilot/Figma, inspeccionar el archivo y obtener aprobación humana explícita del master; una captura plana dentro de un frame no satisface ese paso.

### 10. Instrucción final

Primero usa la evidencia accesible y resuelve sólo la incertidumbre material. Después genera y entrega la imagen PNG real solicitada. Mantén las afirmaciones proporcionadas a lo observado, separa función de estética y deja visibles las limitaciones. Si no hay imagen de entrada, master necesario, referencia de función o capacidad de generación imprescindible, explica exactamente qué falta y formula sólo la pregunta concreta que desbloquea el trabajo.
