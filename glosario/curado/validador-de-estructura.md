# Validador de estructura

## Definición

Un **validador de estructura** es un programa que comprueba propiedades mecánicas de una especificación y falla con un mensaje identificable (SE-156). Comprueba lo que una máquina puede decidir, sin entender el contenido.

## Por qué importa

Detecta defectos mecánicos y barre lo repetitivo antes de la revisión humana, de modo que las personas lean lo que importa. Cambia la división del trabajo de revisión: la máquina garantiza que la especificación esté bien formada; las personas juzgan si es correcta.

## Cómo funciona

El validador comprueba propiedades que se pueden decidir mecánicamente: **identificadores únicos**, **referencias que existen** (un requisito que cita otro inexistente), **campos obligatorios** (origen, criterio, dueño, prioridad), **valores de una escala**, **ausencia de ciclos** en las dependencias y **marcadores** como «por definir». Cada fallo se acompaña de un mensaje identificable (qué requisito, qué regla), para que se corrija sin buscar.

El límite está en la primera frase de la clase: no entiende el contenido. **Una especificación que pasa el validador no está bien: está bien formada.** Puede contener contradicciones, ambigüedades o requisitos equivocados con todos los campos llenos. Por eso SE-156 propone medir qué cubre el validador con **mutaciones**: se inyectan defectos conocidos en una especificación base (la clase usa 16) y se cuenta cuántos detecta. Los que sobreviven revelan qué no ve, y eso se documenta y se completa con revisión humana. La clase lo conecta con el contenido de una especificación: el validador comprueba que estén los elementos, no que sean buenos.

Los datos de SE-156 son supuestos del autor (la especificación base, las 16 mutaciones, los costos y las probabilidades de detección), y la lista de palabras vagas es un ejemplo mínimo.

## Ejemplo

Una especificación con 20 requisitos. El validador comprueba que cada uno tenga identificador único, origen, criterio de aceptación, dueño y prioridad; que las referencias de dependencia apunten a requisitos existentes; que no haya ciclos; y que ningún texto contenga «por definir». Si un requisito cita `REQ-31` y no existe, falla con «REQ-14: dependencia REQ-31 inexistente». Si dos requisitos son contradictorios pero bien formados, pasa. (Ilustración del tipo de comprobaciones de SE-156.)

## Errores y confusiones comunes

- **El validador pasa y hay errores graves**: solo comprueba estructura; corrección: documentar su cobertura con mutaciones y completar con revisión humana.
- **Pensar que «verde» significa «correcta».**
- **Mensajes de fallo ambiguos** que obligan a buscar.
- **Confundirlo con un linter de estilo de prosa**: este comprueba la estructura formal, no la redacción.

## Límites y cuándo no aplica

No detecta contradicciones, ambigüedades ni huecos de contenido (para eso hay técnicas de detección específicas). Requiere que la especificación tenga una estructura regular (formato legible por máquina). En especificaciones muy breves o informales, el costo de mantener el validador supera su beneficio.
