# Amplitud

[↑ Glosario](../../README.md) · [← Amplificación por reintentos](./amplificacion-por-reintentos.md) · [Análisis →](./analisis.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Número complejo cuyo módulo al cuadrado es la probabilidad de un resultado.

Definición de trabajo de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md).

## Por qué importa

En [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), el tema «Amplitudes e interferencia» importa porque es la diferencia entre «probar todo» y un algoritmo cuántico.

## Cómo funciona

Según [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md):

Un qubit no es un bit con valores intermedios: es un par de amplitudes complejas, una para el estado 0 y otra para el 1, cuyos cuadrados de módulo suman 1. Un registro de n qubits tiene 2^n amplitudes. Las puertas son transformaciones lineales que conservan esa suma (matrices unitarias). La medición toma una de las 2^n respuestas con probabilidad igual al cuadrado del módulo de su amplitud, y destruye el resto. En el laboratorio, la puerta H aplicada al estado 0 da probabilidades 0,5 y 0,5; aplicada una segunda vez, devuelve 1,0 y 0,0, porque la amplitud del estado 1 recibe dos contribuciones de signo opuesto que se cancelan.

## Ejemplo

Caso medido en la sección «Qubits, amplitudes y medición» de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md):

Un qubit no es un bit con valores intermedios: es un par de amplitudes complejas, una para el estado 0 y otra para el 1, cuyos cuadrados de módulo suman 1. Un registro de n qubits tiene 2^n amplitudes. Las puertas son transformaciones lineales que conservan esa suma (matrices unitarias). La medición toma una de las 2^n respuestas con probabilidad igual al cuadrado del módulo de su amplitud, y destruye el resto.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un qubit no es un bit con valores intermedios: es un par de amplitudes complejas, una para el estado 0 y otra para el 1, cuyos cuadrados de módulo suman 1. ([SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Módulo](../m/modulo.md), [Resultado](../r/resultado.md), [Cosechar ahora, descifrar después](../c/cosechar-ahora-descifrar-despues.md), [Entrelazamiento](../e/entrelazamiento.md), [Interferencia](../i/interferencia.md), [NISQ](../n/nisq.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-538](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-538-portafolio-entrevistas-y-defensa-profesional/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Amplificación por reintentos](./amplificacion-por-reintentos.md) · [Análisis →](./analisis.md)
