# Evidencia de cumplimiento

## Definición

La **evidencia de cumplimiento** son los artefactos fechados que sostienen una afirmación de que se cumple una obligación (SE-152). SE-514 la formula como un registro verificable de un procedimiento de prueba, su criterio y su resultado. Cumplir es una afirmación; la evidencia es lo que la sostiene.

## Por qué importa

Una afirmación de cumplimiento vale lo que la evidencia que la sostiene. Una norma o un auditor no pide que el sistema sea seguro o resiliente: pide **evidencia de que los controles funcionan**. Cambia el diseño: un requisito necesita, desde su redacción, una forma de producir su evidencia, no solo una forma de cumplirse.

## Cómo funciona

SE-152 enumera ejemplos: la configuración vigente, el resultado fechado de una prueba, el registro del borrado. Una auditoría pregunta por ambas cosas, el control y la evidencia. Tres propiedades se piden a la evidencia: que pueda **generarse sin intervención heroica** (automática o con poco esfuerzo, no reconstruida a mano antes de la auditoría), que **no exponga datos personales** (el recuento de registros borrados por día, no los registros) y que sea **verificable por un tercero**.

Un requisito sin una forma de generar su evidencia cumplida es un requisito que no se puede demostrar. Por eso el síntoma «una auditoría pide evidencia del borrado y no hay» tiene como corrección definir la evidencia junto con el requisito, sin guardar contenido. También las excepciones de la regla (retención legal) deben incluirse en el requisito y en las pruebas.

SE-514 la sitúa en la resiliencia: el reglamento europeo DORA sobre resiliencia operativa digital del sector financiero incluye requisitos de gestión del riesgo de TIC y de pruebas de resiliencia, y la guía de planificación de contingencias del NIST trata la elaboración, la prueba y el mantenimiento de los planes. La clase aclara que no se aplican a la plataforma como obligaciones; sirven de marco para ver qué clase de evidencia piden. El paquete de cumplimiento se estructura con estado del requisito, control, prueba, evidencia, fecha, alcance y dueño, y la evidencia es el resultado ejecutable de una prueba, no una captura de pantalla.

## Ejemplo

Requisito: «los datos de entregas se borran a los 365 días». Evidencia: un informe diario generado por la tarea de borrado con el recuento de registros eliminados por día y la fecha de corte, más el resultado de una prueba que crea un registro de 366 días y comprueba que desaparece. No se guardan los registros borrados. Un auditor puede verificar el control sin ver datos personales. (Ilustración del tipo de evidencia de SE-152.)

## Errores y confusiones comunes

- **Pedir evidencia después**: se reconstruye a mano y no es fiable.
- **Evidencia con datos personales** que crea otro riesgo.
- **Capturas de pantalla** en lugar de resultados ejecutables.
- **Confundir control con evidencia**: el control actúa; la evidencia lo demuestra.

## Límites y cuándo no aplica

La evidencia demuestra que el control se aplicó en un momento, no que sea suficiente. Su generación tiene un costo que debe ponderarse con la obligación. Si la obligación no aplica a la organización (como DORA para la plataforma del programa), la evidencia es un buen hábito, pero no una exigencia legal.
