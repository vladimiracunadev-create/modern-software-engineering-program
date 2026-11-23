# Fuente única

[↑ Glosario](../../README.md) · [← Fuente de verdad y transformación](./fuente-de-verdad-y-transformacion.md) · [Fuentes de no determinismo →](./fuentes-de-no-determinismo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Lugar donde un dato se escribe una vez; las demás menciones lo enlazan, lo incluyen o se generan desde él.

Definición de trabajo de [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md).

## Por qué importa

En [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), el tema «Fuente única» importa porque cada copia añade una oportunidad de olvido; el coste crece con el número de copias.

## Cómo funciona

Según [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), en la sección «Fuente única»:

Una fuente única no obliga a que exista un solo documento; obliga a que cada dato tenga un solo lugar donde se escribe y a que los demás lo enlacen, lo incluyan o se generen desde él. En la plataforma, el tope del 50 % vive en la política académica versionada, y las demás páginas lo citan con enlace. Hay dos excepciones razonables: una página que debe leerse sin conexión (un PDF para el acta) puede copiar el dato si indica de dónde y en qué fecha se copió, y un tutorial puede fijar un valor de ejemplo si lo declara como ejemplo. Lo que no es razonable es copiar sin rastro: una copia sin procedencia no puede revisarse.

## Ejemplo

Ejemplo de [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) (sección «Caso conductor»):

El portal documental de la plataforma de entregas de tareas es el caso conductor de la [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md). Esta clase deja el primer artefacto: un inventario de tareas por audiencia y una fuente única para la regla de penalización. Las clases siguientes lo tipifican (`SE-206`), lo convierten en una puerta de entrada (`SE-207`), registran las decisiones que lo moldearon (`SE-208`), lo dibujan (`SE-209`), lo exponen como API (`SE-210`), lo hacen operable (`SE-211`), lo construyen como código (`SE-212`), lo hacen buscable (`SE-213`), lo preparan para máquinas (`SE-214`), recuperan lo que se perdió (`SE-215`) y lo versionan (`SE-216`).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md)) son:

- **Nadie encuentra «cómo cambiar el plazo» aunque existe la página** — causa: el título usa el nombre del componente («Módulo de calendario») y no la tarea. Corrección: reescribir el título con verbo y resultado y añadirla al índice de tareas.
- **Dos páginas dan topes de penalización distintos** — causa: el dato se copió en lugar de enlazarse. Corrección: elegir una fuente, enlazar desde las demás y añadir un comprobador de enlaces.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una fuente única no obliga a que exista un solo documento; obliga a que cada dato tenga un solo lugar donde se escribe y a que los demás lo enlacen, lo incluyan o se generen desde él. ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Audiencia](../a/audiencia.md), [Prueba de recorrido](../p/prueba-de-recorrido.md), [Tarea](../t/tarea.md), [Vista](../v/vista.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-232](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md), [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis](https://diataxis.fr/) — cuatro necesidades de quien usa documentación y las formas que les corresponden; autoridad: proyecto Diátaxis.
- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — define una guía por su orientación a un objetivo y no a un componente; autoridad: proyecto Diátaxis.
- [Google, Technical Writing One](https://developers.google.com/tech-writing/one) — curso con una unidad sobre audiencia; autoridad: Google for Developers.
- [Digital.gov, guías de lenguaje claro](https://www.plainlanguage.gov/) — escribir y probar el contenido para su audiencia; autoridad: Digital.gov.
- [Barrio-Cantalejo et al., «Validación de la Escala INFLESZ» (Anales del Sistema Sanitario de Navarra, 2008)](https://doi.org/10.4321/S1137-66272008000300004) — interpretación de un índice de legibilidad para español en textos para pacientes; autoridad: Anales del Sistema Sanitario de Navarra.

---

[↑ Glosario](../../README.md) · [← Fuente de verdad y transformación](./fuente-de-verdad-y-transformacion.md) · [Fuentes de no determinismo →](./fuentes-de-no-determinismo.md)
