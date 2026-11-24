# Frontera

## Definición

Una **frontera** es el punto donde cambian la autoridad, la semántica, el rendimiento o la propiedad (`SE-034`). El programa usa la palabra en tres lugares:

- **Frontera de análisis** (`SE-001`): declara qué elementos de un sistema se modelan con detalle y cuáles se tratan como entorno.
- **Frontera de aislamiento** (`SE-034`): hasta dónde un proceso, contenedor o máquina separa lo que ve y comparte con el anfitrión.
- **Valor de frontera** (`SE-422`): el valor de entrada donde cambia la clase de comportamiento; allí la comparación (`<` o `<=`) decide.

## Por qué importa

Casi todo error serio vive en una frontera: donde dos autoridades se pasan un dato, donde un umbral cambia el comportamiento, donde se supone un aislamiento que no existe. Trazar la frontera correcta decide qué se analiza, qué se aísla y qué se prueba.

## Cómo funciona

- **Análisis** (`SE-001`): se declara qué se modela con detalle y qué es entorno, y se acompaña de interfaces y supuestos, porque el entorno sigue condicionando el resultado. Externalizar pagos cambia quién opera el procesador; no externaliza el deber de informar un cobro incierto, reconciliarlo ni ofrecer reparación. Se necesitan las fronteras para responder preguntas distintas, normalmente entre dos y cuatro: una sola mezcla preguntas incompatibles; ocho producen un mapa que nadie mantiene.
- **Aislamiento** (`SE-034`): se enumeran las fronteras y las capacidades efectivas; compartir núcleo, montajes y privilegios debilita la frontera.
- **Valores** (`SE-422`): las clases de equivalencia terminan en fronteras, y los errores `<` contra `<=` solo aparecen probando justo en ellas y alrededor.

## Ejemplo

`SE-422`: la regla «descuento si el pedido es ≥ 100» se prueba con 99, 100 y 101. Una cobertura del 100 % con casos típicos (50 y 500) no rompe si alguien cambia `>=` por `>`; una tabla de fronteras y la medida con mutantes sí lo detecta. Ilustración:

```python
assert descuento(99) == 0 and descuento(100) > 0 and descuento(101) > 0
```

## Errores y confusiones comunes

- **La frontera coincide con el organigrama.** Causa: se modeló autoridad formal, no causalidad; corrección: seguir una solicitud real y mover la frontera según la pregunta (`SE-001`).
- **«Está aislado porque está en un contenedor».** Causa: se ignoraron kernel, montajes y privilegios compartidos; corrección: enumerar fronteras y capacidades efectivas (`SE-034`).
- **Cobertura del 100 % sin valores de frontera.** Causa: casos típicos únicamente; corrección: tabla de fronteras y medida con mutantes (`SE-422`).

## Límites y cuándo no aplica

Una frontera excesiva tiene el problema opuesto: incorpora toda la universidad, pierde responsables concretos y no permite verificar nada (`SE-001`). Los casos de prueba deben cubrir cada clase de comportamiento y cada frontera, no una cantidad fija. Y los tres sentidos no son intercambiables: una frontera de análisis no aísla nada.
