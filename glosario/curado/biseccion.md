# Bisección

## Definición

La **bisección** es una búsqueda binaria en el historial entre un commit bueno y uno malo para localizar el cambio que introdujo un defecto (SE-194). SE-481 la generaliza: búsqueda binaria del primer cambio defectuoso dividiendo repetidamente un conjunto de cambios, algo que se aplica también a lotes de cambios integrados en una canalización. En Git la implementa `git bisect`.

## Por qué importa

Convierte un historial en una búsqueda de coste logarítmico, siempre que cada punto sea comprobable. Sin bisección, encontrar cuándo se rompió algo exige leer commits uno a uno; con ella, mil commits se resuelven en unas diez pruebas. Cambia cómo se escriben los commits: si la historia se va a bisecar, cada commit debe poder probarse.

## Cómo funciona

Dado un commit bueno y uno malo, se prueba el del medio y se descarta la mitad según el resultado; se repite. Con N commits necesita unas log₂ N ejecuciones: 64 commits en 6 pasos y mil en 10 (SE-194). `git bisect run` automatiza el proceso con un programa que devuelve éxito o fallo, de modo que la búsqueda se hace sin intervención.

La técnica requiere dos condiciones. Primero, un **criterio de prueba determinista**: una comprobación corta (por ejemplo, un test concreto) que distinga bueno de malo. Segundo, que **cada punto sea comprobable**: un commit que no compila no es ni bueno ni malo y se omite (código 125 en `bisect run`). Si el defecto está junto a commits omitidos, Git solo puede señalar un conjunto de candidatos. De ahí la regla de la plataforma: cada commit de una rama debe compilar, para que la bisección no deba omitir puntos.

Un segundo requisito es que el commit culpable sea legible. Si mezcla varias intenciones, aunque la bisección lo señale hay que leer cientos de líneas; por eso los commits atómicos y `git add -p` para dividirlos antes de publicar. En SE-481 el mismo principio se aplica a lotes: si una canalización integra varios cambios juntos y falla, se bisecan los lotes para aislar el culpable.

## Ejemplo

En la plataforma, una nota sale mal tras una semana de cambios en `penal.py`. Se marca el commit de hace una semana como bueno y la punta como mala, y se ejecuta `git bisect run pytest -q tests/test_penal.py`. Tras unas seis ejecuciones sobre 64 commits, Git señala el commit que cambió el redondeo. Como ese commit hacía una sola cosa y traía una frase de resumen y el issue, se entiende de inmediato. (Ejemplo derivado de SE-194.)

## Errores y confusiones comunes

- **La bisección no señala un solo commit**: hay un commit que no compila junto al defecto; corrección: reordenar la rama para que cada paso compile y repetir.
- **Hay que leer cientos de líneas tras bisecar**: el commit culpable mezcla intenciones; corrección: dividir con `git add -p`.
- **Usarla con un defecto intermitente**: la prueba no es determinista y la búsqueda se desvía.
- **Marcar mal el commit «bueno».**

## Límites y cuándo no aplica

No sirve si no hay una prueba automatizable ni un punto bueno conocido, ni con historiales donde el defecto se introduce y corrige varias veces. Para defectos que dependen de la combinación de dos cambios, señala uno de ellos y puede engañar. La transferencia está lograda cuando se sabe qué dependía de poder probar cada punto, no solo de recordar los comandos.
