# Entorno aislado

[↑ Glosario](../../README.md) · [← Entorno](./entorno.md) · [Entorno de vista previa →](./entorno-de-vista-previa.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Contexto de ejecución que limita lo que un proceso puede leer, escribir o contactar, con independencia de las reglas del agente.

Definición de trabajo de [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md): Copia independiente del intérprete y sus paquetes que evita mezclar dependencias con las del sistema.

## Por qué importa

En [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), el tema «Entornos aislados» importa porque limitan las consecuencias aunque las reglas fallen.

## Cómo funciona

Según [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md):

Un entorno aislado limita lo que un proceso puede alcanzar con independencia de lo que se le pida: qué directorios puede leer o escribir, a qué dominios puede conectarse, si tiene acceso a las credenciales del usuario. Puede ser el aislamiento de sistema operativo de la herramienta del agente, un contenedor, una máquina virtual o un espacio de trabajo desechable. Protege de los dos tipos de error que las reglas y los ganchos no cubren: el que no se previó y el que se previó mal. Tiene un límite que conviene escribir: lo que el entorno permite sigue siendo posible, y los datos que se montan dentro están a disposición del agente.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* revisa sus controles. Escribe el gancho de política con tres decisiones explícitas: termina con 0 solo cuando ha comprobado y permite, con 2 cuando bloquea, y cualquier otro resultado se interpreta en la capa que lo invoca como bloqueo, para lo cual añade una regla de denegación de las órdenes que el gancho vigila como segunda barrera.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md)) son:

- **El control «no hace nada» y no hay error** — causa: falla abierto: el error del gancho no bloquea. Corrección: usar el código de bloqueo para la política y probar la caída.
- **El agente carga mucho contexto al arrancar** — causa: todas las habilidades completas en memoria. Corrección: cargar descripciones y cuerpos bajo demanda.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un entorno aislado limita lo que un proceso puede alcanzar con independencia de lo que se le pida: qué directorios puede leer o escribir, a qué dominios puede conectarse, si tiene acceso a las credenciales del usuario. ([SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Contextos](../c/contextos.md), [Dependencia](../d/dependencia.md), [Paquete](../p/paquete.md), [Confinamiento de rutas](../c/confinamiento-de-rutas.md), [Deriva del README](../d/deriva-del-readme.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (32 clases más lo mencionan; las que más):

[SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), [SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Entornos aislados».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Claude Code: ganchos](https://code.claude.com/docs/en/hooks) — entrada, códigos de salida, errores que no bloquean y tiempos máximos; autoridad: documentación de Anthropic.
- [Claude Code: habilidades](https://code.claude.com/docs/en/skills) — estructura de una habilidad, carga bajo demanda y presupuesto de descripciones; autoridad: documentación de Anthropic.
- [Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents) — herramientas y ganchos por subagente; autoridad: documentación de Anthropic.
- [Claude Code: aislamiento (sandbox)](https://code.claude.com/docs/en/sandboxing) — aislamiento de sistema de archivos y red; autoridad: documentación de Anthropic.
- [Spec Kit — repositorio](https://github.com/github/spec-kit) — extensiones y catálogos, con la advertencia de revisar el código de la comunidad; autoridad: GitHub y mantenedores.

---

[↑ Glosario](../../README.md) · [← Entorno](./entorno.md) · [Entorno de vista previa →](./entorno-de-vista-previa.md)
