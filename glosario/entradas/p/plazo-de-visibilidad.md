# Plazo de visibilidad

[↑ Glosario](../../README.md) · [← Plazo de los cambios](./plazo-de-los-cambios.md) · [Plegado de mayúsculas →](./plegado-de-mayusculas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Tiempo durante el cual un mensaje recibido no se entrega a otros consumidores si no se confirma.

Definición de trabajo de [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md).

## Por qué importa

La clase donde se define, [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), existe con este propósito: el taller existe para que aprendas a contener duplicados provocándolos primero: producirás a propósito cinco causas distintas de un efecto repetido en un consumidor sin defensa, medirás qué defensa contiene cada una, y descubrirás dos formas en que una defensa mal colocada falla al revés (perdiendo el efecto en lugar de duplicarlo, o descartando intentos legítimos).

## Cómo funciona

Según [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md):

Un efecto repetido tiene al menos cinco orígenes. **El consumidor cae antes de acusar**: procesó, no confirmó y el corredor reentrega. **El acuse se pierde** en el camino: el corredor cree que no se procesó. **El productor reintenta** tras un tiempo agotado: el primer envío sí llegó y el reintento crea un segundo mensaje con otro identificador. **El plazo de visibilidad vence** antes de terminar el proceso: el corredor entrega el mensaje a otro consumidor mientras el primero sigue trabajando. **Se reinician los desplazamientos** o se reprocesa a propósito: los mensajes se releen. La misma entrada produce el mismo síntoma por caminos que se diagnostican y se contienen de forma diferente.

Según [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md):

El equipo reproduce el incidente de las 87 calificaciones dobles con el taller. Primero ejecutan las cinco provocaciones y observan que la configuración del plazo de visibilidad produce más duplicados que cualquier fallo; ajustan el plazo a tres veces el percentil 99 del tiempo de proceso y añaden una extensión del plazo para tareas largas. Después aplican como defensa principal el índice único por `(entrega, intento)` sobre las calificaciones, porque el servicio de entregas puede reintentar con un nuevo identificador y la clave del mensaje no lo cubre; la tabla de mensajes vistos queda como segunda capa para los efectos externos (los correos). Guardan clave y efecto en una sola transacción, y escriben una prueba que inyecta una caída entre ambos pasos.

## Ejemplo

Ejemplo de [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) (sección «Ejemplo profesional»):

El equipo reproduce el incidente de las 87 calificaciones dobles con el taller. Primero ejecutan las cinco provocaciones y observan que la configuración del plazo de visibilidad produce más duplicados que cualquier fallo; ajustan el plazo a tres veces el percentil 99 del tiempo de proceso y añaden una extensión del plazo para tareas largas. Después aplican como defensa principal el índice único por `(entrega, intento)` sobre las calificaciones, porque el servicio de entregas puede reintentar con un nuevo identificador y la clave del mensaje no lo cubre; la tabla de mensajes vistos queda como segunda capa para los efectos externos (los correos).

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Muchas reentregas sin ningún fallo** — causa: plazo de visibilidad menor que el tiempo de proceso. Corrección: medir el percentil 99 y fijar el plazo con margen. ([SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún corredor, red ni concurrencia entre consumidores: las probabilidades, la distribución del tiempo de proceso, el plazo de 30 s, los 200 mensajes del reinicio y los intentos por estudiante son construcciones del autor, y dos de las defensas se miden contando filas y no valores.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actualización condicionada por versión](../a/actualizacion-condicionada-por-version.md), [Clave de negocio](../c/clave-de-negocio.md), [Clave del mensaje](../c/clave-del-mensaje.md), [Transacción única de clave y efecto](../t/transaccion-unica-de-clave-y-efecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

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

[↑ Glosario](../../README.md) · [← Plazo de los cambios](./plazo-de-los-cambios.md) · [Plegado de mayúsculas →](./plegado-de-mayusculas.md)
