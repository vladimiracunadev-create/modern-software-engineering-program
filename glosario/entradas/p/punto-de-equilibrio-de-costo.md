# Punto de equilibrio de costo

[↑ Glosario](../../README.md) · [← Punto de equilibrio](./punto-de-equilibrio.md) · [Punto de extensión →](./punto-de-extension.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Tráfico en el que dos modelos de precio cuestan lo mismo.

Definición de trabajo de [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md).

## Por qué importa

En [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), el tema «Punto de equilibrio de costo» importa porque decide qué estilo conviene según utilización, memoria y duración.

## Cómo funciona

Según [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), en la sección «Punto de equilibrio de costo»:

El pago por uso se escribe como costo por invocación más costo por GB-segundo; un servidor fijo, como un precio mensual con una capacidad. El **punto de equilibrio** es el tráfico en el que ambos cuestan lo mismo: por debajo conviene pagar por uso, por encima conviene el servidor, siempre que ese servidor se mantenga razonablemente lleno. Depende del producto memoria × duración (una función pesada y larga se encarece mucho antes) y del número de servidores que se necesite por disponibilidad (dos o tres reparten el costo fijo en menos tráfico por servidor). Una cuenta con precios supuestos sirve para ver la forma; los precios reales hay que pedirlos y cambian.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md):

El equipo asigna cada pieza de la plataforma a un estilo con su escenario.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md)) son:

- **Lentitud solo en los primeros segundos de un pico** — causa: arranque en frío concentrado. Corrección: aprovisionar instancias en la ventana crítica o reducir la inicialización.
- **La factura de funciones supera a un servidor** — causa: tráfico sostenido y alto con función pesada. Corrección: calcular el equilibrio y volver a un servidor.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún proveedor, función, red ni precio real: los tiempos de arranque, los precios y las redes de pares son construcciones del autor. La siguiente clase convierte los umbrales de estas decisiones en pruebas continuas de la arquitectura.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Arranque en frío](../a/arranque-en-frio.md), [Borde de la red](../b/borde-de-la-red.md), [Difusión por rumor](../d/difusion-por-rumor.md), [Serverless](../s/serverless.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jonas et al., «Cloud Programming Simplified: A Berkeley View on Serverless Computing»](https://arxiv.org/abs/1902.03383) — caracterización y límites de serverless; autoridad: UC Berkeley (preimpresión).
- [Fowler, «Serverless Architectures»](https://martinfowler.com/articles/serverless.html) — beneficios y costes; autoridad: Martin Fowler y Mike Roberts.
- [AWS Lambda: entorno de ejecución](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) — ciclo de vida de los entornos de ejecución; autoridad: Amazon Web Services.
- [Demers et al., «Epidemic algorithms for replicated database maintenance» (PODC, 1987)](https://doi.org/10.1145/41840.41841) — difusión por rumor; autoridad: ACM PODC.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Punto de equilibrio](./punto-de-equilibrio.md) · [Punto de extensión →](./punto-de-extension.md)
