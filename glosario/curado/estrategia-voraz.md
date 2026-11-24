# Estrategia voraz

## Definición

Un **algoritmo voraz** (*greedy*) construye una solución tomando en cada paso la **mejor opción local** y **no retrocede** (`SE-091`). No explora alternativas ni deshace decisiones: cada elección es definitiva. Es una técnica de diseño, no un algoritmo concreto, y su virtud es la simplicidad y la rapidez. Su riesgo es que lo localmente mejor puede no llevar al mejor resultado global; por eso la clase lo contrasta con la programación dinámica y con la exploración con retroceso.

## Por qué importa

Cuando funciona, una estrategia voraz resuelve en tiempo casi lineal problemas que de otro modo exigirían explorar muchas combinaciones. Pero «funciona en los ejemplos» no es evidencia: el error típico es adoptar una regla local plausible y descubrir tarde que da resultados subóptimos en ciertos datos. La decisión que cambia es qué se exige antes de usarla: una **demostración de corrección** o, al menos, una búsqueda sistemática de contraejemplos pequeños contra una referencia correcta.

## Cómo funciona

Para que una regla voraz sea correcta, el problema debe tener dos propiedades (`SE-091`):

- **Elección segura (propiedad de elección voraz):** existe una solución óptima que contiene la decisión local que se toma. Es decir, tomarla no cierra el camino a lo mejor.
- **Subestructura óptima:** tras tomar esa decisión, lo que queda es un subproblema del mismo tipo cuya solución óptima, unida a la decisión, da una solución óptima del conjunto.

La demostración habitual es un **argumento de intercambio**: se toma cualquier solución óptima y se muestra que se puede transformar para incluir la elección voraz sin empeorarla. Si no hay tal argumento, la regla es una heurística. Que la regla funcione en ciertos casos (monedas canónicas, árboles de expansión mínima) **no autoriza a extrapolar** a cualquier asignación: la corrección es propiedad de un problema y una regla concretos.

## Ejemplo

`SE-091` documenta dos fallos reales. Primero, el cambio devuelto usa más monedas de las necesarias porque se usó una regla voraz con un sistema de monedas **no canónico**; la corrección es programación dinámica o demostrar que el sistema es canónico. Segundo, un conteo de actividades menor al esperado porque se ordenó por **inicio**; el criterio correcto para elegir el máximo de actividades compatibles es ordenar por **fin**, y se contrasta con fuerza bruta en casos pequeños.

```python
def max_actividades(acts):             # acts: lista de (inicio, fin)
    elegidas, fin_actual = [], float("-inf")
    for ini, fin in sorted(acts, key=lambda a: a[1]):   # por fin
        if ini >= fin_actual:
            elegidas.append((ini, fin)); fin_actual = fin
    return elegidas
```

Ordenar por fin deja el máximo de tiempo libre para las siguientes, y ese es el argumento de intercambio.

## Errores y confusiones comunes

- **Elegir el criterio local equivocado.** «Más corta primero» o «inicio más temprano» parecen razonables y fallan con contraejemplos.
- **Generalizar de un caso conocido.** Que sirva con monedas de un país no implica que sirva con cualquier sistema.
- **Confundir voraz con heurística.** Una heurística puede estar bien, pero no ofrece garantía de optimalidad; hay que decirlo.
- **No comparar con una referencia.** Sin fuerza bruta o programación dinámica en tamaños pequeños, no se detecta el fallo.

## Límites y cuándo no aplica

Cuando no hay elección segura ni subestructura óptima, la regla local no basta, y hay que explorar (retroceso) o resolver subproblemas superpuestos con una tabla (programación dinámica). Esta última **exige un estado finito y manejable** (`SE-091`). En problemas donde una solución aproximada con garantía acotada es aceptable, una estrategia voraz sin optimalidad puede seguir siendo una buena decisión de ingeniería, siempre que se declare como aproximación.
