# Escalera de herramientas

[↑ Glosario](../../README.md) · [← Escalera de degradación](./escalera-de-degradacion.md) · [Escalón de tráfico →](./escalon-de-trafico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

La **escalera de herramientas** es el orden en que [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md) propone usar los instrumentos de diagnóstico ante un fallo desconocido: se empieza por lo más barato y básico (**versión, registros y reproducción**) y solo se sube a un **depurador**, un **perfilador** o un **análisis** más pesado según la pregunta que quede abierta. Cada peldaño responde a una pregunta distinta, y no se sube por prestigio de la herramienta sino por necesidad. Es una metáfora del programa para ordenar el diagnóstico, no un procedimiento normalizado.

## Por qué importa

Ante un fallo, la tentación es abrir la herramienta más potente o cambiar código «para ver». [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md) lo desaconseja con una regla de evidencia: una herramienta más sofisticada **no implica mejor evidencia**. Un depurador sin reproducción mostrará el estado de una ejecución que quizá no falle; un perfilador sin hipótesis dará números sin pregunta. La decisión que cambia es en qué orden se gasta el esfuerzo: primero se asegura saber *qué* se está ejecutando y *si* se puede repetir el fallo, y después se mide.

## Cómo funciona

Los peldaños, de abajo arriba:

1. **Versión y entorno:** qué se ejecuta realmente (versión del programa, del intérprete, de las dependencias). Muchos fallos son una diferencia de versión.
2. **Registros (*logs*):** qué ocurrió antes del fallo; barato y sin alterar el programa.
3. **Reproducción:** convertir el fallo en un caso que se repite siempre, de preferencia como prueba determinista. Sin reproducción, no se puede comprobar si una corrección funcionó.
4. **Depurador:** detener la ejecución y observar el estado cuando la pregunta es «qué valor tiene esto en este punto».
5. **Perfilador o análisis:** cuando la pregunta es de rendimiento o de uso de memoria, o cuando se necesita un análisis estático o dinámico especializado.

Cada paso **registra qué descartó y qué incertidumbre queda**. Eso evita repetir lo ya hecho y convierte el diagnóstico en algo transferible: otra persona lee qué se probó y por qué se descartó.

## Ejemplo

En [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), el taller diagnostica un fallo desconocido en la biblioteca de estructuras y algoritmos. Una bitácora mínima, con la estructura de la escalera (ilustración, datos inventados):

```text
1. versión: paquete 1.3.0, Python 3.12 -> igual que en CI. Descartado: versión.
2. log: falla tras la 3.ª operación de borrado. Hipótesis: estado tras borrar.
3. reproducción: test_borrado_triple.py falla siempre. Determinista.
4. depurador: tras el 3.º borrado, el contador de elementos es 2, no 3. Causa.
```

Los dos errores documentados en la clase se evitan con este orden: cambiar código antes de reproducir (se actúa sobre una impresión; se corrige escribiendo primero la prueba determinista) y repetir el diagnóstico entre personas por falta de registro (se corrige escribiendo hipótesis, pruebas y descartes).

## Errores y confusiones comunes

- **Saltar al depurador.** Sin reproducción, observar una ejecución no demuestra nada sobre el fallo.
- **Cambiar código para «probar».** Altera el sistema antes de saber qué pasa y mezcla varias causas.
- **No registrar los descartes.** Otra persona repite lo ya descartado.
- **Medir sin pregunta.** Un perfilador ejecutado «a ver» da datos sin hipótesis.

## Límites y cuándo no aplica

El taller produce un diagnóstico del caso dado; no demuestra que todo el equipo pueda recrearlo ([SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md)), y por eso el proyecto siguiente lo convierte en un entorno autocontenido. La escalera es una heurística: algunos fallos exigen subir directamente (un cuelgue en producción puede pedir un volcado de hilos antes de cualquier reproducción), y en fallos de concurrencia la reproducción determinista puede no existir.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Análisis](../a/analisis.md), [Reproducción](../r/reproduccion.md), [Versión](../v/version.md), [Causa, corrección y seguimiento](../c/causa-correccion-y-seguimiento.md), [Cronología y hechos](../c/cronologia-y-hechos.md), [Hipótesis rivales](../h/hipotesis-rivales.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-107 — Taller: diagnosticar un fallo desconocido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Escalera de degradación](./escalera-de-degradacion.md) · [Escalón de tráfico →](./escalon-de-trafico.md)
