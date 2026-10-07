# Auditoría de contenido de fase 3

## Resultado

La fase 3 está **parcialmente construida**. Su alcance correcto es de 180 clases,
`SE-001`–`SE-180`: las 72 clases de las Partes 00–05 están desarrolladas. Las 108
restantes son borradores públicos y aún no superan la revisión definida por el
estándar pedagógico permanente.

Esta auditoría distingue tres hechos:

1. existe la identidad curricular de las 180 clases;
2. existen borradores estructurales, actividades y rúbricas generadas;
3. esos artefactos no equivalen a clases desarrolladas ni aprobadas.

## Evidencia observada el 2026-10-06

| Comprobación | Resultado | Interpretación |
| --- | ---: | --- |
| clases dentro del alcance | 180 | `SE-001`–`SE-180` |
| borradores que repiten el mismo párrafo genérico | 0 | el párrafo señalado en la auditoría anterior ya no aparece |
| clases con sección `Definiciones de trabajo` | 180 | existe una base terminológica inicial |
| clases con sección `Glosario` | 120 | Partes 00–09 reconstruidas; requisito pendiente en las demás partes |
| clases con sección `Preguntas frecuentes` | 180 | existe una capa de aclaración inicial |
| clases con sección `Reto verificable` | 180 | existe una extensión evaluable de la práctica |
| clases desarrolladas | 72 | Partes 00–05; las otras 108 continúan como borradores |

El conteo es evidencia negativa, no un criterio suficiente de calidad. Aunque se
añadieran encabezados, cada clase seguiría necesitando una revisión técnica y
pedagógica integral.

## Defectos cualitativos

- explicaciones intercambiables entre temas distintos;
- conceptos todavía pendientes de validación técnica individual por un revisor;
- ejemplos genéricos que no demuestran el concepto de la clase;
- prácticas sin preparación técnica suficiente ni resultado específico;
- fuentes agrupadas por parte, pero no ligadas a afirmaciones concretas;
- ausencia de un glosario consolidado y de enlaces de fuente por afirmación;
- diagramas formales sin interpretación específica suficiente;
- índices que antes obligaban a recorrer carpetas para localizar una clase.

## Decisión de integridad

- conservar las 180 entradas como borradores públicos para que el defecto sea
  auditable;
- no presentar una clase como desarrollada hasta superar la revisión completa de
  [`PEDAGOGICAL-STANDARD.md`](PEDAGOGICAL-STANDARD.md);
- reconstruir por parte, con un commit independiente y revisión cualitativa;
- publicar índices con enlaces directos a GitHub y GitHub Pages.

## Corrección de nombres y trazabilidad pedagógica

Las etiquetas ficticias de las Partes 01–09 se retiraron de las clases, índices,
generadores y portal. No eran conceptos técnicos ni ayudaban a anticipar la función
del sistema. La equivalencia histórica se conserva únicamente en
[`CASE-LABEL-CORRECTION.md`](CASE-LABEL-CORRECTION.md), fuera del recorrido educativo.

Las 108 clases de esas partes incorporan un punto profesional específico, el error
conceptual que busca corregir, una evidencia observable, su límite y una tabla que
relaciona fuentes con afirmaciones. Los registros de
[`sources/pedagogical/`](../sources/pedagogical/) documentan esa trazabilidad sin
atribuir aprobación: añadir metadatos no equivale a completar contenido.

