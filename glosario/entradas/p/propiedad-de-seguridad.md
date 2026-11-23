# Propiedad de seguridad

[↑ Glosario](../../README.md) · [← Propiedad de archivos](./propiedad-de-archivos.md) · [Propiedad de vivacidad →](./propiedad-de-vivacidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Algo malo nunca ocurre.

Definición de trabajo de [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md).

## Por qué importa

La clase donde se define, [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), existe con este propósito: la clase existe para que entiendas qué demuestra, y qué no, un verificador de modelos o de programas, y cuándo vale la pena usarlo en un sistema crítico.

## Cómo funciona

Según [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md):

Un modelo describe el sistema como un conjunto de estados posibles (valores de las variables y posición de cada proceso) y las transiciones que pueden ocurrir. Una propiedad de seguridad es un invariante: una condición que debe cumplirse en todos los estados alcanzables («no hay dos procesos en la sección crítica»). El verificador parte del estado inicial, explora los sucesores con una búsqueda en anchura y comprueba el invariante en cada estado nuevo; si encuentra uno que lo viola, reconstruye el camino que llega a él. El valor es doble: una demostración dentro del modelo cuando no lo encuentra y un contraejemplo reproducible cuando lo encuentra.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una propiedad de seguridad es un invariante: una condición que debe cumplirse en todos los estados alcanzables («no hay dos procesos en la sección crítica»). ([SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bloqueo](../b/bloqueo.md), [Contraejemplo](../c/contraejemplo.md), [Explosión de estados](../e/explosion-de-estados.md), [Herramientas](../h/herramientas.md), [Invariante](../i/invariante.md), [Modelo de estados](../m/modelo-de-estados.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md), [SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md), [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Propiedad de archivos](./propiedad-de-archivos.md) · [Propiedad de vivacidad →](./propiedad-de-vivacidad.md)
