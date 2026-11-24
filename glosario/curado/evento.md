# Evento

## Definición

Un **evento** es un mensaje que afirma un hecho ya ocurrido, inmutable y sin destinatario conocido (`SE-374`). Otras clases lo matizan: observación estructurada con significado estable (`SE-033`), hecho que puede activar una transición (`SE-057`) y mensaje que comunica que algo ocurrió sin esperar respuesta inmediata (`SE-163`).

## Por qué importa

Permite acoplar poco: el emisor no conoce a quienes reaccionan, así que se puede añadir un consumidor sin tocarlo (`SE-374`). La contrapartida es la que la clase señala: si no hay ningún oyente, nadie se entera. La decisión que cambia es qué se modela como evento (un hecho) y qué como comando (una orden).

## Cómo funciona

Un evento se nombra en pasado («la entrega 4721 fue recibida»), no se modifica (no se puede «desrecibir»: se emite otro evento) y no ordena nada: lo que el receptor haga con él es decisión suya. `SE-374` contrasta:

- un **comando** espera un receptor y falla si no está;
- un **evento** acepta cero o muchos oyentes.

Disfrazar un comando de evento (una «EntregaRecibida» que en realidad dispara al calificador y nadie más debe reaccionar) acopla al emisor con la lógica de otro y esconde una dependencia. El contenido del evento es un diseño: si solo lleva un identificador, los consumidores llaman todos de vuelta; si lleva el estado completo, puede quedar viejo cuando la entidad cambie.

## Ejemplo

```json
{"tipo": "EntregaRecibida", "id": 4721, "version": 3, "curso": "SE-101", "ts": "2026-03-04T10:15:00Z"}
```

Incluir `version` permite que un consumidor compare con la vigente donde importe (`SE-374`). En `SE-033`, un evento de registro es una observación estructurada con significado estable, lo que habilita la correlación entre señales.

## Errores y confusiones comunes

- **Nadie reacciona y no hay error.** Causa: ningún oyente registrado y el bus descarta en silencio; corrección: alarma por eventos sin consumidor donde importe (`SE-374`).
- **Los consumidores llaman todos de vuelta.** Causa: el evento solo lleva un identificador; corrección: incluir el contenido mínimo que casi todos necesitan (`SE-374`).
- **Los consumidores operan con datos viejos.** Causa: el evento lleva el estado y la entidad cambió; corrección: incluir una versión y comparar con la vigente (`SE-374`).

## Límites y cuándo no aplica

Un evento no sirve cuando se necesita una respuesta inmediata o una garantía de que alguien actúe: ahí corresponde un comando. Una arquitectura basada en eventos hace más difícil seguir el flujo de punta a punta, y lo que `SE-374` describe es el sentido del programa, no el de todos los marcos de mensajería (algunos llaman «evento» a cualquier notificación).
