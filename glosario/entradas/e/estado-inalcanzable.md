# Estado inalcanzable

[↑ Glosario](../../README.md) · [← Estado imposible](./estado-imposible.md) · [Estado inicial →](./estado-inicial.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Estado que no se puede alcanzar desde el estado inicial por ninguna secuencia de eventos.

Definición de trabajo de [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md).

## Por qué importa

La clase donde se define, [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), existe con este propósito: el taller existe para que reúnas lo que las diez clases anteriores trataron por separado en un solo flujo, el de entregar una tarea con una conexión que falla, y lo especifiques como una máquina de estados explícita, lo pruebes con fallos inyectados y declares qué comprobaciones automáticas lo cubren y cuáles exigen a una persona.

## Cómo funciona

Según [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md):

Resultado, idéntico en Windows (CPython 3.12.9) y en Ubuntu bajo WSL2 (3.12.3): quitar la transición `Editando → Listo` (validar) deja **7 estados inalcanzables**, quitar `Enviando → Reintentando` (tiempo agotado) deja 2 y quitar `Reintentando → Fallido` deja 1: **3 de 18** mutaciones dejan estados inalcanzables; quitar `Conflicto → Listo` (resolver) deja **1** estado sin salida y sin camino a «Enviado». Las **otras 14 mutaciones no activan ninguna comprobación de forma**, aunque cambian el comportamiento: sin `cancelar` desde la cola o sin `reintentar manual` desde el fallo, la persona queda sin una acción que antes tenía.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md):

El flujo de entrega se publica como una tabla de estados y transiciones en el repositorio, con una prueba que comprueba su forma y otra que ejecuta, para cada transición, el escenario que la dispara. El cliente reintenta con retroceso exponencial y dispersión completa, con un máximo de seis intentos, y el servidor limita la tasa y reconoce la clave de idempotencia. El estado «en cola» se anuncia en una región de estado y se muestra con texto («se enviará cuando haya conexión»), no solo con un icono.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md)) son:

- **Una entrega queda «enviando» sin fin** — causa: falta la transición para un evento de fallo. Corrección: escribir la tabla con todos los eventos y probar cada transición.
- **Mil clientes agotan al servidor al recuperarse** — causa: reintentos sincronizados sin dispersión. Corrección: retroceso exponencial con dispersión, máximo de intentos y límite de tasa.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **3 de 18** mutaciones dejan estados inalcanzables; quitar `Conflicto → Listo` (resolver) deja **1** estado sin salida y sin camino a «Enviado». ([SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado inicial](./estado-inicial.md), [Estado](./estado.md), [Evento](./evento.md), [Secuencia](../s/secuencia.md), [Dispersión](../d/dispersion.md), [Escenario de integración](./escenario-de-integracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Harel, «Statecharts: a visual formalism for complex systems» (Sci. Comput. Program., 1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — estados y transiciones para comportamiento reactivo; autoridad: Science of Computer Programming.
- [AWS Builders' Library: timeouts, reintentos y retroceso con dispersión](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — por qué sincronizan los reintentos y cómo repartirlos; autoridad: Amazon Web Services.
- [W3C WAI: evaluación preliminar de accesibilidad](https://www.w3.org/WAI/test-evaluate/preliminary/) — alcance y límites de las comprobaciones rápidas; autoridad: W3C WAI.
- [W3C: Website Accessibility Conformance Evaluation Methodology (WCAG-EM)](https://www.w3.org/TR/WCAG-EM/) — metodología para evaluar la conformidad de un sitio; autoridad: W3C.
- [WCAG 2.2 (W3C)](https://www.w3.org/TR/WCAG22/) — criterios de éxito aplicados al flujo; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Estado imposible](./estado-imposible.md) · [Estado inicial →](./estado-inicial.md)
