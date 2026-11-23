# Cola de radio

[↑ Glosario](../../README.md) · [← Cola de muertos](./cola-de-muertos.md) · [Cola de rechazos →](./cola-de-rechazos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Tiempo durante el cual la radio sigue activa tras transmitir y que puede costar más energía que la transmisión.

Definición de trabajo de [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md).

## Por qué importa

La clase donde se define, [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), existe con este propósito: la clase existe para que trates el rendimiento, la batería y la memoria de un cliente como presupuestos que se miden y se reparten, no como adjetivos: cuánto trabajo hace la interfaz por elemento, cuántas veces despierta la radio y cuánta memoria compra cada punto de aciertos de una caché.

## Cómo funciona

[SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md):

El equipo del cliente define su presupuesto en un dispositivo de referencia modesto: la lista de tareas responde en menos de 100 ms con 3000 elementos, la sincronización en segundo plano no despierta la radio más de 24 veces al día y las miniaturas ocupan menos de 30 MB. Cada cifra tiene un nombre de responsable y una prueba automática que mide en una ejecución de referencia.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md)) son:

- **La lista se vuelve lenta al crecer** — causa: se construye cada elemento aunque no se vea. Corrección: virtualizar la lista y medir con 100 000 elementos.
- **La batería baja mucho con la aplicación en segundo plano** — causa: sondeo frecuente que despierta la radio. Corrección: empuje o lote y agrupar trabajo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): las cifras deterministas fueron idénticas y los tiempos se informan por sistema. No se midió ningún teléfono ni batería: los costes de energía y los accesos son del autor. La siguiente clase revisa la seguridad del cliente.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Energía](../e/energia.md), [Caché LRU](./cache-lru.md), [Presupuesto de recursos](../p/presupuesto-de-recursos.md), [Tasa de aciertos](../t/tasa-de-aciertos.md), [Virtualización de lista](../v/virtualizacion-de-lista.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

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

[↑ Glosario](../../README.md) · [← Cola de muertos](./cola-de-muertos.md) · [Cola de rechazos →](./cola-de-rechazos.md)
