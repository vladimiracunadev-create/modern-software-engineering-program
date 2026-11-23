# Factor de autobús

[↑ Glosario](../../README.md) · [← Factor contribuyente](./factor-contribuyente.md) · [Factor de camión →](./factor-de-camion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Número de personas que pueden irse antes de que un proyecto se detenga por falta de conocimiento.

Definición de trabajo de [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md).

## Por qué importa

La clase donde se define, [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), existe con este propósito: la clase existe para que trates la estructura de los equipos como parte de la arquitectura: para que midas cuánta coordinación exige un reparto de módulos, cuánto conocimiento se pierde cuando alguien se va y cuánto se alarga un cambio que pasa por varios equipos.

## Cómo funciona

Según [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md):

La **propiedad** define quién decide sobre un módulo, y el **conocimiento** quién lo entiende: pueden no coincidir. Cuando un único integrante concentra el conocimiento de un módulo, una salida lo deja huérfano. El riesgo se estima con el «factor de autobús» (cuántas personas pueden irse antes de que el proyecto se detenga) y se reduce con rotación, revisión por pares, pares de programación y documentación que sirva de hecho. Dos personas por módulo bajan el riesgo de forma muy marcada; la tercera aporta menos. Las salidas no son independientes (reorganizaciones, cierres de proyecto), así que conviene un margen.

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
- **Ver también:** [Carga cognitiva de un equipo](../c/carga-cognitiva-de-un-equipo.md), [Ley de Conway](../l/ley-de-conway.md), [Maniobra inversa de Conway](../m/maniobra-inversa-de-conway.md), [Traspaso](../t/traspaso.md).
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

[↑ Glosario](../../README.md) · [← Factor contribuyente](./factor-contribuyente.md) · [Factor de camión →](./factor-de-camion.md)
