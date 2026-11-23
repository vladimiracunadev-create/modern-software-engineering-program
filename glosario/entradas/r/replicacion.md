# Replicación

[↑ Glosario](../../README.md) · [← Réplica pequeña](./replica-pequena.md) · [Replicación asíncrona →](./replicacion-asincrona.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Llegar a una conclusión consistente con datos nuevos obtenidos de forma independiente.

Definición de trabajo de [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md).

## Por qué importa

En [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), el tema «Repetición, reproducción y replicación» importa porque decide qué se promete y qué se verifica en una publicación o un informe.

## Cómo funciona

Según [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md):

**Repetir** es ejecutar de nuevo el mismo programa con los mismos datos y obtener el mismo resultado; lo hace quien lo escribió, para comprobar que no depende de algo olvidado. **Reproducir**, en el sentido que fija el informe de las Academias Nacionales, es que otra persona, con los mismos datos y el mismo código, obtenga el mismo resultado dentro de una tolerancia declarada. **Replicar** es llegar a una conclusión consistente con datos nuevos. Son promesas distintas y cada una falla por razones distintas: la repetición falla por estado oculto (una variable de entorno, un archivo sin versionar), la reproducción por diferencias numéricas o de dependencias, la replicación porque el efecto no existía o dependía de la muestra.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md):

El equipo de la plataforma crea `model/` con un `requirements.txt` fijado, una función `simular(semilla, n)` pura, un script `repetir.py` que ejecuta 200 semillas y escribe la media, la desviación y los percentiles 5 y 95, y una prueba que compara dos ejecuciones con la misma semilla con igualdad exacta y dos plataformas con tolerancia relativa de 10⁻⁹. El informe publica una frase con la forma «entregas a tiempo: media (intervalo p5 a p95, 200 semillas, versión de Python)» y no la cifra de una ejecución.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md)) son:

- **El total difiere en la última cifra entre dos ejecuciones** — causa: orden de suma distinto (hilos, particiones). Corrección: fijar el orden o usar una suma con error acotado y comparar con tolerancia.
- **Una estimación cambia de decimales con otra semilla** — causa: se publicó una muestra de tamaño uno. Corrección: repetir con muchas semillas y publicar la dispersión.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Son promesas distintas y cada una falla por razones distintas: la repetición falla por estado oculto (una variable de entorno, un archivo sin versionar), la reproducción por diferencias numéricas o de dependencias, la replicación porque el efecto no existía o dependía de la muestra. ([SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Horizonte de predictibilidad](../h/horizonte-de-predictibilidad.md), [No asociatividad](../n/no-asociatividad.md), [Repetición](./repeticion.md), [Reproducción](./reproduccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (16 clases más lo mencionan; las que más):

[SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Peng, «Reproducible Research in Computational Science» (Science, 2011)](https://doi.org/10.1126/science.1213847) — espectro de reproducibilidad en ciencia computacional; autoridad: Science.
- [National Academies, «Reproducibility and Replicability in Science» (2019)](https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science) — definiciones de reproducir y replicar; autoridad: National Academies of Sciences, Engineering, and Medicine.
- [Goldberg, «What every computer scientist should know about floating-point arithmetic» (ACM Computing Surveys, 1991)](https://doi.org/10.1145/103162.103163) — redondeo y no asociatividad; autoridad: ACM Computing Surveys.
- [Wilson et al., «Good enough practices in scientific computing» (PLOS Computational Biology, 2017)](https://doi.org/10.1371/journal.pcbi.1005510) — prácticas básicas para software científico; autoridad: PLOS Computational Biology.
- [Wilkinson et al., «The FAIR Guiding Principles for scientific data management and stewardship» (Scientific Data, 2016)](https://doi.org/10.1038/sdata.2016.18) — datos localizables, accesibles, interoperables y reutilizables; autoridad: Scientific Data.

---

[↑ Glosario](../../README.md) · [← Réplica pequeña](./replica-pequena.md) · [Replicación asíncrona →](./replicacion-asincrona.md)
