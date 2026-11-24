# Amplificación por reintentos

[↑ Glosario](../../README.md) · [← Amplificación de reintentos](./amplificacion-de-reintentos.md) · [Amplitud →](./amplitud.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

La **amplificación por reintentos** es la multiplicación de la carga sobre una dependencia causada por intentos repetidos de peticiones que fallan. Es la definición de trabajo de [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md). El mecanismo que debía proteger (repetir la llamada ante un fallo) se convierte en el que agrava el problema cuando el fallo no es transitorio sino una sobrecarga.

## Por qué importa

Cambia una decisión cotidiana: «añade un reintento por si acaso» deja de ser gratis. Un reintento ayuda cuando el fallo fue un tropiezo breve; ante una dependencia saturada, añade trabajo a quien ya no da abasto. Además el costo es invisible desde el cliente, porque la persona usuaria no sabe que hubo varios intentos, y evidente en la dependencia. [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) cita la documentación de Google SRE, que la identifica como una de las causas de las fallas en cascada, y la guía de AWS sobre el papel de la pausa con azar.

## Cómo funciona

Si cada petición hace hasta `1 + r` intentos y cada intento falla con probabilidad `f` (por ejemplo, por espera agotada), los intentos por petición son `1 + f + f² + … + f^r`. Cuando `f` se acerca a 1 esa suma tiende a `1 + r`: con `r = 2` y `f = 1`, cada petición envía tres intentos y la dependencia recibe el triple de trabajo justo cuando tiene menos capacidad.

Hay un segundo efecto: el cliente abandona la espera pero la dependencia no cancela el trabajo, de modo que cada intento abandonado sigue consumiendo hilos. El servidor gasta el tiempo de un intento que nadie espera. Y los reintentos de muchos clientes tienden a sincronizarse, así que la carga llega en oleadas.

Las defensas que enseña [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) actúan sobre esas causas: **cortacircuitos** (deja de llamar cuando la dependencia está enferma), **descarte de carga** (rechaza lo que no puede atender) y **pausa con azar** (reparte los reintentos en el tiempo). La figura de la clase lo muestra: sin reintentos se envía 1 intento por petición; con tres reintentos y sin pausa, 2,3 con la dependencia lenta y 3,6 con la caída; con cortacircuitos, cerca de 1 porque deja de llamar.

## Ejemplo

En [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), el cliente de la API de entregas llama a una dependencia de 8 hilos con 90 peticiones por segundo (cifras construidas por el autor, no una medición real). La dependencia empieza a responder lento. Con la configuración de tres reintentos sin pausa, cada petición agota hasta cuatro intentos dentro del plazo de 1 s: la dependencia recibe varias veces su tráfico normal, sus hilos se ocupan con trabajo abandonado y, aunque la causa original desaparezca, el servicio no se recupera porque reintentos y cola mantienen la sobrecarga. Es la forma de fallo que el programa llama metaestable.

## Errores y confusiones comunes

- **«Todo parece resiliente en el documento».** Se revisó que los mecanismos existan, no cómo se comportan. Corrección ([SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md)): inyectar la falla que cada mecanismo dice cubrir.
- **El servicio no se recupera tras la falla.** Reintentos y cola sostienen la sobrecarga; hace falta cortacircuitos, descarte de carga o pausa con azar.
- **Reintentar en cada capa.** Si tres capas reintentan tres veces, el factor se multiplica, no se suma (consecuencia de la fórmula de arriba, aplicada capa por capa).
- **Medir solo el cliente.** Desde allí se ve un éxito tardío; el costo está en la dependencia.

## Límites y cuándo no aplica

El factor de la figura son intentos *por petición de persona*; el efecto real sobre la dependencia depende además de cuántas peticiones llegan y de cuántas ya estaban en cola. En [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) nada se inyectó en un sistema real: tráfico, hilos y umbrales son construcciones del autor para mostrar el fenómeno. Y la amplificación no significa que reintentar sea malo: ante un fallo realmente transitorio y con pausa con azar, el reintento sigue siendo útil. Lo que importa es acotarlo (pocos intentos, plazo total, interrupción cuando hay señales de sobrecarga).

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
