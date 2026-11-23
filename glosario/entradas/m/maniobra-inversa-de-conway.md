# Maniobra inversa de Conway

[↑ Glosario](../../README.md) · [← Manifiesto de respaldo](./manifiesto-de-respaldo.md) · [Mantenimiento →](./mantenimiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Diseño deliberado de la estructura de equipos para producir la arquitectura deseada.

Definición de trabajo de [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md).

## Por qué importa

La clase donde se define, [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), existe con este propósito: la clase existe para que trates la estructura de los equipos como parte de la arquitectura: para que midas cuánta coordinación exige un reparto de módulos, cuánto conocimiento se pierde cuando alguien se va y cuánto se alarga un cambio que pasa por varios equipos.

## Cómo funciona

Según [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md):

La **maniobra inversa de Conway** consiste en diseñar la estructura de los equipos para producir la arquitectura deseada: si quieres que «notas» y «entregas» sean módulos independientes, organiza dos equipos con propiedad separada y una interfaz acordada. Funciona solo si el reparto sigue la afinidad real del sistema; reorganizar equipos sin mirar las dependencias reales no produce los límites buscados. Y tiene un coste: reorganizar es caro, desorienta y puede romper redes de confianza existentes. La decisión es otra más que se registra con su sacrificio y una señal de revisión.

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
- **Ver también:** [Arquitectura](../a/arquitectura.md), [Estructura](../e/estructura.md), [Carga cognitiva de un equipo](../c/carga-cognitiva-de-un-equipo.md), [Factor de autobús](../f/factor-de-autobus.md), [Ley de Conway](../l/ley-de-conway.md), [Traspaso](../t/traspaso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

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

[↑ Glosario](../../README.md) · [← Manifiesto de respaldo](./manifiesto-de-respaldo.md) · [Mantenimiento →](./mantenimiento.md)
