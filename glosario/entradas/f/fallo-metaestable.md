# Fallo metaestable

[↑ Glosario](../../README.md) · [← Fallo latente](./fallo-latente.md) · [Fallo parcial →](./fallo-parcial.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Un **fallo metaestable** es un estado degradado que persiste después de que desapareció el disparador que lo causó, porque un efecto de refuerzo lo sostiene. Es la definición de [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md); [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) lo presenta como un estado de sobrecarga que se sostiene por sí mismo cuando ya no está su causa inicial. El trabajo de Bronson et al. (HotOS 2021) lo formaliza como una clase de falla.

## Por qué importa

Rompe la intuición «arreglé la causa, el sistema se recuperará». En un fallo metaestable, retirar el disparador (un pico de carga, una dependencia lenta) no alcanza: el sistema sigue enfermo hasta que alguien interrumpe el ciclo. Cambia las prácticas de recuperación (hay que tener una acción para romper el ciclo, no solo para quitar la causa) y de diseño (evitar efectos de refuerzo).

## Cómo funciona

Hay tres elementos: un **disparador** temporal, un **estado degradado** y un **bucle de refuerzo** que alimenta el estado después del disparador. El refuerzo más común, según [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), son los reintentos. La falla termina, pero la cola que se formó sigue llena y las esperas siguen agotándose; entonces cada petición se reintenta y la carga efectiva sigue siendo triple de la capacidad. El trabajo útil por segundo cae mientras la carga ofrecida sube.

El sistema vuelve a ser sano solo si algo interrumpe el ciclo: un cortacircuitos que corta el flujo, un descarte de carga o un reinicio. [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) cita el libro de SRE para el descarte de carga y las respuestas degradadas como formas de cortar el ciclo. La causa estructural es que el sistema tiene dos equilibrios estables, uno sano y otro degradado, y el disparador solo lo empuja del primero al segundo.

## Ejemplo

El experimento de [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) (tiempo virtual, datos del autor): entre los 30 y los 60 s se retira la mitad de los hilos de la dependencia (la capacidad pasa de 200 a 100 peticiones por segundo, con 90 de demanda) y se mide cada 10 s la fracción de peticiones correctas.

- La configuración **A**, sin reintentos, no se entera: 90 caben en 100.
- La **C**, con reintentos y sin protección, cae a 10 % durante la falla y, cuando la dependencia recupera su capacidad a los 60 s, **sigue en 0 % durante los 60 s restantes**: cada petición agota otra vez la espera de 250 ms porque la cola de intentos viejos no se vacía, y cada fracaso se reintenta.
- La **E**, con cortacircuitos, baja a 44 % y sube a 100 % a los 75 s.

## Errores y confusiones comunes

- **Todo parece resiliente en el documento.** Se revisó la presencia de mecanismos, no su comportamiento; corrección de [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md): inyectar la falla que cada mecanismo dice cubrir.
- **«El servicio no se recupera tras la falla».** Reintentos y cola mantienen la sobrecarga; hay que cortar el ciclo con cortacircuitos, descarte de carga o pausa con azar.
- **Buscar la causa raíz en el disparador.** El disparador explica el inicio; lo que mantiene el fallo es el refuerzo.
- **Confundirlo con una falla en cascada.** La cascada propaga a otros componentes; la metaestabilidad persiste sin disparador.

## Límites y cuándo no aplica

En [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) no se inyectó ninguna falla en un sistema real: la dependencia de 8 hilos, el tráfico de 90 peticiones por segundo, las cinco configuraciones y las seis fallas son construcciones del autor, y los umbrales se eligieron para mostrar el fenómeno. El concepto aplica donde existe un bucle de refuerzo y capacidad limitada; un sistema sin reintentos ni colas persistentes se recupera al cesar la causa. La detección real suele llegar tarde, porque desde fuera el estado degradado parece una falla en curso.

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
