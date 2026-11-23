# Actualización condicionada por versión

[↑ Glosario](../../README.md) · [← Actores y objetivos](./actores-y-objetivos.md) · [Actualización condicional atómica →](./actualizacion-condicional-atomica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Escritura que se aplica solo si la versión del cambio supera la guardada.

Definición de trabajo de [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md).

## Por qué importa

La clase donde se define, [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), existe con este propósito: el taller existe para que aprendas a contener duplicados provocándolos primero: producirás a propósito cinco causas distintas de un efecto repetido en un consumidor sin defensa, medirás qué defensa contiene cada una, y descubrirás dos formas en que una defensa mal colocada falla al revés (perdiendo el efecto en lugar de duplicarlo, o descartando intentos legítimos).

## Cómo funciona

Según [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md):

La tercera defensa es cambiar la forma del efecto para que repetirlo no cambie el resultado. **Actualización condicionada por versión**: «poner la nota de la entrega 7 en 6,0 si la versión es mayor que la guardada». **Operación naturalmente idempotente**: «poner» en lugar de «sumar». Estas formas no necesitan recordar mensajes ni claves, porque el estado final es el mismo con una o con diez aplicaciones. Su límite es que solo funcionan cuando el efecto se puede expresar como estado: enviar un correo o cobrar una tarjeta no es un valor que se «ponga», y ahí hace falta una clave que el proveedor reconozca.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md):

El equipo reproduce el incidente de las 87 calificaciones dobles con el taller. Primero ejecutan las cinco provocaciones y observan que la configuración del plazo de visibilidad produce más duplicados que cualquier fallo; ajustan el plazo a tres veces el percentil 99 del tiempo de proceso y añaden una extensión del plazo para tareas largas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md)) son:

- **Efectos que nunca se aplican, sin error** — causa: la clave se guardó antes que el efecto, en otra transacción. Corrección: clave y efecto en una sola transacción.
- **Efectos duplicados tras una caída** — causa: el efecto se aplicó antes de guardar la clave. Corrección: clave y efecto en una sola transacción.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún corredor, red ni concurrencia entre consumidores: las probabilidades, la distribución del tiempo de proceso, el plazo de 30 s, los 200 mensajes del reinicio y los intentos por estudiante son construcciones del autor, y dos de las defensas se miden contando filas y no valores.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Versión](../v/version.md), [Clave de negocio](../c/clave-de-negocio.md), [Clave del mensaje](../c/clave-del-mensaje.md), [Plazo de visibilidad](../p/plazo-de-visibilidad.md), [Transacción única de clave y efecto](../t/transaccion-unica-de-clave-y-efecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Amazon SQS: tiempo de visibilidad](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) — reentrega de un mensaje cuyo proceso supera el plazo; autoridad: Amazon Web Services.
- [EIP: Idempotent Receiver](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera mensajes repetidos; autoridad: autores del libro.
- [Stripe: peticiones idempotentes](https://docs.stripe.com/api/idempotent_requests) — clave reutilizada en los reintentos; autoridad: documentación oficial de Stripe.
- [SQLite: UPSERT](https://www.sqlite.org/lang_upsert.html) — inserción con conflicto y actualización condicionada; autoridad: documentación oficial de SQLite.
- [SQLite: cláusula ON CONFLICT](https://www.sqlite.org/lang_conflict.html) — `INSERT OR IGNORE` y `INSERT OR REPLACE`; autoridad: documentación oficial de SQLite.

---

[↑ Glosario](../../README.md) · [← Actores y objetivos](./actores-y-objetivos.md) · [Actualización condicional atómica →](./actualizacion-condicional-atomica.md)
