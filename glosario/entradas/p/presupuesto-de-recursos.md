# Presupuesto de recursos

[↑ Glosario](../../README.md) · [← Presupuesto de privacidad](./presupuesto-de-privacidad.md) · [Presupuesto de reintentos →](./presupuesto-de-reintentos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Conjunto de límites medibles de tiempo de respuesta, energía y memoria que el producto acepta en un dispositivo de referencia.

Definición de trabajo de [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md): Lista de supuestos de energía, memoria y precisión con las consecuencias de cada uno.

## Por qué importa

En [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), el tema «Presupuesto de recursos» importa porque un presupuesto convierte «rápido» y «ligero» en números con un responsable.

## Cómo funciona

Según [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), en la sección «Presupuesto de recursos»:

El presupuesto fija cuánto tiempo puede tardar en responder cada pantalla, cuánta energía puede gastar en segundo plano y cuánta memoria puede ocupar, medidos en un dispositivo de referencia modesto. Sin un número, nadie puede decidir si un cambio empeora la situación. El presupuesto se mide y se revisa, y su cifra depende del dispositivo: la de un equipo de escritorio no sirve para un teléfono.

## Ejemplo

Ejemplo de [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md) (sección «Caso conductor»):

El cliente de entregas de la [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) deja aquí su presupuesto de recursos y sus decisiones de lista, sincronización y caché. `SE-262` revisa la superficie de seguridad que cada una añade, `SE-263` mide diferencias entre dos plataformas y `SE-264` integra el presupuesto en el proyecto. Cambia después una sola decisión, el sondeo cada 5 minutos por empuje, y revisa qué cifras cambian.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md)) son:

- **La lista se vuelve lenta al crecer** — causa: se construye cada elemento aunque no se vea. Corrección: virtualizar la lista y medir con 100 000 elementos.
- **La batería baja mucho con la aplicación en segundo plano** — causa: sondeo frecuente que despierta la radio. Corrección: empuje o lote y agrupar trabajo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): las cifras deterministas fueron idénticas y los tiempos se informan por sistema. No se midió ningún teléfono ni batería: los costes de energía y los accesos son del autor. La siguiente clase revisa la seguridad del cliente.

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
