# Generador

## Definición

En pruebas basadas en propiedades, un **generador** es el procedimiento que produce las entradas de prueba, con una semilla si la ejecución debe ser reproducible. Es la definición de trabajo de `SE-425`. (No se debe confundir con los generadores de Python, las funciones con `yield`, ni con los generadores de código; aquí el término es el de las pruebas.)

## Por qué importa

Una prueba basada en propiedades afirma algo para *todas* las entradas, pero solo comprueba las que el generador produce. Por tanto, el generador decide qué defectos pueden aparecer. Cambia una decisión cotidiana: dar una propiedad por buena porque «pasó cien casos» es un error si esos cien casos nunca tocaron la frontera donde vive el defecto.

## Cómo funciona

`SE-425` da el ejemplo numérico. Un generador **uniforme** sobre un rango grande produce valores típicos y casi nunca las fronteras: con `n` entre 0 y 600 y `k` entre 1 y 12, la probabilidad de que `n < k` es de aproximadamente el 1 %. Por eso un generador útil añade **sesgo**:

- hacia los **bordes**: vacío, uno, el límite, el límite más uno;
- hacia **combinaciones raras** de parámetros.

La otra propiedad es la **semilla**. Una ejecución con generación aleatoria falla «a veces»; registrar la semilla convierte ese fallo en uno repetible: se vuelve a ejecutar con la misma semilla y se obtiene el mismo caso. La causa de la utilidad es práctica: sin semilla, un fallo intermitente no se puede diagnosticar, y con semilla es un caso de prueba más.

## Ejemplo

Función que debería rechazar listas de menos de `k` elementos:

```python
import random

def generar_caso(rng):
    k = rng.randint(1, 12)
    # sesgo: la mitad de los casos cae en la frontera
    if rng.random() < 0.5:
        n = rng.choice([0, 1, k - 1, k, k + 1])
    else:
        n = rng.randint(0, 600)
    return n, k

rng = random.Random(42)   # semilla registrada
casos = [generar_caso(rng) for _ in range(200)]
```

Con generación uniforme sobre 0-600, el defecto de `n == k - 1` casi nunca saldría; con el sesgo, aparece en las primeras decenas de casos. El código es una ilustración, no una cita de la clase.

## Errores y confusiones comunes

- **La propiedad pasa y la función tiene un defecto conocido.** Causa señalada en `SE-425`: generador que no llega a la frontera. Corrección: sesgo hacia vacío, límites y combinaciones.
- **Creer que más casos compensan un mal generador.** Un millón de casos uniformes siguen sin tocar un borde que ocupa el 1 %.
- **No registrar la semilla.** El fallo no se puede reproducir.
- **Generar entradas inválidas sin querer.** Si el generador viola precondiciones, la propiedad falla por entradas fuera de dominio.

## Límites y cuándo no aplica

Un generador sesgado a las fronteras que el autor *conoce* no encuentra las que no conoce; conviene una parte uniforme o de otra naturaleza. Para estructuras complejas (árboles, documentos válidos) construir un generador que cubra el dominio es trabajo en sí, y generadores demasiado restrictivos descartan muchos casos. La reproducibilidad por semilla exige que todo el azar de la prueba salga del mismo generador. Y ninguna cantidad de entradas generadas demuestra corrección: reduce la probabilidad de defectos no vistos, no la elimina.
