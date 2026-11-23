# Serverless

[↑ Glosario](../../README.md) · [← Serie temporal](./serie-temporal.md) · [Service worker →](./service-worker.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Modelo en el que el proveedor ejecuta código bajo demanda, escala a cero y cobra por uso.

Definición de trabajo de [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md).

## Por qué importa

En [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), el tema «Serverless y su modelo de pago» importa porque cambia coste fijo por coste por uso y traslada la operación al proveedor.

## Cómo funciona

Según [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md):

En el modelo **serverless** el proveedor ejecuta el código bajo demanda, escala hacia arriba y hacia cero y cobra por invocaciones y por recursos consumidos en el tiempo (memoria × duración). Jonas y colaboradores lo presentan como una abstracción de la nube que oculta el servidor y facilita el pago por uso. Beneficia a las cargas con picos y poco uso medio, porque no se paga la capacidad ociosa. Impone límites: duración máxima por invocación, estado que debe vivir fuera de la función, comunicación entre funciones por servicios externos y dependencia de las características del proveedor. No es «sin servidores», sino «servidores que otro opera».

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md):

El equipo asigna cada pieza de la plataforma a un estilo con su escenario.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md)) son:

- **Lentitud solo en los primeros segundos de un pico** — causa: arranque en frío concentrado. Corrección: aprovisionar instancias en la ventana crítica o reducir la inicialización.
- **La factura de funciones supera a un servidor** — causa: tráfico sostenido y alto con función pesada. Corrección: calcular el equilibrio y volver a un servidor.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún proveedor, función, red ni precio real: los tiempos de arranque, los precios y las redes de pares son construcciones del autor. La siguiente clase convierte los umbrales de estas decisiones en pruebas continuas de la arquitectura.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Arranque en frío](../a/arranque-en-frio.md), [Borde de la red](../b/borde-de-la-red.md), [Difusión por rumor](../d/difusion-por-rumor.md), [Punto de equilibrio de costo](../p/punto-de-equilibrio-de-costo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-331 — Arquitecturas serverless, edge y peer-to-peer](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md).

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

[↑ Glosario](../../README.md) · [← Serie temporal](./serie-temporal.md) · [Service worker →](./service-worker.md)
