# Benchmark

[↑ Glosario](../../README.md) · [← Batería hostil](./bateria-hostil.md) · [Benchmark versionado →](./benchmark-versionado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Un **benchmark** es una medición repetible del tiempo o del consumo de un fragmento de código, con una entrada y un protocolo declarados ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md)). [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) lo presenta como un experimento comparativo bajo protocolo y [SE-055](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-055-complejidad-temporal-y-espacial/README.md) como la medición controlada de una implementación. La palabra no designa «un número»: designa el número junto con la descripción que lo hace interpretable.

## Por qué importa

Las decisiones de rendimiento (elegir una estructura de datos, aceptar o rechazar una optimización, fijar un timeout) se apoyan en cifras. Si la cifra mide otra cosa, la decisión es errónea y además parece fundada. [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) toma los tiempos medidos para decidir timeouts y reintentos, así que un benchmark defectuoso se propaga a esas decisiones.

## Cómo funciona

Un benchmark puede medir lo que no se quería ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md)). Las causas típicas:

- **Caché o resultado constante:** si la función usa `functools.lru_cache` y se llama con el mismo argumento, se mide una búsqueda en un diccionario y no el trabajo.
- **Entrada demasiado pequeña:** domina el costo fijo de la llamada.
- **Entrada demasiado regular:** el procesador predice los saltos y la caché la favorece más que a datos reales.
- **Estado global modificado:** la segunda ejecución ya no parte del mismo estado.

La regla es describir qué entrada, qué estado inicial y qué se descarta. [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) añade que hay que distinguir qué se mide: latencia (cuánto tarda una unidad), *throughput* (cuántas se completan por tiempo) y utilización (cuánto ocupa un recurso); mejorar una puede empeorar otra. La carga incluye tamaño, distribución, concurrencia, estado y criterio de corrección. [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) propone una prueba A/A (comparar una versión consigo misma) para ver cuánta falsa diferencia produce el protocolo.

## Ejemplo

En el caso conductor de [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) (ordenación de entregas de la API), el artefacto es un protocolo de benchmark con su prueba A/A; al cambiar el número de repeticiones, cambia la tasa de falsas diferencias. Ilustración mínima de un defecto:

```python
@lru_cache
def f(x): return sorted(range(x))
timeit.timeit(lambda: f(10_000), number=1000)   # mide el diccionario
```

## Errores y confusiones comunes

- **Un tiempo imposible.** Causa: caché o resultado constante medido en lugar del trabajo; corrección: variar la entrada y reiniciar la caché ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md)).
- **Comparar versiones que dan resultados distintos.** No es un benchmark ([SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md)): primero hay que verificar la corrección.
- **Confundirlo con un perfil.** El perfil dice dónde se gasta el tiempo; el benchmark compara cuánto.

## Límites y cuándo no aplica

Un benchmark vale para la entrada, el entorno y el protocolo declarados; no se extrapola sin más a producción. Un número sin descripción de entrada, estado inicial y descartes no tiene significado ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md)). Y medir bien no decide por sí solo: el costo de una optimización en complejidad también cuenta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fragmento](../f/fragmento.md), [Medición](../m/medicion.md), [Amortizado](../a/amortizado.md), [Complejidad](../c/complejidad.md), [Cota](../c/cota.md), [Cuello de botella](../c/cuello-de-botella.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-022 — Rendimiento, consumo energético y límites físicos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-055 — Complejidad temporal y espacial](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-055-complejidad-temporal-y-espacial/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (17 clases más lo mencionan; las que más):

[SE-095](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-095-taller-elegir-por-carga-y-no-por-costumbre/README.md), [SE-094](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md), [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md).

**Aparece en los casos de estudio:** [Discord](../../../casos/exito/discord.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Mytkowicz et al., «Producing wrong data without doing anything obviously wrong!»](https://doi.org/10.1145/1508244.1508275) — factores ocultos que invierten conclusiones de benchmarks; autoridad: ASPLOS 2009.
- [Python: functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) — caché que puede distorsionar un benchmark; autoridad: documentación de Python.
- [Kalibera y Jones, «Rigorous benchmarking in reasonable time»](https://doi.org/10.1145/2464157.2464160) — repeticiones, niveles y reporte de incertidumbre; autoridad: ISMM 2013.
- [Python: timeit](https://docs.python.org/3/library/timeit.html) — uso del mínimo y advertencias de medición; autoridad: documentación de Python.
- [Python: profile y cProfile](https://docs.python.org/3/library/profile.html) — perfilado determinista y su sobrecarga; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Batería hostil](./bateria-hostil.md) · [Benchmark versionado →](./benchmark-versionado.md)
