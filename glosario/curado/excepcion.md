# Excepción

## Definición

**Excepción** tiene dos sentidos que el programa mantiene separados:

- **En el código** (`SE-065`): un objeto que señala una interrupción anormal del flujo.
- **En gobernanza** (`SE-552`, `SE-468`): un cambio o incumplimiento que no sigue la política, aceptado con **dueño, razón y fecha de vencimiento**. `SE-414` la usa para un cambio de un derecho a un cliente, con vencimiento y autorización.

## Por qué importa

En código, decide cómo se comunica un fallo: por una interrupción del flujo o por un resultado esperado. En gobernanza, decide si una política es real: sin excepciones registradas, la política se incumple en silencio; con excepciones sin dueño ni fecha, se convierten en la regla. `SE-552` lo resume: una política que nadie comprueba es una intención.

## Cómo funciona

- **Código** (`SE-065`): cuando ausencia o rechazo es parte esperada del dominio, un resultado etiquetado evita usar excepciones como control ordinario (por ejemplo, `{'ok': False, 'error': ...}` o `Result<T,E>` en Rust). Un resultado como `DNS_TIMEOUT` puede ser un dato normal del diagnóstico y no una excepción. Al traducir una excepción hay que conservar la causa con `raise ... from e`.
- **Política** (`SE-552`): las excepciones se registran con dueño y fecha, se revisan periódicamente y se comprueban mecánicamente donde se pueda (por ejemplo, el comprobador de forma o el contrato en integración continua).
- **Derechos** (`SE-414`): una excepción de un cliente (más cupo, una función habilitada) tiene vencimiento y autorización; sin ellos, el modelo de derechos se llena de casos sueltos.

## Ejemplo

```python
try:
    resolver(nombre)
except socket.gaierror as e:
    raise ErrorDeDiagnostico("fallo de resolución") from e   # conserva la causa
```

En gobernanza (`SE-468`): «incumplimiento aceptado: cifrado en reposo del bucket X, dueño: plataforma, razón: migración en curso, vence: 2026-06-30».

## Errores y confusiones comunes

- **El mensaje final no menciona el fallo original.** Causa: se tradujo la excepción sin `from`; corrección: `raise ... from e` (`SE-065`).
- **Excepciones de política sin vencimiento.** Se vuelven permanentes y la política deja de ser cierta.
- **Usar excepciones para el flujo ordinario.** Cuando el rechazo es esperado, un resultado etiquetado es más claro.

## Límites y cuándo no aplica

No todo error de dominio es una excepción de código (`SE-065`). Un modelo de derechos con muchas excepciones indica que el modelo propio de la base de clientes sería más claro (`SE-414`). Y una excepción de política aprobada no reduce el riesgo: solo lo hace explícito y con dueño.
