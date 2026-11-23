# Horizonte de predictibilidad

[↑ Glosario](../../README.md) · [← Horizonte de equilibrio](./horizonte-de-equilibrio.md) · [Horizonte de reintentos →](./horizonte-de-reintentos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Número de pasos tras el cual una diferencia inicial pequeña se amplifica hasta igualar la señal.

Definición de trabajo de [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md).

## Por qué importa

La clase donde se define, [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), existe con este propósito: la clase existe para que distingas tres cosas que el lenguaje cotidiano confunde: repetir una ejecución, obtener un resultado estable y poder defender que ese resultado describe el fenómeno.

## Cómo funciona

[SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el modelo de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md):

El equipo de la plataforma crea `model/` con un `requirements.txt` fijado, una función `simular(semilla, n)` pura, un script `repetir.py` que ejecuta 200 semillas y escribe la media, la desviación y los percentiles 5 y 95, y una prueba que compara dos ejecuciones con la misma semilla con igualdad exacta y dos plataformas con tolerancia relativa de 10⁻⁹. El informe publica una frase con la forma «entregas a tiempo: media (intervalo p5 a p95, 200 semillas, versión de Python)» y no la cifra de una ejecución.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se exige igualdad exacta tras miles de pasos de un sistema caótico** — causa: se ignora el horizonte de predictibilidad. Corrección: comparar estadísticos y trayectorias hasta el horizonte medido. ([SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md)) son: Las definiciones son operativas para el modelo de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún código científico real, ningún compilador distinto de CPython ni otras arquitecturas de procesador: las magnitudes de los números, la estimación de π y el mapa logístico son construcciones del autor. La siguiente clase mueve los datos del modelo por una cadena de procesamiento analítico.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Señal](../s/senal.md), [No asociatividad](../n/no-asociatividad.md), [Repetición](../r/repeticion.md), [Replicación](../r/replicacion.md), [Reproducción](../r/reproduccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

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

[↑ Glosario](../../README.md) · [← Horizonte de equilibrio](./horizonte-de-equilibrio.md) · [Horizonte de reintentos →](./horizonte-de-reintentos.md)
