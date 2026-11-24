# Arranque en frío

[↑ Glosario](../../README.md) · [← Arquitectura MooN](./arquitectura-moon.md) · [Arreglo contiguo y localidad →](./arreglo-contiguo-y-localidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

**Arranque en frío** es la creación de un entorno de ejecución para atender una petición cuando no hay uno disponible. Es el sentido principal de [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) (serverless y ejecución gestionada). El programa lo usa en cuatro contextos relacionados por la misma idea («parte de cero»): en [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), arranque de una aplicación sin proceso ni estado en memoria; en [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), latencia añadida al crear un entorno inexistente; en [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), tiempo desde que se pide una réplica hasta que sirve; y en [SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), el problema distinto de las plataformas de dos lados que no llegan sin masa en el otro lado.

## Por qué importa

La primera petición tras un silencio paga el costo de crear el entorno. Eso no es una falla: según [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), es el precio de pagar solo cuando hay uso. La decisión que cambia es si ese costo es tolerable para el escenario de latencia, y qué hacer si no lo es.

## Cómo funciona

En serverless ([SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md)), para atender una petición la plataforma necesita un entorno con el código cargado. Si hay uno libre y vigente lo reutiliza (arranque caliente); si no, crea uno: reserva recursos, descarga o monta el código, inicia el proceso y ejecuta la inicialización. Los entornos pueden reutilizarse, pero la documentación de Lambda no promete cuánto se conservan inactivos. Resultado: mayor latencia tras un silencio y en cada pico que supera las instancias existentes.

En aplicaciones de teléfono y escritorio ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md)) el arranque en frío parte sin proceso; en caliente encuentra el proceso vivo. La fracción de arranques fríos depende de la presión de memoria y del tiempo fuera, y el equipo no la controla; por eso restaurar el estado desde disco debe ser parte normal del arranque.

En servir modelos ([SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md)), es el tiempo hasta que una réplica nueva sirve, lo que limita cuán rápido puede reaccionar el escalado.

## Ejemplo

[SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md): la revisión antivirus pasa a funciones bajo demanda con 10 instancias provisionadas durante la ventana de cierre, porque el 11,1 % de arranques en frío al inicio del pico era inaceptable. Con una función de 512 MB y 0,15 s, el equilibrio de costo es de 7,8 peticiones por segundo; como el tráfico medio ronda 2,5 por segundo, gana el pago por uso. Los números son del patrón simulado de la clase.

## Errores y confusiones comunes

- **Primera petición lenta tras un silencio:** causa, inicialización pesada; corrección, reducir dependencias de arranque y medir ([SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md)).
- **Lentitud solo en los primeros segundos de un pico:** arranque concentrado; se aprovisionan instancias en la ventana crítica ([SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md)).
- **Confundirlo con el calentamiento:** el arranque en frío es crear el entorno; el calentamiento es llenar cachés y conexiones de uno ya creado.

## Límites y cuándo no aplica

Con tráfico sostenido y alto el costo de arranque se amortiza y deja de ser relevante. Los tiempos de [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) son construcciones del autor, no mediciones de un proveedor. Y el sentido de [SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) es de mercado, no técnico: no se resuelve con instancias aprovisionadas.

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
