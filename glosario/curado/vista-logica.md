# Vista lógica

## Definición

La **vista lógica** es la vista arquitectónica que muestra módulos o componentes y las dependencias *permitidas* entre ellos (`SE-326`). Responde a la pregunta «¿qué puedo cambiar sin romper a quién?» y gobierna la modificabilidad.

## Por qué importa

Un diagrama de módulos suele leerse como una descripción del sistema, pero describe una intención. La decisión que cambia es cómo se trata ese diagrama: como una regla que se verifica contra el código y las trazas, no como un dibujo que se acepta.

## Cómo funciona

`SE-326` señala el defecto característico de la vista lógica: **declara lo permitido, no lo que ocurre**. Con el tiempo, el código acumula dependencias que nadie dibujó: un módulo importa algo de otro por comodidad, y el diagrama sigue mostrando las flechas originales. La vista deja de ser un mapa fiel y pasa a ser una ilusión de orden.

La corrección es tratarla como una regla comprobable: comparar con las dependencias reales del código (un comprobador de importaciones) o con las trazas de ejecución en cada cambio. Hay dos señales de desajuste:

- Una **dependencia real no dibujada**: el código la usa y el diagrama no la permite (violación).
- Una **arista declarada que nunca se usa**: o el diagrama está viejo o hay código muerto.

Se relaciona con el monolito modular, que impone justo esta clase de regla con un comprobador, y con la vista de ejecución, que muestra la otra cara: lo que realmente se llama y en qué orden. La clase subraya que son vistas distintas y que mezclarlas produce diagramas que no responden bien a ninguna pregunta.

## Ejemplo

La vista lógica dice que Avisos puede depender de Entregas pero no de Calificaciones. Un comprobador recorre las importaciones y detecta que Avisos importa una función interna de Calificaciones, una arista que nadie dibujó. La integración falla hasta que se corrige. Aplicación del principio de `SE-326`.

## Errores y confusiones comunes

- **El código tiene dependencias que nadie dibujó**: la vista lógica declara lo permitido y no se verifica; se corrige comparando con trazas o con el código en cada cambio.
- **Tomar el diagrama como descripción de la realidad**.
- **Mezclarla con la vista de ejecución** en un solo dibujo.
- **Ignorar las aristas declaradas pero no usadas**.

## Límites y cuándo no aplica

La vista lógica solo dice qué dependencias están permitidas, no cuánto se usan ni cuándo: para latencia y capacidad hace falta la vista de ejecución. Su valor depende de verificarla; sin comprobación automática, tiende a desactualizarse. En sistemas muy pequeños, mantenerla formalmente puede costar más de lo que aporta.
