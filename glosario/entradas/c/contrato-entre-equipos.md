# Contrato entre equipos

[↑ Glosario](../../README.md) · [← Contrato ejecutable](./contrato-ejecutable.md) · [Contrato inteligente →](./contrato-inteligente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Interfaz documentada con propietario, versiones y vía de solicitud de cambios.

Definición de trabajo de [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md).

## Por qué importa

En [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), el tema «Contratos entre equipos» importa porque reduce relevos sin mezclar responsabilidades.

## Cómo funciona

Según [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), en la sección «Contratos entre equipos»:

Cuando una frontera inevitable existe (la exportación al ministerio la necesitan varios equipos), lo que baja el costo de cruzarla es el **contrato**: una interfaz documentada, versiones, un propietario claro y un acuerdo sobre cómo se solicitan cambios (por qué canal, con qué plazo, con qué información). Un contrato es mejor que una reunión porque no depende de quién esté disponible. Sin contrato, la frontera se negocia en cada cambio. Con un contrato demasiado rígido, el equipo que usa la interfaz espera semanas por una modificación trivial. Por eso el contrato incluye una vía de autoservicio: qué puede cambiar una persona de otro equipo en este módulo con la revisión de las dueñas, sin esperar su iteración.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo calcula el factor de camión de los cuatro módulos y encuentra que actas tiene factor 1. Acuerdan una política en tres pasos. Primero, un mapa de propiedad con responsable y segundo conocedor para cada módulo, y propiedad débil con `CODEOWNERS` para los dos módulos con reglas externas. Segundo, una rotación trimestral de quien responde de cada módulo en la guardia, de modo que cada persona sea principal en uno y secundaria en otro.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md)) son:

- **Un archivo espera semanas por una persona** — causa: propiedad fuerte sin segundo conocedor. Corrección: revisión obligatoria por una segunda persona y rotación.
- **Todo cambio requiere tres equipos** — causa: fronteras por capa. Corrección: reorganizar por dominio o abrir vía de autoservicio.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md)) son: Las definiciones son operativas para el equipo de plataforma educativa. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes primarias enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se analizó ningún repositorio, equipo ni guardia reales; el reparto del conocimiento, las capas tocadas, el costo por relevo y la llegada de avisos son construcciones del autor, y el modelo supone archivos independientes y avisos sin agrupamiento.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Solicitud de cambio](../s/solicitud-de-cambio.md), [Interfaz](../i/interfaz.md), [Propietario](../p/propietario.md), [Versión](../v/version.md), [Carga cognitiva](./carga-cognitiva.md), [Factor de camión](../f/factor-de-camion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Contratos entre equipos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Conway, «How Do Committees Invent?»](http://www.melconway.com/Home/Committees_Paper.html) — ley de Conway; autoridad: artículo original del autor.
- [Fowler, «Conway's Law»](https://martinfowler.com/bliki/ConwaysLaw.html) — síntesis de la ley y su uso; autoridad: autor del texto.
- [Team Topologies, conceptos clave](https://teamtopologies.com/key-concepts) — tipos de equipo, interacción y carga cognitiva; autoridad: autores del marco.
- [Avelino et al., «A novel approach for estimating Truck Factors»](https://doi.org/10.1109/ICPC.2016.7503718) — definición y estimación del factor de camión; autoridad: ICPC 2016.
- [Fowler, «Code Ownership»](https://martinfowler.com/bliki/CodeOwnership.html) — propiedad fuerte, débil y colectiva; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Contrato ejecutable](./contrato-ejecutable.md) · [Contrato inteligente →](./contrato-inteligente.md)
