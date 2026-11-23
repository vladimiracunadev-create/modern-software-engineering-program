# Factor de camión

[↑ Glosario](../../README.md) · [← Factor de autobús](./factor-de-autobus.md) · [Factor de carga y crecimiento →](./factor-de-carga-y-crecimiento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Número mínimo de personas cuya salida deja sin conocedor a más de la mitad de los archivos según la autoría registrada.

Definición de trabajo de [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md): Número de personas cuya salida dejaría al proyecto sin conocimiento suficiente de una parte esencial.
- En [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md): Número mínimo de personas que, al irse, dejan a un proyecto o a un archivo sin conocimiento clave.

## Por qué importa

En [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), el tema «Factor de camión» importa porque mide cuánto depende el conocimiento de pocas personas.

## Cómo funciona

Según [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), en la sección «Factor de camión»:

El **factor de camión** (bus factor) es el número mínimo de personas cuya salida deja sin conocedor a una parte significativa del sistema. Avelino et al. lo definen sobre los archivos de un repositorio: el mínimo de autoras cuya salida deja abandonados a más de la mitad de los archivos, con el abandono medido por la autoría. Es una definición operativa con límites claros: la autoría en el historial no equivale a conocimiento (alguien pudo escribir un archivo y olvidarlo; otra persona pudo aprenderlo leyéndolo), y no distingue archivos críticos de triviales. Aun así, es útil como alarma: si el factor es uno o dos, la pregunta es qué hacer. Las palancas son tres:

## Ejemplo

Ejemplo de [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el factor de camión de un repositorio pequeño probando combinaciones de salidas. Antes de ejecutarlo, predice qué devuelve.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md)) son:

- **Un archivo espera semanas por una persona** — causa: propiedad fuerte sin segundo conocedor. Corrección: revisión obligatoria por una segunda persona y rotación.
- **Todo cambio requiere tres equipos** — causa: fronteras por capa. Corrección: reorganizar por dominio o abrir vía de autoservicio.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **factor de camión** (bus factor) es el número mínimo de personas cuya salida deja sin conocedor a una parte significativa del sistema. ([SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [ADR retrospectivo](../a/adr-retrospectivo.md), [Archivo huérfano](../a/archivo-huerfano.md), [Búsqueda por contenido](../b/busqueda-por-contenido.md), [Churn](../c/churn.md), [Código muerto](../c/codigo-muerto.md), [Conocimiento perdido](../c/conocimiento-perdido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.
- [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Avelino et al., «A novel approach for estimating Truck Factors»](https://doi.org/10.1109/ICPC.2016.7503718) — definición y estimación del factor de camión; autoridad: ICPC 2016.
- [Conway, «How Do Committees Invent?»](http://www.melconway.com/Home/Committees_Paper.html) — ley de Conway; autoridad: artículo original del autor.
- [Fowler, «Conway's Law»](https://martinfowler.com/bliki/ConwaysLaw.html) — síntesis de la ley y su uso; autoridad: autor del texto.
- [Team Topologies, conceptos clave](https://teamtopologies.com/key-concepts) — tipos de equipo, interacción y carga cognitiva; autoridad: autores del marco.
- [Fowler, «Code Ownership»](https://martinfowler.com/bliki/CodeOwnership.html) — propiedad fuerte, débil y colectiva; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Factor de autobús](./factor-de-autobus.md) · [Factor de carga y crecimiento →](./factor-de-carga-y-crecimiento.md)
