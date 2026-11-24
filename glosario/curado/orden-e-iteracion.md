# Orden e iteración

## Definición

**Orden e iteración** designa, en `SE-087`, la pregunta de **en qué orden entrega sus elementos una colección al recorrerla** y qué garantías ofrece el lenguaje sobre eso. En Python: el `dict` **garantiza el orden de inserción**; el `set` **no promete un orden estable entre ejecuciones**. Es la razón por la que «iterar» no equivale a «iterar en un orden de fiar»: depende de la estructura y de lo que la documentación promete, no de lo que se ve en una ejecución.

## Por qué importa

Un programa que depende del orden observado de un conjunto funciona hoy y falla mañana, sin cambios de código: otra versión del intérprete, otra ejecución con otra semilla de hash, otros datos. `SE-087` lo señala con un caso: usar el orden observado de un `set` como desempate **crea pruebas frágiles**. La decisión que cambia es dónde vive el orden: si importa, **debe representarse explícitamente** (una lista, una clave de ordenamiento), no heredarse como efecto secundario de la estructura.

## Cómo funciona

Una tabla hash coloca cada elemento según el valor de su *hash*, no según su llegada. Un `set` de cadenas, en Python, usa un *hash* **aleatorizado por ejecución** (una medida de seguridad contra colisiones deliberadas), de modo que el orden de iteración puede cambiar de una ejecución a otra. Un `dict`, desde las versiones modernas de Python, conserva el **orden de inserción** como parte de su contrato, porque guarda las entradas en un arreglo ordenado además de la tabla.

Eso produce reglas prácticas:

- Si se necesita recorrer en el orden en que se insertó, el `dict` lo garantiza; un `set` no.
- Si se necesita un orden por valor, se **ordena explícitamente** antes de producir resultados (`sorted`).
- Si el resultado de un programa depende de un orden que no se ordenó, es un defecto latente aunque las pruebas hoy pasen.

`SE-087` documenta dos síntomas: el orden de salida cambia entre ejecuciones porque se itera un `set` de cadenas con *hash* aleatorizado (se ordena antes de producir resultados), y una búsqueda en un `dict` falla para una clave que «seguro» se insertó porque la clave se mutó después de insertarla (se usan claves inmutables o un identificador estable).

## Ejemplo

```python
etiquetas = {"rojo", "verde", "azul"}
print(list(etiquetas))          # puede variar entre ejecuciones del programa

print(sorted(etiquetas))        # ['azul', 'rojo', 'verde']: orden definido por el programa

d = {}
d["b"] = 1; d["a"] = 2
print(list(d))                  # ['b', 'a']: orden de inserción, garantizado
```

Una prueba que compara `list(etiquetas)` con una lista fija es frágil: pasa o falla según la ejecución. La corrección es comparar con `sorted(etiquetas)` o con otro conjunto, que no depende del orden.

## Errores y confusiones comunes

- **Tomar el orden observado por garantía.** Que un `set` salga ordenado un día no lo promete.
- **Pruebas que dependen del orden de un `set`.** Son intermitentes.
- **Confundir orden de inserción con orden por clave.** El `dict` conserva el primero, no ordena.
- **Mutar una clave después de insertarla.** La búsqueda falla porque el *hash* cambió.

## Límites y cuándo no aplica

Las tablas hash no mantienen rangos ni prefijos ordenados (`SE-087`): para consultas por rango se necesita una estructura ordenada, como un árbol de búsqueda, que la clase siguiente estudia. La garantía de orden del `dict` es de Python moderno; en otros lenguajes los mapas hash pueden no ofrecerla, y hay que consultar la documentación de cada uno antes de apoyarse en ella.
