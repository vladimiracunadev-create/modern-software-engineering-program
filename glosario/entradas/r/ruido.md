# Ruido

[↑ Glosario](../../README.md) · [← Rúbrica de investigabilidad](./rubrica-de-investigabilidad.md) · [Ruido de evaluación →](./ruido-de-evaluacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Limita la profundidad de los circuitos fiables.

Es uno de los temas de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), donde se enseña como «Ruido».

## Por qué importa

En [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), el tema «Ruido» importa porque limita la profundidad de los circuitos fiables.

En [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), el tema «Ruido» importa porque con pocos despliegues una diferencia entre equipos puede ser azar.

## Cómo funciona

Según [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md):

Porque simular fija el modelo con código que se ve entero y se reproduce; un servicio cuántico real añade ruido, colas, costos y dependencia de un proveedor que esta clase no necesita.

Según [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md):

Una tasa mensual calculada con pocos despliegues es una estimación con mucho error. Si la probabilidad real de fallo es del 12 % y el equipo despliega 8 veces al mes, la tasa observada puede ser del 0 % o del 37 % sin que nada haya cambiado. El **intervalo de confianza** de una proporción cuantifica ese margen: el intervalo de Wilson se comporta bien con muestras pequeñas y es preferible al intervalo normal, que puede salir de [0, 1]. Dos consecuencias: comparar la tasa mensual de dos equipos pequeños es comparar ruido, y detectar una mejora real exige volumen o ventanas largas.

## Ejemplo

Ejemplo de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) (sección «Preguntas frecuentes»):

Porque simular fija el modelo con código que se ve entero y se reproduce; un servicio cuántico real añade ruido, colas, costos y dependencia de un proveedor que esta clase no necesita.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un equipo pequeño «empeora» de un mes a otro** — causa: ruido del volumen. Corrección: intervalo de Wilson; agregar por trimestre. ([SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Porque simular fija el modelo con código que se ve entero y se reproduce; un servicio cuántico real añade ruido, colas, costos y dependencia de un proveedor que esta clase no necesita. ([SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md))
- La transferencia está lograda cuando puedes decir qué diferencia es ruido y qué atajo no detectarías, no cuando el panel se parece al de la plataforma. ([SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Amplitud](../a/amplitud.md), [Cosechar ahora, descifrar después](../c/cosechar-ahora-descifrar-despues.md), [Entrelazamiento](../e/entrelazamiento.md), [Frecuencia de despliegue](../f/frecuencia-de-despliegue.md), [Interferencia](../i/interferencia.md), [Medida de contrapeso](../m/medida-de-contrapeso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (159 clases más lo mencionan; las que más):

[SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md), [SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md), [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DORA: guía de métricas](https://dora.dev/guides/dora-metrics/) — definición de las métricas de rendimiento e inestabilidad de la entrega; autoridad: DORA, Google Cloud, consultada el 15 de noviembre de 2026.
- [Forsgren et al., «The SPACE of Developer Productivity»](https://doi.org/10.1145/3454122.3454124) — productividad multidimensional (ACM Queue, 2021); autoridad: artículo con DOI verificado en Crossref.
- [Wilson, «Probable inference, the law of succession, and statistical inference»](https://doi.org/10.1080/01621459.1927.10502953) — intervalo para proporciones (Journal of the American Statistical Association, 1927); autoridad: artículo con DOI verificado en Crossref.

---

[↑ Glosario](../../README.md) · [← Rúbrica de investigabilidad](./rubrica-de-investigabilidad.md) · [Ruido de evaluación →](./ruido-de-evaluacion.md)
