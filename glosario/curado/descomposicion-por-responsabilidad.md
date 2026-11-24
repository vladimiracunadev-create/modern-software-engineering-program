# Descomposición por responsabilidad

## Definición

La **descomposición por responsabilidad** es dividir un programa según los **motivos por los que puede cambiar** cada parte, no según su tamaño. En `SE-074`, el ejemplo central es separar **parseo, validación, decisión y presentación**: cuatro responsabilidades distintas que suelen vivir mezcladas en una sola función. Cada pieza puede cambiarse sin arrastrar las otras tres. Es la versión procedimental de la idea de cohesión: lo que cambia junto, junto; lo que cambia por otra razón, aparte.

## Por qué importa

Una función que lee un texto, valida sus campos, decide qué hacer y formatea la respuesta cambia cada vez que cambia el formato de entrada, una regla de validez, la política o el diseño de la salida; cada cambio obliga a releer todo y puede romper lo que no se quería tocar. La decisión que cambia es dónde cortar: `SE-074` advierte que cortar por **cantidad de líneas** produce piezas arbitrarias, mientras que cortar por **transformación y política** produce unidades que pueden explicarse y probarse con ejemplos propios.

## Cómo funciona

Cada responsabilidad se vuelve una función con una entrada y una salida claras:

- **Parseo:** convierte texto o bytes en una estructura. No decide nada.
- **Validación:** comprueba que la estructura cumple reglas de forma y de dominio. No decide la acción.
- **Decisión:** aplica la política de negocio sobre datos ya válidos. Es la parte con más valor y conviene que sea **pura** (mismo input, mismo output, sin efectos).
- **Presentación:** convierte el resultado en lo que se muestra o se envía.

Como cada etapa recibe lo que la anterior produce, se pueden probar por separado: la decisión con datos ya construidos, sin simular entradas de texto. Y como la parte pura no tiene efectos, también se puede razonar sobre ella con ejemplos. `SE-074` tiene dos advertencias sobre el mecanismo: una descomposición **recursiva** sobre una entrada lineal larga puede provocar `RecursionError`, y se corrige con un bucle con acumulador o una pila explícita; y **memoizar** una función con efectos hace que el efecto «desaparezca» tras la primera llamada, así que solo se memoiza la parte pura.

## Ejemplo

Una función que recibe una línea `"cliente=42;monto=1500"`, comprueba que el monto sea positivo, decide si requiere revisión y devuelve un mensaje. Separada:

```python
def parsear(linea):      # texto -> dict
    return dict(par.split("=") for par in linea.split(";"))

def validar(datos):      # dict -> dict o error
    if int(datos["monto"]) <= 0:
        raise ValueError("monto debe ser positivo")
    return datos

def decidir(datos):      # política pura
    return "revisar" if int(datos["monto"]) > 1000 else "aprobar"

def presentar(accion):   # presentación
    return f"Resultado: {accion}"
```

Cambiar el umbral de revisión toca solo `decidir`; cambiar el formato de entrada, solo `parsear`.

## Errores y confusiones comunes

- **Dividir por líneas.** Una función de 20 líneas no es mejor por ser corta si mezcla responsabilidades.
- **Dividir sin separar decisiones.** Mover código a otro archivo sin separar el motivo de cambio no mejora nada.
- **Recursión sobre listas largas.** `RecursionError` en un recorrido lineal.
- **Memoizar funciones con efectos.** El efecto se ejecuta una sola vez.

## Límites y cuándo no aplica

La descomposición procedural no define por sí misma cómo representar entidades con identidad o ciclos de vida largos (`SE-074`); para eso la clase siguiente contrasta objetos y mensajes. En un script corto y desechable, cuatro funciones pueden ser más ruido que ayuda. Y llevar la separación al extremo (una función por línea) vuelve costoso seguir el flujo: se corta donde hay un motivo de cambio distinto, no por sistema.
