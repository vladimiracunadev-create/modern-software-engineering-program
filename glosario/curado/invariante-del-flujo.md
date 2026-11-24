# Invariante del flujo

## Definición

Una **invariante del flujo** es una propiedad que debe cumplirse sin importar las fallas, por ejemplo que cada entrega tenga exactamente una calificación (`SE-384`). Es la afirmación contra la cual se comprueba un flujo de integración: sin ella, «el flujo funciona» no es algo que se pueda verificar.

## Por qué importa

Un flujo basado en mensajes puede perder, duplicar, retrasar o reordenar. Si no se dice qué se espera pase lo que pase, cualquier resultado parece aceptable y los fallos aparecen en producción. La decisión que cambia es el orden del trabajo: primero se escribe lo que debe ser cierto, después se diseña y se prueba que lo sea.

## Cómo funciona

`SE-384` enumera cinco invariantes del flujo de la plataforma de entregas:

1. **Cada entrega recibida tiene exactamente una calificación** (ni cero ni dos).
2. **Cada calificación publicada produce como mucho un aviso**, y eventualmente uno.
3. **Un mensaje que no se puede procesar no detiene a los demás.**
4. **El estado final de una entrega no depende del orden de llegada de sus mensajes.**
5. **Todo mensaje fallido es visible y recuperable.**

Cada una conecta con un mecanismo de las clases: la primera con el outbox, la segunda con la inbox y la política del notificador, la tercera con la cola de mensajes fallidos, la cuarta con la guarda de versión y la quinta con la observabilidad. Esa correspondencia es lo que las hace útiles: cada invariante señala qué mecanismo la sostiene y qué prueba la demostraría.

La comprobación se hace con **inyección de fallas**: se provocan caídas, duplicados, retrasos y mensajes inválidos y se mira si las cinco siguen cumpliéndose. Una invariante que se viola con una falla concreta indica qué mecanismo falta.

## Ejemplo

Se inyecta una caída del consumidor a mitad de un lote y reentregas duplicadas. Se comprueba entonces la invariante 1 contando, por cada entrega, cuántas calificaciones hay: debe ser exactamente una. Si aparece una segunda, falta idempotencia en el consumidor. Si hay cero, falta el outbox o la recuperación. Procedimiento de `SE-384`.

## Errores y confusiones comunes

- **Duplicados minutos después del original**: ventana de deduplicación menor que el horizonte de reintentos; se corrige con una ventana mayor que el horizonte máximo, con la aleatoriedad incluida.
- **Un solo mensaje detiene el flujo**: no hay cola de mensajes fallidos; se corrige desviando tras N intentos con alarma y dueño.
- **Escribir invariantes vagas** («que funcione bien») que no se pueden comprobar.
- **Confundirlas con aserciones de una prueba unitaria**: se comprueban sobre el flujo completo bajo fallas.

## Límites y cuándo no aplica

`SE-384` aclara que sus experimentos usan datos sintéticos, sin corredor, red ni concurrencia: el paquete es un texto sintético, el validador se ajustó con los mismos casos que lo evalúan, y las fallas inyectadas y sus tasas son del autor. Las cinco invariantes son las de ese flujo; otro sistema tendrá otras. Una invariante comprobada bajo las fallas que se probaron no garantiza las que no se probaron.
