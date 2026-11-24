# Postcondición

## Definición

Una **postcondición** es una condición que una operación garantiza al terminar, siempre que se haya cumplido su precondición (SE-159). Es la mitad de un contrato de diseño en el sentido de Meyer: la precondición es lo que el cliente debe cumplir; la postcondición, lo que el proveedor garantiza a cambio.

## Por qué importa

Fija lo que el cliente puede suponer tras la llamada sin tener que mirar cómo se calculó. Sin postcondiciones, quien usa la operación depende de lo que observó que hacía, y ese comportamiento puede cambiar sin aviso. Cambia dos cosas: cómo se documenta una operación (qué queda garantizado) y cómo se razona sobre herencia y sustitución.

## Cómo funciona

SE-159 ilustra con `calificar`: tras la llamada, la nota está en el rango permitido y el estado es «calificada». Meyer presenta la postcondición como el **beneficio del cliente** a cambio de cumplir la precondición. Sirve a dos lectores: a la persona, que sabe qué puede suponerse; y al comprobador, que puede verificar en ejecución (con aserciones) o en pruebas que se cumple, sin conocer el cálculo.

La regla que conecta con la sustitución es la de la herencia: una subclase puede **aceptar al menos lo mismo** (precondición igual o más débil) y **garantizar al menos lo mismo** (postcondición igual o más fuerte). Si refuerza una precondición o debilita una postcondición, los clientes de la clase base se rompen aunque el código compile: es el síntoma que SE-159 señala. Es la base contractual del principio de sustitución de Liskov, y conecta con el subtipado conductual.

Su límite lo declara la clase: la postcondición solo afirma lo que está escrito. Una operación que duplica una prórroga sin pasar del tope cumple todas las postcondiciones que nadie escribió. Por eso conviene acompañar las postcondiciones con invariantes de clase y con pruebas.

## Ejemplo

SE-159 declara una precondición y una postcondición para la prórroga y pide predecir cuál de dos llamadas falla. Una formulación equivalente, a modo de ilustración:

```python
def conceder_prorroga(entrega, horas):
    assert 0 < horas <= 72            # precondición
    anterior = entrega.plazo
    entrega.plazo = anterior + horas  # (horas, simplificado)
    assert entrega.plazo > anterior   # postcondición
```

La llamada con `horas = 0` viola la precondición (culpa del cliente); si la operación no mueve el plazo, viola la postcondición (culpa del proveedor).

## Errores y confusiones comunes

- **La subclase compila y rompe a los clientes de la base**: reforzó una precondición o debilitó una postcondición.
- **Postcondiciones que repiten la implementación**: no comprueban nada nuevo.
- **No escribir las que importan**: la operación cumple todas las que nadie escribió.
- **Confundirla con la precondición**: la primera obliga al proveedor; la segunda, al cliente.

## Límites y cuándo no aplica

Muchos lenguajes no tienen soporte nativo de contratos y las aserciones se desactivan en producción; entonces las postcondiciones sirven como documentación y como pruebas. No sustituyen la validación de entradas de fuentes externas. Algunas postcondiciones (por ejemplo, sobre estado externo, tiempo o concurrencia) son difíciles de expresar y de comprobar.
