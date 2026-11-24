# Invariantes alrededor de transiciones

## Definición

**Invariantes alrededor de transiciones** es la disciplina que `SE-073` propone para programar con estado mutable: **no se trata de prohibir la mutación, sino de acotarla**. Una *transición* es un cambio de estado; una *invariante* es una condición que debe cumplirse antes y después de cada transición (por ejemplo, «la prioridad nunca es negativa» o «la autorización se preserva»). Antes de la transición se comprueban las **precondiciones**; después deben sostenerse las invariantes. Lo que no puede ocurrir es que un estado intermedio inválido sea observable.

## Por qué importa

El estado mutable es la fuente de muchos errores porque cualquier parte del programa puede dejarlo en una condición inesperada. La respuesta no es la inmutabilidad total (a menudo impracticable) sino concentrar los cambios en puntos bien definidos y verificables. La decisión que cambia es cómo se razona sobre un programa: en lugar de seguir cada asignación, se razona por transiciones completas, cada una con su contrato. `SE-073` señala la condición: una función que **deja un estado intermedio observable rompe el razonamiento, incluso si luego intenta repararlo**.

## Cómo funciona

El patrón tiene tres partes:

1. **Precondiciones:** lo que debe ser cierto para que la transición tenga sentido (el caso existe, está abierto, el valor es válido). Si no se cumplen, se rechaza sin tocar el estado.
2. **Cambio:** la modificación del estado, idealmente en un único lugar.
3. **Postcondiciones e invariantes:** lo que debe seguir siendo cierto al terminar.

Para que la transición sea indivisible desde fuera, se aplica una técnica sencilla: **calcular sobre una copia y confirmar al final**. Si algo falla en medio, el estado original no cambió. La clase documenta dos síntomas de no hacerlo: un rechazo que deja el puntaje distinto del inicial porque se mutó antes de decidir el resultado (se calcula sobre una copia y se confirma al final), y una copia «aislada» que cambia cuando se modifica la original porque la copia es superficial y comparte listas o diccionarios internos (se copia en profundidad solo lo mutable o se usan estructuras inmutables).

## Ejemplo

Una operación que aplica una penalización al puntaje de un caso, con la regla «el puntaje nunca es negativo» y «una operación rechazada no cambia nada»:

```python
def penalizar(caso, puntos):
    if puntos < 0 or not caso["abierto"]:           # precondiciones
        raise ValueError("penalización inválida")
    nuevo = dict(caso)                               # copia: no se toca el original
    nuevo["puntaje"] = max(0, caso["puntaje"] - puntos)
    assert nuevo["puntaje"] >= 0                     # invariante
    caso.update(nuevo)                               # confirmar al final
```

Si `puntos` fuera inválido, se rechaza antes de mutar nada. Un estado intermedio (puntaje ya restado pero sin verificar) nunca queda visible para otro código.

## Errores y confusiones comunes

- **Mutar antes de decidir.** Un rechazo deja el estado a medio cambiar.
- **Copia superficial.** La copia comparte objetos internos con la original.
- **Reparar después.** Un estado inválido que se corrige al final fue observable en medio.
- **Confundir invariantes con validación de entrada.** La validación revisa datos de afuera; la invariante describe el estado interno siempre.

## Límites y cuándo no aplica

La ejecución secuencial no explica por sí sola la concurrencia, la persistencia ni la consistencia distribuida (`SE-073`): con varios hilos, un estado intermedio observable es posible aunque cada transición parezca indivisible, y se necesitan cerrojos o estructuras inmutables. La clase siguiente reduce la superficie mutable con procedimientos de contratos estrechos. En scripts breves, formalizar precondiciones e invariantes puede ser más peso que valor.
