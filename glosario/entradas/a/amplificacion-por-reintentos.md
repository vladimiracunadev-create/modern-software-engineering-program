# Amplificación por reintentos

[↑ Glosario](../../README.md) · [← Amplificación de reintentos](./amplificacion-de-reintentos.md) · [Amplitud →](./amplitud.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Multiplicación de la carga sobre una dependencia por intentos repetidos de peticiones que fallan.

Definición de trabajo de [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md).

## Por qué importa

En [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), el tema «Amplificación por reintentos» importa porque un mecanismo de protección puede multiplicar la carga que debía amortiguar.

## Cómo funciona

Según [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), en la sección «Amplificación por reintentos»:

Un **reintento** repite una llamada fallida con la esperanza de que el fallo sea transitorio. Si el fallo no es transitorio sino una sobrecarga, el reintento añade trabajo al componente que ya no da abasto. Como la persona usuaria no se entera de que hubo varios intentos, el costo es invisible desde el cliente y evidente en la dependencia. La documentación de Google SRE lo identifica como una de las causas de las fallas en cascada, y la guía de AWS explica el papel de la pausa con azar para repartir los reintentos en el tiempo.

El cálculo es directo. Si cada petición hace hasta 1 + r intentos y cada intento falla con probabilidad f (por espera agotada), los intentos por petición son `1 + f + f² + … + f^r`, que tiende a 1 + r cuando f se acerca a 1. Con r = 2 y f = 1 cada petición envía 3 intentos: la dependencia recibe el triple del trabajo justo cuando tiene menos capacidad. Y como el cliente abandona la espera pero la dependencia no cancela el trabajo, cada intento abandonado consume hilos. En el modelo, el servidor desperdicia el tiempo de cada intento que el cliente ya no espera.

**Cómo leer la figura.** Cada par de barras es una configuración y su largo, los intentos que envía por cada petición de una persona mientras dura la falla; la línea punteada es 1. A manda 1 en los dos casos porque no reintenta. B manda 2,3 con la dependencia lenta y 3,6 con la caída: con tres reintentos y sin pausa cada petición agota hasta cuatro intentos dentro del plazo de 1 s. C manda 3,0 en ambos casos: todos los intentos se agotan. D y E mandan cerca de 1 porque el cortacircuitos abre y deja de llamar. **Dónde deja de valer:** las cifras son intentos *por petición de persona*; el factor sobre la dependencia depende además de cuántas peticiones llegan y de cuántas ya estaban en cola.

## Ejemplo

Caso medido en la sección «Amplificación por reintentos» de [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md):

El cálculo es directo. Si cada petición hace hasta 1 + r intentos y cada intento falla con probabilidad f (por espera agotada), los intentos por petición son `1 + f + f² + … + f^r`, que tiende a 1 + r cuando f se acerca a 1. Con r = 2 y f = 1 cada petición envía 3 intentos: la dependencia recibe el triple del trabajo justo cuando tiene menos capacidad. Y como el cliente abandona la espera pero la dependencia no cancela el trabajo, cada intento abandonado consume hilos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md)) son:

- **Todo parece resiliente en el documento** — causa: se revisó la presencia de mecanismos, no su comportamiento. Corrección: inyectar la falla que cada mecanismo dice cubrir.
- **El servicio no se recupera tras la falla** — causa: reintentos y cola mantienen la sobrecarga. Corrección: cortacircuitos, descarte de carga o pausa con azar.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md)) son: Las definiciones son operativas para el cliente de la API de entregas. No fijan sinónimos para términos con una historia más amplia y deben contrastarse con las fuentes enlazadas. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se inyectó ninguna falla en un sistema real; la dependencia de 8 hilos, el tráfico de 90 peticiones por segundo, las cinco configuraciones y las seis fallas son construcciones del autor, y los umbrales de los cortacircuitos se eligieron para mostrar el fenómeno.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Sobre](../s/sobre.md), [Debilidad sistémica](../d/debilidad-sistemica.md), [Fallo metaestable](../f/fallo-metaestable.md), [Ingeniería del caos](../i/ingenieria-del-caos.md), [Resiliencia declarada](../r/resiliencia-declarada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Principles of Chaos Engineering](https://principlesofchaos.org/) — definición, pasos y principios avanzados; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Basiri et al., «Chaos Engineering»](https://arxiv.org/abs/1702.05843) — IEEE Software 33(3), 2016; autoridad: artículo revisado de ingenieros de Netflix.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — sobrecarga, reintentos y cascadas; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) — descarte de carga y respuestas degradadas; autoridad: libro de ingeniería de confiabilidad de Google.
- [AWS Builders' Library: Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — reintentos y pausa con azar; autoridad: biblioteca de ingeniería de Amazon Web Services.

---

[↑ Glosario](../../README.md) · [← Amplificación de reintentos](./amplificacion-de-reintentos.md) · [Amplitud →](./amplitud.md)
