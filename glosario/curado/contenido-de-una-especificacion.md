# Contenido de una especificación

## Definición

El **contenido de una especificación** es el conjunto de elementos que permite a una lectora decidir sin preguntar. Según `SE-156`, una especificación revisable incluye el problema, los supuestos, el alcance, los requisitos con origen y criterio, las dependencias y la línea base. El criterio de suficiencia es funcional: si la lectora necesita llamar al autor para entender qué falta, la especificación está incompleta.

## Por qué importa

Cambia contra qué se revisa un documento. Una especificación puede estar bien escrita y no responder lo esencial. `SE-156` fija la prueba: debe responder sin que su autor esté presente. Cuando falta un elemento, la lectora tendrá que preguntar, que es exactamente lo que el expediente debe evitar.

## Cómo funciona

`SE-156` enumera lo que la especificación debe responder:

- cuál es el problema y a quién afecta;
- qué se supone del mundo;
- qué queda fuera de alcance;
- cuáles son los requisitos, cada uno con **origen**, **texto singular y verificable**, **criterio de aceptación**, **dueño** y **prioridad**;
- cómo se relacionan (dependencias);
- qué obligaciones externas hay y quién las interpretó;
- qué **línea base** representa;
- qué defectos conocidos quedan abiertos.

La lista funciona como lista de verificación para la revisión. Un validador puede comprobar que cada elemento esté presente, pero eso es solo estructura: la clase muestra con mutaciones que un validador puede pasar mientras la especificación contiene errores graves, y por eso su cobertura se documenta y se complementa con revisión humana.

## Ejemplo

`SE-156` entrega la especificación de la plataforma con un encabezado (problema, supuestos, alcance, línea base) y un registro de revisión que la acompaña. Cada requisito lleva su origen y su criterio; las dependencias forman un grafo explícito. Una lectora externa puede decidir si el requisito está completo mirando solo ese expediente.

## Errores y confusiones comunes

- **La lectora tarda un día en entender qué falta.** El expediente no responde sin su autor; corrección: revisar el contenido contra la lista de elementos obligatorios.
- **El validador pasa y la especificación tiene errores graves.** Solo comprueba estructura; documentar su cobertura con mutaciones y completar con revisión humana.
- **Omitir los supuestos y el alcance excluido.** Son lo que más preguntas genera.
- **Escribir requisitos sin origen.** Impiden saber a quién preguntar y qué cambiaría si el origen cambia.

## Límites y cuándo no aplica

La lista es un contenido mínimo para una especificación revisable de la plataforma, no un estándar universal: un prototipo desechable no necesita todos los elementos. Las 16 mutaciones, costos y probabilidades de detección de `SE-156` son supuestos del autor, con datos sintéticos; sirven para entender qué detecta un validador, no para predecir cuántos errores atrapará en un proyecto real. Que el contenido esté completo no garantiza que sea correcto.
