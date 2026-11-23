# Puerta

[↑ Glosario](../../README.md) · [← Publicación y repositorio](./publicacion-y-repositorio.md) · [Puerta de aprobación →](./puerta-de-aprobacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Transformación unitaria aplicada a uno o varios qubits.

Definición de trabajo de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md): Comprobación entre pasos con una acción definida al fallar.

## Por qué importa

La clase donde se define, [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), existe con este propósito: la clase existe para que un ingeniero de software pueda leer una afirmación sobre computación cuántica (un titular, una propuesta de un proveedor, una exigencia de cumplimiento) y decidir qué parte es verificable, qué parte es especulación y qué decisión concreta le cambia.

## Cómo funciona

Según [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md):

Un qubit no es un bit con valores intermedios: es un par de amplitudes complejas, una para el estado 0 y otra para el 1, cuyos cuadrados de módulo suman 1. Un registro de n qubits tiene 2^n amplitudes. Las puertas son transformaciones lineales que conservan esa suma (matrices unitarias). La medición toma una de las 2^n respuestas con probabilidad igual al cuadrado del módulo de su amplitud, y destruye el resto. En el laboratorio, la puerta H aplicada al estado 0 da probabilidades 0,5 y 0,5; aplicada una segunda vez, devuelve 1,0 y 0,0, porque la amplitud del estado 1 recibe dos contribuciones de signo opuesto que se cancelan.

Según [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md):

**Diagnóstico paso a paso.** (1) Se pregunta contra qué se comparó: contra la implementación existente del cliente (un algoritmo ingenuo en un lenguaje interpretado), no contra el mejor algoritmo clásico del problema. (2) Se pregunta el tamaño: 40 variables, que un solucionador clásico resuelve en milisegundos. (3) Se pregunta si el dispositivo es un recocido cuántico o un procesador de puertas, y qué garantía de optimalidad da. (4) Se ejecuta un solucionador clásico especializado sobre el mismo caso y resuelve igual o mejor. (5) La afirmación queda clasificada como «no respaldada»: la comparación no es con el mejor clásico y el tamaño no discrimina.

## Ejemplo

Ejemplo de [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) (sección «Ejemplo mínimo»):

Una puerta programática entre extraer y confirmar un silencio:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En el laboratorio, la puerta H aplicada al estado 0 da probabilidades 0,5 y 0,5; aplicada una segunda vez, devuelve 1,0 y 0,0, porque la amplitud del estado 1 recibe dos contribuciones de signo opuesto que se cancelan. ([SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Qubit](../q/qubit.md), [Amplitud](../a/amplitud.md), [Cobertura con umbral](../c/cobertura-con-umbral.md), [Cosechar ahora, descifrar después](../c/cosechar-ahora-descifrar-despues.md), [Encadenado](../e/encadenado.md), [Enrutador](../e/enrutador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (75 clases más lo mencionan; las que más):

[SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md), [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md), [SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Spotify](../../../casos/exito/spotify.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Publicación y repositorio](./publicacion-y-repositorio.md) · [Puerta de aprobación →](./puerta-de-aprobacion.md)
