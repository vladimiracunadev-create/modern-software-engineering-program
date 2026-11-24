# Grupo de control

[↑ Glosario](../../README.md) · [← Green Software Engineer](./green-software-engineer.md) · [Guarda →](./guarda.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Un **grupo de control** es la parte del tráfico (o de la población) que no recibe la intervención y se mide a la vez que el grupo experimental, para tener un punto de comparación ([SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md)). El programa usa el término con matices:

- En [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) y [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) (ingeniería del caos): grupo comparable que recibe el mismo tráfico sin la falla.
- En [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md) (ML en producción): parte de la población a la que no se aplica la decisión, para medir su efecto.
- En [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) (plataforma): *cgroup*, un mecanismo del núcleo que reparte y limita el consumo de recursos de un conjunto de procesos. Es un homónimo técnico sin relación con el diseño experimental.

## Por qué importa

Sin un grupo de control, una diferencia observada puede deberse a la intervención o a cualquier otra cosa que cambió en ese momento: la hora, el cierre de un plazo, un pico de tráfico. La decisión que cambia es cómo se concluye de un experimento: comparando contra un control contemporáneo, no contra una memoria de cómo era antes.

## Cómo funciona

[SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) presenta el método de la ingeniería del caos en cuatro pasos: definir el estado estable como una salida medible que indica comportamiento normal; formular la hipótesis de que continuará en un grupo de control y en uno experimental; introducir variables que reflejen eventos reales; e intentar refutar la hipótesis buscando una diferencia entre ambos grupos. La falla solo se aplica al experimental; el control recibe el mismo tráfico sin falla.

[SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) muestra la arquitectura: un enrutador envía casi todo el tráfico a la flota normal y dos porciones pequeñas (de ejemplo, 2 %) a los grupos de control y experimental; un comparador mide a ambos, y un interruptor detiene el experimento si el experimental se degrada más que un límite. La razón del grupo contemporáneo es estadística: absorbe las variaciones comunes (hora, cierre de plazo) que una línea base de otra hora no absorbe. Por eso es la forma de medir sobre tráfico real.

En [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), el control es la parte de la población a la que no se aplica la decisión de un modelo, y permite medir su efecto real.

## Ejemplo

Se inyecta latencia en el 2 % del tráfico (experimental) mientras otro 2 % (control) sigue sin falla. Si ambos suben su tasa de errores por un pico de entregas, la diferencia entre ellos sigue siendo cero; si solo sube la del experimental, la falla es la causa. Diseño de [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

## Errores y confusiones comunes

- **El estado estable cambia con el día**: línea base de un día excepcional; se corrige midiendo en días comparables y prefiriendo el grupo de control ([SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md)).
- **Una divergencia pequeña no se ve**: comparación con una línea base de otra hora; se corrige con un grupo de control contemporáneo ([SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md)).
- **Control y experimental no comparables**: si los grupos se reparten con un sesgo, la comparación no vale.
- **Confundirlo con el cgroup del núcleo**: homónimo sin relación.

## Límites y cuándo no aplica

[SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) advierte que el dibujo es un esquema de ejemplo con proporciones ilustrativas, no el diseño de una plataforma real. Con muy poco tráfico, los grupos pequeños no tienen potencia para detectar diferencias. Y en algunos sistemas no se puede reservar una parte de la población sin la decisión (por ejemplo, por razones éticas o legales), lo que limita el diseño con control.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Efecto](../e/efecto.md), [Mecanismo](../m/mecanismo.md), [Núcleo](../n/nucleo.md), [Banda](../b/banda.md), [Contenedor](../c/contenedor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), [SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Netflix: «Chaos Engineering Upgraded»](https://netflixtechblog.com/chaos-engineering-upgraded-878d341f15fa) — ejemplo de experimento con estado estable, hipótesis y grupo de control; autoridad: blog de ingeniería de Netflix.
- [Control Group v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — grupos de control y distribución de recursos; autoridad: documentación del núcleo Linux.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — estado estable, hipótesis y salida medible; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, ventanas y percentiles; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuesto de error; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← Green Software Engineer](./green-software-engineer.md) · [Guarda →](./guarda.md)
