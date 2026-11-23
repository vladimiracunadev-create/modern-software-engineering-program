# Ejecución gestionada

[↑ Glosario](../../README.md) · [← Ejecución en sombra](./ejecucion-en-sombra.md) · [Ejemplo ancla →](./ejemplo-ancla.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Modelo en que la plataforma crea, escala y apaga las instancias que ejecutan el código a partir de eventos o peticiones.

Definición de trabajo de [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md).

## Por qué importa

La clase donde se define, [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), existe con este propósito: la clase existe para que, cuando alguien proponga «pasarlo a funciones» o «a un servicio gestionado sin servidores», puedas decir qué deja de hacer tu equipo, qué sigue haciendo con otra forma y qué consecuencias nuevas aparecen: arranques en frío, entregas repetidas y un costo que ya no es una cuota fija sino una función del tráfico.

## Cómo funciona

Según [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md):

En un servicio de ejecución gestionada entregas tu código y la plataforma se ocupa del sistema operativo, del escalado, de arrancar y apagar instancias y, según el producto, del balanceo y de la integración con colas o eventos. Tu parte son el código, las dependencias, la configuración, los permisos y todo lo que ocurre alrededor de una invocación: tiempo máximo, memoria, reintentos y estado. Las funciones suelen ser sin estado entre invocaciones y de duración limitada, lo que obliga a guardar el estado fuera y a dividir los trabajos largos. Hellerstein y colaboradores señalaron en 2019 que esas limitaciones, el estado, la comunicación y la ausencia de coordinación, restringen a qué cargas conviene este modelo.

Según [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md):

El equipo de la plataforma clasifica sus piezas. El aviso de recibo, con poco tráfico fuera del cierre, tolera un arranque de un segundo y pasa a ejecución gestionada con un identificador de entrega como clave de idempotencia guardada junto al registro de aviso, de modo que dos eventos iguales no envían dos correos. La conversión de archivos de entregas, con picos fuertes y trabajos de minutos, se queda en contenedores con una cola porque supera el tiempo máximo de una función. El servicio de calificación, con tráfico constante y estado en memoria, no se mueve. Para el aviso mide el arranque con y sin la biblioteca de plantillas de correo, la carga de forma diferida y deja un presupuesto de latencia explícito.

## Ejemplo

Ejemplo de [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma clasifica sus piezas. El aviso de recibo, con poco tráfico fuera del cierre, tolera un arranque de un segundo y pasa a ejecución gestionada con un identificador de entrega como clave de idempotencia guardada junto al registro de aviso, de modo que dos eventos iguales no envían dos correos. La conversión de archivos de entregas, con picos fuertes y trabajos de minutos, se queda en contenedores con una cola porque supera el tiempo máximo de una función. El servicio de calificación, con tráfico constante y estado en memoria, no se mueve.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md)) son:

- **La primera petición tras un silencio tarda segundos** — causa: arranque en frío con inicialización pesada. Corrección: reducir dependencias de inicio y medir; reservar capacidad si la latencia importa.
- **Un correo o un cobro se repite** — causa: manejador no idempotente con entrega al menos una vez. Corrección: guardar el identificador del evento con el efecto.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una instancia permanente cuesta lo mismo con tráfico que sin él; una ejecución gestionada cobra por petición y por recursos consumidos. ([SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md))
- La transferencia está lograda cuando puedes decir qué piezas no pasarías a ejecución gestionada y por qué, no cuando el código se parece. ([SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](./evento.md), [Instancia](../i/instancia.md), [Modelo](../m/modelo.md), [Plataforma](../p/plataforma.md), [Arranque en frío](../a/arranque-en-frio.md), [Entrega al menos una vez](./entrega-al-menos-una-vez.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Lambda: entorno de ejecución](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) — fases de un entorno y su reutilización; autoridad: documentación del proveedor.
- [Google Cloud Run: documentación](https://cloud.google.com/run/docs) — servicio gestionado con escalado automático; autoridad: documentación del proveedor.
- [Serverless Computing: One Step Forward, Two Steps Back](https://arxiv.org/abs/1812.03651) — límites del modelo; autoridad: artículo de investigación (CIDR 2019).
- [CloudEvents](https://cloudevents.io/) — identificación de eventos y reenvíos; autoridad: proyecto de la Cloud Native Computing Foundation.
- [Python: opciones de línea de comandos](https://docs.python.org/3/using/cmdline.html) — medición del tiempo de importación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Ejecución en sombra](./ejecucion-en-sombra.md) · [Ejemplo ancla →](./ejemplo-ancla.md)
