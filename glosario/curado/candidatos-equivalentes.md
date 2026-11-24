# Candidatos equivalentes

## Definición

Los **candidatos equivalentes** son las alternativas que se comparan en el taller de `SE-095` bajo una condición estricta: **cada una implementa la misma interfaz y los mismos errores**. Si se compara un `set`, una lista ordenada y un diccionario para la misma tarea, los tres deben ofrecer las mismas operaciones con la misma semántica ante entradas inválidas. Es un requisito de método propio del programa: sin equivalencia, la medición no compara estructuras sino programas distintos.

## Por qué importa

Elegir una estructura de datos «por costumbre» es un hábito caro: `SE-095` propone elegir por carga. Pero una comparación de rendimiento solo vale si los candidatos hacen el mismo trabajo. Un candidato que omite una validación, o que devuelve resultados en otro orden, parece más rápido porque trabaja menos. La decisión que cambia es qué se mide: antes de cronometrar nada, se prueba que todos los candidatos dan resultados idénticos, y solo entonces el tiempo y la memoria son comparables.

## Cómo funciona

El método se apoya en tres reglas:

- **Misma interfaz.** Se define el contrato mínimo (operaciones, tipos, errores) y cada candidato lo cumple. Las diferencias de forma las absorben **adaptadores**.
- **Sin trabajo extra para uno solo.** Un adaptador que normaliza, copia o ordena solo para un candidato le suma o le resta costo y falsea la comparación. Si algo se normaliza, se normaliza para todos o se declara.
- **Validación antes de medir.** Un conjunto de entradas verifica que todos devuelvan los mismos resultados; `SE-095` lo plantea para evitar que «una simplificación incorrecta parezca más eficiente».

La causa de fondo es de control de variables: para atribuir una diferencia de tiempo a la estructura, lo demás debe permanecer igual. Esto conecta con el perfil de operaciones y tamaños que se escribe antes de medir: la equivalencia fija *qué* se hace; el perfil, *cuánto* y *con qué mezcla*.

## Ejemplo

En el taller de `SE-095`, la biblioteca de estructuras y algoritmos gestiona casos con identidad, prioridad, dependencias e instante de llegada. Para decidir cómo comprobar pertenencia se comparan tres candidatos detrás de una misma interfaz `contiene(clave)`. Antes de medir, una prueba comparte entradas y verifica que los tres devuelven lo mismo, incluidos el caso de clave ausente y el de clave no válida (mismo error). Un error documentado de la clase es elegir `set` para todo: se ignoró el costo de construirlo y la memoria, y la corrección es calcular el **umbral de reutilización** (cuántas consultas amortizan la construcción) y la memoria.

```python
def verificar(candidatos, entradas):
    base = [candidatos[0].contiene(e) for e in entradas]
    return all([c.contiene(e) for e in entradas] == base for c in candidatos)
```

## Errores y confusiones comunes

- **Medir sin validar.** Un candidato que devuelve resultados erróneos puede ganar el cronómetro.
- **Adaptadores desiguales.** Si solo uno copia o convierte datos, el costo medido no es el de la estructura.
- **Equivalencia solo en el caso feliz.** Los errores y las entradas límite también deben coincidir.
- **Recomendar sin declarar la carga.** Una recomendación que no declara tamaños ni mezcla de operaciones no convence a otro equipo.

## Límites y cuándo no aplica

El taller cubre cargas sintéticas y una plataforma (`SE-095`): la equivalencia garantiza una comparación justa en ese terreno, no que el orden se mantenga con otros datos u otra máquina. A veces no existe equivalencia real: dos estructuras pueden ofrecer garantías distintas (orden, estabilidad, memoria) y forzar la misma interfaz oculta una diferencia que justamente decide la elección; entonces se comparan por esa garantía, no por velocidad.
