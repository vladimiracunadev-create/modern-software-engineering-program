# Riesgo

## Definición

Un **riesgo** es, en el programa, un evento incierto que, si ocurre, afecta a lo que se persigue. La palabra cambia de escala según la clase, siempre con la idea de incertidumbre más consecuencia:

- **En un proyecto** (`SE-187`): un evento incierto futuro con una causa, un efecto, una probabilidad, un impacto, un disparador y una respuesta.
- **En la estrategia de pruebas** (`SE-421`): la pérdida esperada de un componente, estimada como probabilidad de defecto por impacto.
- **En sistemas críticos** (`SE-445`): la combinación de la gravedad de un daño posible y la probabilidad de que ocurra.
- **En una restricción de diseño** (`SE-008`): una cadena causal con señal, mitigación y contingencia; la clase advierte que un riesgo escrito como sustantivo («rendimiento») no sirve.

## Por qué importa

Decide dónde se gasta el esfuerzo limitado. `SE-421` usa el riesgo para priorizar pruebas: no todo componente merece la misma inversión, y la pérdida esperada ordena las decisiones. `SE-187` lo usa para gobernar un proyecto: Boehm propuso ordenar los riesgos por exposición, el producto de probabilidad y pérdida, y revisar la lista de los principales cada vez.

## Cómo funciona

Para que un riesgo sirva, se describe como cadena causal, no como etiqueta. `SE-187` pide escribirlo con una **causa**, un **evento** y un **efecto** («si el proveedor de identidad cambia su contrato, la integración se retrasa»), estimarlo con probabilidad e impacto y acompañarlo de un **disparador** (la señal de que se está materializando), una **respuesta** (reducir, evitar, aceptar o transferir) y un **responsable**. Se mantiene separado de otros registros: tareas (se hacen), problemas o *issues* (ya ocurrieron), supuestos (se creen) y decisiones. En una pérdida esperada (`SE-421`), la cuenta es probabilidad de defecto por impacto; en seguridad funcional (`SE-445`), se combinan gravedad y probabilidad para clasificar el daño posible.

## Ejemplo

En `SE-187`, «el proveedor de identidad cambia su contrato» tiene una causa (cambio del proveedor), un evento (cambio del contrato), un efecto (retraso de la integración), un disparador (aviso del proveedor), una respuesta y un responsable. En `SE-421`, un componente con alta probabilidad de defecto y alto impacto recibe más pruebas que uno de impacto bajo, aunque tenga el mismo tamaño.

## Errores y confusiones comunes

- **Una hoja de riesgos que mezcla tareas, problemas y creencias.** Todo se llama «riesgo»; corrección (`SE-187`): clasificar en cuatro registros con campos distintos.
- **La contingencia se agota con un único evento.** Riesgos con causa común tratados como independientes; corrección: registrar las causas comunes y reservar por percentil.
- **Un riesgo escrito como sustantivo.** Faltan causa y consecuencia; corrección (`SE-008`): formular cadena causal, señal, mitigación y contingencia.

## Límites y cuándo no aplica

Las tres definiciones no son intercambiables: la pérdida esperada de `SE-421` es una estimación numérica para priorizar pruebas, mientras que la combinación de gravedad y probabilidad de `SE-445` clasifica daños con normas de seguridad, donde el producto de números no basta por sí solo. Las cifras de probabilidad e impacto son estimaciones y la exposición de Boehm ordena, no predice. Al usar la palabra hay que confirmar a qué escala se refiere.
