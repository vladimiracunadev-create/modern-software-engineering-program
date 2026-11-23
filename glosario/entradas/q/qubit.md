# Qubit

[↑ Glosario](../../README.md) · [← Quality gate](./quality-gate.md) · [Qubit lógico y físico →](./qubit-logico-y-fisico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Unidad de información cuántica descrita por dos amplitudes complejas.

Definición de trabajo de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md).

## Por qué importa

La clase donde se define, [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), existe con este propósito: la clase existe para que un ingeniero de software pueda leer una afirmación sobre computación cuántica (un titular, una propuesta de un proveedor, una exigencia de cumplimiento) y decidir qué parte es verificable, qué parte es especulación y qué decisión concreta le cambia.

## Cómo funciona

Según [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md):

Un qubit no es un bit con valores intermedios: es un par de amplitudes complejas, una para el estado 0 y otra para el 1, cuyos cuadrados de módulo suman 1. Un registro de n qubits tiene 2^n amplitudes. Las puertas son transformaciones lineales que conservan esa suma (matrices unitarias). La medición toma una de las 2^n respuestas con probabilidad igual al cuadrado del módulo de su amplitud, y destruye el resto. En el laboratorio, la puerta H aplicada al estado 0 da probabilidades 0,5 y 0,5; aplicada una segunda vez, devuelve 1,0 y 0,0, porque la amplitud del estado 1 recibe dos contribuciones de signo opuesto que se cancelan.

Según [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md):

El equipo de *Avisos* responde al cuestionario con tres frases. Primera: «Nuestro cifrado actual de claves públicas (RSA y curvas elípticas) sería vulnerable a un ordenador cuántico de escala suficiente; no existe hoy un dispositivo así, y las estimaciones publicadas requieren del orden de un millón de qubits ruidosos». Segunda: «Los datos con vida de más de diez años (historiales de estudiantes) se consideran expuestos a la estrategia de almacenar hoy y descifrar después; por eso hemos iniciado un inventario criptográfico y un plan de migración con hitos». Tercera: «No afirmamos ser resistentes a ataques cuánticos hasta completar la migración; el plan, con fechas y responsables, está adjunto».

## Ejemplo

Ejemplo de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* responde al cuestionario con tres frases. Primera: «Nuestro cifrado actual de claves públicas (RSA y curvas elípticas) sería vulnerable a un ordenador cuántico de escala suficiente; no existe hoy un dispositivo así, y las estimaciones publicadas requieren del orden de un millón de qubits ruidosos». Segunda: «Los datos con vida de más de diez años (historiales de estudiantes) se consideran expuestos a la estrategia de almacenar hoy y descifrar después; por eso hemos iniciado un inventario criptográfico y un plan de migración con hitos». Tercera: «No afirmamos ser resistentes a ataques cuánticos hasta completar la migración; el plan, con fechas y responsables, está adjunto».

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un qubit no es un bit con valores intermedios: es un par de amplitudes complejas, una para el estado 0 y otra para el 1, cuyos cuadrados de módulo suman 1. ([SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Amplitud](../a/amplitud.md), [Cosechar ahora, descifrar después](../c/cosechar-ahora-descifrar-despues.md), [Entrelazamiento](../e/entrelazamiento.md), [Interferencia](../i/interferencia.md), [NISQ](../n/nisq.md), [Puerta](../p/puerta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Quality gate](./quality-gate.md) · [Qubit lógico y físico →](./qubit-logico-y-fisico.md)
