# Traspaso

[↑ Glosario](../../README.md) · [← Transición](./transicion.md) · [Traversal de rutas →](./traversal-de-rutas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Paso de un cambio de un equipo a otro, con su cola.

Definición de trabajo de [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md).

## Por qué importa

En [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), el tema «Colas y traspasos» importa porque cada traspaso añade espera, y la espera no es trabajo.

## Cómo funciona

Según [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md):

Cada vez que un cambio pasa a otro equipo se añade una cola. Si cada equipo está ocupado al 90 %, el tiempo de espera de un traspaso es muy superior al trabajo que se hace, y los esperas se suman. La teoría de colas lo expresa con una relación no lineal: la espera crece mucho cuando la utilización se acerca a 1. Reducir traspasos tiene más efecto que acelerar a cada equipo. La métrica práctica es el tiempo de entrega del cambio completo (de la idea a producción) y su distribución, no el tiempo de trabajo de cada equipo. La investigación DORA usa el plazo de entrega de cambios como una de sus medidas centrales.

Según [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md):

Ajusta la arquitectura a la organización (fronteras que coincidan con los equipos existentes), reduce los traspasos con interfaces estables y documenta la coordinación que inevitablemente hace falta.

## Ejemplo

Ejemplo de [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) (sección «Preguntas frecuentes»):

Ajusta la arquitectura a la organización (fronteras que coincidan con los equipos existentes), reduce los traspasos con interfaces estables y documenta la coordinación que inevitablemente hace falta.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El tiempo de entrega es varias veces el tiempo de trabajo** — causa: colas por traspasos con equipos muy ocupados. Corrección: reducir traspasos y la ocupación de los equipos. ([SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La figura dice que la espera crece más que linealmente con la ocupación y con los traspasos, y que acelerar a un equipo no ayuda si el cuello de botella es la cola. ([SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Carga cognitiva de un equipo](../c/carga-cognitiva-de-un-equipo.md), [Factor de autobús](../f/factor-de-autobus.md), [Ley de Conway](../l/ley-de-conway.md), [Maniobra inversa de Conway](../m/maniobra-inversa-de-conway.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Conway, «How Do Committees Invent?» (1968)](https://www.melconway.com/Home/Committees_Paper.html) — enunciado original de la ley; autoridad: Melvin Conway.
- [Fowler, «Conway's Law»](https://martinfowler.com/bliki/ConwaysLaw.html) — la ley y la maniobra inversa; autoridad: Martin Fowler.
- [Skelton y Pais, «Team Topologies»: conceptos clave](https://teamtopologies.com/key-concepts) — tipos de equipo, modos de interacción y carga cognitiva; autoridad: Team Topologies.
- [DORA, programa de investigación](https://dora.dev/research/) — capacidades técnicas y organizativas y rendimiento de la entrega; autoridad: DORA (Google Cloud).
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Transición](./transicion.md) · [Traversal de rutas →](./traversal-de-rutas.md)
