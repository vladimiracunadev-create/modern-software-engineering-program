# Aserción

## Definición

Una **aserción** es la comprobación en ejecución de un supuesto del programa (`SE-452`): una condición que el código declara cierta en un punto y que se verifica al llegar a él.

## Por qué importa

Convierte un supuesto silencioso en un fallo inmediato y localizado. En sistemas críticos, `SE-452` recoge las reglas de Holzmann, diez reglas que caben en una página, escritas para que una herramienta las compruebe; una de ellas pide un mínimo de aserciones por función.

## Cómo funciona

La aserción documenta una precondición, una postcondición o un invariante y falla de forma ruidosa cuando se viola, en lugar de dejar que el dato corrupto se propague. Funciona junto con otras reglas del estándar: flujo de control simple (sin saltos arbitrarios ni recursión), bucles con una cota fija comprobable, funciones que caben en una página y comprobación del valor de retorno de lo que puede fallar. La causa de su utilidad es que acorta la distancia entre el defecto y su síntoma.

## Ejemplo

```python
def promedio(notas):
    assert len(notas) > 0, "promedio requiere al menos una nota"
    resultado = sum(notas) / len(notas)
    assert 0 <= resultado <= 7
    return resultado
```

## Errores y confusiones comunes

Usar aserciones para validar entradas externas (esas se validan con errores normales: las aserciones pueden desactivarse); poner efectos secundarios dentro de la condición.

## Límites y cuándo no aplica

`SE-452` aclara que las ideas (cotas, comprobación de retornos, aserciones, sin excepciones vacías) se trasladan a otros lenguajes, mientras que las reglas de C sobre punteros o preprocesador no. En Python, ejecutar con optimización elimina las sentencias `assert`, así que no deben ser la única defensa.
