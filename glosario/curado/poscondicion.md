# Poscondición

## Definición

Una **poscondición** es la propiedad que una operación garantiza al terminar, siempre que se haya cumplido su contrato (`SE-052`). `SE-547` la formula como lo que la rutina garantiza al terminar. Es la mitad del contrato que obliga al proveedor; la otra mitad, la precondición, obliga a quien llama.

## Por qué importa

Una operación sin poscondición explícita no se puede probar ni consumir con seguridad: nadie sabe qué esperar. Con ella, el cliente puede apoyarse en el resultado y las pruebas tienen un oráculo. `SE-052` la usa para que, cuando una función falla, se sepa quién se equivocó: sin contrato escrito, el defecto cae en un limbo.

## Cómo funciona

La poscondición relaciona estado previo, entrada y salida (`SE-052`). La diferencia entre débil y contrastable es el valor práctico:

- **Débil:** «devuelve una lista».
- **Contrastable:** «devuelve solo pruebas autorizadas y toda hipótesis descartada cita evidencia».

Una operación puede garantizar distintas poscondiciones para éxito y para error: por ejemplo, en éxito el estado cambió y se devuelve el nuevo valor; en error, el estado no cambió y se informa la causa. Lo que la implementación garantiza incluye también lo que no oculta: en la clase, las observaciones contradictorias se informan, no se esconden. La poscondición se puede ejecutar como afirmación (`assert`), como prueba basada en propiedades o como contrato en tiempo de ejecución (`SE-159` la trata como parte de un contrato ejecutable).

## Ejemplo

```python
def descartar(hipotesis, evidencia):
    assert hipotesis in estado.abiertas                     # precondición
    resultado = _descartar(hipotesis, evidencia)
    assert resultado.cita == evidencia and hipotesis not in estado.abiertas   # poscondición
    return resultado
```

La poscondición dice qué es verdad después: la hipótesis ya no está abierta y el resultado cita la evidencia.

## Errores y confusiones comunes

- **La función falla sin decir quién se equivocó.** Causa: contrato implícito; corrección: escribir precondición, invariante y poscondición (`SE-052`).
- **Poscondición vacía.** «Devuelve algo» no permite decidir si el resultado es correcto.
- **Confundirla con la precondición.** La poscondición es obligación del proveedor; la precondición, del cliente.

## Límites y cuándo no aplica

Una poscondición bien escrita puede ser cara de comprobar en producción: se verifica en pruebas y se desactiva o se muestrea después. Algunas propiedades (equidad, calidad de una recomendación) no se expresan como un predicado simple. Y la poscondición solo vale si la precondición se cumplió: si el cliente la violó, el proveedor no promete nada (`SE-159`).
