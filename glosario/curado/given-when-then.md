# Given-When-Then

## Definición

**Given-When-Then** (Dado–Cuando–Entonces) es una forma de escribir un ejemplo como contexto, acción y resultado observable (SE-149, SE-158). Es la estructura de los escenarios del lenguaje Gherkin y de la especificación por ejemplos.

## Por qué importa

Estructura el ejemplo y permite automatizarlo. Un escenario escrito así lo puede leer una persona no técnica y ejecutar una herramienta. Cambia cómo se redactan los criterios de aceptación: de frases generales a escenarios concretos con un resultado verificable.

## Cómo funciona

La forma separa tres partes:

- **Dado** (el contexto): lo que ya era verdad, por ejemplo «una estudiante con sesión válida y un archivo de 10,1 MB».
- **Cuando** (la acción): lo que ocurre, «intenta entregarlo».
- **Entonces** (el resultado observable): lo que debe observarse, «ve el mensaje del límite y la entrega no se guarda».

SE-158 subraya que la utilidad **no es sintáctica**: obliga a separar lo que ya era verdad de lo que ocurre y de lo que debe observarse. Un escenario con dos acciones o con una verificación en el contexto suele indicar que son dos escenarios. Los pasos se redactan en el **lenguaje del dominio** («la entrega llega 30 horas tarde»), no en el de la interfaz.

Gherkin lo hace ejecutable: cada paso se vincula con código que prepara el contexto, ejecuta la acción y comprueba el resultado. Su riesgo, dice SE-149, es la **verbosidad**: escenarios que describen la interfaz clic por clic en lugar del comportamiento se rompen con cada cambio visual y nadie los mantiene. La corrección es escribir el comportamiento de negocio y dejar el detalle de interfaz para la implementación de los pasos.

Los escenarios sirven de criterios de aceptación y de fuente de casos de prueba. Los que se eligen deben incluir los **valores de frontera** (10 MB y 10,1 MB), no solo el camino típico.

## Ejemplo

```gherkin
Escenario: Archivo por encima del límite
  Dado una estudiante con sesión válida
  Y un archivo PDF de 10,1 MB
  Cuando intenta entregarlo
  Entonces ve un mensaje que indica el límite de 10 MB
  Y la entrega no se guarda
```

Un escenario gemelo con un archivo de exactamente 10 MB y resultado «la entrega se guarda» fija la frontera. (Escenario ilustrativo basado en el ejemplo de SE-149.)

## Errores y confusiones comunes

- **Las pruebas pasan y el cliente rechaza la entrega**: el criterio solo cubría ejemplos felices; corrección: añadir ejemplos en las fronteras y en clases no válidas.
- **Describir la interfaz clic por clic.**
- **Varias acciones en un escenario.**
- **Confundir la forma con el valor**: escribirlo en Gherkin no mejora un ejemplo mal elegido.

## Límites y cuándo no aplica

Para reglas con muchas combinaciones, una tabla de decisión es más compacta que decenas de escenarios. El mantenimiento de las definiciones de pasos es un costo real. Si nadie de negocio lee los escenarios, parte de su valor se pierde, y entonces puede bastar con pruebas automáticas normales.
