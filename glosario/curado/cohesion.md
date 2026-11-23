# Cohesión

## Definición

La **cohesión** es el grado en que los elementos de un módulo cambian juntos y se entienden juntos (`SE-301`). Para una clase, `SE-317` la expresa como el grado en que lo que hace la clase tiene un propósito común, y `SE-322` la reduce a una medida: la fracción de pares de métodos que comparten estado. Las tres versiones son la misma idea con distinto nivel de precisión. El programa la usa como propiedad **observable** (cuántos lugares hay que tocar cuando una decisión cambia), no como un adjetivo de estilo como «limpio».

## Por qué importa

Una clase con poca cohesión cambia por varias razones a la vez: modificar la plantilla de un aviso obliga a releer el cálculo del costo. `SE-301` corrige el error de tratarla como una opinión: es una propiedad que se mide, de forma parcial y con límites conocidos. Esa medida permite discutir un diseño con datos y decidir qué separar antes de que el costo del cambio lo imponga.

## Cómo funciona

Un módulo es cohesivo cuando sus partes cambian juntas y se entienden juntas. En una clase, una forma operativa de mirarlo (`SE-301`) es ver qué métodos comparten atributos o se llaman entre sí: si forman un solo grupo conectado, la clase cuenta una sola historia; si forman varios, son varias clases con un nombre común. **LCOM4** cuenta esos grupos conectados. `SE-317` y `SE-322` usan una aproximación hermana: para cada par de métodos, ¿comparten algún atributo de la instancia?

La cohesión no pide clases pequeñas: pide que lo que se agrupa tenga un motivo común de cambio (`SE-301`). Y se contrapesa con el acoplamiento: bajar uno sin mirar el otro desplaza el problema (`SE-317` los presenta como criterios que tiran en direcciones opuestas).

## Ejemplo

En el experimento de `SE-317`, la clase `Servicio` tiene 10 métodos y 8 dependencias, y 37 de los 45 pares de métodos no comparten ningún atributo: es el síntoma clásico de baja cohesión. Al separar el servicio en tres clases pequeñas, la barra de pares sin estado compartido desaparece. En `SE-301`, una clase `Envio` con siete métodos se separa en `Precio`, `Aviso` y `Bitacora`, y se comprueba con LCOM4 de cada clase y con los sitios que hay que editar para el cambio previsto. Las clases y los números son sintéticos.

## Errores y confusiones comunes

- **Confiar solo en la métrica.** Un atributo común (`self.datos`) puede conectar todo y dar LCOM4 = 1 en una clase que sigue siendo un cajón de sastre; hay que revisar los motivos de cambio (`SE-301`).
- **Mover código sin separar decisiones.** Se mueve a otro archivo y no mejora nada porque se separó la ubicación, no la decisión; la pregunta es qué cambio se volvió local (`SE-301`).
- **Equiparar cohesión con tamaño.** Una clase de dos métodos que no se tocan es pequeña y tiene LCOM4 = 2 (`SE-301`).

## Límites y cuándo no aplica

«No comparten atributos» es una aproximación a la falta de cohesión: dos métodos pueden estar cohesionados por el dominio sin tocar el mismo atributo, y un atributo compartido puede ser accidental (`SE-317`). LCOM4 no distingue una clase con tres responsabilidades de una con tres métodos sencillos que simplemente no comparten atributos, y sube o baja con la densidad de uso de los atributos (`SE-301`). La medida orienta la conversación; la decisión se toma mirando un cambio probable y su costo.
