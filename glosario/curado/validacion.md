# Validación

## Definición

La **validación** es la comprobación, con las personas que tienen la necesidad, de que lo especificado es lo que se necesita (`SE-145`). `SE-003` la resume como utilidad en contexto. Contrasta con la **verificación**: validar es preguntar si el requisito es el correcto; verificar es preguntar si el sistema cumple el requisito.

## Por qué importa

Boehm lo resume como construir lo *correcto* frente a construirlo *correctamente* (`SE-145`). Un requisito puede estar perfectamente escrito, perfectamente verificado y perfectamente equivocado. Sin validación, un equipo entrega con rigor algo que nadie necesita. Cambia con quién se habla y qué se muestra antes de construir.

## Cómo funciona

La validación ocurre **con las personas que tienen la necesidad**: revisión de requisitos, prototipos, ejemplos concretos y observación del trabajo real. La verificación ocurre **contra el texto**: pruebas e inspecciones. `SE-145` pide un acta de validación que diga con quién se revisó, qué se mostró y qué se decidió, no solo «aprobado»; así se puede saber después si se validó con quien paga o con quien usa.

Una causa de fallo frecuente: solo se entrevistó a quien paga y el conocimiento tácito no se elicitó. La corrección es añadir observación del trabajo real y validar con la persona usuaria, no solo con el cliente. Otra: dos equipos discuten una frase durante una hora porque mezcla un requisito y una solución; se separan necesidad, requisito y supuesto y se registra el origen de cada uno.

## Ejemplo

```text
Acta de validación — REQ-12 "avisar antes del vencimiento"
Con: 3 docentes y 5 estudiantes | Se mostró: prototipo de avisos y 4 ejemplos reales
Se decidió: aviso a 48 h y 12 h; sin aviso nocturno | Pendiente: canal para estudiantes sin correo institucional
```

En contraste, `verificar` sería: la prueba automática confirma que se envía un aviso 48 h antes.

## Errores y confusiones comunes

- **La especificación está completa y el sistema decepciona.** Causa: solo se entrevistó a quien paga; corrección: observar el trabajo real y validar con la persona usuaria (`SE-145`).
- **Dos equipos discuten una frase durante una hora.** Causa: la frase mezcla requisito y solución; corrección: separar necesidad, requisito y supuesto y registrar el origen (`SE-145`).
- **Confundir validar con verificar.** Pasar todas las pruebas no valida nada sobre la necesidad.

## Límites y cuándo no aplica

No toda validación es posible antes de construir: algunas necesidades solo aparecen al usar el producto (`SE-003`: la operación informa nuevos requisitos). Validar con una muestra pequeña o no representativa da falsa seguridad. Y la palabra tiene otro uso técnico, la validación de entradas (formato, tipo), que es verificación contra reglas y no la validación de necesidades.
