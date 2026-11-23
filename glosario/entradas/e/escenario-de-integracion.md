# Escenario de integración

[↑ Glosario](../../README.md) · [← Escenario de calidad](./escenario-de-calidad.md) · [Escenario de uso →](./escenario-de-uso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Secuencia de acciones y condiciones que cruza varias piezas y tiene un resultado esperado escrito.

Definición de trabajo de [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md).

## Por qué importa

La clase donde se define, [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), existe con este propósito: el taller existe para que reúnas lo que las diez clases anteriores trataron por separado en un solo flujo, el de entregar una tarea con una conexión que falla, y lo especifiques como una máquina de estados explícita, lo pruebes con fallos inyectados y declares qué comprobaciones automáticas lo cubren y cuáles exigen a una persona.

## Cómo funciona

[SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para esta clase y deben contrastarse con la documentación enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md):

El flujo de entrega se publica como una tabla de estados y transiciones en el repositorio, con una prueba que comprueba su forma y otra que ejecuta, para cada transición, el escenario que la dispara. El cliente reintenta con retroceso exponencial y dispersión completa, con un máximo de seis intentos, y el servidor limita la tasa y reconoce la clave de idempotencia. El estado «en cola» se anuncia en una región de estado y se muestra con texto («se enviará cuando haya conexión»), no solo con un icono.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md)) son:

- **Una entrega queda «enviando» sin fin** — causa: falta la transición para un evento de fallo. Corrección: escribir la tabla con todos los eventos y probar cada transición.
- **Mil clientes agotan al servidor al recuperarse** — causa: reintentos sincronizados sin dispersión. Corrección: retroceso exponencial con dispersión, máximo de intentos y límite de tasa.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con la documentación enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El flujo, el servidor de capacidad fija y los nueve defectos son construcciones del autor; no se usó un navegador, un lector de pantalla ni una red real. La siguiente clase es el proyecto que lo verifica de punta a punta: una aplicación web accesible y offline con evidencia revisable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Resultado](../r/resultado.md), [Secuencia](../s/secuencia.md), [Dispersión](../d/dispersion.md), [Estado inalcanzable](./estado-inalcanzable.md), [Máquina de estados](../m/maquina-de-estados.md).
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

[↑ Glosario](../../README.md) · [← Escenario de calidad](./escenario-de-calidad.md) · [Escenario de uso →](./escenario-de-uso.md)
