# Semántica antes que sintaxis

## Definición

**Semántica antes que sintaxis** es el principio de comparación de `SE-082`: **dos implementaciones son comparables si aceptan el mismo dominio y producen resultados equivalentes para casos normales, límite y de error**. La semántica es lo que el programa *significa* (qué devuelve, qué rechaza, en qué orden resuelve un empate); la sintaxis, cómo está escrito. Antes de comparar la longitud, la elegancia o el estilo de dos soluciones, hay que haber establecido que hacen lo mismo.

## Por qué importa

Es fácil comparar implementaciones por lo visible: cuántas líneas tienen, cuántos *tokens*. Pero `SE-082` advierte que **contar líneas o *tokens* sin verificar la semántica premia las omisiones**: la versión más corta puede serlo porque no valida entradas, no maneja el empate o ignora un caso de error. La decisión que cambia es el orden de las preguntas: primero «¿hacen lo mismo?» y solo si la respuesta es sí, «¿cuál es más clara, corta o mantenible?».

## Cómo funciona

El procedimiento de la clase es:

1. **Congelar el contrato:** la entrada aceptada, la salida, el **orden de empate**, los errores y los casos (normales, límite, error).
2. **Buscar una representación equivalente** en cada modelo. `SE-082` da ejemplos de mapeos: `None` puede corresponder a `Option`; una excepción recuperable, a `Result`; un diccionario heterogéneo, a un registro con campos (*struct*).
3. **Juzgar la equivalencia por comportamiento, no por parecido textual,** con fixtures comunes. Solo se normalizan diferencias de **presentación** (formato de un texto de salida), no de decisión.

La razón de fondo es que los lenguajes y paradigmas representan el mismo concepto de maneras distintas, y un parecido textual engaña: dos funciones que se parecen mucho pueden diferir en un caso límite, y dos que no se parecen nada pueden ser equivalentes. Solo ejecutar el mismo conjunto de casos lo revela.

## Ejemplo

Dos versiones de una regla de aprobación:

```python
# A: corta
def aprobar(c): return c["puntaje"] > 60

# B: más larga, maneja los casos de borde
def aprobar_b(c):
    if "puntaje" not in c or not isinstance(c["puntaje"], (int, float)):
        raise ValueError("puntaje inválido")
    return c["puntaje"] > 60
```

A es tres veces más corta y pierde frente a B en solidez: ante un caso sin puntaje, A lanza `KeyError`, y ante un puntaje de texto, `TypeError`; el contrato congelado decía que debía lanzar `ValueError("puntaje inválido")`. Con el fixture común (que incluye «dato inválido») las dos no son comparables hasta que A cumpla el mismo contrato. Solo entonces tiene sentido comparar longitud y claridad. `SE-082` documenta dos riesgos relacionados: elegir un paradigma por moda, por falta de criterios explícitos, y que la comparación favorezca al paradigma conocido porque las reglas son simples y no ejercitan lo propio de otros (se incluye una regla que dependa de otra o de estado).

## Errores y confusiones comunes

- **Comparar por líneas o *tokens*.** Premia omitir casos.
- **Juzgar equivalencia por parecido.** Solo la ejecución común lo establece.
- **Normalizar diferencias de decisión.** Solo se normalizan las de presentación.
- **Casos solo felices.** Sin límite ni error, la equivalencia es aparente.

## Límites y cuándo no aplica

Una matriz organiza el juicio, no sustituye un prototipo ni datos de mantenimiento (`SE-082`). La equivalencia total es difícil en la práctica: los paradigmas expresan ciertos casos con dificultad o no los expresan, y esa imposibilidad es información, no un defecto del método. Para decisiones de estilo puro, donde ambas versiones ya son equivalentes y probadas, la comparación sintáctica es legítima.
