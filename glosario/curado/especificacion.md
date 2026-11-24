# Especificación

## Definición

Una **especificación** es el texto acordado de lo que el sistema debe hacer, escrito para que pueda construirse, probarse y auditarse sin preguntar a su autor (`SE-145`). `SE-565` la precisa para el trabajo con agentes: documento versionado que declara qué comportamiento observable debe tener un sistema y por qué, con requisitos identificables y criterios comprobables. `SE-060` la reduce a una descripción verificable de comportamiento y restricciones.

## Por qué importa

Es el punto donde un deseo se vuelve contrato. Sin ella, quien construye, quien prueba y quien audita trabajan con tres lecturas distintas. Con agentes que implementan (`SE-565`) importa más: lo que no está especificado lo decide la máquina, y la entrega puede «funcionar» y no ser lo pedido.

## Cómo funciona

`SE-145`, siguiendo a Zave y Jackson, separa tres cosas que suelen mezclarse:

- **Requisito:** lo que se quiere en el mundo («la estudiante recupera su trabajo»).
- **Supuestos del dominio:** lo que se cree del mundo («la sesión dura 30 minutos y el navegador conserva el almacenamiento local»).
- **Especificación:** lo que el sistema hará («guardará el borrador cada 30 s»).

El programa satisface el requisito solo si especificación y supuestos, juntos, lo implican. Si un supuesto es falso (el navegador borra el almacenamiento al cerrar), la especificación puede cumplirse al pie de la letra y el requisito no. De ahí dos prácticas: listar los supuestos con responsable y forma de comprobarlos, y escribir los criterios en la especificación *antes* de implementar (`SE-565`).

## Ejemplo

Requisito: la estudiante recupera su trabajo. Supuesto: el almacenamiento local persiste. Especificación: guardado cada 30 s en el servidor y en el navegador. Si el supuesto falla, el servidor sigue conservando el borrador: la especificación cubre el caso porque no depende de un solo supuesto. Ilustración de criterio comprobable:

```text
REQ-12: tras cerrar y reabrir, el borrador coincide con el último guardado (<= 30 s de antigüedad).
```

## Errores y confusiones comunes

- **Especificación completa y sistema que decepciona.** Causa: solo se entrevistó a quien paga y no se elicitó el conocimiento tácito; corrección: observar el trabajo real y validar con quien usa (`SE-145`).
- **Cumple la especificación y falla en producción.** Causa: un supuesto falso que nadie escribió; corrección: listar supuestos (`SE-145`).
- **Pruebas que pasan con otro comportamiento.** Causa: las escribió quien implementó, desde su propia lectura; corrección: criterios en la especificación antes de implementar (`SE-565`).

## Límites y cuándo no aplica

Un documento de requisitos que nadie compara con el sistema es una especificación en el nombre, no en la práctica (`SE-565`). En exploración temprana, especificar en detalle algo que se está descubriendo cuesta más de lo que protege. Y ninguna especificación es completa: dónde se detiene es una decisión, y lo omitido queda delegado.
