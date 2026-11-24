# Presupuesto de recursos

[↑ Glosario](../../README.md) · [← Presupuesto de privacidad](./presupuesto-de-privacidad.md) · [Presupuesto de reintentos →](./presupuesto-de-reintentos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

El **presupuesto de recursos** es el conjunto de límites medibles de tiempo de respuesta, energía y memoria que el producto acepta en un dispositivo de referencia. Es el sentido de [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md) (rendimiento, batería y recursos limitados). [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) lo usa en dispositivos embebidos con un matiz: una lista de supuestos de energía, memoria y precisión con las consecuencias de cada uno.

## Por qué importa

Convierte «rápido» y «ligero» en números con un responsable. Sin un número, nadie puede decidir si un cambio empeora la situación: cada cambio parece pequeño y la suma es un producto lento que agota la batería.

## Cómo funciona

[SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md): el presupuesto fija

- **cuánto tiempo puede tardar** en responder cada pantalla,
- **cuánta energía puede gastar** en segundo plano,
- **cuánta memoria puede ocupar**,

todo medido en un **dispositivo de referencia modesto**. Debe medirse y revisarse, y su cifra depende del dispositivo: la de un equipo de escritorio no sirve para un teléfono. Un presupuesto sin medición automática ni dueño es una intención.

En el mundo embebido ([SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md)), el presupuesto es la lista de supuestos y sus consecuencias: cuánta corriente media consume el dispositivo (determinada por el ciclo de trabajo), cuánta memoria deja libre el firmware y qué precisión numérica se acepta. Cada supuesto se anota con lo que ocurre si no se cumple.

## Ejemplo

El cliente de entregas de la [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) deja en [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md) su presupuesto de recursos y sus decisiones de lista, sincronización y caché. Luego [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) revisa la superficie de seguridad que cada decisión añade, [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) mide diferencias entre dos plataformas y [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) integra el presupuesto en el proyecto. Cambiar una sola decisión, el sondeo cada 5 minutos por notificaciones por empuje, muestra qué cifras cambian: menos despertares y menos energía, con otra dependencia.

## Errores y confusiones comunes

- **Fijarlo sin dispositivo de referencia** o con el equipo de desarrollo, que es potente.
- **Medirlo una vez y no revisarlo.**
- **Un presupuesto sin dueño ni acción al superarlo.**
- **Confundirlo con el presupuesto de rendimiento web,** que se mide en bytes y métricas de carga ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md)), o con el presupuesto de fotograma, que es un plazo de dibujo.

## Límites y cuándo no aplica

El dispositivo de referencia envejece: lo modesto de hoy no lo es en dos años. Las cifras exactas dependen del producto; la clase da el método, no los valores universales. En un sistema de servidor la analogía se expresa en capacidad y costo, no en batería.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tiempo de respuesta](../t/tiempo-de-respuesta.md), [Conjunto](../c/conjunto.md), [Consecuencia](../c/consecuencia.md), [Dispositivo](../d/dispositivo.md), [Caché LRU](../c/cache-lru.md), [Ciclo de trabajo](../c/ciclo-de-trabajo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Android Developers, «Optimize for Doze and App Standby»](https://developer.android.com/training/monitoring-device-state/doze-standby) — restricciones de segundo plano y cómo agrupar trabajo; autoridad: Google.
- [Android Developers, «App performance»](https://developer.android.com/topic/performance) — medición y mejora del rendimiento en Android; autoridad: Google.
- [Apple Developer, «Energy Efficiency Guide for iOS Apps»](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/) — principios de eficiencia energética en iOS; autoridad: Apple.
- [Electron, «Performance»](https://www.electronjs.org/docs/latest/tutorial/performance) — lista de comprobaciones de rendimiento en aplicaciones de escritorio; autoridad: OpenJS Foundation.
- [Balasubramanian et al., «Energy consumption in mobile phones» (IMC 2009)](https://doi.org/10.1145/1644893.1644927) — consumo de la radio y fase de cola; autoridad: ACM IMC.

---

[↑ Glosario](../../README.md) · [← Presupuesto de privacidad](./presupuesto-de-privacidad.md) · [Presupuesto de reintentos →](./presupuesto-de-reintentos.md)
