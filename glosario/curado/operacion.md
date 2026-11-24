# Operación

## Definición

**Operación** tiene dos sentidos en el programa que importa distinguir:

- **Fase del ciclo de vida** (`SE-003`): la etapa en la que el software sirve a quienes lo usan, con niveles de servicio y respuesta. Informa nuevos requisitos y no es el final del producto.
- **Acción individual que un sistema ejecuta** (`SE-040`, `SE-048`): una llamada, una escritura, un cobro; sobre todo cuando importa si puede repetirse sin daño.

## Por qué importa

Tratar la entrega como final del producto deja a la operación, al soporte y a los usuarios con el trabajo invisible (`SE-003`). Y en el sentido de acción, repetir una operación tras un timeout puede duplicarla: el timeout no prueba que no se ejecutó (`SE-040`). Cambia qué se diseña antes del despliegue (responsables, niveles de servicio, retiro) y qué contrato tiene cada acción (idempotencia).

## Cómo funciona

**Fase** (`SE-003`): un ciclo profesional conserva bucles. Lo aprendido al operar corrige requisitos; una dificultad de retiro revela una decisión de diseño pendiente. Cambiar un proveedor de correo, por ejemplo, involucra a producto (experiencia), ingeniería (contrato), seguridad (secretos), soporte (comunicación), operaciones (observación) y legal (conservación), y el retiro revoca las credenciales antiguas.

**Acción** (`SE-040`, `SE-048`): ante un fallo, un cliente no sabe si la operación se ejecutó o no. Reintentar una operación que no es idempotente produce peticiones duplicadas. Por eso se exige idempotencia, claves de idempotencia o consulta previa del estado, y un plazo finito con una salida diagnóstica que indique la fase donde falló, sin repetir automáticamente.

## Ejemplo

```text
POST /cobros  (Idempotency-Key: 7f3a...)
-> primera vez: cobra y guarda resultado
-> reintento con la misma clave tras un timeout: devuelve el resultado guardado, no cobra otra vez
```

Para la fase, `SE-003` pide añadir al ciclo operación, evolución, conservación y retiro con responsables.

## Errores y confusiones comunes

- **El ciclo termina en el despliegue.** Causa: se definió entrega como final del producto; corrección: añadir operación, evolución, conservación y retiro con responsables (`SE-003`).
- **Peticiones duplicadas tras un timeout.** Causa: se reintentan operaciones no idempotentes; corrección: claves de idempotencia o consulta previa del estado (`SE-048`).
- **Reintentar un cobro.** El timeout no prueba que no se ejecutó (`SE-040`).

## Límites y cuándo no aplica

Si el equipo dice «terminado» sin decir cuál criterio, el trabajo restante queda invisible y suele caer sobre operación, soporte o usuarios (`SE-003`). En software de un solo uso o desechable, la fase de operación es mínima. Y la idempotencia no se logra con reintentos automáticos: requiere un diseño explícito de la operación.
