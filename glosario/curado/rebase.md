# Rebase

## Definición

El **rebase** es la reaplicación de commits sobre otra base, que crea commits nuevos con otros identificadores (SE-195). Toma los commits de una rama y los reaplica uno por uno sobre otro punto de partida; el resultado es una historia lineal.

## Por qué importa

Cambia cómo se ve y cómo se comparte la historia. Un rebase limpia la bifurcación (la rama parece haberse escrito sobre la última versión de `main`), pero reescribe los commits. Elegirlo bien evita historias confusas; usarlo donde no corresponde provoca commits duplicados y conflictos repetidos.

## Cómo funciona

Git toma cada commit de la rama, calcula su cambio respecto de su padre y lo aplica sobre la nueva base. Cada commit reaplicado es un **objeto nuevo con otro identificador**, aunque diga lo mismo, porque el identificador depende del contenido, del padre y de los metadatos. Los commits originales siguen existiendo hasta que dejan de ser alcanzables (SE-193): el registro de movimientos (reflog) permite recuperarlos.

Esa reescritura explica la regla central de SE-195: **rebasar solo ramas propias no publicadas, o ramas acordadas**. Si otra persona ya tiene los commits originales, tras el rebase tendrá commits «duplicados» con otro nombre, y al integrar aparecerán dos versiones del mismo trabajo. Un segundo problema es la repetición: una rama que vive semanas y se rebasa varias veces repite los mismos conflictos; `rerere` (reutilizar resoluciones registradas) ahorra la decisión, pero la rama larga es el problema de fondo (SE-197).

La clase insiste en elegir la estrategia por la rama y documentarla (squash para ramas cortas de intención única, fusión cuando importa quién hizo qué, rebase para correcciones urgentes antes de la revisión), en lugar de aplicar una sola a todo, porque se pierde la información que alguna rama sí necesitaba.

## Ejemplo

Una rama `arreglo-plazo` con tres commits sale de `main` en el commit A; mientras tanto `main` avanza a D. Un `git rebase main` reaplica los tres commits sobre D, creando tres commits nuevos (B', C', E'). Si el compañero ya había descargado los originales, ahora ve B, C y E junto a B', C' y E' tras un merge. Con el comando `git pull --rebase` sobre una rama propia no publicada, el mismo proceso es seguro. (Ilustración del mecanismo de Git.)

## Errores y confusiones comunes

- **Commits duplicados tras un rebase**: se rebasó una rama que otra persona ya tenía; corrección: rebasar solo ramas propias no publicadas o acordadas.
- **Un conflicto que reaparece**: la rama vive mucho y se repite el rebase; corrección: acortar la rama o activar `rerere` y revisar las resoluciones.
- **Rebasar `main` o ramas compartidas.**
- **Confundirlo con fusión**: la fusión conserva la forma de la bifurcación y no reescribe commits.

## Límites y cuándo no aplica

Reescribir historia ya publicada obliga a empujes forzados y a coordinar con el equipo. El rebase pierde la información de cuándo se integró cada línea de trabajo. En una rama con commits atómicos que alguien podría querer bisecar, conviene conservarlos (integrar sin squash). Para ramas de vida corta con intención única, el squash suele ser más simple que el rebase.
