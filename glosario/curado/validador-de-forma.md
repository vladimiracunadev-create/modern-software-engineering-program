# Validador de forma

## Definición

Un **validador de forma** es un programa que comprueba la estructura y las referencias de un dosier, no su sentido. `SE-408` (proyecto: plataforma mínima reproducible) lo define como un comprobador que decide si un paquete está completo y es coherente en su estructura, sin interpretar su contenido; `SE-276` lo describe como un programa que comprueba la estructura de un documento sin entender su sentido; `SE-336` lo usa en el dosier de arquitectura.

## Por qué importa

Impide dosieres rotos sin pretender evaluarlos. Es barato y se ejecuta en cada cambio. Pero conviene no confundir un validador en verde con un dosier correcto: detecta lo estructural y deja pasar lo que exige interpretar.

## Cómo funciona

`SE-336` enumera reglas típicas de un validador:

- Identificadores únicos.
- Referencias que existen.
- Umbrales numéricos con unidad.
- Al menos dos alternativas por ADR.
- Estados válidos.
- Vistas con los mismos componentes.
- **Cobertura:** todo driver tiene un escenario, todo escenario una decisión, y todo escenario alto una función de aptitud o una excepción.

Son reglas locales y de referencia que un programa puede comprobar mecánicamente. Su límite está en el nombre: valida la *forma*. No sabe si un umbral es razonable, si una función de aptitud comprueba lo que dice o si una decisión contradice a otra. Para esas cosas hace falta revisión humana. Esta división de trabajo (máquina para lo estructural, personas para el sentido) es la que sostiene la entrega.

## Ejemplo

En `SE-336`, el equipo entrega `architecture-dossier/` con un `modelo.yaml` del que se generan las cuatro vistas, doce escenarios y cuatro ADR. El validador comprueba que cada driver tenga escenario y que cada escenario alto tenga función de aptitud. En `SE-276`, el paquete del dispositivo pasa su validador y aun así puede fallar en la flota si falta una regla de sentido.

## Errores y confusiones comunes

- **El paquete pasa el validador y falla en la flota:** validador de forma sin reglas de sentido; corrección, reglas de sentido y revisión humana (`SE-276`).
- **Tomar «validado» por «correcto».**
- **Un dosier completo con afirmaciones sin evidencia** (`SE-300`).
- **Añadir reglas que parecen de sentido pero solo comprueban presencia.**

## Límites y cuándo no aplica

Cuanto más rica la estructura, más útil el validador; para documentos sin estructura formal, no hay mucho que comprobar. Y no sustituye las pruebas del comportamiento del sistema descrito. Agregar reglas de sentido tiene un límite: lo que requiere juicio queda en manos de personas.
