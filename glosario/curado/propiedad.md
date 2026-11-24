# Propiedad

## Definición

En pruebas, una **propiedad** es una afirmación que debe cumplirse para toda entrada del dominio de una función, y que se comprueba con muchas entradas generadas (SE-425, SE-166, SE-316). Es la base de las pruebas basadas en propiedades (*property-based testing*). No debe confundirse con la «propiedad de archivos» (ownership, quién es responsable de qué) ni con una propiedad de un objeto o una clase.

## Por qué importa

Dice qué debe cumplirse sin enumerar casos. Una prueba de ejemplos comprueba lo que alguien pensó; una propiedad cubre una región entera del dominio y encuentra entradas en las que nadie pensó. Cambia cómo se diseñan las pruebas: en lugar de «para 3 y 4 devuelve 7», se afirma «la suma de las cantidades repartidas es `n`».

## Cómo funciona

SE-425 da ejemplos de propiedades: la suma de las cantidades repartidas es `n`; normalizar dos veces da lo mismo que normalizar una (idempotencia); invertir una lista dos veces devuelve la original. Un generador produce entradas (por ejemplo, 200 casos aleatorios) y el marco comprueba la propiedad en cada una. Se escribe **sin repetir la implementación**: «el resultado es lo que calcula la función» no comprueba nada.

La clase enumera familias útiles de propiedades: invariantes que se conservan, idempotencia, relaciones entre entradas (si se añade un elemento, el resultado cambia así), comparación con un modelo más simple y propiedades metamórficas. Dos mecanismos hacen utilizable el método. El **generador** debe llegar a las fronteras (listas vacías, valores límite, combinaciones), con sesgo hacia ellas; si no, la propiedad pasa y el defecto sigue ahí. Y la **reducción** (*shrinking*): ante un contraejemplo de 22 elementos, el marco lo reduce a su forma mínima antes de analizarlo, porque un contraejemplo enorme no se entiende (SE-166).

## Ejemplo

SE-425 incluye un fragmento que comprueba tres propiedades de una función de reparto con 200 casos aleatorios y pide predecir si pasa la versión que olvida el resto. Una propiedad ilustrativa:

```python
@given(st.integers(0, 1000), st.integers(1, 10))
def test_reparto_suma_n(n, k):
    assert sum(repartir(n, k)) == n
```

Si `repartir` pierde el resto de la división, el marco encuentra un contraejemplo pequeño como `n=1, k=2` tras reducir. (Código ilustrativo con la biblioteca Hypothesis; la clase usa su propio fragmento.)

## Errores y confusiones comunes

- **La propiedad pasa y la función tiene un defecto conocido**: el generador no llega a la frontera; corrección: sesgo hacia vacío, límites y combinaciones.
- **La propiedad repite la implementación**: se calcula el esperado con la misma fórmula; corrección: invariantes o un modelo distinto.
- **Contraejemplo ilegible**: no hay reducción.
- **Creer que reemplaza las pruebas de ejemplos**: se complementan; los ejemplos documentan y fijan casos concretos.

## Límites y cuándo no aplica

No toda función tiene propiedades fáciles de enunciar; a veces solo se conoce el resultado esperado para casos concretos. Con generadores mal diseñados da una falsa sensación de cobertura. Las propiedades pasan con 200 casos y pueden fallar con el 201: son pruebas probabilísticas, no demostraciones. Las operaciones lentas o con efectos externos encarecen la ejecución de cientos de casos.
