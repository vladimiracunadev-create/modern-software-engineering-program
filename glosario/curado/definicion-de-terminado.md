# Definición de terminado

## Definición

La **definición de terminado** (*Definition of Done*) es el conjunto de comprobaciones que un incremento debe pasar para considerarse utilizable y liberable: pruebas, revisión, análisis, documentación mínima y criterios de aceptación. Es el sentido de `SE-188`. Es una promesa compartida de calidad y, según la clase, la guía de Scrum la hace obligatoria.

## Por qué importa

Cambia qué quiere decir «hecho» en una conversación. Sin una definición compartida, cada persona termina en un punto distinto y la deuda aparece al final. `SE-188` fija el corolario: un incremento que no la cumple no está parcialmente terminado, no lo está. Sirve también para no confundir terminado con aceptado: lo primero es calidad técnica; lo segundo, el reconocimiento de que resuelve el problema.

## Cómo funciona

La definición es una lista de comprobaciones aplicable a todo incremento. Para que funcione tiene que mantenerse viva: se revisa con los defectos que se escaparon y se calibra por tipo de trabajo, porque un cambio de texto y un cambio de la regla de penalización no necesitan las mismas barreras.

El defecto típico es la lista que crece: catorce casillas con comprobaciones correlacionadas, que ven lo mismo y no reducen los escapes. La corrección de `SE-188` es medir qué ve cada casilla y retirar las que ven lo mismo; cada casilla debe tener una razón registrada, el escape concreto que evitó. Si tras añadir dos casillas los escapes del trimestre no bajan, el síntoma es que las nuevas son redundantes.

## Ejemplo

El equipo de la plataforma de entregas reduce su definición de catorce casillas a tres niveles. Cambios de texto: revisión y prueba de aceptación automática. Cambios de interfaz: además, comprobación de accesibilidad con una herramienta y una lectora de pantalla. Cambios en la regla de penalización o en notas: además, comparación contra la función de referencia de `SE-157` y una segunda persona que lee el sentido. Cada casilla lleva la razón que la justifica.

## Errores y confusiones comunes

- **Catorce casillas y los escapes no bajan.** Comprobaciones correlacionadas; medir qué ve cada una y retirar las redundantes.
- **Una lista única para todo.** Frena lo trivial y no basta para lo crítico.
- **Confundirla con los criterios de aceptación.** Esos son por historia; la definición es común a todas.
- **Terminado a medias.** No existe: o cumple la definición o no.

## Límites y cuándo no aplica

La definición garantiza que se hicieron ciertas comprobaciones, no que el incremento sea el correcto: puede estar terminado y no ser aceptado. No sustituye a la definición de «listo» (*Ready*), que regula la entrada del trabajo, ni a la aceptación por quien lo pidió. Una definición demasiado ambiciosa para el contexto se incumple por sistema y deja de ser promesa.
