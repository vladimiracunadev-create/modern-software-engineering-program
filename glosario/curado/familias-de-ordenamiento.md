# Familias de ordenamiento

## Definición

Las **familias de ordenamiento** son los grandes enfoques para ordenar una colección por comparaciones, que `SE-090` agrupa por sus garantías y compromisos: **merge sort** (ordenamiento por mezcla) garantiza `O(n log n)` y usa memoria adicional; **quicksort** depende de la elección del **pivote** y puede degradar a `O(n²)`; **heapsort** acota el tiempo a `O(n log n)` y opera con otros compromisos (en el sitio, sin memoria adicional significativa, pero con peor localidad y sin estabilidad). El programa las usa para que quien programa no infiera la implementación a partir del nombre `sort`.

## Por qué importa

Llamar a `sort` es una de las operaciones más frecuentes, y es fácil creer que el nombre dice cómo funciona. No lo dice: cada biblioteca elige un algoritmo (a menudo un **híbrido**) con sus garantías de tiempo, memoria y estabilidad. La decisión que cambia es cuándo escribir un ordenamiento propio y qué suponer del ordenamiento de la plataforma. Casi siempre se usa el de la biblioteca; saber las familias sirve para entender qué se promete, qué no y cuándo un rendimiento inesperado tiene explicación.

## Cómo funciona

Cada familia obtiene `O(n log n)` por un camino distinto:

- **Merge sort:** divide la entrada en mitades, ordena cada una y las **mezcla**. El tiempo es `O(n log n)` incluso en el peor caso; el precio es memoria auxiliar `O(n)` para mezclar. Es estable.
- **Quicksort:** elige un **pivote**, reparte los elementos en menores y mayores y ordena cada parte. En promedio es `O(n log n)` y muy rápido en la práctica por su buena localidad; pero si el pivote es sistemáticamente malo (por ejemplo, el primer elemento en una entrada ya ordenada), las particiones quedan desbalanceadas y el costo pasa a `O(n²)`. No es estable en su forma clásica.
- **Heapsort:** construye un **montículo** (heap) y extrae el máximo repetidamente. Su tiempo está acotado a `O(n log n)` en todos los casos y funciona en el sitio, pero accede a la memoria de forma dispersa y no es estable.

Los entornos de ejecución usan **híbridos**: por ejemplo, el ordenamiento de Python (Timsort) combina mezcla con inserción y aprovecha tramos ya ordenados, y otros usan quicksort con cambio a heapsort si la recursión se vuelve profunda. Comprenderlos evita suponer.

## Ejemplo

`SE-090` documenta el síntoma clásico: un ordenamiento propio es lento con datos casi ordenados porque usa un quicksort ingenuo con pivote fijo. La corrección es usar `sorted` o un pivote aleatorio, y probar con entrada ya ordenada.

```python
def quicksort_ingenuo(a):               # pivote fijo: el primero
    if len(a) <= 1: return a
    p, resto = a[0], a[1:]
    return (quicksort_ingenuo([x for x in resto if x < p]) + [p] +
            quicksort_ingenuo([x for x in resto if x >= p]))
# con a ya ordenada: particiones de tamaño 0 y n-1 -> O(n^2) y recursión profunda
```

Ante la misma entrada, `sorted(a)` detecta el tramo ordenado y termina en tiempo lineal.

## Errores y confusiones comunes

- **Inferir el algoritmo del nombre.** `sort` no dice si es estable, si usa memoria extra ni cuál es su peor caso.
- **Escribir un quicksort sin pensar en el pivote.** Los datos casi ordenados son frecuentes.
- **Ignorar el contrato de comparación.** Con `NaN` o un comparador no transitivo, el resultado «ordenado» no lo está.
- **Creer que `O(n log n)` es la última palabra.** Las constantes y la localidad deciden entre algoritmos de igual cota.

## Límites y cuándo no aplica

Las cotas de `O(n log n)` valen para ordenamiento **por comparación**; para claves enteras acotadas o cadenas existen algoritmos que no comparan (conteo, radix) con otras cotas. Elegir los *k* mejores no requiere ordenar todo y no resuelve decisiones secuenciales con subproblemas o restricciones (`SE-090`). Para colecciones pequeñas, la diferencia práctica entre familias es irrelevante frente a la claridad.
