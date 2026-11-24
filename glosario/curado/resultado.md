# Resultado

## Definición

En métricas de producto, el **resultado** (*outcome*) es el cambio observable en quien usa el producto o en su organización, con definición calculable y fuente de datos (SE-135): la persona logra su objetivo, el docente tarda menos, el centro reduce reclamos. Es el tercer escalón de la cadena producción → actividad → resultado.

## Por qué importa

Es lo que de verdad importa y lo que más cuesta medir. Cambia a qué se le llama éxito: no a cuántas funciones se lanzaron ni a cuánta gente entró, sino a si algo mejoró para alguien. SE-135 lo contrasta con la producción: un equipo con alta producción y resultados nulos es posible, y también uno con poca producción y alto resultado.

## Cómo funciona

El resultado se mide con **eventos de logro, tiempos y encuestas** con definición calculable (numerador, denominador, ventana, filtros). «La entrega llegó» es un evento de logro; «el docente corrigió en menos tiempo» es un tiempo comparado; «el centro redujo reclamos» es un conteo por periodo. La definición calculable es lo que evita que dos paneles den cifras distintas para «lo mismo».

Dos propiedades lo distinguen. Primero, es **más difícil de falsear** que la producción: cerrar más tickets se logra con fraccionarlos, pero hacer que más entregas lleguen requiere que el flujo funcione. Segundo, **se atribuye con cautela**: que el resultado mejore tras un cambio no prueba que el cambio lo causó, y SE-138 enseña los experimentos, los controles y la regresión a la media precisamente para eso.

Aun así, el resultado no se persigue solo: se acompaña de una **métrica contraria** (algo que no debe empeorar mientras se mejora, como la calidad de lo entregado o el tiempo de respuesta), y la regla de la auditoría de métricas de SE-135 es que ninguna métrica se convierte en meta sin su contraria y sin la pregunta «qué haría distinto si bajara».

## Ejemplo

En la plataforma de entregas, **producción**: funciones lanzadas en el trimestre. **Actividad**: inicios de sesión de estudiantes. **Resultado**: proporción de entregas aceptadas antes del plazo, o minutos que tarda un docente en revisar un lote. Si se lanza un panel de seguimiento y el tiempo de revisión baja de 40 a 25 minutos por lote, hay un resultado asociado (con las cautelas de atribución). (Cifras ilustrativas.)

## Errores y confusiones comunes

- **La meta se cumple y nadie mejora**: se premió la producción; corrección: reemplazar o acompañar con un resultado y su contraria.
- **Un equipo gana premios con malos resultados**: se compararon producciones.
- **Confundir resultado con actividad**: en el experimento de equipos de SE-135, la actividad correlaciona 0,20 con el resultado.
- **Atribuir causalidad sin diseño**: una mejora tras un cambio puede tener otras causas.

## Límites y cuándo no aplica

Los resultados suelen tardar en notarse y requieren instrumentación y a veces encuestas, lo que no siempre es viable. Para productos en fase muy temprana, con pocos usuarios, el resultado tiene mucha incertidumbre (intervalos anchos). Hay resultados que no se miden de forma directa y se aproximan con indicadores sustitutos; hay que declararlo. Y optimizar un solo resultado puede dañar otros, por eso la métrica contraria.
