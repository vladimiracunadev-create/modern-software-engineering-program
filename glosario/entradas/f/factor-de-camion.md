# Factor de camión

[↑ Glosario](../../README.md) · [← Factor de autobús](./factor-de-autobus.md) · [Factor de carga y crecimiento →](./factor-de-carga-y-crecimiento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

El **factor de camión** (*bus factor*) es el número mínimo de personas cuya salida deja sin conocedor a una parte significativa del sistema. [SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md) lo presenta así; [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) lo define como el mínimo de personas que, al irse, dejan a un proyecto o a un archivo sin conocimiento clave, y [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) como el número cuya salida dejaría al proyecto sin conocimiento suficiente de una parte esencial. La versión operativa más precisa es la de Avelino et al., que [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) recoge: el mínimo de autoras cuya salida deja abandonados a más de la mitad de los archivos de un repositorio, con el abandono medido por la autoría.

## Por qué importa

Cambia dónde se invierte en repartir conocimiento. Mide cuánto depende el conocimiento de pocas personas, y por eso orienta decisiones concretas: dónde exigir una segunda persona que conozca el código, qué rotaciones hacer y qué documentar primero. Un factor de 1 significa que una sola salida deja zonas del sistema sin nadie que las entienda.

## Cómo funciona

El cálculo operativo prueba combinaciones de salidas: se retiran personas del conjunto de autoras hasta que más de la mitad de los archivos queda sin ninguna autora que los conozca; el número mínimo de retiradas necesarias es el factor. La clase incluye un fragmento que lo calcula para un repositorio pequeño y pide predecir el resultado antes de ejecutarlo.

La definición tiene límites claros, que [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) subraya: la autoría en el historial no equivale a conocimiento (alguien pudo escribir un archivo y olvidarlo, o conocer a fondo uno que nunca tocó). Es, por tanto, una aproximación que conviene contrastar con una conversación y no tomar como medida exacta. Los síntomas de un factor bajo, según [SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), son un archivo que espera semanas por una persona (propiedad fuerte sin segundo conocedor; corrección: revisión obligatoria por una segunda persona y rotación) o fronteras por capa que obligan a tres equipos en cada cambio (corrección: organizar por dominio).

## Ejemplo

En el taller de [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md), se reconstruye conocimiento perdido de un módulo cuya única autora se fue. El cálculo del factor ya lo anticipaba: el módulo dependía de una sola persona. La recuperación pasa por leer el historial, documentar decisiones y asignar un segundo conocedor.

## Errores y confusiones comunes

- **Equiparar autoría con conocimiento.** El historial es una aproximación.
- **Usarlo como ranking de personas.** Mide riesgo del sistema, no valor individual.
- **Corregirlo solo documentando.** Se necesita práctica compartida: revisión cruzada y rotación.
- **Calcularlo una vez.** Cambia con cada salida e ingreso.

## Límites y cuándo no aplica

No ve el conocimiento que no deja huella en el repositorio (operación, decisiones de negocio, contexto de clientes). En equipos de una persona es 1 por definición. Y un factor alto no garantiza que el conocimiento sea bueno, solo que está repartido.

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
