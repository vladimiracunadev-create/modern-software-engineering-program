# HMAC

[↑ Glosario](../../README.md) · [← Historias de usuario](./historias-de-usuario.md) · [Holgura →](./holgura.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Código de autenticación con clave construido sobre una función hash.

Definición de trabajo de [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md): Código de autenticación de mensajes calculado con una función hash y un secreto compartido.

## Por qué importa

La clase donde se define, [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md), existe con este propósito: la clase existe para que gobiernes los datos de una plataforma como una responsabilidad con mecanismos comprobables y no como un documento de políticas.

## Cómo funciona

Según [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md):

Reemplazar un identificador por un seudónimo permite unir tablas sin mostrar el identificador. Con SHA-256 sin clave, el seudónimo es una función pública del correo: un atacante que conozca el formato y pruebe 18 000 candidatos recuperó los 5 000 correos (100 %); contra un HMAC-SHA-256 con una clave que el atacante no tiene, recuperó 0. La clave convierte el seudónimo en algo que solo puede calcular quien la tiene, y por eso su gestión ([SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md)) es parte del diseño: si la clave se filtra, se revierten todos los seudónimos. El HMAC conserva la propiedad útil: el mismo correo da siempre el mismo seudónimo, de modo que las uniones entre tablas funcionan. Los datos seudonimizados siguen siendo personales para quien tenga la clave o una tabla de correspondencia.

Según [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md):

El equipo de *Avisos* hace el inventario de datos personales de su plataforma. Ejecuta el clasificador por contenido sobre las veinte tablas más usadas y encuentra seis columnas con correos o teléfonos que el nombre no delataba, dos de ellas en campos de texto libre. Marca cada una en el catálogo con dueño, plazo y base de tratamiento, y cambia la ingesta para seudonimizar con HMAC antes de la zona intermedia. Antes de entregar estadísticas a un investigador, calcula los grupos pequeños y generaliza el año de nacimiento a década. Para las solicitudes de supresión escribe un procedimiento que recorre el linaje de tablas, borra por seudónimo en cada una y lista las copias exportadas con su plazo de retirada.

## Ejemplo

Ejemplo de [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) (sección «Ejemplo mínimo»):

El hash sin clave se revierte con una lista de candidatos plausibles; el HMAC conserva la unión y exige la clave.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Alguien crea eventos falsos con una herramienta** — causa: la dirección del webhook no verifica firma. Corrección: firma HMAC con secreto y comparación de tiempo constante. ([SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con SHA-256 sin clave, el seudónimo es una función pública del correo: un atacante que conozca el formato y pruebe 18 000 candidatos recuperó los 5 000 correos (100 %); contra un HMAC-SHA-256 con una clave que el atacante no tiene, recuperó 0. ([SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Secreto](../s/secreto.md).
- **Ver también:** [Código de autenticación de mensaje](../c/codigo-de-autenticacion-de-mensaje.md), [Autenticación](../a/autenticacion.md), [Función](../f/funcion.md), [Huella](./huella.md), [Cuasi-identificador](../c/cuasi-identificador.md), [Dato personal](../d/dato-personal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-358](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: validar entregas de webhooks](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries) — HMAC-SHA256 y comparación de tiempo constante; autoridad: documentación oficial de GitHub.
- [RFC 2104: HMAC](https://www.rfc-editor.org/rfc/rfc2104) — código de autenticación de mensajes; autoridad: IETF.
- [Stripe: webhooks](https://docs.stripe.com/webhooks) — firmas, tolerancia de marca de tiempo, reintentos y eventos repetidos; autoridad: documentación oficial de Stripe.
- [Standard Webhooks](https://www.standardwebhooks.com/) — convención de identificador, marca de tiempo y firma; autoridad: especificación comunitaria.
- [RFC 9110: semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — validadores y peticiones condicionales; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Historias de usuario](./historias-de-usuario.md) · [Holgura →](./holgura.md)