La secuencia activa conocimiento previo y contexto según
[*How People Learn II*](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures),
exige explicar y contrastar mecanismos de acuerdo con
[ICAP](https://icap.education.asu.edu/research), y usa recuperación activa para
comprobar comprensión duradera, respaldada por el estudio de
[Roediger y Karpicke](https://pubmed.ncbi.nlm.nih.gov/16507066/). Estas referencias
fundamentan la actividad pedagógica; no sustituyen las fuentes técnicas de cada clase.

## Avance editorial de la Parte 00

Las doce clases `SE-001`–`SE-012` ya no dependen del generador temático genérico:
sus fuentes canónicas están en `content/part-00/` y el portal publica ese texto
íntegro. Cada clase desarrolla mecanismos propios, ejemplo y contraejemplo,
práctica, fallo controlado, glosario, transferencia, límites y fuentes próximas.
La revisión posterior añadió el caso conductor `Campus Abierto`, una activación
“Antes de empezar” específica, conexiones visibles con la clase anterior y siguiente,
progreso dentro de la parte y mapas conceptuales renderizados con alternativa textual.
El portal fue verificado en escritorio y en un viewport móvil de 390 px sin
desbordamiento horizontal.
Tras revisar enlaces, contenido, publicación y validadores, las doce clases de la
Parte 00 pueden describirse como desarrolladas. Esto no afirma que todas sus prácticas
se hayan ejecutado, probado, integrado u operado, ni se extiende a las demás partes.

## Avance editorial de la Parte 01

Las clases `SE-013`–`SE-024` tienen fuentes canónicas en `content/part-01/`. Un
analizador local de eventos conecta representación, Unicode, aritmética, CPU, memoria,
procesos, traducción, runtime y medición hasta un taller y un informe reproducible.
La revisión completa sustituyó la secuencia pedagógica repetida por predicciones,
fallos y transferencias específicas; actualizó Unicode 18.0 y JVM SE 27; y añadió
`labs/part-01-machine-observer`, con fixture sintético, variantes materializada y
streaming, inspección de AST/bytecode, seis pruebas automáticas y separación explícita
entre observado, inferido y no medido. El laboratorio fue ejecutado localmente en
CPython 3.12.9 sobre Windows 11; la portabilidad queda limitada a la matriz que termine
verde en CI. Tras revisar las doce clases, el índice narrativo, las actividades, las
rúbricas, las fuentes y la publicación íntegra, la Parte 01 puede describirse como
desarrollada sin afirmar mediciones físicas de caché, energía o carbono.

## Avance editorial de la Parte 02

Las clases `SE-025`–`SE-036` se reconstruyeron desde fuentes canónicas en
`content/part-02/`. Un kit de diagnóstico multiplataforma conecta plataforma, sistemas de archivos,
autorización, procesos, shells, configuración, procedencia, observabilidad y
virtualización hasta un taller de recuperación y un kit diagnóstico multiplataforma.
Cada clase desarrolla mecanismos propios, mapa causal, ejemplos, práctica, reto,
fallo controlado, seguridad, transferencia y fuentes oficiales próximas. PowerShell
contrasta semántica de objetos, errores, quoting, entorno y códigos de salida con Bash;
no se presenta como un curso independiente de cmdlets. El laboratorio compartido
`labs/part-02-cross-platform-diagnostic-kit` implementa preparación, inspección sin
mutación, reparación idempotente y limpieza protegida por marcador de propiedad. Sus
diez pruebas y los adaptadores PowerShell/Bash separan datos observados, secretos
redactados y límites. La ejecución local demuestra el entorno Windows disponible; la
portabilidad Linux/macOS sólo se acepta cuando la matriz remota termina verde.

## Avance editorial de la Parte 03

Las clases `SE-037`–`SE-048` se revisaron como fuentes canónicas en
`content/part-03/`. Una petición observable se sigue desde la red local hasta IP,
transporte, DNS, HTTP, TLS, intermediarios y conexiones persistentes; después la
mide, la integra en un taller de extremo a extremo y la convierte en un servicio
observable con recuperación controlada. Cada clase desarrolla cinco mecanismos
propios, contrasta una hipótesis rival, exige primera divergencia y conserva el caso
sano, degradado y restaurado. Las fuentes RFC se enlazan junto al mecanismo que
sustentan, y las prácticas limitan captura, privilegios y datos sensibles. Las doce
clases incorporan un laboratorio local ejecutable y no afirman que sus modelos prueben redes
de producción.

## Avance editorial de la Parte 04

Las clases `SE-049`–`SE-060` se reconstruyeron en `content/part-04/` alrededor de
un modelo de decisión diagnóstica que transforma trazas de red en decisiones
contrastables. La progresión conecta descomposición, lógica, conjuntos, relaciones,
grafos, contratos, inducción, corrección, terminación, complejidad, heurísticas,
máquinas de estado y registro de hipótesis. Cada clase contiene un contraejemplo y
exige distinguir ejemplos empíricos de argumentos generales; el proyecto termina en
una matriz problema–regla–caso–evidencia y un laboratorio con trece pruebas. Las doce
clases superaron revisión integral sin atribuir corrección universal a los casos ejecutados.

## Avance editorial de la Parte 05

Las clases `SE-061`–`SE-072` se reconstruyeron en `content/part-05/` como una
implementación incremental del modelo de decisión mediante una CLI diagnóstica. El recorrido desarrolla
valores, control, iteración, funciones, resultados de error, colecciones, I/O,
serialización, módulos, pruebas y legibilidad; el taller contrasta Python con Rust y
el proyecto integra una CLI con contratos de streams y códigos de salida. Cada clase
incluye código explicado, predicción previa, fallo controlado y caso de regresión. El
laboratorio aporta quince contratos, paquete local, JSONL acotado, códigos de salida y
un puerto Rust contrastado en CI. Las doce clases superaron revisión integral; no se
presenta el paquete como publicado ni la equivalencia parcial como portabilidad total.

## Avance editorial de la Parte 06

Las clases `SE-073`–`SE-084` se reconstruyeron en `content/part-06/` alrededor de
un motor de reglas comparado que expresa el mismo contrato mediante modelos imperativos,
procedurales, orientados a objetos, funcionales, declarativos, lógicos, orientados a
eventos, reactivos y de actores. Las clases explican estado, control, composición,
unificación, backpressure, cancelación y aislamiento con contraejemplos propios. El
taller fija fixtures comunes y el proyecto termina con corpus, propiedades, trazas e
informe de decisión contextual. Las doce clases todavía requieren revisión sin declarar un
paradigma ganador universal ni atribuir benchmarks no ejecutados.

## Avance editorial de la Parte 07

Las clases `SE-085`–`SE-096` se reconstruyeron en `content/part-07/` alrededor de
una biblioteca de estructuras y algoritmos que obliga a elegir representación desde operaciones
e invariantes. El recorrido conecta secuencias, colas, heaps, hashing, árboles,
tries, grafos, búsqueda, ordenamiento, selección, estrategias voraces, programación
dinámica, backtracking, divide y vencerás, índices, estructuras probabilísticas y
persistentes. El taller decide por perfiles de carga y el proyecto entrega una
biblioteca comparada con propiedades, casos límite y benchmarks interpretados. Las
doce clases todavía requieren revisión y no convierten mediciones locales en promesas
universales de rendimiento.

## Avance editorial de la Parte 08

Las clases `SE-097`–`SE-108` se reconstruyeron en `content/part-08/` alrededor de
un entorno reproducible para investigar una regresión de la biblioteca de algoritmos
que solo aparece bajo cierta configuración. El recorrido distingue editor, IDE, LSP y DAP; explica breakpoints, frames,
perfiles de CPU, memoria e I/O, compilación, linters, tipos, REPL, notebooks,
selección de runtimes, entornos virtuales y Dev Containers. Después reduce el caso,
incorpora ergonomía y accesibilidad, ejecuta un taller de diagnóstico y entrega un
entorno autocontenido con bootstrap, doctor, rebuild y limpieza acotada. Las doce
clases todavía requieren revisión y no afirman que un contenedor elimine toda variabilidad
ni que una herramienta aislada demuestre causalidad.

## Avance editorial de la Parte 09

Las clases `SE-109`–`SE-120` se reconstruyeron en `content/part-09/` alrededor de
la conversión de la biblioteca de algoritmos y su entorno reproducible en un producto
reutilizable con SDK y CLI. El
recorrido delimita biblioteca, framework, runtime, plataforma y SDK; desarrolla API
pública, SemVer, resolución, lockfiles, build y publicación; después integra CLI,
configuración, códigos de salida, automatización idempotente, plugins, generación,
licencias SPDX/REUSE y diseño de experiencia para desarrolladores. El taller consume
el artefacto fuera del checkout y el proyecto prueba un SDK+CLI entre versiones. Las
doce clases todavía requieren revisión y no presentan SemVer, lockfiles, contenedores o SBOM
como garantías automáticas de compatibilidad, reproducibilidad o cumplimiento.

## Orden de reconstrucción

La fase se desarrolla en quince entregas: partes 00 a 14. Cada entrega debe incluir
las doce clases de la parte, el README narrativo de la parte, fuentes trazables,
actividades, rúbricas, publicación visual y workflows verdes. No se contabiliza una
parte por archivos creados, sino por la revisión completa de su enseñanza y evidencia.
