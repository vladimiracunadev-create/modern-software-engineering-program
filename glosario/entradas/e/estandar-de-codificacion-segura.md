# Estándar de codificación segura

[↑ Glosario](../../README.md) · [← Estampida](./estampida.md) · [Estilo arquitectónico →](./estilo-arquitectonico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Conjunto de reglas que restringen el uso del lenguaje para evitar clases de defectos.

Definición de trabajo de [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md).

## Por qué importa

La clase donde se define, [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), existe con este propósito: la clase existe para que entiendas qué hace un estándar de codificación segura, por qué sus reglas son restricciones sobre el lenguaje y no consejos de estilo, y cómo se integra una política así en un proyecto sin convertirla en un rito.

## Cómo funciona

Según [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md):

Los lenguajes de uso general permiten construcciones difíciles de razonar: recursión sin cota, bucles que dependen de datos externos, punteros que se redirigen sin control, comportamientos indefinidos del lenguaje. Un estándar de codificación segura prohíbe o restringe esas construcciones para que el programa que queda sea analizable por herramientas y por personas. La idea de las reglas de Holzmann es notable por su economía: diez reglas que caben en una página, escritas para que una herramienta las compruebe. Entre ellas: flujo de control simple (sin saltos arbitrarios ni recursión), todos los bucles con una cota fija comprobable, funciones que caben en una página, un mínimo de aserciones por función, y comprobar siempre el valor de retorno de las funciones que pueden fallar.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md)) son: Las reglas son una versión en Python de ideas de Holzmann, no MISRA ni CERT; no se ejecutó C y el desbordamiento se emula; los textos de los estándares no se reproducen y no se afirma conformidad con ninguno. El siguiente paso, `SE-453`, pasa de reglas sobre el código a la verificación de propiedades de un modelo: explorar todos los estados y obtener una prueba o un contraejemplo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Regla](../r/regla.md), [Aserción](../a/asercion.md), [Cota de bucle](../c/cota-de-bucle.md), [Desviación](../d/desviacion.md), [Envoltorio de enteros](./envoltorio-de-enteros.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Estampida](./estampida.md) · [Estilo arquitectónico →](./estilo-arquitectonico.md)
