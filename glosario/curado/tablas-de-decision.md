# Tablas de decisión

## Definición

Una **tabla de decisión** es una enumeración de combinaciones de condiciones con la acción de cada una, que permite comprobar completitud y consistencia (SE-146). Es una técnica de especificación para reglas que dependen de varias condiciones.

## Por qué importa

Muestra huecos y contradicciones que el texto corrido oculta. Cuando una regla depende de varias condiciones, la prosa invita a describir los casos felices y olvidar el resto. La tabla obliga a mirar cada combinación y asignarle una acción o reconocer que no la tiene. Cambia el momento en que se descubre «¿qué pasa si…?»: en la mesa y no en producción.

## Cómo funciona

Se listan las condiciones (columnas de entrada) y las acciones; cada fila es una combinación de valores de las condiciones con la acción resultante. SE-146 destaca dos propiedades que la tabla permite comprobar:

- **Completitud**: ninguna combinación queda sin acción.
- **Consistencia**: ninguna combinación recibe acciones contradictorias.

El costo es exponencial: **n condiciones binarias dan 2ⁿ filas**. Por eso se limita a reglas con pocas condiciones o se complementa con técnicas de reducción (combinar filas que comparten acción, o aplicar cobertura combinatoria). La tabla de la plataforma de entregas es de penalización: condiciones como «¿hay gracia?», «¿hay prórroga?» y «¿se pasó del tope?», con la acción de cada combinación. La clase propone cambiar una sola regla (por ejemplo, que la prórroga se sume a la gracia) y revisar qué filas cambian.

Dos fallos que la clase prevé, con su causa: dos módulos calculan una nota distinta para la misma entrega porque la regla vive duplicada en el código y cada copia evolucionó por su lado (se extrae la regla a un único punto con identificador y responsable); el comité de política pregunta «¿qué pasa si…?» y nadie lo sabe porque se redactaron solo los casos felices (se enumeran combinaciones y se asigna a cada una una acción o una decisión pendiente).

## Ejemplo

Condiciones: **A** = entrega dentro de gracia; **B** = prórroga concedida. Acciones: nota completa, descuento, descuento reducido.

| A | B | Acción |
| --- | --- | --- |
| sí | sí | nota completa |
| sí | no | nota completa |
| no | sí | descuento reducido |
| no | no | descuento |

Cuatro filas cubren las dos condiciones binarias. Si alguien añade una tercera condición («¿pasó el tope?»), la tabla crece a ocho filas y aparecen combinaciones que la prosa no había considerado. (Tabla ilustrativa, no la de SE-146.)

## Errores y confusiones comunes

- **Dos módulos calculan notas distintas**: regla duplicada; corrección: único punto con identificador y responsable.
- **Nadie sabe qué pasa en un caso raro**: solo casos felices; corrección: enumerar y asignar acción o decisión pendiente.
- **Dejar filas «imposibles» sin declarar por qué lo son.**
- **Tablas enormes que nadie lee**: demasiadas condiciones.

## Límites y cuándo no aplica

El crecimiento exponencial las vuelve impracticables con muchas condiciones; ahí se descompone la regla o se usan otras técnicas. No expresan bien secuencias o estados (para eso, máquinas de estados). Con condiciones continuas, hay que discretizarlas en rangos, y la discretización es una decisión que debe justificarse.
