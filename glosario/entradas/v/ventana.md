# Ventana

[↑ Glosario](../../README.md) · [← Vendorización](./vendorizacion.md) · [Ventana de contexto →](./ventana-de-contexto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Conjunto de observaciones recientes que se compara con la referencia.

Definición de trabajo de [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md): Intervalo del tiempo del evento sobre el que se agrega.

## Por qué importa

En [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), el tema «Ventana» importa porque una ventana pequeña es ruidosa y una grande es lenta.

## Cómo funciona

Según [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md):

La calidad de entrada comprueba el rango, los nulos, el esquema y las unidades de cada lote: es inmediata, barata y detecta las fallas más frecuentes (un campo en cero, una unidad cambiada). La distribución compara las entradas y las salidas de una ventana con una referencia: tarda horas o días en acumular datos y produce falsas alarmas. La métrica con etiquetas mide el desempeño real, y tarda el retraso de la etiqueta (`SE-602`), que en *Avisos-ML* es de siete días. Un plan de monitoreo debe tener las tres, porque cada una ve lo que las otras no, y debe asignar a cada una una acción: la calidad de entrada bloquea o degrada, la distribución abre un diagnóstico, la métrica con etiquetas puede disparar un reentrenamiento.

Según [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md):

El equipo de *Avisos-ML* redefine su monitoreo en tres capas. Calidad de entrada: comprobaciones de rango y nulos por característica con un umbral del 1 %, que bloquean el lote y degradan a la regla (`SE-601`), con dueño operaciones. Distribución: PSI por característica sobre ventanas diarias de 5 000 observaciones, con umbral de 0,2 como ticket de baja urgencia con dueño datos, y tasa de marcados por segmento con una guarda de 10 puntos. Etiquetas: AUC semanal por segmento con las etiquetas de hace siete días, y una muestra de 200 casos revisados cada semana para detectar caídas grandes antes.

## Ejemplo

Ejemplo de [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) (sección «Ejemplo mínimo»):

Con una ventana de la misma distribución devuelve valores cercanos a cero y con un desplazamiento de la media, valores crecientes. El recorte de 1e-4 evita logaritmos de cero; el número de tramos y el recorte son decisiones que cambian el valor, de modo que el umbral debe calibrarse con datos propios.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Son convenciones, no leyes: dependen del número de tramos, del tamaño de la ventana y de la naturaleza de la variable. ([SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md))
- El que calibres con tus datos: mide la tasa de falsas alarmas con ventanas sin deriva y la sensibilidad con derivas que te importen. ([SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md))

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
