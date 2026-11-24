# Entorno aislado

[↑ Glosario](../../README.md) · [← Entorno](./entorno.md) · [Entorno de vista previa →](./entorno-de-vista-previa.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Un **entorno aislado** es un contexto de ejecución que limita lo que un proceso puede leer, escribir o contactar, con independencia de las reglas que se le den al agente o al programa. Es el sentido principal de [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) (habilidades, extensiones, ganchos y entornos aislados para agentes). [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) usa la misma palabra en un sentido más modesto: una copia independiente del intérprete y sus paquetes (un entorno virtual) que evita mezclar dependencias con las del sistema.

## Por qué importa

Cambia dónde se pone la barrera. Las reglas y los ganchos dependen de que se hayan previsto bien; el aislamiento limita las consecuencias aunque fallen. Según [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), protege de los dos tipos de error que reglas y ganchos no cubren: el que no se previó y el que se previó mal.

## Cómo funciona

El entorno acota qué directorios puede leer o escribir el proceso, a qué dominios puede conectarse y si tiene acceso a las credenciales de la persona. Puede ser el aislamiento del sistema operativo que ofrece la herramienta del agente, un contenedor, una máquina virtual o un espacio de trabajo desechable. Funciona por **capas independientes**: una regla de denegación sobre el comando, un gancho de política y el aislamiento actúan como barreras sucesivas, de modo que el fallo de una no deja todo abierto.

La capa de política (el gancho) debe fallar cerrado: [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) muestra el defecto de un control que «no hace nada» sin error porque falla abierto; la corrección es que el gancho termine con éxito solo cuando comprobó y permite, y que cualquier otro resultado se interprete como bloqueo. El aislamiento de [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) es otro mecanismo con otro alcance: separa paquetes, no limita permisos de seguridad.

## Ejemplo

En el escenario hipotético de [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), el equipo de *Avisos* revisa sus controles. El gancho de política tiene tres decisiones explícitas (éxito solo si comprobó y permite; código de bloqueo si bloquea; cualquier otro resultado se interpreta como bloqueo) y se añade una regla de denegación de las órdenes que el gancho vigila, como segunda barrera. El entorno aislado es la tercera.

## Errores y confusiones comunes

- **El control no hace nada y no hay error.** Falla abierto: usar el código de bloqueo para la política y probar la caída.
- **Confundir entorno virtual con aislamiento de seguridad.** Separa dependencias, no limita lo que el proceso puede alcanzar.
- **Dar acceso a las credenciales por comodidad.** Anula el valor del aislamiento.
- **Cargar todas las habilidades en memoria al arrancar.** Es un problema de contexto, no de aislamiento; cargarlas bajo demanda.

## Límites y cuándo no aplica

El aislamiento tiene un coste de fricción: lo que un proceso necesita y el entorno bloquea hay que permitirlo con criterio. No impide un uso indebido de lo que sí se le dejó alcanzar, y un contenedor mal configurado puede dar una falsa seguridad. El escenario de [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) es hipotético, sin datos reales.

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
