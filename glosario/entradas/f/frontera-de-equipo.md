# Frontera de equipo

[↑ Glosario](../../README.md) · [← Frontera de confirmación](./frontera-de-confirmacion.md) · [Frontera de módulo →](./frontera-de-modulo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Línea que separa lo que un equipo puede cambiar completo de lo que requiere relevo con otro.

Definición de trabajo de [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md).

## Por qué importa

En [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), el tema «Ley de Conway y fronteras de equipo» importa porque la estructura fija cuántos cambios cruzan equipos.

## Cómo funciona

[SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el equipo de plataforma educativa. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes primarias enlazadas al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo calcula el factor de camión de los cuatro módulos y encuentra que actas tiene factor 1. Acuerdan una política en tres pasos. Primero, un mapa de propiedad con responsable y segundo conocedor para cada módulo, y propiedad débil con `CODEOWNERS` para los dos módulos con reglas externas. Segundo, una rotación trimestral de quien responde de cada módulo en la guardia, de modo que cada persona sea principal en uno y secundaria en otro.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md)) son:

- **Un archivo espera semanas por una persona** — causa: propiedad fuerte sin segundo conocedor. Corrección: revisión obligatoria por una segunda persona y rotación.
- **Todo cambio requiere tres equipos** — causa: fronteras por capa. Corrección: reorganizar por dominio o abrir vía de autoservicio.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md)) son: Las definiciones son operativas para el equipo de plataforma educativa. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes primarias enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se analizó ningún repositorio, equipo ni guardia reales; el reparto del conocimiento, las capas tocadas, el costo por relevo y la llegada de avisos son construcciones del autor, y el modelo supone archivos independientes y avisos sin agrupamiento.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Relevo](../r/relevo.md), [Carga cognitiva](../c/carga-cognitiva.md), [Contrato entre equipos](../c/contrato-entre-equipos.md), [Factor de camión](./factor-de-camion.md), [Propiedad del código](../p/propiedad-del-codigo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Conway, «How Do Committees Invent?»](http://www.melconway.com/Home/Committees_Paper.html) — ley de Conway; autoridad: artículo original del autor.
- [Fowler, «Conway's Law»](https://martinfowler.com/bliki/ConwaysLaw.html) — síntesis de la ley y su uso; autoridad: autor del texto.
- [Team Topologies, conceptos clave](https://teamtopologies.com/key-concepts) — tipos de equipo, interacción y carga cognitiva; autoridad: autores del marco.
- [Avelino et al., «A novel approach for estimating Truck Factors»](https://doi.org/10.1109/ICPC.2016.7503718) — definición y estimación del factor de camión; autoridad: ICPC 2016.
- [Fowler, «Code Ownership»](https://martinfowler.com/bliki/CodeOwnership.html) — propiedad fuerte, débil y colectiva; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Frontera de confirmación](./frontera-de-confirmacion.md) · [Frontera de módulo →](./frontera-de-modulo.md)
