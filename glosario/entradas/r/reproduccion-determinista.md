# Reproducción determinista

[↑ Glosario](../../README.md) · [← Reproducción](./reproduccion.md) · [Reproducción y revisión →](./reproduccion-y-revision.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

La **reproducción determinista** es, en [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), el procedimiento de **fijar todas las variables que influyen en un fallo hasta que el síntoma aparece siempre, o con una tasa conocida**: la **entrada**, la **semilla** de los generadores aleatorios, el **reloj**, la **versión** del software y el **comando** exacto. El objetivo es convertir «a veces falla» en «con esta entrada y esta semilla, falla siempre». Es el paso previo a reducir el caso, a diagnosticar y a escribir la prueba de regresión.

## Por qué importa

Sin reproducción no hay forma de saber si una corrección funcionó: si el fallo es esporádico, «ya no ocurrió» puede ser suerte. La decisión que cambia es qué se hace antes de modificar el código: primero se logra reproducir. [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md) lo refuerza con un síntoma de diagnóstico: se cambia código antes de reproducir porque se actúa sobre una impresión, y la corrección es **escribir primero la prueba determinista**. Reproducir también define el límite de lo que se puede afirmar con honestidad.

## Cómo funciona

Cada fuente de no determinismo se controla con una técnica distinta:

- **Entrada:** guardar la entrada exacta que produjo el fallo, no una descripción.
- **Aleatoriedad:** fijar la semilla del generador y registrarla en cada ejecución.
- **Tiempo:** inyectar un reloj controlado en lugar de leer la hora del sistema.
- **Versión y entorno:** registrar versión del programa, de las dependencias y del *runtime*.
- **Comando:** fijar el comando exacto, con sus argumentos y variables de entorno.

Cuando tras controlar todo el fallo **sigue siendo intermitente** (por concurrencia o por factores del entorno), la regla de [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md) es honesta: **se registra la frecuencia, no se finge determinismo**. Por ejemplo, «falla 3 de cada 100 ejecuciones» es información útil y permite comparar antes y después de una corrección con ejecuciones repetidas. Y una advertencia: una prueba inestable no es prueba de corrección; que pase una vez no demuestra nada.

## Ejemplo

Un fallo que ocurre «a veces» al ordenar tareas con desempate aleatorio. Para reproducirlo:

```python
import random

def reproducir(semilla):
    random.seed(semilla)
    casos = generar_casos(200)
    return ordenar(casos)

for semilla in range(1000):
    try:
        reproducir(semilla)
    except Exception as e:
        print("falla con semilla", semilla, type(e).__name__)
        break
```

El bucle encuentra una semilla que provoca el fallo. Desde entonces, `reproducir(<semilla>)` lo produce siempre, y esa llamada se convierte en la prueba de regresión. [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md) documenta dos consecuencias: la reducción devuelve resultados distintos porque la prueba es intermitente (se repite cada decisión y se fijan semillas), y la bisección de *commits* señala un *commit* inocente por dos defectos o prueba inestable (se estabiliza la prueba y se comprueba el *commit* señalado).

## Errores y confusiones comunes

- **Aceptar «a veces falla» como descripción.** Sin entrada y semilla no hay reproducción.
- **Fingir determinismo.** Una ejecución que pasa no es evidencia; hay que registrar la tasa.
- **No registrar la versión y el entorno.** El fallo puede depender de ellos.
- **Dar por corregido tras una ejecución verde.** En un fallo intermitente, una ejecución no basta.

## Límites y cuándo no aplica

El caso mínimo aún debe poder ejecutarlo otra persona con modalidades distintas ([SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md)). Algunos fallos no admiten reproducción determinista barata: concurrencia con muchas combinaciones de intercalado, errores que dependen de hardware o de carga en producción. En esos casos se apoya el diagnóstico en trazas, en medición de frecuencia y en herramientas especializadas, y se declara la incertidumbre que queda.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Comando](../c/comando.md), [Semilla](../s/semilla.md), [Versión](../v/version.md), [Caso mínimo y representatividad](../c/caso-minimo-y-representatividad.md), [Primera divergencia](../p/primera-divergencia.md), [Reducción por dimensiones](./reduccion-por-dimensiones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-105 — Reproducción de errores y reducción de casos](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md).

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

[↑ Glosario](../../README.md) · [← Reproducción](./reproduccion.md) · [Reproducción y revisión →](./reproduccion-y-revision.md)
