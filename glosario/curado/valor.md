# Valor

## Definición

Un **valor** es un **dato concreto que el programa puede manipular**: un entero, una cadena, una lista. En `SE-061` se precisa que es información concreta **interpretada según un tipo**: `800`, `800.0` y `'800'` son tres valores distintos, no intercambiables. Un valor no tiene por sí mismo nombre (eso lo da una variable), unidades ni dominio de negocio: eso no viene incluido en el tipo incorporado. Aquí se usa el sentido de la programación; el «valor» de negocio (el beneficio que aporta un producto) es otro concepto y se trata en otras clases.

## Por qué importa

Muchos defectos son confusiones entre valor y representación. `SE-061` da el ejemplo de un indicador `--enabled false` que queda **activado**: `bool('false')` es `True`, porque la cadena `'false'` es un valor de tipo cadena no vacía, no el booleano falso. La decisión que cambia es cuándo se convierte un dato de texto en un valor del dominio: con un analizador explícito que acepte solo lo documentado, y no con las reglas implícitas de conversión del lenguaje.

## Cómo funciona

Cada valor pertenece a un tipo, que define qué operaciones admite y cómo se interpreta:

- **Enteros** de Python tienen precisión arbitraria, limitada en la práctica solo por la memoria.
- **`float`** aproxima números binarios: muchos decimales (como `0.1`) **no se representan exactamente**, y por eso `0.1 + 0.2` no da exactamente `0.3`.
- **`bool`** modela dos valores; **no sirve para distinguir «desconocido» de «falso»**: para eso hace falta un tercer estado (`None` u otro).
- Una función sin `return` explícito **devuelve `None`**, que es también un valor (`SE-064`).

Una pregunta frecuente que `SE-061` responde: ¿por qué `256 is 256` es verdadero y `257 is 257` no siempre? Porque **CPython reutiliza objetos enteros pequeños** (la clase midió que 256 sí y 257 no). Es un **detalle de implementación**: el programa debe comparar **valores** con `==` y reservar `is` (identidad de objeto) para `None`.

## Ejemplo

El ejercicio mínimo de `SE-061` pide evaluar expresiones prediciendo valor y tipo antes de ejecutarlas:

```python
0.1 + 0.2        # 0.30000000000000004  (float: aproximación binaria)
bool('false')    # True                 (cadena no vacía)
3 / 2            # 1.5                  (división real)
3 // 2           # 1                    (división entera)
'3' * 2          # '33'                 (repetición de cadena)
```

Cada resultado depende del tipo del valor, no de su aspecto. Otros defectos del curso relacionados con valores: un valor negativo clasificado como válido porque la cadena de condiciones no tiene rama de entrada inválida (`SE-062`; se corrige con una guarda inicial que rechace el dominio no admitido) y el resultado de una función que depende de llamadas anteriores por un **valor por defecto mutable compartido** (`SE-064`; se usa `None` como centinela y se crea el objeto dentro).

## Errores y confusiones comunes

- **Confundir `'800'`, `800` y `800.0`.** No son intercambiables.
- **Convertir texto a booleano con `bool()`.** Cualquier cadena no vacía es verdadera.
- **Comparar valores con `is`.** Funciona por accidente para enteros pequeños.
- **Usar `float` para dinero.** No representa exactamente muchos decimales.

## Límites y cuándo no aplica

El tipo incorporado no lleva unidades ni dominio: `800` puede ser metros, segundos o pesos, y el programa no lo sabe. Esa información debe expresarse con tipos propios o con convenciones, o aparecen defectos silenciosos. Además, `bool` no distingue desconocido de falso (`SE-061`). El concepto de valor como dato inmutable o mutable, y su relación con la identidad, se desarrolla en otras clases; aquí se trata el valor como dato concreto de un programa.
