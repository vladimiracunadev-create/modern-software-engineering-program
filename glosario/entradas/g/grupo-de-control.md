# Grupo de control

[↑ Glosario](../../README.md) · [← Green Software Engineer](./green-software-engineer.md) · [Guarda →](./guarda.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Parte del tráfico que no recibe la falla y se mide a la vez que el grupo experimental.

Definición de trabajo de [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md): Grupo comparable que recibe el mismo tráfico sin la falla.
- En [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md): Parte de la población a la que no se le aplica la decisión, para medir su efecto.
- En [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md): Mecanismo del núcleo que reparte y limita el consumo de recursos de un conjunto de procesos.

## Por qué importa

En [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), el tema «Grupo de control» importa porque la comparación en la misma ejecución absorbe las variaciones comunes.

## Cómo funciona

Según [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md):

Un diseño **declara** resiliencia cuando dice que hay tiempos de espera, reintentos y cortacircuitos; una resiliencia **demostrada** es el comportamiento observado cuando alguien provocó la falla. La definición oficial describe la ingeniería del caos como la disciplina de experimentar sobre un sistema para ganar confianza en su capacidad de resistir condiciones turbulentas, y su método tiene cuatro pasos: definir el estado estable como una salida medible que indica comportamiento normal; formular la hipótesis de que continuará en un grupo de control y en uno experimental; introducir variables que reflejen eventos reales; e intentar refutar la hipótesis buscando una diferencia entre ambos grupos. Esta clase desarrolla los dos primeros pasos, que son los que casi nadie escribe;

Según [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md):

**Cómo leer la figura.** El tráfico real entra por un enrutador que envía casi todo a la flota normal y dos porciones pequeñas a los grupos de control y experimental; la falla solo se aplica al experimental; el comparador mide a ambos y el interruptor detiene el experimento si el experimental se degrada más que un límite. **Dónde deja de valer:** el dibujo es un esquema de ejemplo con proporciones ilustrativas (2 %) y no el diseño de ninguna plataforma real; su valor es mostrar el papel de cada pieza. La comparación con un control contemporáneo absorbe las variaciones comunes (hora, cierre de plazo) que una línea base de otra hora no absorbe, y por eso es la forma de medir sobre tráfico real.

## Ejemplo

Ejemplo de [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* revisa su sistema antes de ampliar el modelo a otra universidad. Dibuja el mapa de diez eslabones y asigna dueños: datos (equipo de plataforma), etiquetas (producto), características y entrenamiento (datos), registro y despliegue (ingeniería de plataforma), servicio y monitoreo (operaciones). Marca tres eslabones sin dueño claro: las etiquetas, el reentrenamiento y la decisión de retirar el modelo. Mide la regla con el mismo conjunto de evaluación y descubre que el modelo mejora al AUC en 0,096. Decide mantener el modelo, pero reservar un 5 % de los estudiantes sin recordatorio para medir el efecto y para reentrenar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El estado estable cambia con el día** — causa: línea base de un día excepcional. Corrección: medir en días comparables y preferir el grupo de control. ([SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md))
- **Una divergencia pequeña no se ve** — causa: comparación con una línea base de otra hora. Corrección: grupo de control contemporáneo. ([SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** El tráfico real entra por un enrutador que envía casi todo a la flota normal y dos porciones pequeñas a los grupos de control y experimental; la falla solo se aplica al experimental; el comparador mide a ambos y el interruptor detiene el experimento si el experimental se degrada más que un límite. ([SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md))

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
