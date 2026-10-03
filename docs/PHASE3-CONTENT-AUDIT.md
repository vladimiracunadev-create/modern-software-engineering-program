# Auditoría de contenido de fase 3

## Resultado

La fase 3 está **parcialmente construida**. Su alcance correcto es de 180 clases,
`SE-001`–`SE-180`: las partes 00–06 aportan 84 clases `GUIDED` y las 96 restantes aún
no superan el estándar pedagógico permanente.

Esta auditoría distingue tres hechos:

1. existe la identidad curricular de las 180 clases;
2. existen borradores estructurales, actividades y rúbricas generadas;
3. esos artefactos no equivalen a clases desarrolladas ni aprobadas.

## Evidencia observada el 2026-10-03

| Comprobación | Resultado | Interpretación |
| --- | ---: | --- |
| clases dentro del alcance | 180 | `SE-001`–`SE-180` |
| borradores que repiten el mismo párrafo genérico | 0 | el párrafo señalado en la auditoría anterior ya no aparece |
| clases con sección `Definiciones de trabajo` | 180 | existe una base terminológica inicial |
| clases con sección `Glosario` | 84 | Partes 00–06 reconstruidas; requisito pendiente en las demás partes |
| clases con sección `Preguntas frecuentes` | 180 | existe una capa de aclaración inicial |
| clases con sección `Reto verificable` | 180 | existe una extensión evaluable de la práctica |
| clases aprobadas | 84 | Partes 00–06 aprobadas; las otras 96 permanecen `PLANNED` |

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
- conservar `PLANNED` en toda clase que no haya superado el gate completo;
- no usar `GUIDED` hasta superar
  [`PEDAGOGICAL-STANDARD.md`](PEDAGOGICAL-STANDARD.md);
- reconstruir por parte, con un commit independiente y revisión cualitativa;
- publicar índices con enlaces directos a GitHub y GitHub Pages.

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
Tras revisar enlaces, contenido, publicación y validadores, la Parte 00 superó el
gate y sus doce clases avanzaron a `GUIDED`. Esta promoción no atribuye estados
`EXECUTABLE`, `TESTED` u `OPERABLE` ni se extiende a las demás partes.

## Avance editorial de la Parte 01

Las clases `SE-013`–`SE-024` fueron reemplazadas por fuentes canónicas en
`content/part-01/`. El caso conductor `Pulso` conecta representación, Unicode,
aritmética, CPU, memoria, procesos, traducción, runtime y medición hasta un taller y
un informe reproducible. Cada clase declara mecanismo, entorno, práctica segura,
fallo controlado, errores, fuentes y límites instrumentales. El README completo de la
parte se publica también en Pages. Tras revisión clase por clase y de la progresión
completa, las doce clases avanzaron a `GUIDED`; no se promovieron a estados que exigen
ejecución o evidencia productiva.

## Avance editorial de la Parte 02

Las clases `SE-025`–`SE-036` se reconstruyeron desde fuentes canónicas en
`content/part-02/`. El caso `Faro` conecta plataforma, sistemas de archivos,
autorización, procesos, shells, configuración, procedencia, observabilidad y
virtualización hasta un taller de recuperación y un kit diagnóstico multiplataforma.
Cada clase desarrolla mecanismos propios, mapa causal, ejemplos, práctica, reto,
fallo controlado, seguridad, transferencia y fuentes oficiales próximas. La revisión
completa confirmó el contrato pedagógico y la publicación íntegra en el portal; las
doce clases avanzaron a `GUIDED` sin atribuir ejecución en plataformas no probadas.

## Avance editorial de la Parte 03

Las clases `SE-037`–`SE-048` se reconstruyeron como fuentes canónicas en
`content/part-03/`. El caso `Nexo` sigue una petición desde la red local hasta IP,
transporte, DNS, HTTP, TLS, intermediarios y conexiones persistentes; después la
mide, la integra en un taller de extremo a extremo y la convierte en un servicio
observable con recuperación controlada. Cada clase desarrolla cinco mecanismos
propios, contrasta una hipótesis rival, exige primera divergencia y conserva el caso
sano, degradado y restaurado. Las fuentes RFC se enlazan junto al mecanismo que
sustentan, y las prácticas limitan captura, privilegios y datos sensibles. Tras la
revisión completa de clases, progresión, enlaces y publicación, las doce clases
avanzaron a `GUIDED` sin afirmar que los laboratorios se ejecutaron en redes de
producción.

## Avance editorial de la Parte 04

Las clases `SE-049`–`SE-060` se reconstruyeron en `content/part-04/` alrededor de
`Atlas`, un planificador que transforma las trazas de Nexo en decisiones
contrastables. La progresión conecta descomposición, lógica, conjuntos, relaciones,
grafos, contratos, inducción, corrección, terminación, complejidad, heurísticas,
máquinas de estado y registro de hipótesis. Cada clase contiene un contraejemplo y
exige distinguir ejemplos empíricos de argumentos generales; el proyecto termina en
una matriz problema–regla–caso–evidencia lista para implementar. Tras revisar las
doce clases y la publicación íntegra de la parte, avanzaron a `GUIDED` sin atribuir
ejecución a los modelos o pruebas de papel.

## Avance editorial de la Parte 05

Las clases `SE-061`–`SE-072` se reconstruyeron en `content/part-05/` como una
implementación incremental de Atlas llamada `Brújula`. El recorrido desarrolla
valores, control, iteración, funciones, resultados de error, colecciones, I/O,
serialización, módulos, pruebas y legibilidad; el taller contrasta Python con Rust y
el proyecto integra una CLI con contratos de streams y códigos de salida. Cada clase
incluye código explicado, predicción previa, fallo controlado y caso de regresión,
pero la promoción se limita a `GUIDED`: los snippets no se presentan como un paquete
publicado ni como evidencia automática de ejecución multiplataforma. Tras revisar
contenido, progresión, fuentes oficiales y portal, las doce clases superaron el gate.

## Avance editorial de la Parte 06

Las clases `SE-073`–`SE-084` se reconstruyeron en `content/part-06/` alrededor de
`Prisma`, un motor que expresa el mismo contrato mediante modelos imperativos,
procedurales, orientados a objetos, funcionales, declarativos, lógicos, orientados a
eventos, reactivos y de actores. Las clases explican estado, control, composición,
unificación, backpressure, cancelación y aislamiento con contraejemplos propios. El
taller fija fixtures comunes y el proyecto termina con corpus, propiedades, trazas e
informe de decisión contextual. Tras revisar las doce clases, sus fuentes primarias,
la continuidad y la publicación íntegra, avanzaron a `GUIDED` sin declarar un
paradigma ganador universal ni atribuir benchmarks no ejecutados.

## Orden de reconstrucción

La fase se desarrolla en quince entregas: partes 00 a 14. Cada entrega debe incluir
las doce clases de la parte, el README narrativo de la parte, fuentes trazables,
actividades, rúbricas, publicación visual y workflows verdes. No se contabiliza una
parte por archivos creados, sino por clases aprobadas contra el gate.
