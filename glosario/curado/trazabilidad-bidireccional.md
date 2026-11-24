# Trazabilidad bidireccional

## Definición

La **trazabilidad bidireccional** es la capacidad de seguir un elemento hacia su origen y hacia su implementación y verificación (SE-151). SE-450 la formula para sistemas con peligros: vínculos de peligros a requisitos a pruebas y de vuelta.

## Por qué importa

Permite saber por qué existe algo y qué cubre cada prueba. Una sola dirección deja puntos ciegos: sin la trazabilidad hacia atrás, hay trabajo que nadie pidió; sin la de adelante, hay promesas que nadie comprueba. Cambia lo que una auditoría o una revisión puede responder.

## Cómo funciona

**Hacia atrás**, la trazabilidad responde «¿de dónde viene este requisito?»: necesidad, entrevista, norma. Detecta **requisitos sin origen** (trabajo que nadie pidió). **Hacia adelante** responde «¿qué lo implementa y cómo se verifica?»: diseño, código, prueba. Detecta **requisitos sin evidencia** (promesas que nadie comprueba). Ambas direcciones son necesarias.

SE-450 la cuantifica con un ejemplo: con 30 requisitos y 45 pruebas generados con semilla 47, **9 requisitos quedan sin ninguna prueba y 2 pruebas sin requisito**. Son hallazgos antes de que cualquier regulador los pregunte: los 9 son promesas sin comprobar, y las 2 son pruebas huérfanas, que quizá prueban algo que ya no se necesita. La clase añade que una trazabilidad que solo se construye al final suele fallar; la que se mantiene durante el desarrollo, con política de cambio, funciona.

Para que no se vuelva una matriz muerta, SE-151 propone poner una **etiqueta** en cada artefacto y verificar al integrar que los enlaces existen en ambas direcciones. Con una granularidad adecuada de enlaces (requisito–prueba–módulo, no línea de código), la matriz responde preguntas reales. Y se distingue el enlace de la evidencia: que la prueba esté enlazada no prueba que verifique el requisito.

En el sentido de SE-450, el recorrido incluye los **peligros**: de un peligro identificado se llega a los requisitos que lo mitigan y a las pruebas que lo verifican, y a la inversa, de una prueba se sube al requisito y al peligro que cubre.

## Ejemplo

Hacia adelante: REQ-12 («un PDF de 10 MB se acepta y uno de 10,1 MB se rechaza») → TST-31, TST-32. Hacia atrás: TST-33 → REQ-15 → entrevista E-04 con docentes. Un verificador al integrar lista: «REQ-19 sin prueba», «TST-40 sin requisito». Esos dos son los hallazgos que la trazabilidad bidireccional exige corregir. (Ilustración con la lógica de SE-151 y SE-450.)

## Errores y confusiones comunes

- **Auditoría que tarda un día en encontrar una prueba**: matriz en un documento que nadie actualiza.
- **Casi todo cambio «afecta» a casi todo**: se enlazó todo con todo.
- **Mantener una sola dirección.**
- **Tomar el enlace por evidencia.**

## Límites y cuándo no aplica

Mantener la trazabilidad cuesta; en proyectos pequeños o de bajo riesgo una versión ligera basta. Los números de SE-450 son de una simulación con semilla fija y muestran el tipo de hallazgo, no una tasa real.
