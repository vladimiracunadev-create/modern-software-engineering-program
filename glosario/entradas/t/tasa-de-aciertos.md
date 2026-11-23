# Tasa de aciertos

[↑ Glosario](../../README.md) · [← Tarjeta de modelo](./tarjeta-de-modelo.md) · [Tasa de consumo →](./tasa-de-consumo.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Fracción de los accesos que se sirven desde la caché sin reconstruir o descargar el elemento.

Definición de trabajo de [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md).

## Por qué importa

La clase donde se define, [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), existe con este propósito: la clase existe para que trates el rendimiento, la batería y la memoria de un cliente como presupuestos que se miden y se reparten, no como adjetivos: cuánto trabajo hace la interfaz por elemento, cuántas veces despierta la radio y cuánta memoria compra cada punto de aciertos de una caché.

## Cómo funciona

Según [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md):

Resultado: con el **1 %** del catálogo la tasa de aciertos es **30,3 %**; con **5 %**, **56,8 %**; con **10 %**, **67,3 %**; con **25 %**, **80,4 %**; con **50 %**, **90,0 %**; con **100 %**, **98,0 %** (el resto son las primeras lecturas). Con un 10 % de la memoria se consiguen dos tercios de los aciertos; pasar del 50 % al 100 % cuesta el doble de memoria para ocho puntos.

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
- **Ver también:** [Caché LRU](../c/cache-lru.md), [Cola de radio](../c/cola-de-radio.md), [Presupuesto de recursos](../p/presupuesto-de-recursos.md), [Virtualización de lista](../v/virtualizacion-de-lista.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-261 — Rendimiento, batería y recursos limitados](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md), [SE-556](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md).

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

[↑ Glosario](../../README.md) · [← Tarjeta de modelo](./tarjeta-de-modelo.md) · [Tasa de consumo →](./tasa-de-consumo.md)
