# Fatiga de aprobación

[↑ Glosario](../../README.md) · [← Fatiga de alertas](./fatiga-de-alertas.md) · [Fecha de revisión →](./fecha-de-revision.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Pérdida de atención de quien aprueba cuando las solicitudes son muchas y casi siempre inocuas.

Definición de trabajo de [SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md).

## Por qué importa

En [SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md), el tema «Fatiga de aprobación» importa porque preguntar de más reduce la atención en lo importante.

## Cómo funciona

[SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Caso medido en la sección «La fatiga de aprobación» de [SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md):

Cada solicitud consume atención, y la atención de quien responde no se mantiene constante cuando las solicitudes son muchas, parecidas y casi siempre inocuas. El modelo de la clase es deliberadamente simple: la probabilidad de detectar una acción peligrosa empieza en 0,95 y baja 0,012 por cada aprobación seguida sin incidentes, hasta un mínimo de 0,35. No es una medida de ninguna persona; es una forma de mostrar una dinámica plausible: cuanto más se aprueba sin incidentes, menos se revisa. De esta dinámica se derivan tres consecuencias de diseño.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md)) son:

- **Se aprueban acciones sin leerlas** — causa: demasiadas solicitudes, todas iguales. Corrección: reducir el número y separar las de riesgo.
- **Una aprobación no permite decidir** — causa: falta el efecto, el número de afectados o la reversibilidad. Corrección: plantilla con cinco preguntas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: la aprobación y las compensaciones son simulaciones con semilla fija y el diario de deshacer es código real sobre archivos en un directorio temporal. No participó ninguna persona, no se invocó ningún modelo y no se probó el diario con enlaces simbólicos, permisos especiales ni caídas a mitad de acción.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Acción compensable](../a/accion-compensable.md), [Acción irreversible](../a/accion-irreversible.md), [Acción reversible](../a/accion-reversible.md), [Compensación](../c/compensacion.md), [Persona en el bucle](../p/persona-en-el-bucle.md), [Saga](../s/saga.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Especificación MCP: herramientas](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) — persona en el bucle con capacidad de denegar; autoridad: mantenedores de MCP.
- [Anuncio de la especificación MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — rondas múltiples para confirmaciones; autoridad: mantenedores de MCP.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — puntos de control y supervisión humana; autoridad: Anthropic.
- [Garcia-Molina y Salem, «Sagas»](https://doi.org/10.1145/38713.38742) — compensaciones; autoridad: ACM SIGMOD, 1987.

---

[↑ Glosario](../../README.md) · [← Fatiga de alertas](./fatiga-de-alertas.md) · [Fecha de revisión →](./fecha-de-revision.md)
