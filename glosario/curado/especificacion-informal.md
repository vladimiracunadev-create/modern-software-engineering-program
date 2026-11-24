# Especificación informal

## Definición

Una **especificación informal** es una descripción en lenguaje natural sin reglas de forma que permitan decidir mecánicamente si dos lecturas coinciden. Es el primer nivel de la escala de `SE-157` (informal, semiformal, formal). Su rasgo no es la falta de rigor del autor sino la ausencia de un procedimiento para comparar lecturas.

## Por qué importa

Cambia dónde se invierte esfuerzo de precisión. La prosa es barata y legible para todos, y es la que más lecturas admite. Un texto que dos personas leen distinto produce dos implementaciones que ambas «cumplen» la política y dan resultados diferentes. Saber que la prosa tiene este límite lleva a reforzar solo los puntos donde la ambigüedad cuesta.

## Cómo funciona

`SE-157` describe la prosa como el nivel donde empieza todo y donde casi todo se queda. Su fortaleza es que cualquiera la lee, la discute y la corrige; su debilidad, que no tiene un procedimiento para decidir si dos lecturas son la misma. Una especificación informal **bien hecha** hace tres cosas: declara sus términos («día» significa bloque de 24 horas desde el plazo), nombra sus casos límite y trae ejemplos con valores.

No se vuelve semiformal por usar viñetas: se vuelve semiformal cuando una regla de forma permite comprobar mecánicamente algo del texto, por ejemplo que cada requisito tenga identificador y criterio. Y se vuelve formal cuando admite un procedimiento de decisión sobre su significado. La clase recomienda, para una frase ambigua, enumerar las lecturas posibles, elegir una y escribirla como predicado y como ejemplos de frontera.

## Ejemplo

En `SE-157`, la política de penalización por entrega tardía admite varias lecturas: ¿un retraso de 25 horas son uno o dos días? Dos sistemas dan notas distintas para la misma entrega y ambos cumplen la frase. La corrección es declarar «día» como bloque de 24 horas, añadir ejemplos en múltiplos de 24 horas, en el tope y con nota 0, que son los puntos que más separan lecturas.

## Errores y confusiones comunes

- **Dos sistemas, notas distintas y ambos «cumplen».** La frase admite varias lecturas y nadie ejecutó ninguna; enumerar lecturas, elegir una, escribirla como predicado y ejemplos.
- **Ejemplos solo del camino típico.** Los defectos aparecen en el límite; añadir ejemplos en las fronteras.
- **Creer que informal significa mala.** Puede estar bien hecha.
- **Confundir viñetas con formalidad.** El formato no agrega decidibilidad.

## Límites y cuándo no aplica

Para reglas críticas o numéricas, la prosa sola es insuficiente: conviene un nivel superior (semiformal o formal) o ejemplos ejecutables. Para exploración inicial, en cambio, forzar formalidad temprana frena la conversación. La clase no afirma que haya un nivel correcto universal: el nivel se elige por el costo de una lectura equivocada.
