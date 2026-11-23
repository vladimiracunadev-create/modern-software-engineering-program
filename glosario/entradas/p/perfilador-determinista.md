# Perfilador determinista

[↑ Glosario](../../README.md) · [← Perfil y atribución](./perfil-y-atribucion.md) · [Performance Engineer →](./performance-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Herramienta que registra cada llamada y retorno para contar y cronometrar funciones, con sobrecarga por evento.

Definición de trabajo de [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md).

## Por qué importa

La clase donde se define, [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), existe con este propósito: la clase existe para que sepas qué hace tu reloj, tu perfilador y tu benchmark cuando miden: qué parte del número es del programa y qué parte es del instrumento, del equipo y de la elección de estadístico.

## Cómo funciona

Según [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md):

Un **perfilador determinista** como `cProfile` registra cada llamada y cada retorno y devuelve contadores y tiempos acumulados por función. Es exacto para contar llamadas y aproximado para el tiempo, porque la propia instrumentación tiene un costo por evento y ese costo se carga a las funciones medidas. Una función muy pequeña llamada muchas veces paga la sobrecarga proporcionalmente más que una grande llamada pocas veces, de manera que el perfil exagera o subestima su peso según cómo se atribuya. Un **perfilador de muestreo** interrumpe el programa a intervalos regulares y anota qué estaba ejecutando; añade menos sobrecarga y distorsiona menos, a costa de resolver menos las funciones muy cortas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md):

El equipo quiere decidir si la nueva ordenación de entregas es más rápida. Antes de medir, escribe el protocolo: entrada de 20 000 entregas con la distribución del cierre anterior, 30 repeticiones por versión en 5 procesos nuevos intercalados (A, B, A, B), mediana como estadístico, diferencia mínima relevante del 10 % y criterio de «no distinguible» si el intervalo de las diferencias incluye cero.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md)) son:

- **Una mejora desaparece al repetir** — causa: ejecución única en un proceso con interferencias. Corrección: repetir en varios procesos con un estadístico robusto.
- **El perfil acusa a una función que no es el cuello de botella** — causa: sobrecarga del perfilador atribuida a funciones pequeñas. Corrección: verificar con una medición sin perfilador.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **perfilador determinista** como `cProfile` registra cada llamada y cada retorno y devuelve contadores y tiempos acumulados por función. ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Función](../f/funcion.md), [Herramientas](../h/herramientas.md), [Retorno](../r/retorno.md), [Benchmark](../b/benchmark.md), [Calentamiento](../c/calentamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md).

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

[↑ Glosario](../../README.md) · [← Perfil y atribución](./perfil-y-atribucion.md) · [Performance Engineer →](./performance-engineer.md)
