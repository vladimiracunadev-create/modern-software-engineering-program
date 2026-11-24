# Mutación

## Definición

Una **mutación** es un cambio malo inyectado deliberadamente para probar un control (SE-372). El programa usa el término con el mismo núcleo en varios contextos: copia de un árbol de métricas con un defecto conocido para evaluar un validador (SE-143), cambio deliberado de un defecto en una especificación válida para medir qué detecta el validador (SE-516, SE-144), cambio deliberado de una respuesta para comprobar si una comprobación lo detecta (SE-244). Es la unidad de la prueba de mutación.

## Por qué importa

Un control que nunca ha fallado no se sabe si funciona. Un validador que siempre da verde puede estar ciego. La mutación lo comprueba introduciendo defectos conocidos y viendo si el control los detecta. Cambia la confianza que se puede tener: de «el validador pasa» a «el validador detecta estos N tipos de defecto».

## Cómo funciona

SE-372 prueba un control como se prueba un detector: **con incidentes sembrados**. Las diez mutaciones del proyecto de la clase son defectos concretos sobre un registro de metadatos de datos: quitar el dueño; añadir una columna al mart sin actualizar el contrato; exponer una columna de correo en el mart (actualizando el contrato, para que otra regla no la vea); declarar una retención de 10 días sin purga; quitar todas las comprobaciones de un conjunto; hacer que el mart lea de la capa cruda sin pasar por la capa intermedia; entre otras. Para cada mutación, se ejecuta el control y se anota si la detecta.

El resultado es una **tabla de cobertura**: qué defectos ve el control y cuáles no. Las mutaciones no detectadas señalan huecos del control o mutantes equivalentes (que no cambian nada observable). En la práctica, el equipo de la clase ejecuta las diez mutaciones cada trimestre como prueba del propio control: si un cambio de reglas deja de detectar alguna, la prueba falla y el cambio no entra. Cuando ocurre un incidente real que el control no vio, se añade una mutación inspirada en él.

El mismo mecanismo sirve para validadores de especificaciones (SE-516, SE-144: 16 mutaciones sobre una especificación base) y de árboles de métricas (SE-143). En todos los casos la mutación es **un cambio pequeño, conocido y malo**, y la medida es cuántos detecta el control.

## Ejemplo

Una especificación base válida se copia 16 veces; en cada copia se introduce un defecto distinto (un requisito sin dueño, una referencia a un requisito inexistente, un ciclo de dependencias, etc.). El validador se ejecuta sobre cada copia: detecta 13 de 16. Los 3 que no detecta son huecos documentados que se cubren con revisión humana. (Escenario construido con el método de SE-516.)

## Errores y confusiones comunes

- **Creer que un validador verde significa especificación sana**: solo comprueba lo que sabe comprobar.
- **Elegir mutaciones fáciles** que el control detecta de sobra.
- **Contar equivalentes como fallos del control.**
- **No ejecutarlas de forma periódica**: el control se degrada con los cambios.

## Límites y cuándo no aplica

Las mutaciones las elige el autor, de modo que la cobertura medida es sobre ese conjunto, no sobre todos los defectos posibles. Su valor depende de que representen defectos reales. No reemplazan la revisión humana ni las pruebas con datos reales.
