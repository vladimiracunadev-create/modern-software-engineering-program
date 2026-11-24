# Perfil como hipótesis

[↑ Glosario](../../README.md) · [← Pérdida selectiva de telemetría](./perdida-selectiva-de-telemetria.md) · [Perfil de operaciones →](./perfil-de-operaciones.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

**Perfil como hipótesis** es la lectura que [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md) propone de los resultados de un *profiler* (perfilador): **el perfil señala dónde se observa el costo, no por qué**. Un perfilador de CPU, memoria, entrada y salida o red mide en qué funciones o líneas se gasta tiempo o recursos; esa información es una pista y no una explicación. La causa se formula como una **hipótesis**, se cambia una variable y se repite la medición con la salida correcta para confirmar o descartar.

## Por qué importa

El perfil produce una lista ordenada y convincente, y es tentador optimizar lo primero que aparece. Pero una función «caliente» puede serlo por razones ajenas a su código (se llama demasiadas veces desde otro lugar, espera una red lenta) o ser irrelevante para el objetivo del servicio. [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md) lo resume: **optimizar una función caliente irrelevante para el SLO es trabajo sin impacto**. La decisión que cambia es qué se hace tras ver el perfil: no se edita, se formula una causa y se prueba.

## Cómo funciona

El ciclo tiene cuatro pasos:

1. **Fijar el objetivo:** qué se quiere mejorar (latencia, memoria, rendimiento) y qué umbral importa (el SLO).
2. **Perfilar y formular la hipótesis:** «el tiempo se va en serializar, porque se serializa cada elemento por separado».
3. **Cambiar una variable** (agrupar la serialización) y **repetir la medición comprobando que la salida sigue siendo correcta**. Una versión más rápida que devuelve resultados erróneos no es una mejora.
4. **Confirmar con la medición sin perfilador:** el perfilador mismo altera el tiempo.

Por eso [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md) documenta dos trampas. Un perfil determinista (que registra cada llamada) puede **inflar** el costo de funciones muy llamadas y llevar a optimizar lo que no era el problema; se confirma con el tiempo total sin perfilador. Y activar el perfil de memoria durante la medición de tiempo distorsiona el resultado: en la clase, con `tracemalloc` activo la prueba fue 62 veces más lenta; se perfilan memoria y tiempo en ejecuciones separadas.

## Ejemplo

Se perfila un servicio que tarda más de lo permitido. El perfil muestra que 60 % del tiempo está en `serializar`. La hipótesis: se llama una vez por elemento. Se cambia una variable:

```python
# antes: for c in casos: salida.append(serializar(c))
# después:
salida = serializar_lote(casos)        # misma salida, una llamada
assert salida == [serializar(c) for c in casos]   # la salida sigue siendo correcta
```

Se mide de nuevo **sin perfilador** con la misma carga. Si el tiempo total baja de forma relevante respecto del SLO, la hipótesis se confirma; si no, se descarta y se pasa a la siguiente. El perfil nunca fue la conclusión: fue el punto de partida.

## Errores y confusiones comunes

- **Optimizar la primera función de la lista.** Puede ser inflada por el perfilador o irrelevante para el objetivo.
- **Medir con el perfilador activo.** Altera el tiempo.
- **Mezclar perfil de memoria y de tiempo.** Se distorsionan mutuamente.
- **Mejorar sin verificar la salida.** Se puede acelerar un resultado incorrecto.

## Límites y cuándo no aplica

Un perfil dinámico observa **las entradas ejecutadas** ([SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md)): lo que no se ejercitó en la medición no aparece. No dice nada del comportamiento con otros datos ni de rutas raras. Perfilar tampoco reemplaza el diseño: si el problema es algorítmico (un `O(n²)` que solo duele con tamaños grandes), el perfil con datos pequeños no lo muestra. La clase siguiente complementa con análisis estático, que detecta clases distintas de defectos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Costo](../c/costo.md), [Asignaciones, retención y pico](../a/asignaciones-retencion-y-pico.md), [I/o y red](../i/i-o-y-red.md), [Perfil determinista y muestreo](./perfil-determinista-y-muestreo.md), [Tiempo de pared y cpu](../t/tiempo-de-pared-y-cpu.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-099 — Profilers de CPU, memoria, I/O y red](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) — Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft.
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) — Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Pdb, cprofile, timeit, tracemalloc y límites instrumentales; autoridad: Python Software Foundation.
- [Python venv](https://docs.python.org/3/library/venv.html) — Aislamiento de intérprete, scripts y entorno virtual; autoridad: Python Software Foundation.
- [Development Container Specification](https://containers.dev/implementors/spec/) — Configuración reproducible de herramientas y ciclo de vida del contenedor; autoridad: Dev Container Specification maintainers.

---

[↑ Glosario](../../README.md) · [← Pérdida selectiva de telemetría](./perdida-selectiva-de-telemetria.md) · [Perfil de operaciones →](./perfil-de-operaciones.md)
