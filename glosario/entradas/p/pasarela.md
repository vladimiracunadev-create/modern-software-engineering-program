# Pasarela

[↑ Glosario](../../README.md) · [← Partida doble](./partida-doble.md) · [Paso ambiguo →](./paso-ambiguo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Una **pasarela** (*gateway*) es un equipo que conecta dispositivos de una red local con una red mayor, traduciendo protocolos y agregando datos. Es el sentido de [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) (edge, gateways y procesamiento local). No debe confundirse con una pasarela de pagos ni con un API gateway de servicios web, que [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md) trata aparte.

## Por qué importa

Concentra confianza, almacenamiento y un punto único de fallo. Un diseño con pasarela decide dónde se toman decisiones y qué sigue funcionando cuando cada nivel cae.

## Cómo funciona

[SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md): la pasarela es un punto de concentración de confianza y de fallo. Si cae, todos los nodos de su piso quedan incomunicados; si se compromete, expone todos sus datos. Por eso necesita sus propias actualizaciones, identidad, almacenamiento con política y monitorización. De ello se sigue una regla de diseño: los nodos no deben depender de ella para decisiones críticas, y la pasarela debe poder funcionar sin la nube. La arquitectura se decide por *qué debe seguir funcionando cuando cada nivel cae*.

Funciones típicas: traducir entre el protocolo del nodo y el de la red mayor, agregar y filtrar datos antes de subirlos (ahorra ancho de banda), guardar mientras la nube no responde, y distribuir configuración y umbrales firmados a los nodos.

## Ejemplo

El equipo de la plataforma de [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) asigna cada decisión a un nivel. La alarma de ventilación se decide en el nodo, con un umbral guardado en memoria y un valor seguro por defecto. La pasarela del piso agrupa los 20 nodos, aplica la banda muerta de 0,5 °C a la temperatura y el promedio por minuto al CO₂ más un evento si hay un pico, almacena hasta tres horas por si cae la nube y envía en lotes de 60 muestras en binario comprimido. La nube guarda el histórico y ajusta umbrales, que la pasarela distribuye a los nodos con firma ([SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md)).

## Errores y confusiones comunes

- **Una pasarela caída silencia un piso:** punto único de fallo. Corrección: redundancia y alarma de silencio de nodos ([SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md)).
- **Poner decisiones críticas solo en la pasarela.**
- **Tratarla como un equipo sin mantenimiento:** necesita actualizaciones, identidad y monitorización.
- **Confundirla con el borde de la red** en sentido amplio: la pasarela es una pieza del borde.

## Límites y cuándo no aplica

No hace falta cuando los dispositivos hablan directamente con la red mayor y no necesitan traducción ni agregación. Las cifras del ejemplo (20 nodos, tres horas, lotes de 60) son del escenario de la clase. Añadir una pasarela añade un componente que operar y proteger.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Banda muerta](../b/banda-muerta.md), [Borde de la red](../b/borde-de-la-red.md), [Carga útil](../c/carga-util.md), [Decisión con plazo](../d/decision-con-plazo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (15 clases más lo mencionan; las que más):

[SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md).

**Aparece en los casos de estudio:** [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «gateway», «Pasarelas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Bormann, Ersue y Keränen, RFC 7228: Terminology for Constrained-Node Networks](https://www.rfc-editor.org/rfc/rfc7228) — restricciones de nodos y redes; autoridad: IETF.
- [Hartke, RFC 8576: IoT Security: State of the Art and Challenges](https://www.rfc-editor.org/rfc/rfc8576) — desafíos de seguridad del IoT; autoridad: IETF.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — latencia y plazos en sistemas ciberfísicos; autoridad: autores del libro (UC Berkeley).
- [Python: `struct`](https://docs.python.org/3/library/struct.html) — empaquetado binario; autoridad: documentación de Python.
- [Python: `zlib`](https://docs.python.org/3/library/zlib.html) — compresión usada en la comparación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Partida doble](./partida-doble.md) · [Paso ambiguo →](./paso-ambiguo.md)
