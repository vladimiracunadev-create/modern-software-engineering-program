# Fusión de tres vías

## Definición

La **fusión de tres vías** (*three-way merge*) es la combinación de dos puntas de rama respecto de su ancestro común, que crea un commit con dos padres. Es el sentido de `SE-195` (ramas, integración, rebase y conflictos). Se llama «de tres vías» porque intervienen tres versiones: la base y las dos puntas.

## Por qué importa

Cambia qué queda registrado en la historia. Según `SE-195`, combina dos cambios respecto de una base común y conserva la forma de la bifurcación: se ve que hubo dos líneas de trabajo, quién hizo qué y cuándo. Frente a alternativas como el squash o el rebase, es la integración que no reescribe nada.

## Cómo funciona

Git compara cada punta con el ancestro común. Lo que cambió solo en un lado se toma tal cual; lo que cambió en ambos lados en lugares distintos se combina automáticamente. Si ambos cambiaron el mismo lugar, Git no decide: deja marcas de conflicto para que una persona resuelva. El resultado es un commit de fusión con dos padres, que fija en la historia el momento de la integración.

La elección de estrategia es una decisión de equipo. En la plataforma de entregas de `SE-195`, las ramas de funcionalidad viven pocos días y se integran con *squash* porque cada una es un cambio de intención única. Las ramas de varias personas se integran con fusión para conservar quién hizo qué. Las correcciones urgentes se rebasan sobre `main` antes de la revisión. La regla está escrita en `CONTRIBUTING.md`, con una excepción: una rama con commits atómicos y comprobables que alguien podría querer bisecar se integra sin squash. Dos defectos típicos se asocian: commits duplicados tras un rebase de una rama que otra persona ya tenía, y un conflicto que reaparece cuando la rama vive mucho tiempo.

## Ejemplo

Dos personas parten de la misma base. Una cambia la función de cálculo; otra, el texto de ayuda de otro archivo. La fusión de tres vías toma ambos cambios sin conflicto y crea un commit con dos padres. Si ambas hubieran tocado la misma línea, Git dejaría marcas y la resolución sería manual.

## Errores y confusiones comunes

- **Commits duplicados tras un rebase.** Se rebasó una rama que otra persona ya tenía; rebasar solo ramas propias no publicadas o acordadas.
- **El mismo conflicto reaparece.** La rama vive demasiado; acortarla o activar `rerere` y revisar las resoluciones.
- **Creer que sin conflicto la fusión es correcta.** Dos cambios que no chocan textualmente pueden romper el comportamiento juntos.
- **Confundir fusión con rebase.** El rebase reescribe; la fusión añade un commit.

## Límites y cuándo no aplica

Genera un historial más ancho y difícil de leer cuando hay muchas ramas largas. Detecta conflictos textuales, no semánticos: una prueba tras la fusión sigue siendo necesaria. Los experimentos de `SE-195` usan repositorios temporales con datos sintéticos.
