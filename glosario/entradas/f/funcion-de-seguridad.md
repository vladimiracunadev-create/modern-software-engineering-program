# Función de seguridad

[↑ Glosario](../../README.md) · [← Función de aptitud arquitectónica](./funcion-de-aptitud-arquitectonica.md) · [Función hash y buckets →](./funcion-hash-y-buckets.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Acción que lleva al sistema a un estado seguro o lo mantiene en él ante una condición peligrosa.

Definición de trabajo de [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md).

## Por qué importa

En [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), el tema «Función de seguridad» importa porque define qué debe detectar, hacer y en cuánto tiempo.

## Cómo funciona

Según [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md):

Una función de seguridad es una acción que se realiza para llevar el sistema a un estado seguro o mantenerlo en él cuando ocurre una condición peligrosa. En el horno es «si la temperatura medida supera 250 °C o la puerta se abre, desconectar el calentador en menos de dos segundos». La función incluye el sensor que mide, la lógica que decide y el actuador que corta, y a veces también a la persona que actúa. Su nivel de integridad es el de la cadena completa: el eslabón más débil y las causas comunes entre eslabones deciden. Escribir la función con su tiempo de respuesta es parte de la especificación: una protección que actúa tarde (`SE-451`) puede ser correcta y no servir.

Según [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md):

Elige una función de seguridad de tu entorno (un corte, un bloqueo, una alarma que debe actuar). Escríbela con su condición, acción y tiempo. Calcula su probabilidad de fallo con dos arquitecturas posibles y dos intervalos de prueba y determina qué parámetro domina. Documenta cómo se probaría de verdad cada fallo latente y qué porcentaje cubriría tu prueba actual.

## Ejemplo

Caso medido en la sección «Función de seguridad: lo que se protege, no el dispositivo» de [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md):

Una función de seguridad es una acción que se realiza para llevar el sistema a un estado seguro o mantenerlo en él cuando ocurre una condición peligrosa. En el horno es «si la temperatura medida supera 250 °C o la puerta se abre, desconectar el calentador en menos de dos segundos». La función incluye el sensor que mide, la lógica que decide y el actuador que corta, y a veces también a la persona que actúa. Su nivel de integridad es el de la cadena completa: el eslabón más débil y las causas comunes entre eslabones deciden.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Elige una función de seguridad de tu entorno (un corte, un bloqueo, una alarma que debe actuar). ([SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado seguro](../e/estado-seguro.md), [Condición](../c/condicion.md), [Estado](../e/estado.md), [Β](../c/concepto.md), [Arquitectura MooN](../a/arquitectura-moon.md), [Causa común](../c/causa-comun.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md).

**Aparece en los casos de estudio:** [Cloudflare](../../../casos/exito/cloudflare.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Función de aptitud arquitectónica](./funcion-de-aptitud-arquitectonica.md) · [Función hash y buckets →](./funcion-hash-y-buckets.md)
