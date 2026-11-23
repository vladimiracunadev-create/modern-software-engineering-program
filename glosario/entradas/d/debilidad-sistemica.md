# Debilidad sistémica

[↑ Glosario](../../README.md) · [← Deadline](./deadline.md) · [Debounce →](./debounce.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Propiedad de un sistema que convierte una falla localizada en daño visible para las personas usuarias.

Definición de trabajo de [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md).

## Por qué importa

La clase donde se define, [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), existe con este propósito: la clase existe para que distingas una resiliencia **declarada** (el diseño dice que hay tiempos de espera, reintentos y cortacircuitos) de una resiliencia **demostrada** (alguien provocó la falla y el sistema se comportó como se prometió), para que sepas qué es y qué no es ingeniería del caos y para que reconozcas cuándo un mecanismo de protección es la causa de la caída.

## Cómo funciona

Según [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md):

Conviene fijar el vocabulario antes de seguir. Una **falla** es un evento o condición que se aparta del funcionamiento normal (un proceso que cae, un disco que se detiene, una dependencia lenta). Una **debilidad sistémica** es una propiedad del sistema que convierte esa falla en un daño visible para las personas usuarias. Un **experimento** es una intervención controlada que busca refutar una afirmación sobre esa propiedad. La definición oficial pone el acento en la confianza: la ingeniería del caos es la disciplina de experimentar sobre un sistema para ganar confianza en su capacidad de resistir condiciones turbulentas. No promete eliminar las fallas ni asegura que el sistema no caerá; reduce la distancia entre lo que se cree y lo que se sabe.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md):

Supón, como caso hipotético y no como medición, que el equipo de la API de entregas completa la tabla «mecanismo declarado → falla que lo pone a prueba → resultado esperado» antes de la próxima revisión de arquitectura.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md)) son:

- **Todo parece resiliente en el documento** — causa: se revisó la presencia de mecanismos, no su comportamiento. Corrección: inyectar la falla que cada mecanismo dice cubrir.
- **El servicio no se recupera tras la falla** — causa: reintentos y cola mantienen la sobrecarga. Corrección: cortacircuitos, descarte de carga o pausa con azar.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md)) son: Las definiciones son operativas para el cliente de la API de entregas. No fijan sinónimos para términos con una historia más amplia y deben contrastarse con las fuentes enlazadas. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se inyectó ninguna falla en un sistema real; la dependencia de 8 hilos, el tráfico de 90 peticiones por segundo, las cinco configuraciones y las seis fallas son construcciones del autor, y los umbrales de los cortacircuitos se eligieron para mostrar el fenómeno.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Daño](./dano.md), [Propiedad](../p/propiedad.md), [Amplificación por reintentos](../a/amplificacion-por-reintentos.md), [Fallo metaestable](../f/fallo-metaestable.md), [Ingeniería del caos](../i/ingenieria-del-caos.md), [Resiliencia declarada](../r/resiliencia-declarada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md).

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

[↑ Glosario](../../README.md) · [← Deadline](./deadline.md) · [Debounce →](./debounce.md)
