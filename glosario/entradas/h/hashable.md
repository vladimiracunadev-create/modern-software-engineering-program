# Hashable

[↑ Glosario](../../README.md) · [← Hash por encuentro](./hash-por-encuentro.md) · [Hazard →](./hazard.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Valor con hash estable utilizable como clave.

Definición de trabajo de [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md).

## Por qué importa

La clase donde se define, [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md), existe con este propósito: la clase existe para seleccionar colecciones y transformaciones según orden, unicidad, acceso, memoria y mutabilidad.

## Cómo funciona

Según [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md):

Un dict asocia claves hashables con valores y conserva orden de inserción como propiedad del lenguaje moderno, pero su razón principal es acceso por clave. Una asignación repetida reemplaza el valor; para detectar duplicado se valida antes de insertar.

Según [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md):

Lista para una secuencia que crece o se modifica; tupla para una secuencia fija o un registro ligero. La tupla comunica que no se va a modificar y es hashable si sus elementos lo son.

## Ejemplo

Ejemplo de [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md) (sección «Preguntas frecuentes»):

Lista para una secuencia que crece o se modifica; tupla para una secuencia fija o un registro ligero. La tupla comunica que no se va a modificar y es hashable si sus elementos lo son.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md)) son:

- **cambiar una fila cambia todas** — causa: multiplicar una lista de listas comparte el objeto interno. Corrección: construir con una comprensión.
- **la copia «cambia sola»** — causa: copia superficial de una estructura anidada. Corrección: `copy.deepcopy` o evitar la mutación.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un `frozenset` expresa «solo pertenencia, no cambia» y es hashable, de modo que puede ser clave de un diccionario o miembro de otro conjunto. ([SE-066](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md))
- La tupla comunica que no se va a modificar y es hashable si sus elementos lo son. ([SE-066](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Huella](./huella.md), [Valor](../v/valor.md), [Comprensión](../c/comprension.md), [Conjunto](../c/conjunto.md), [Contrato](../c/contrato.md), [Control](../c/control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-087](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md), [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Hash por encuentro](./hash-por-encuentro.md) · [Hazard →](./hazard.md)
