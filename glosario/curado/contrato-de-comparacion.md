# Contrato de comparación

## Definición

El **contrato de comparación** es el conjunto de propiedades que una relación de orden debe cumplir para que ordenar tenga sentido. `SE-090` lo enuncia así: ordenar requiere una relación **consistente**, normalmente **total**, o una **clave total derivada** a partir de los datos. Importan la antisimetría, la transitividad y el tratamiento de los iguales. Quien pasa un comparador o una clave a un algoritmo de ordenamiento está firmando este contrato, aunque el lenguaje no lo compruebe.

## Por qué importa

Los algoritmos de ordenamiento se demuestran correctos **bajo el supuesto** de que la comparación es un orden bien definido. Si el supuesto falla, el resultado deja de estar garantizado: puede quedar «ordenado» sin estarlo, o variar según el algoritmo o la versión del lenguaje, sin ningún error visible. La decisión que cambia es dónde se invierte la atención al ordenar: no solo en elegir el algoritmo, sino en definir y probar la relación. La mayoría de los defectos de ordenamiento viven en el comparador, no en el algoritmo.

## Cómo funciona

Las propiedades exigidas, para elementos `a`, `b`, `c`:

- **Total:** para todo par, `a ≤ b` o `b ≤ a`. Si hay pares incomparables, no hay orden total.
- **Antisimétrica:** si `a ≤ b` y `b ≤ a`, entonces son iguales según el criterio.
- **Transitiva:** si `a ≤ b` y `b ≤ c`, entonces `a ≤ c`.
- **Iguales definidos:** qué pasa con elementos equivalentes (¿se conserva su orden original? Un ordenamiento **estable** lo garantiza).

Los problemas reales vienen de datos que violan estas propiedades. Los valores no numéricos de punto flotante (`NaN`) no son menores, mayores ni iguales a nada, así que rompen la totalidad. Fechas sin zona horaria pueden representar instantes distintos con la misma etiqueta; valores ausentes (`None`) no se comparan con números. Por eso `SE-090` indica que deben **normalizarse antes del comparador**: se construye una **clave total derivada** (por ejemplo, la fecha en UTC y la ausencia convertida a un valor definido) y se ordena por ella.

## Ejemplo

En `SE-090`, un resultado «ordenado» que no lo está tiene como causa la presencia de `NaN` o un comparador no transitivo, y la corrección es normalizar el criterio y verificar con una prueba de orden total. Ilustración:

```python
datos = [3.0, float("nan"), 1.0, 2.0]
sorted(datos)          # el resultado depende de dónde cae el NaN

def clave(x):          # clave total derivada: NaN al final, de forma explícita
    return (x != x, x if x == x else 0.0)
sorted(datos, key=clave)   # [1.0, 2.0, 3.0, nan]
```

Una prueba de orden total comprueba, sobre un conjunto de muestras, que para todo par se cumpla la totalidad y para toda terna la transitividad; falla si el comparador las rompe.

## Errores y confusiones comunes

- **Comparador que devuelve «menor» en un sentido y en el otro.** Viola la antisimetría y puede hacer entrar en bucle a algunos algoritmos.
- **Restar para comparar.** `a - b` puede desbordar o redondear en flotantes y producir inconsistencias.
- **Ignorar los ausentes y los `NaN`.** Rompen la totalidad sin error evidente.
- **Esperar estabilidad sin pedirla.** Si se necesita conservar el orden de iguales, hay que usar un algoritmo estable o añadir un desempate explícito.

## Límites y cuándo no aplica

Elegir los *k* mejores no resuelve decisiones secuenciales con subproblemas o restricciones; ahí la relación de orden no basta y se pasa a estrategias voraces o programación dinámica (`SE-090`). Para órdenes parciales (dependencias entre tareas) se usa ordenamiento topológico, no un comparador. Y si el orden depende de contexto cambiante (preferencias del usuario), no existe un contrato único estable.
