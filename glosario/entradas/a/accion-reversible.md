# Acción reversible

[↑ Glosario](../../README.md) · [← Acción irreversible](./accion-irreversible.md) · [Acción verificable →](./accion-verificable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Acción cuyo efecto puede deshacerse restaurando el estado anterior que el sistema controla.

Definición de trabajo de [SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md).

## Por qué importa

La clase donde se define, [SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md), existe con este propósito: la clase existe para que diseñes la intervención humana como un componente con sus propias propiedades y no como un botón de «aceptar» que se pone al final.

## Cómo funciona

[SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* clasifica las acciones de su agente. Leer, buscar y listar son reversibles por no tener efecto. Escribir, borrar y renombrar archivos del proyecto son reversibles con un diario previo; confirmar cambios en una rama local lo es con el sistema de control de versiones. Empujar a un remoto y escribir en la base de pruebas son compensables. Enviar correos, escribir en la base real y publicar son irreversibles.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md)) son:

- **Se aprueban acciones sin leerlas** — causa: demasiadas solicitudes, todas iguales. Corrección: reducir el número y separar las de riesgo.
- **Una aprobación no permite decidir** — causa: falta el efecto, el número de afectados o la reversibilidad. Corrección: plantilla con cinco preguntas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: la aprobación y las compensaciones son simulaciones con semilla fija y el diario de deshacer es código real sobre archivos en un directorio temporal. No participó ninguna persona, no se invocó ningún modelo y no se probó el diario con enlaces simbólicos, permisos especiales ni caídas a mitad de acción.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Estado](../e/estado.md), [Acción compensable](./accion-compensable.md), [Acción irreversible](./accion-irreversible.md), [Compensación](../c/compensacion.md), [Fatiga de aprobación](../f/fatiga-de-aprobacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Especificación MCP: herramientas](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) — persona en el bucle con capacidad de denegar; autoridad: mantenedores de MCP.
- [Anuncio de la especificación MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — rondas múltiples para confirmaciones; autoridad: mantenedores de MCP.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — puntos de control y supervisión humana; autoridad: Anthropic.
- [Garcia-Molina y Salem, «Sagas»](https://doi.org/10.1145/38713.38742) — compensaciones; autoridad: ACM SIGMOD, 1987.

---

[↑ Glosario](../../README.md) · [← Acción irreversible](./accion-irreversible.md) · [Acción verificable →](./accion-verificable.md)
