# Prueba unitaria

## Definición

Una **prueba unitaria** es la comprobación de una unidad pequeña cuyo resultado no depende de recursos que la prueba no controla (`SE-422`). Llama a la unidad (una función o una clase pequeña) con una entrada conocida y afirma algo sobre el resultado o el efecto visible.

## Por qué importa

Es la prueba más barata y rápida, y la base de la pirámide, pero solo vale por lo que *protege*. `SE-422` lo dice así: ejecutar una línea no es comprobarla; una prueba sin aserciones, o con una aserción que no puede fallar, «cubre» código sin protegerlo.

## Cómo funciona

Lo decisivo es que el resultado no dependa de nada que la prueba no controle: reloj, azar, red, orden de ejecución. Si depende, se inyecta (la hora, la semilla). Cada prueba debe poder responder qué cambio del código la haría fallar; si la respuesta es «ninguno», es ruido. Una forma de medir si una suite protege es el **análisis de mutantes**: cambiar un operador y ver si alguna prueba falla.

## Ejemplo

```python
def test_aprueba_en_la_frontera():
    assert aprobado(4.0) is True
    assert aprobado(3.9) is False
```

Los valores 4,0 y 3,9 están en la frontera; una prueba con solo 6,0 no detectaría un cambio de `>=` a `>`.

## Errores y confusiones comunes

- **La cobertura es 100 % y un cambio de operador no rompe ninguna prueba.** Casos típicos sin valores de frontera; tabla de fronteras y medida con mutantes (`SE-422`).
- **Una prueba falla de vez en cuando sin cambios en el código.** Depende del reloj, del azar o del orden; inyectar la hora y la semilla.

## Límites y cuándo no aplica

No ve defectos de integración entre piezas (para eso, pruebas de integración y de contrato). Una suite muy acoplada a la implementación se rompe con cada refactor sin proteger comportamiento.
