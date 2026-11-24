# Ventana

[↑ Glosario](../../README.md) · [← Vendorización](./vendorizacion.md) · [Ventana de contexto →](./ventana-de-contexto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Una **ventana** es, en el sentido principal del programa ([SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md)), el conjunto de observaciones recientes que se compara con una referencia, por ejemplo para detectar deriva en un modelo. [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) usa el término en procesamiento de flujos: un intervalo del tiempo del evento sobre el que se agrega. En ambos, una ventana acota el tramo de datos sobre el que se calcula algo.

## Por qué importa

Un flujo de datos no tiene fin, así que cualquier medida o comparación necesita un recorte. La decisión que cambia es qué tramo se mira y de qué tamaño: una ventana corta reacciona rápido y da ruido; una larga es estable y tarda en notar el cambio.

## Cómo funciona

En monitoreo de modelos ([SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md)), un plan debe tener tres capas, porque cada una ve lo que las otras no:

- **Calidad de entrada**: comprueba rango, nulos, esquema y unidades de cada lote. Es inmediata y barata, y detecta las fallas más frecuentes (un campo en cero, una unidad cambiada).
- **Distribución**: compara las entradas y las salidas de una **ventana** con una referencia. Tarda horas o días en acumular datos y produce falsas alarmas.
- **Métrica con etiquetas**: mide el desempeño real, pero tarda el retraso de la etiqueta (siete días en el ejemplo de la clase).

El ejemplo de *Avisos-ML* usa PSI por característica sobre ventanas diarias de 5 000 observaciones, con umbral de 0,2 como ticket de baja urgencia, y una guarda de 10 puntos sobre la tasa de marcados por segmento. A cada capa se le asigna una acción: la calidad de entrada bloquea o degrada, la distribución abre un diagnóstico, la métrica con etiquetas puede disparar un reentrenamiento.

En procesamiento de flujos ([SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md)), la ventana se define sobre el **tiempo del evento** (cuándo ocurrió el hecho), no sobre el tiempo de llegada, lo que obliga a tratar los datos tardíos: hay que decidir cuánto esperar antes de cerrar una ventana. Los tamaños y umbrales son decisiones que dependen del volumen y de la variable observada.

## Ejemplo

Cada día se toma la ventana de las últimas 5 000 observaciones de cada característica y se compara con la referencia de entrenamiento usando PSI. Si supera 0,2, se abre un ticket de baja urgencia con dueño del equipo de datos; el bloqueo inmediato queda para fallas de calidad de entrada. Plan de monitoreo de [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md).

## Errores y confusiones comunes

- **Una ventana demasiado pequeña**: el ruido genera falsas alarmas continuas.
- **Una ventana demasiado grande**: la deriva se nota tarde.
- **Confundir tiempo del evento con tiempo de llegada** al agregar flujos.
- **Usar un solo tipo de comprobación**: cada capa ve lo que las otras no.

## Límites y cuándo no aplica

[SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) advierte que los umbrales son convenciones, no leyes: dependen del número de tramos, del tamaño de la ventana y de la naturaleza de la variable; hay que calibrarlos con datos propios, midiendo la tasa de falsas alarmas con ventanas sin deriva y la sensibilidad con derivas que importen. Una ventana no explica la causa de un cambio, solo lo señala.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tiempo del evento](../t/tiempo-del-evento.md), [Conjunto](../c/conjunto.md), [Evento](../e/evento.md), [Intervalo](../i/intervalo.md), [Dato tardío](../d/dato-tardio.md), [Deriva de concepto](../d/deriva-de-concepto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (168 clases más lo mencionan; las que más):

[SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md), [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [Discord](../../../casos/exito/discord.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Vendorización](./vendorizacion.md) · [Ventana de contexto →](./ventana-de-contexto.md)
