# Fallo metaestable

[↑ Glosario](../../README.md) · [← Fallo latente](./fallo-latente.md) · [Fallo parcial →](./fallo-parcial.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Estado degradado que persiste tras desaparecer su disparador por un efecto de refuerzo, como los reintentos.

Definición de trabajo de [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md): Estado de sobrecarga que se sostiene por sí mismo después de desaparecer su causa inicial.

## Por qué importa

En [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), el tema «Fallos metaestables» importa porque un sistema puede quedar caído después de que la falla desaparece.

## Cómo funciona

Según [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), en la sección «Fallos metaestables»:

Un **fallo metaestable** es un estado degradado que persiste después de que desapareció el disparador que lo causó, porque un efecto de refuerzo lo sostiene. El mecanismo más común es el reintento: la falla termina, pero la cola que se formó sigue llena y las esperas siguen agotándose, de modo que cada petición se reintenta y la carga efectiva sigue siendo triple de la capacidad. El sistema vuelve a ser sano solo si algo interrumpe el ciclo (un cortacircuitos que corta el flujo, un descarte de carga, un reinicio). El trabajo de Bronson et al. (HotOS 2021) lo formaliza como una clase de falla; el libro de SRE describe cómo el descarte de carga y las respuestas degradadas cortan el ciclo.

Se ve en una serie temporal. Se retiran la mitad de los hilos de la dependencia entre los 30 y los 60 s (la capacidad pasa de 200 a 100 peticiones por segundo con 90 de demanda) y se mide cada 10 s la fracción de peticiones correctas para A, C y E.

**Cómo leer la figura.** El eje horizontal es el tiempo y el vertical, las peticiones correctas por ventana; las líneas verticales marcan el inicio y el fin de la falla. A no se entera: 90 peticiones por segundo caben en 100 de capacidad, y no multiplica la carga. C cae a 10 % durante la falla, y a los 60 s, cuando la dependencia recupera su capacidad, **sigue en 0 % durante el resto de la ejecución (60 s)**: cada petición vuelve a agotar la espera de 250 ms porque la cola de intentos viejos sigue sin vaciarse, y cada fracaso se reintenta. E baja a 44 % y sube a 100 % a los 75 s, porque el cortacircuitos corta el flujo y la cola se drena.

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

- **Prerrequisito:** las clases previas [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Disparador](../d/disparador.md), [Efecto](../e/efecto.md), [Estado](../e/estado.md), [Reintentos](../r/reintentos.md), [Amplificación por reintentos](../a/amplificacion-por-reintentos.md), [Debilidad sistémica](../d/debilidad-sistemica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-507 — Inyección de fallos de red, latencia y dependencias](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Fallos metaestables».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Principles of Chaos Engineering](https://principlesofchaos.org/) — definición, pasos y principios avanzados; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Basiri et al., «Chaos Engineering»](https://arxiv.org/abs/1702.05843) — IEEE Software 33(3), 2016; autoridad: artículo revisado de ingenieros de Netflix.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — sobrecarga, reintentos y cascadas; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) — descarte de carga y respuestas degradadas; autoridad: libro de ingeniería de confiabilidad de Google.
- [AWS Builders' Library: Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — reintentos y pausa con azar; autoridad: biblioteca de ingeniería de Amazon Web Services.

---

[↑ Glosario](../../README.md) · [← Fallo latente](./fallo-latente.md) · [Fallo parcial →](./fallo-parcial.md)
