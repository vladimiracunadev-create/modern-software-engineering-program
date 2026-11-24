# Fronteras entre modelos

## Definición

Las **fronteras entre modelos** son los puntos de un programa donde se combinan paradigmas distintos (objetos, funciones, eventos, reglas) y, por tanto, hay que **traducir** de una representación a otra. `SE-082` lo expresa así: combinar modelos exige **adaptadores**: evento a valor, objeto a registro, resultado a excepción o mensaje. Cada adaptador es una frontera, y el término designa tanto el lugar como el acuerdo sobre qué atraviesa. No es un concepto de una norma; es una forma de pensar la mezcla de paradigmas.

## Por qué importa

Los programas reales mezclan estilos: un núcleo funcional rodeado de objetos, un sistema de eventos que alimenta reglas, una base de datos relacional detrás de un modelo de objetos. Mezclar es normal; lo costoso es mezclar sin pensar en las traducciones. En cada una puede perderse algo y el programa seguirá compilando. La decisión que cambia es cómo se diseña la unión: la frontera se trata como una interfaz con su propio contrato, no como un detalle incidental.

## Cómo funciona

Cada traducción puede perder tres cosas (`SE-082`):

- **Orden:** un evento llega en una secuencia; al convertirlo en valor para una función pura, se pierde cuál vino antes si no se lo registra.
- **Identidad:** un objeto tiene identidad y estado en el tiempo; al convertirlo en un registro plano (para guardarlo o enviarlo) queda una instantánea sin identidad propia.
- **Información de error:** un resultado con un valor de error explícito se convierte en una excepción (o al revés) y puede perderse el contexto, la causa o la distinción entre errores recuperables y fatales.

Por eso el **contrato de la frontera** debe declarar **qué se preserva y qué se descarta**. Un adaptador sin contrato esconde decisiones: nadie sabe si el orden sobrevive, si dos objetos que eran el mismo se vuelven dos registros, o si un error se aplana en un mensaje de texto. Declararlo permite probarlo con casos específicos de la frontera.

## Ejemplo

Un servicio recibe eventos de entrada y los pasa a un núcleo funcional que decide una recomendación. En la frontera de entrada se convierte cada evento en un valor y se decide qué se conserva:

```python
def evento_a_caso(evento):
    """Preserva: id, monto, instante. Descarta: cabeceras de transporte.
    Orden: el instante permite reconstruirlo; no se asume orden de llegada."""
    return Caso(id=evento["id"], monto=evento["monto"], instante=evento["ts"])

def resultado_a_respuesta(resultado):
    """Un error de dominio se convierte en código 422 con 'causa';
    una excepción inesperada se convierte en 500 sin detalle interno."""
```

Cada docstring es una declaración de contrato. Una prueba comprueba, por ejemplo, que dos eventos con el mismo `id` no se confundan.

## Errores y confusiones comunes

- **Elegir un paradigma por moda.** No hay criterios explícitos; se escriben criterios y la evidencia de cada uno.
- **Adaptadores sin contrato.** No se sabe qué se pierde.
- **Comparar paradigmas con reglas simples.** La comparación favorece al que se conoce; hay que incluir una regla que dependa de otra o de estado.
- **Traducir errores a texto.** Pierde la distinción entre fallos recuperables y fatales.

## Límites y cuándo no aplica

Una matriz organiza juicio, no sustituye un prototipo ni datos de mantenimiento (`SE-082`). En un programa de un solo paradigma y pocas capas casi no hay fronteras que gobernar. Y cuando se pueden evitar las traducciones usando un solo modelo en toda una zona, es preferible a diseñar adaptadores muy elaborados: cada frontera es un costo permanente de pruebas y de mantenimiento.
