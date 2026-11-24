# Borde de la red

[↑ Glosario](../../README.md) · [← Borde](./borde.md) · [BPF_PROG_TEST_RUN →](./bpf-prog-test-run.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

El **borde de la red** (*edge*) es el conjunto de puntos de ejecución cercanos al usuario que ejecutan cómputo o sirven datos sin pasar por el origen. Es el sentido de [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md). [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) lo usa con un matiz del mundo embebido: dispositivos y pasarelas cercanos a la fuente de los datos, donde se procesa antes de enviar a la nube. En ambos, la idea es la misma: acercar el trabajo a quien lo origina o lo consume.

## Por qué importa

La decisión es qué piezas viven lejos y cuáles cerca. Acercar reduce la latencia de ida y vuelta y descarga el origen; a cambio cuesta consistencia, operación y limitaciones del entorno. [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) lo trata como un trade-off, no como mejora gratuita.

## Cómo funciona

[SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) describe tres beneficios y tres costos:

- **Beneficios:** menor latencia, menos carga en el origen, y funcionamiento con datos locales cuando el origen está lejos o inaccesible.
- **Costos:** *consistencia* (las copias pueden estar desactualizadas); *operación* (muchos puntos que desplegar y observar); *limitaciones del entorno de ejecución* (lo que puede correr en el borde es menos que en el origen).

Por eso una pieza se lleva al borde si su escenario es de latencia o de disponibilidad local y si tolera datos algo viejos. Es natural para contenido que cambia poco o para decisiones con datos locales. El **estado autoritativo sigue en el origen**.

En [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) (IoT), el borde son dispositivos y pasarelas que filtran, agregan o deciden localmente antes de subir datos, lo que ahorra ancho de banda y permite seguir operando sin conexión.

## Ejemplo

[SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) asigna cada pieza de la plataforma de entregas a un estilo según su escenario: unas funciones bajo demanda, otras en servidor, y las que sirven contenido estable cerca del usuario. Un ejemplo ilustrativo (no de la clase): una página de ayuda que cambia una vez al mes se sirve desde el borde; el saldo de una cuenta, no, porque una copia vieja daría una respuesta incorrecta.

## Errores y confusiones comunes

- **Llevar al borde estado que exige consistencia fuerte:** copias viejas dan respuestas erróneas.
- **Subestimar la operación:** desplegar y observar muchos puntos es trabajo propio.
- **Confundir el borde de [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) (puntos de presencia de una red) con el de [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) (pasarelas y dispositivos):** comparten el principio, no la infraestructura.

## Límites y cuándo no aplica

No conviene cuando el dato cambia constantemente y debe leerse al instante, cuando el entorno limitado no soporta la lógica, o cuando el volumen de tráfico no justifica operar muchos puntos. Las simulaciones de [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) no midieron ningún proveedor real; sus tiempos y precios son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Dispositivo](../d/dispositivo.md), [Origen](../o/origen.md), [Pasarela](../p/pasarela.md), [Arranque en frío](../a/arranque-en-frio.md), [Banda muerta](./banda-muerta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-089](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md), [SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «edge».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jonas et al., «Cloud Programming Simplified: A Berkeley View on Serverless Computing»](https://arxiv.org/abs/1902.03383) — caracterización y límites de serverless; autoridad: UC Berkeley (preimpresión).
- [Fowler, «Serverless Architectures»](https://martinfowler.com/articles/serverless.html) — beneficios y costes; autoridad: Martin Fowler y Mike Roberts.
- [AWS Lambda: entorno de ejecución](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) — ciclo de vida de los entornos de ejecución; autoridad: Amazon Web Services.
- [Demers et al., «Epidemic algorithms for replicated database maintenance» (PODC, 1987)](https://doi.org/10.1145/41840.41841) — difusión por rumor; autoridad: ACM PODC.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Borde](./borde.md) · [BPF_PROG_TEST_RUN →](./bpf-prog-test-run.md)
