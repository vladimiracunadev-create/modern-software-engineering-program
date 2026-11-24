# Criterio de salida

## Definición

Un **criterio de salida** es la condición comprobable que debe cumplirse para dar un trabajo por terminado o para avanzar a la etapa siguiente (`SE-492`). Según el contexto: condición verificable para avanzar (`SE-012`) o condición observable para cerrar una fase (`SE-059`). Lo esencial es que lo pueda verificar alguien distinto de quien hizo el trabajo.

## Por qué importa

Sin criterio de salida, «terminado» es una sensación. El trabajo se declara completo por cansancio, por calendario o por completar actividades en vez de resultados. `SE-012` lo muestra en el aprendizaje profesional: el criterio no es «sentirme experto» sino una observación que una persona revisora puede verificar. En entrega continua (`SE-492`), cada etapa tiene criterio de paso o de retroceso, y eso es lo que permite automatizar la decisión.

## Cómo funciona

Un buen criterio es **observable, binario y externo**:

- *observable:* se puede medir o inspeccionar, no depende de opinión;
- *binario:* se cumple o no;
- *externo:* lo verifica otra persona o un sistema, no solo el autor.

`SE-012` pide para cada experimento un artefacto, un criterio de salida y una revisión, y limita el trabajo en curso para no acumular diez cursos sin evidencia. En `SE-492`, el camino de entrega encadena criterios: ramas de menos de dos días, compuertas ordenadas por razón de detección, escaneo de secretos que siempre bloquea, canario del 5 % con criterio de retroceso automático y observación de métricas con intervalos. Cada paso responde a la pregunta «¿qué debe ser verdad para pasar?».

## Ejemplo

`SE-492`: un canario del 5 % tiene un criterio de retroceso automático; si la métrica cruza el umbral, la versión se retira sin pedir permiso. Ilustración de formulación débil frente a fuerte:

- Débil: «el módulo está casi listo».
- Fuerte: «las 12 pruebas de aceptación pasan en CI y una segunda persona revisó el diff».

## Errores y confusiones comunes

- **«Completar un curso» como criterio de salida.** Causa: consumo confundido con desempeño; corrección: exigir tarea, evidencia y revisión externa (`SE-012`).
- **Criterio que depende de una opinión.** No puede automatizarse ni discutirse.
- **Confundir criterio de salida con criterio de aceptación.** El primero cierra una fase o etapa; el segundo valida un requisito concreto.

## Límites y cuándo no aplica

Un criterio verificable puede medir lo equivocado y dar falsa seguridad (cumplir el umbral sin cumplir el objetivo). En trabajo exploratorio, fijar un criterio demasiado temprano puede cerrar preguntas; entonces el criterio es una decisión (avanzar, repetir, dividir o cambiar estrategia, `SE-012`) más que un umbral. Y un criterio que nadie revisa es solo un texto.
