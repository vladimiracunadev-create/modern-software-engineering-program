# Ley de Conway

[↑ Glosario](../../README.md) · [← Ley de Amdahl](./ley-de-amdahl.md) · [Ley de Fitts →](./ley-de-fitts.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Observación de que la estructura de un sistema copia la estructura de comunicación de la organización que lo diseña.

Definición de trabajo de [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md).

## Por qué importa

En [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), el tema «Ley de Conway» importa porque explica por qué la arquitectura copia la organización.

## Cómo funciona

Según [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), en la sección «Ley de Conway»:

Conway observó en 1968 que las organizaciones que diseñan sistemas producen diseños que son copias de su estructura de comunicación. Si cuatro equipos trabajan en un compilador, saldrá un compilador de cuatro pasadas. La razón es práctica: las fronteras técnicas que son fáciles de mantener coinciden con las fronteras entre grupos que se hablan poco, y las que cruzan equipos exigen coordinación continua que, con el tiempo, el trabajo evita. Entender la ley sirve para dos cosas: explicar por qué la arquitectura actual se parece al organigrama y anticipar qué fronteras se erosionarán.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md):

El equipo de la plataforma calcula el grafo de dependencias y el historial de cambios conjuntos de los 24 módulos y encuentra cuatro comunidades (entregas, evaluación, identidad, notificaciones). Propone reorganizar los cuatro equipos por comunidad y registra en un ADR el sacrificio (se pierde el equipo de datos común y habrá cuatro formas de modelar datos) y la señal de revisión (si más del 25 % de los cambios cruza equipos tras dos trimestres).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md)) son:

- **Cada cambio de negocio involucra varios equipos** — causa: equipos organizados por capa técnica. Corrección: reorganizar por flujo de valor o comunidad de dependencias.
- **La arquitectura se «erosiona» entre dos equipos** — causa: la frontera técnica cruza un límite que exige coordinación constante. Corrección: mover la frontera o ponerla donde los equipos coinciden.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se observó ningún equipo, repositorio ni persona: el grafo con cuatro comunidades, las probabilidades de arista, las salidas independientes y las colas M/M/1 son modelos del autor. La siguiente clase es un taller que revisa una arquitectura completa contra escenarios.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estructura](../e/estructura.md), [Observación](../o/observacion.md), [Organización](../o/organizacion.md), [Carga cognitiva de un equipo](../c/carga-cognitiva-de-un-equipo.md), [Factor de autobús](../f/factor-de-autobus.md), [Maniobra inversa de Conway](../m/maniobra-inversa-de-conway.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md).

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

[↑ Glosario](../../README.md) · [← Ley de Amdahl](./ley-de-amdahl.md) · [Ley de Fitts →](./ley-de-fitts.md)
