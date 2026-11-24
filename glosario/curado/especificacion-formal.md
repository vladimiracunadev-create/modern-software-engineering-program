# Especificación formal

## Definición

Una **especificación formal** es una descripción en una notación con semántica definida, ejecutable o comprobable por una herramienta, en un dominio acotado o con una demostración (SE-157). Es el nivel más riguroso de una escala que empieza en la especificación informal (prosa) y pasa por la semiformal (estructura comprobable).

## Por qué importa

Un predicado sin ambigüedad se comprueba mecánicamente, a cambio de esfuerzo y de leerse con dificultad. Cambia lo que se puede afirmar de una implementación: no «cumple, según las pruebas que escribimos» sino «coincide con la referencia en todo el dominio acotado». Para reglas de alto riesgo es la diferencia entre un acuerdo aparente y una comprobación.

## Cómo funciona

SE-157 ejemplifica con la penalización de la plataforma de entregas: `nota_final(n, h) = redondear(n · (1 − min(0,10 · ⌈h/24⌉, 0,50)))` para `h > 0`. Esta fórmula **no admite lecturas**: fija el redondeo, el tope (50 %), la unidad de retraso (bloques de 24 horas, redondeando hacia arriba) y el cálculo del número de días.

Su valor principal es que **se ejecuta**: el predicado se transforma en una **función de referencia** con la que comparar cualquier implementación en todo un dominio acotado (por ejemplo, todas las notas de 0 a 100 en saltos de uno y todos los retrasos de 1 a 200 horas). La comparación exhaustiva encuentra diferencias que ninguna prueba de ejemplos habría buscado.

El coste es **doble**: escribirlo exige acordar antes todos los puntos abiertos (qué es un día, cómo se redondea, cuál es el tope), y leerlo exige formación; quien decide la política puede no entender la fórmula. Por eso la plataforma publica la regla en tres artefactos coordinados: prosa en la política académica (una frase con los cuatro términos definidos), tabla de decisión en el documento de diseño y predicado en una función de referencia con sus pruebas.

La clase aclara dos límites: la especificación formal da la referencia contra la que se prueba, pero **hay que ejecutar esa comparación**; y **no protege de especificar lo que nadie quería**: el predicado es exacto y podría ser el equivocado.

## Ejemplo

Con la función de referencia anterior, un equipo compara su implementación de producción para h de 1 a 200 y n de 0 a 100: 20.100 casos. La comparación revela que la implementación redondea hacia abajo con 24 h exactas (cuenta un día menos), una diferencia que las pruebas de ejemplos típicos no cubrían. (Ilustración construida sobre el predicado de SE-157.)

## Errores y confusiones comunes

- **Creer que formal implica correcta**: el predicado puede ser exacto y equivocado.
- **No ejecutar la comparación.**
- **Formalizar todo**: el costo no se justifica para reglas simples o de bajo riesgo.
- **Dos sistemas dan notas distintas y ambos «cumplen»**: sin predicado, la política admite varias lecturas.

## Límites y cuándo no aplica

Solo comprueba el dominio acotado que se ejecuta; fuera de él no hay garantía salvo una demostración. Exige capacidades específicas del equipo y tiempo. Para requisitos de interfaz o de experiencia de usuario, una notación formal rinde poco.
