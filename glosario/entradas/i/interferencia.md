# Interferencia

[↑ Glosario](../../README.md) · [← Interfaz de secuencia](./interfaz-de-secuencia.md) · [Intermediario →](./intermediario.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Efecto de una carga sobre la latencia o el éxito de otra que comparte recursos.

Definición de trabajo de [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md): Efecto sobre una medición de actividad ajena al programa, como otro proceso o un cambio de frecuencia.
- En [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md): Suma de amplitudes que se refuerzan o se cancelan.

## Por qué importa

En [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), el tema «Interferencia» importa porque una lectura larga puede bloquear escrituras.

## Cómo funciona

Según [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md):

Un sistema con pocos miles de filas, preguntas poco frecuentes y un equipo que responde a mano no necesita una plataforma de datos. Una réplica de lectura o una vista materializada resuelven la interferencia sin añadir procesos. La separación empieza a compensar cuando se cumplen a la vez tres cosas: el volumen hace que las preguntas analíticas compitan con la operación, la historia se necesita y se está perdiendo, y varias personas o sistemas piden los mismos números. Si solo ocurre una, suele bastar una solución local. Una plataforma que no se usa es un costo que se paga todos los meses.

Según [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md):

Resuelve la interferencia y no la historia ni la forma. Para volúmenes pequeños y preguntas sobre el presente, basta; para preguntas sobre el pasado o agregados sobre años, la réplica sigue guardando solo el estado actual y recorriendo filas completas.

## Ejemplo

Ejemplo de [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) (sección «Preguntas frecuentes»):

Resuelve la interferencia y no la historia ni la forma. Para volúmenes pequeños y preguntas sobre el presente, basta; para preguntas sobre el pasado o agregados sobre años, la réplica sigue guardando solo el estado actual y recorriendo filas completas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una mejora desaparece al repetir** — causa: ejecución única en un proceso con interferencias. Corrección: repetir en varios procesos con un estadístico robusto. ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md))
- **Dos copias idénticas «difieren»** — causa: pocas repeticiones o media con interferencias. Corrección: prueba A/A y mediana con más repeticiones. ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una réplica de lectura o una vista materializada resuelven la interferencia sin añadir procesos. ([SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md))
- Resuelve la interferencia y no la historia ni la forma. ([SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Medición](../m/medicion.md).
- **Ver también:** [Actividad](../a/actividad.md), [Amplitud](../a/amplitud.md), [Efecto](../e/efecto.md), [Latencia](../l/latencia.md), [Capa](../c/capa.md), [Carga analítica](../c/carga-analitica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md), [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), [SE-094](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Mytkowicz et al., «Producing wrong data without doing anything obviously wrong!»](https://doi.org/10.1145/1508244.1508275) — factores ocultos que invierten conclusiones de benchmarks; autoridad: ASPLOS 2009.
- [Kalibera y Jones, «Rigorous benchmarking in reasonable time»](https://doi.org/10.1145/2464157.2464160) — repeticiones, niveles y reporte de incertidumbre; autoridad: ISMM 2013.
- [Python: timeit](https://docs.python.org/3/library/timeit.html) — uso del mínimo y advertencias de medición; autoridad: documentación de Python.
- [Python: profile y cProfile](https://docs.python.org/3/library/profile.html) — perfilado determinista y su sobrecarga; autoridad: documentación de Python.
- [Python: functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) — caché que puede distorsionar un benchmark; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Interfaz de secuencia](./interfaz-de-secuencia.md) · [Intermediario →](./intermediario.md)
