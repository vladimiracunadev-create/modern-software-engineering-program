# Difusión por rumor

[↑ Glosario](../../README.md) · [← Diferencias de plataforma](./diferencias-de-plataforma.md) · [Dimensión →](./dimension.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Propagación de información por la elección aleatoria de pares en cada ronda.

Definición de trabajo de [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md).

## Por qué importa

La clase donde se define, [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), existe con este propósito: la clase existe para que decidas dónde ejecutar cada parte del sistema (funciones bajo demanda, un servidor siempre encendido, el borde de la red o una malla de pares) con una cuenta de latencia, de costo y de disponibilidad, y no con el nombre de la tecnología.

## Cómo funciona

Según [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md):

En una red **entre pares** no hay un coordinador central: cada nodo habla con otros y la información se propaga de par en par. Las técnicas de difusión por rumor (gossip) escogen pares al azar en cada ronda y convergen en un número de rondas del orden del logaritmo del tamaño de la red, con un coste de mensajes controlado. Dan resiliencia (no hay un punto único de fallo) y escalan bien, y a cambio ofrecen consistencia eventual y probabilística, dependen de que la red de pares siga conectada y abren nuevos problemas (confianza entre pares, descubrimiento, privacidad). Sirve para difusión de estado entre pares cooperativos, no para decidir quién tiene la razón sobre una nota.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md):

El equipo asigna cada pieza de la plataforma a un estilo con su escenario.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md)) son:

- **Lentitud solo en los primeros segundos de un pico** — causa: arranque en frío concentrado. Corrección: aprovisionar instancias en la ventana crítica o reducir la inicialización.
- **La factura de funciones supera a un servidor** — causa: tráfico sostenido y alto con función pesada. Corrección: calcular el equilibrio y volver a un servidor.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La figura dice que la difusión por rumor converge rápido y barato en una red conectada, y nada acerca de quién tiene la razón: la convergencia de la información no decide conflictos entre versiones. ([SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propagación](../p/propagacion.md), [Arranque en frío](../a/arranque-en-frio.md), [Borde de la red](../b/borde-de-la-red.md), [Punto de equilibrio de costo](../p/punto-de-equilibrio-de-costo.md), [Serverless](../s/serverless.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Demers et al., «Epidemic algorithms for replicated database maintenance» (PODC, 1987)](https://doi.org/10.1145/41840.41841) — difusión por rumor; autoridad: ACM PODC.
- [Jonas et al., «Cloud Programming Simplified: A Berkeley View on Serverless Computing»](https://arxiv.org/abs/1902.03383) — caracterización y límites de serverless; autoridad: UC Berkeley (preimpresión).
- [Fowler, «Serverless Architectures»](https://martinfowler.com/articles/serverless.html) — beneficios y costes; autoridad: Martin Fowler y Mike Roberts.
- [AWS Lambda: entorno de ejecución](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) — ciclo de vida de los entornos de ejecución; autoridad: Amazon Web Services.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Diferencias de plataforma](./diferencias-de-plataforma.md) · [Dimensión →](./dimension.md)
