# Visited

[↑ Glosario](../../README.md) · [← Virtualización de lista](./virtualizacion-de-lista.md) · [Vista →](./vista.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Conjunto de identidades ya procesadas.

Definición de trabajo de [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md).

## Por qué importa

La clase donde se define, [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md), existe con este propósito: la clase existe para elegir iteración, recursión o recorrido manteniendo una invariante explícita.

## Cómo funciona

Según [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md):

La recursión resuelve una estructura mediante subestructuras y caso base. Python no optimiza tail calls y limita profundidad; árboles profundos necesitan pila explícita. Para grafos, `visited` impide ciclos y repetición.

Según [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md):

La CLI diagnóstica recorre un grafo con pila explícita y `visited`. Cada extracción consume un nodo y cada nodo se añade una vez. Un límite de nodos produce `INCOMPLETE` con cursor; no finge resultado completo.

## Ejemplo

Ejemplo de [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md) (sección «Ejemplo profesional»):

La CLI diagnóstica recorre un grafo con pila explícita y `visited`. Cada extracción consume un nodo y cada nodo se añade una vez. Un límite de nodos produce `INCOMPLETE` con cursor; no finge resultado completo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md)) son:

- **el resultado cambia según los datos, sin error** — causa: se elimina de la lista que se recorre. Corrección: construir una lista nueva o iterar sobre una copia.
- **`RuntimeError: dictionary changed size`** — causa: se añaden o quitan claves durante el recorrido. Corrección: recorrer `list(d)` o construir un diccionario nuevo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md)) son: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas. Un recorrido correcto puede ser demasiado costoso y Python impone límites de recursos. La siguiente clase encapsula decisiones mediante funciones y contratos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Conjunto](../c/conjunto.md), [Caso base](../c/caso-base.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Efecto](../e/efecto.md), [Invariante de bucle](../i/invariante-de-bucle.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), [SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Virtualización de lista](./virtualizacion-de-lista.md) · [Vista →](./vista.md)
