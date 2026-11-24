# Elicitación

## Definición

La **elicitación** es el conjunto de técnicas para hacer aparecer el conocimiento sobre lo que se necesita, incluida la parte que nadie escribe ni enuncia. Es el sentido de `SE-145`, donde es la primera de cuatro actividades de la ingeniería de requisitos: elicitación, análisis, especificación y validación. Elicitar es provocar que aparezca conocimiento que no está escrito en ningún sitio.

## Por qué importa

Cambia qué técnica se usa para cada tipo de conocimiento. Entrevistar no llega a lo tácito, y una especificación puede quedar «completa» y decepcionar a quienes usan el sistema porque solo se entrevistó a quien paga. `SE-145` ilustra el límite con una simulación: hablar con todo el mundo cubre apenas el 77 % de lo necesario.

## Cómo funciona

Cada técnica tiene un alcance. Una **entrevista** recoge lo que la persona sabe y es capaz de decir. La **observación** recoge lo que hace. El **análisis de documentos** recoge lo que la organización ya decidió. Un **prototipo** recoge reacciones ante algo concreto. La razón es que el conocimiento tácito no se declara: preguntarle a una docente «¿qué necesita el sistema?» no revelará que siempre abre las entregas en el móvil mientras camina, porque ella no lo considera un dato.

Elegir la técnica es, entonces, elegir qué clase de conocimiento se puede obtener. Y como cada técnica deja huecos, se combinan. Después de elicitar viene el análisis, que trata lo recogido como conjunto para encontrar conflictos, y la validación con la persona usuaria, no solo con el cliente. Un requisito debe registrar además su origen, y hay que separar necesidad, requisito y supuesto: si una frase mezcla requisito y solución, dos equipos pueden discutirla una hora porque entienden cosas distintas.

## Ejemplo

En la plataforma de entregas de `SE-145`, entrevistar a la docente produce los requisitos que ella sabe nombrar; observar cómo corrige entregas en su jornada revela restricciones que no mencionó; analizar el reglamento académico recoge plazos ya decididos; un prototipo muestra reacciones ante el flujo. Ninguna técnica sola cubre todo.

## Errores y confusiones comunes

- **Identificar elicitar con «hablar con el cliente».** Es una técnica entre varias.
- **Entrevistar solo a quien paga.** El conocimiento tácito de quien usa no se elicita; añadir observación y validar con la persona usuaria.
- **Confundir elicitar con analizar.** El análisis empieza cuando lo recogido se trata como conjunto.
- **Registrar la solución en lugar de la necesidad.** Mezcla requisito y solución.

## Límites y cuándo no aplica

La elicitación solo obtiene lo que alguien sabe, hace o decidió; no descubre lo que nadie sabe todavía, para lo cual se usan experimentos y descubrimiento de producto. El 77 % de `SE-145` sale de una simulación, no de un estudio de proyectos reales. Y con requisitos regulados la elicitación se apoya en documentos y no en preferencias.
