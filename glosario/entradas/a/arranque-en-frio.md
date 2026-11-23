# Arranque en frío

[↑ Glosario](../../README.md) · [← Arquitectura MooN](./arquitectura-moon.md) · [Arreglo contiguo y localidad →](./arreglo-contiguo-y-localidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Creación de un entorno de ejecución para atender una petición cuando no hay uno disponible.

Definición de trabajo de [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md): Arranque que parte sin proceso ni estado en memoria y debe reconstruir la aplicación desde el disco o el servidor.
- En [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md): El problema de que ninguno de los dos lados llega sin masa en el otro.
- En [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md): Latencia añadida cuando una petición exige crear un entorno de ejecución que no existía.
- En [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md): Tiempo desde que se pide una réplica hasta que sirve.

## Por qué importa

En [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), el tema «Arranque en frío» importa porque la primera petición tras un silencio paga la creación del entorno.

En [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), el tema «Arranque en frío» importa porque si el sistema recupera la memoria, parte de los regresos arrancan sin estado en memoria y el cliente debe reconstruirlo.

En [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), el tema «Arranque en frío» importa porque sin masa en un lado, el otro no llega.

## Cómo funciona

Según [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), en la sección «Arranque en frío»:

Para atender una petición, la plataforma necesita un entorno con el código cargado. Si hay uno libre y vigente, lo reutiliza (arranque caliente); si no, crea uno: reserva recursos, descarga o monta el código, inicia el proceso y ejecuta el código de inicialización. La documentación de Lambda describe esas fases y que los entornos pueden reutilizarse, y no promete cuánto tiempo se conservan inactivos. La consecuencia es una latencia mayor en la primera petición después de un silencio y en cada pico que supera las instancias existentes. No es una falla: es el precio de pagar solo cuando hay uso.

Según [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), en la sección «Arranque en frío»:

Se llama arranque en frío al que parte sin proceso ni estado en memoria, y arranque en caliente al que encuentra el proceso vivo. En escritorio casi todos los regresos son calientes porque el proceso permanece; en un teléfono, la fracción de arranques fríos depende de la presión de memoria y del tiempo que la persona estuvo fuera. Esa fracción no la controla el equipo, pero la restauración del estado desde el disco debe ser parte normal del arranque y no un camino excepcional.

## Ejemplo

Ejemplo de [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) (sección «Ejemplo profesional»):

El equipo asigna cada pieza de la plataforma a un estilo con su escenario. La revisión antivirus pasa a funciones bajo demanda con 10 instancias provisionadas durante la ventana de cierre, porque el tráfico es de picos con poco uso medio y el 11,1 % de arranques en frío del inicio del pico era inaceptable; con una función de 512 MB y 0,15 s el equilibrio es de 7,8 peticiones por segundo y el tráfico medio de la revisión es de unas 2,5 por segundo (9 033 por hora en el patrón simulado), así que gana el pago por uso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La primera petición tras un silencio tarda segundos** — causa: arranque en frío con inicialización pesada. Corrección: reducir dependencias de inicio y medir; reservar capacidad si la latencia importa. ([SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md))
- **La aplicación se comporta bien en el equipo de desarrollo y mal en uso real** — causa: el equipo de desarrollo casi nunca recupera memoria ni abre varias copias. Corrección: forzar el arranque en frío y la segunda instancia en las pruebas. ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md))
- **Lentitud solo en los primeros segundos de un pico** — causa: arranque en frío concentrado. Corrección: aprovisionar instancias en la ventana crítica o reducir la inicialización. ([SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La decisión no se reduce a ese cruce: añade el costo de los arranques en frío, de los límites de tiempo y de reescribir lo que no encaja, y la facilidad de operar o no una flota. ([SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md))
- Traslada el análisis a otro dominio (por ejemplo, un servicio que genera facturas al recibir un pago): cambia las piezas y conserva el procedimiento de clasificar cada pieza, simular el arranque en frío con su tráfico, medir el peso de sus dependencias y diseñar la idempotencia con su ventana. ([SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Entorno](../e/entorno.md), [Estado](../e/estado.md), [Latencia](../l/latencia.md), [Problemas](../p/problemas.md), [Borde de la red](../b/borde-de-la-red.md), [Difusión por rumor](../d/difusion-por-rumor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md), [Cloudflare](../../../casos/exito/cloudflare.md).

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

[↑ Glosario](../../README.md) · [← Arquitectura MooN](./arquitectura-moon.md) · [Arreglo contiguo y localidad →](./arreglo-contiguo-y-localidad.md)
