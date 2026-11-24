# Producción

## Definición

En el vocabulario de métricas del programa, la **producción** (*output*) es lo que el equipo entrega, contable y controlable: líneas de código, versiones, tickets cerrados, funciones lanzadas (SE-135). No es el entorno de producción donde corre el software (ese es otro concepto del glosario), sino el primer eslabón de la cadena producción → actividad → resultado.

## Por qué importa

Es lo más fácil de contar y por eso lo más fácil de convertir en meta. Cambia cómo se evalúa a un equipo: con producción se mide cuánto hizo; con resultado, qué cambió en la vida de quien usa el producto. SE-135 advierte que un equipo con alta producción y resultados nulos es posible, y que uno con poca producción y alto resultado también.

## Cómo funciona

La producción tiene una virtud y un límite. La virtud: es **controlable por el equipo** y se cuenta sin ambigüedad (un ticket está cerrado o no). El límite: **no dice si lo producido sirvió**. Un ticket cerrado puede resolver un problema real o ser trabajo innecesario; una función lanzada puede ser ignorada.

Por eso sirve para **planificar capacidad** (cuánto puede entregar el equipo en un periodo) y no para evaluar valor. Cuando se convierte en meta se activa la ley de Goodhart: la gente optimiza la cifra. SE-135 describe dos síntomas con su causa: la meta se cumple y nadie mejora (se premió la producción), y un equipo gana premios con malos resultados (se compararon producciones). La corrección es acompañar o reemplazar la producción con un resultado y su métrica contraria, y comparar equipos por resultado o por una métrica equilibrada.

En la auditoría de métricas de la plataforma, cada métrica se clasifica en producción, actividad, resultado o vanidad, con la decisión que informa y su métrica contraria. Esa clasificación hace visible cuántas métricas del panel son solo producción.

## Ejemplo

El equipo de la plataforma cierra 40 tickets en el trimestre y lanza 6 funciones: es producción. Si la meta fuera «cerrar más tickets», un equipo podría dividir un ticket en tres para triplicar la cifra. Si la meta es «porcentaje de entregas aceptadas a la primera», mejora solo si el trabajo hace que más estudiantes lo logren, y entonces la producción queda como un medio. (Ilustración construida sobre el escenario de la clase.)

## Errores y confusiones comunes

- **Premiar la producción**: la meta se cumple y nadie mejora.
- **Comparar equipos por producción**: un equipo gana premios con malos resultados.
- **Confundirla con el entorno de producción**: son sentidos distintos de la misma palabra.
- **Descartarla del todo**: es útil para capacidad y para ver si el flujo de trabajo funciona.

## Límites y cuándo no aplica

No sirve para medir valor ni calidad. En contextos donde el entregable es el objetivo (una obra por encargo con alcance fijo), la producción es en buena medida el resultado, y la distinción pierde fuerza. Aun así, una entrega contratada puede cumplirse a cabalidad y no resolver el problema de quien la pidió.
