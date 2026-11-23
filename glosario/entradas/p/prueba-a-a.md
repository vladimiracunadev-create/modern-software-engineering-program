# Prueba A/A

[↑ Glosario](../../README.md) · [← Proyector](./proyector.md) · [Prueba basada en requisitos →](./prueba-basada-en-requisitos.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Comparación de dos copias idénticas para estimar la tasa de falsas diferencias de un protocolo.

Definición de trabajo de [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md).

## Por qué importa

La clase donde se define, [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), existe con este propósito: la clase existe para que sepas qué hace tu reloj, tu perfilador y tu benchmark cuando miden: qué parte del número es del programa y qué parte es del instrumento, del equipo y de la elección de estadístico.

## Cómo funciona

Según [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md):

Comparar dos versiones es decidir si dos distribuciones difieren. Con pocas repeticiones, la media es muy sensible a las ejecuciones lentas ocasionales (una interferencia de +50 % en una de cinco ejecuciones mueve la media un 10 %); la mediana es robusta a ellas; el mínimo estima el tiempo sin interferencias pero también es un estadístico extremo que cambia con cada muestra. Ninguno es universalmente correcto. Lo que sí hace falta es fijar de antemano el estadístico, el número de repeticiones y la diferencia mínima relevante, y comprobar cuántas veces el protocolo declara una diferencia cuando comparas dos copias idénticas (una prueba A/A). Si el protocolo «descubre» diferencias entre dos copias iguales, no sirve para comparar dos versiones distintas.

Según [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md):

El equipo quiere decidir si la nueva ordenación de entregas es más rápida. Antes de medir, escribe el protocolo: entrada de 20 000 entregas con la distribución del cierre anterior, 30 repeticiones por versión en 5 procesos nuevos intercalados (A, B, A, B), mediana como estadístico, diferencia mínima relevante del 10 % y criterio de «no distinguible» si el intervalo de las diferencias incluye cero. Ejecuta una prueba A/A para verificar que el protocolo no declara diferencias entre copias iguales y registra el equipo, la carga de fondo y las versiones. Obtiene una diferencia del 4 % con intervalo que incluye cero y concluye «no distinguible»; en lugar de aprobar el cambio por velocidad, lo aprueba por legibilidad.

## Ejemplo

Ejemplo de [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) (sección «Ejemplo profesional»):

El equipo quiere decidir si la nueva ordenación de entregas es más rápida. Antes de medir, escribe el protocolo: entrada de 20 000 entregas con la distribución del cierre anterior, 30 repeticiones por versión en 5 procesos nuevos intercalados (A, B, A, B), mediana como estadístico, diferencia mínima relevante del 10 % y criterio de «no distinguible» si el intervalo de las diferencias incluye cero. Ejecuta una prueba A/A para verificar que el protocolo no declara diferencias entre copias iguales y registra el equipo, la carga de fondo y las versiones.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Dos copias idénticas «difieren»** — causa: pocas repeticiones o media con interferencias. Corrección: prueba A/A y mediana con más repeticiones. ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo que sí hace falta es fijar de antemano el estadístico, el número de repeticiones y la diferencia mínima relevante, y comprobar cuántas veces el protocolo declara una diferencia cuando comparas dos copias idénticas (una prueba A/A). ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Benchmark](../b/benchmark.md), [Calentamiento](../c/calentamiento.md), [Interferencia](../i/interferencia.md), [Perfilador determinista](./perfilador-determinista.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md).

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

[↑ Glosario](../../README.md) · [← Proyector](./proyector.md) · [Prueba basada en requisitos →](./prueba-basada-en-requisitos.md)
