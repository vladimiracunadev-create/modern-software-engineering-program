# Huella

[↑ Glosario](../../README.md) · [← Hueco de contenido](./hueco-de-contenido.md) · [Huella (resumen) SHA-256 →](./huella-resumen-sha-256.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Una **huella** es un valor derivado del contenido de un archivo, un resultado, una configuración o una especificación, normalmente un resumen criptográfico como SHA-256, que cambia si cambia el contenido. Es el término que el programa usa para lo que la bibliografía llama *hash* o *checksum*: [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) la define como un valor de longitud fija que cambia si cambia cualquier bit, [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) como un valor derivado del contenido que permite comprobar su integridad y [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md) como un valor calculado a partir de los bytes de un artefacto. Diez clases la usan, siempre con el mismo núcleo y con funciones distintas: comprobar integridad, comparar ejecuciones, fijar dependencias, detectar cambios en una herramienta o identificar datos y configuraciones.

## Por qué importa

Permite responder «¿es el mismo contenido?» sin comparar el contenido entero y sin confiar en la memoria de nadie. Sirve para detectar un archivo truncado o corrupto ([SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md)), para fijar una dependencia por su contenido y no solo por su nombre ([SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md)), para saber si dos ejecuciones produjeron lo mismo ([SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md)), y para detectar que una herramienta aprobada cambió ([SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md)). La clave de su utilidad es una condición: la huella solo prueba **identidad de contenido**, no autoría.

## Cómo funciona

Un resumen criptográfico produce un valor de longitud fija a partir de cualquier cantidad de bytes y cambia si cambia un solo bit. [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) lo contrasta con alternativas: un archivo de 20 MB con un bit alterado cambia de huella (CRC32, MD5 y SHA-256) pero no de longitud; truncado o ampliado cambia ambas. Un CRC32 detecta errores accidentales, pero tiene 32 bits: en la simulación se encontró una colisión entre dos mensajes de 8 bytes tras 87 650 intentos, de modo que no protege frente a una alteración deliberada.

Los usos en el programa, cada uno con su variante:

- **Integridad de lo recibido** ([SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md)): el cliente envía la huella al principio o al final y el servidor la compara con la del contenido recibido; para calcularla no hace falta tener el archivo entero en memoria, se actualiza trozo a trozo.
- **Builds reproducibles** ([SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md)): las dependencias se fijan por huella; si dos extracciones del repositorio dan huellas distintas, la causa suelen ser saltos de línea convertidos, fechas o rutas incrustadas.
- **Resultados comparables** ([SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md)): el resumen de un resultado serializado de forma determinista permite comparar ejecuciones.
- **Herramientas aprobadas** ([SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md)): una huella del nombre, la descripción y el esquema de una herramienta detecta cualquier cambio, incluso de un carácter invisible, y obliga a una nueva aprobación.
- **Experimentos** ([SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md)): el registro de una corrida guarda la huella de los datos, de las etiquetas y de la configuración.

## Ejemplo

En [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), regenerar los datos con la misma semilla produjo la misma huella, y con otra semilla una distinta: es la prueba mínima de que la huella detecta lo que debe detectar. En [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md), un archivo sintético de 20 MB alterado de tres maneras (un bit cambiado, truncado en 1 000 bytes y con 16 bytes añadidos) cambia de huella en las tres, mientras que un archivo idéntico coincide en todo.

## Errores y confusiones comunes

- **Alguien sustituyó el archivo y su hash.** La huella viaja por el mismo canal que el archivo; quien puede alterar uno puede alterar el otro. Corrección ([SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md)): una firma con una clave pública que el cliente conozca por otro camino.
- **Confundir integridad con autenticidad.** La huella detecta corrupción accidental; para un atacante que controla el archivo y la huella no prueba autenticidad ([SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md)).
- **«Cada build produce un hash distinto».** Fechas, orden o rutas incrustadas; corrección ([SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md)): normalizar tiempo y orden y eliminar rutas.
- **Una revisión que se vuelve rutina.** Con una huella sin triaje, toda actualización legítima dispara la alerta y se deja de leer ([SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md)).

## Límites y cuándo no aplica

Una huella no prueba el origen: [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) separa explícitamente integridad y origen y exige una firma para lo segundo. Es sensible a detalles de formato (saltos de línea convertidos por el control de versiones, orden de campos, fechas), de ahí que [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) serialice de forma determinista antes de resumir y que [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md) pida fijar la normalización de la fuente. Y el algoritmo importa: [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) muestra que CRC32, con 32 bits, no protege frente a una alteración deliberada.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Archivo generado](../a/archivo-generado.md), [Artefacto](../a/artefacto.md), [Byte](../b/byte.md), [Conjunto](../c/conjunto.md), [Ancla](../a/ancla.md), [Construcción reproducible](../c/construccion-reproducible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.
- [SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.
- [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (133 clases más lo mencionan; las que más):

[SE-087](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md), [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md), [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Slack](../../../casos/exito/slack.md), [Instagram](../../../casos/exito/instagram.md), [Discord](../../../casos/exito/discord.md), [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «resumen criptográfico».

**Forma en inglés o término técnico original:** «hash».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: hashlib](https://docs.python.org/3/library/hashlib.html) — huellas calculadas por trozos; autoridad: Python Software Foundation.
- [Write the Docs: Docs as Code](https://www.writethedocs.org/guide/docs-as-code/) — práctica y herramientas; autoridad: Write the Docs.
- [CommonMark: especificación](https://spec.commonmark.org/) — sintaxis de Markdown; autoridad: proyecto CommonMark.
- [GitHub Flavored Markdown: especificación](https://github.github.com/gfm/) — extensiones de Markdown de GitHub; autoridad: GitHub.
- [markdownlint: reglas](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md) — catálogo de reglas de estilo de Markdown; autoridad: proyecto markdownlint.

---

[↑ Glosario](../../README.md) · [← Hueco de contenido](./hueco-de-contenido.md) · [Huella (resumen) SHA-256 →](./huella-resumen-sha-256.md)
