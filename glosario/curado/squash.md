# Squash

## Definición

El **squash** es una integración que reduce los cambios de una rama a un solo commit nuevo en la rama de destino (SE-195). Los commits originales no entran en esa historia. Es una de las estrategias de integración, junto con la fusión (merge) y el rebase.

## Por qué importa

Da una historia lineal con una entrada por cambio y descarta los pasos intermedios. Cambia cómo se lee y se recorre el historial: cada commit de la rama principal cuenta un cambio completo. A cambio, se pierde la granularidad que sirve para una bisección fina.

## Cómo funciona

Un squash junta todos los cambios de una rama en **un solo commit nuevo** en la rama de destino. Los commits originales de la rama quedan fuera de la historia principal (siguen existiendo en la rama mientras no se borre). El mensaje del commit nuevo resume el cambio, y la plataforma suele conservar el enlace al pull request.

SE-195 lo sitúa donde conviene: cuando los pasos intermedios son **ruido** (commits tipo «arreglo», «otro intento», «corrijo typo»), no cuando **cada uno es atómico y comprobable**. En la plataforma de entregas, las ramas de funcionalidad viven pocos días y se integran con squash porque cada una es un cambio de intención única; las ramas de varias personas se integran con fusión para conservar quién hizo qué; y las correcciones urgentes se rebasan sobre `main`. La regla está escrita en `CONTRIBUTING.md`, con una excepción: una rama con commits atómicos y comprobables que alguien podría querer bisecar se integra sin squash.

La causa del problema que evita es de legibilidad; la del problema que crea, de información: al aplastar, se pierden el orden de los pasos y la autoría individual de cada uno, y la bisección solo puede señalar el commit aplastado, que puede ser muy grande. El síntoma que la clase asocia: se pierde la historia de una rama porque se hizo squash de commits atómicos; se elige la estrategia por rama y se documenta la excepción.

## Ejemplo

Una rama de tres días con seis commits («wip», «arreglo test», «renombro», «fix real», «formato», «corrijo mensaje») se integra con squash en un solo commit «fix(penalizacion): aplicar el tope en el redondeo (#42)». La rama principal gana una entrada limpia. En cambio, una rama con cuatro commits atómicos («refactor», «prueba», «fix», «docs») conviene integrarla sin squash para poder bisecar el «fix». (Ilustración de la regla de SE-195.)

## Errores y confusiones comunes

- **Perder la historia de una rama** de commits atómicos al aplastarla.
- **Aplicar una sola estrategia a todas las ramas.**
- **Confundirlo con rebase**: el rebase conserva los commits, reescritos; el squash los reduce a uno.
- **Mensaje del squash genérico** que no explica el cambio.

## Límites y cuándo no aplica

No conviene cuando se necesita bisecar con precisión, cuando varias personas aportaron a la rama y se quiere conservar la autoría, o cuando la rama es grande y mezcla intenciones (es mejor dividirla antes). Si los commits intermedios ya son limpios, el squash no aporta.
