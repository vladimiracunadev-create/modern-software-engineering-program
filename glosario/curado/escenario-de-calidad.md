# Escenario de calidad

## Definición

Un **escenario de calidad** es la formulación estructurada de un atributo de calidad con seis partes: **fuente** del estímulo, **estímulo**, **artefacto**, **entorno**, **respuesta** y **medida de la respuesta** (`SE-147`, `SE-433`, `SE-325`, `SE-337`). `SE-007` lo resume como situación y respuesta medible. Convierte un adjetivo («rápido», «seguro») en una frase que puede probarse.

## Por qué importa

Un requisito como «el sistema debe ser seguro» no se puede probar (`SE-433`). Sin escenario, dos personas creen cumplir lo mismo con sistemas distintos, y las decisiones de arquitectura se toman sin saber qué atributo importa y cuánto. Con escenarios, el equipo ordena qué atributos dominan el diseño y qué pruebas lo verifican (`SE-325`, `SE-337`).

## Cómo funciona

Cada parte elimina una ambigüedad (`SE-147`, `SE-433`):

- **fuente:** una persona, otro sistema, un fallo;
- **estímulo:** qué ocurre;
- **artefacto:** qué parte del sistema se ve afectada;
- **entorno:** en qué condiciones (carga, datos, modo de operación);
- **respuesta:** qué hace el sistema;
- **medida:** el estadístico, el umbral y la unidad que permiten decidir.

Sin entorno, «p95 ≤ 300 ms» se cumple con un usuario y se rompe con doscientos; sin estadístico, «300 ms» puede ser media o máximo; sin unidad, puede ser milisegundos o segundos. La medida es lo que hace al escenario falsable: si no se puede medir, aún no es un escenario.

## Ejemplo

`SE-147`: «Cuando una estudiante (fuente) abre su borrador (estímulo) en la aplicación web (artefacto) con 200 usuarios activos (entorno), el sistema lo muestra (respuesta) en menos de 1,5 s en el percentil 95 de las aperturas diarias (medida)». Se puede convertir directamente en una prueba de carga con ese entorno y ese umbral.

## Errores y confusiones comunes

- **El tablero está verde y la gente se queja.** Causa: el objetivo usa la media y la cola concentra el daño; corrección: fijar percentil y fracción de peticiones, y vigilar la cola (`SE-147`).
- **Se cumple el 99,9 % anual con un mes catastrófico.** Causa: la ventana anual diluye una caída larga; corrección: declarar la ventana (mensual) o añadir un tope de caída continua (`SE-147`).
- **Escribir seis partes de relleno.** Una medida vaga («rápido») invalida el escenario.

## Límites y cuándo no aplica

El formato de seis partes es una convención del programa, tomada del trabajo sobre arquitectura; no es la única forma de expresar atributos. Los números de `SE-147` son de la plataforma de entregas (datos sintéticos): no se midió ningún sistema real. Un escenario sin entorno realista puede dar falsa seguridad, y demasiados escenarios sin prioridad paralizan el diseño.
