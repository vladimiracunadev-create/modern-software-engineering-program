# Confinamiento

[↑ Glosario](../../README.md) · [← Configuración y precedencia](./configuracion-y-precedencia.md) · [Confinamiento de rutas →](./confinamiento-de-rutas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Restricción de las rutas que el agente puede tocar.

Definición de trabajo de [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md): Limitación de lo que una operación puede tocar a una región resuelta (un directorio, un dominio).

## Por qué importa

En [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), el tema «Confinamiento por rutas» importa porque impide el daño fuera del proyecto con un costo bajo.

## Cómo funciona

Según [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md):

El confinamiento por rutas resuelve cada ruta que el agente quiere leer o escribir (siguiendo `..` y enlaces) y la compara con la raíz permitida. En el laboratorio, el confinamiento bloquea dos de las cinco acciones (el borrado con `../home/config.txt` y la escritura con una ruta absoluta) y deja los dos archivos «personales» intactos. Es barato y exacto en lo que cubre. No cubre un proceso hijo que el agente lance con una herramienta permitida: ese proceso no pasa por la comprobación de rutas. El aislamiento que sí lo cubre, un sandbox del sistema operativo que restringe el sistema de archivos y la red del proceso entero, es otro nivel de control, y Anthropic lo presenta como la forma de reducir los permisos que hay que pedir sin perder seguridad.

Según [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md):

Lo cubre y lo supera para procesos hijos y red: restringe lo que el proceso puede hacer en el sistema. El confinamiento por rutas es un control del harness que decide qué *llamadas* acepta; un contenedor decide qué puede *ocurrir*. Se complementan.

## Ejemplo

Ejemplo de [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) (sección «Ejemplo mínimo»):

El confinamiento por resolución de rutas:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md)) son: Se ejecutaron cuatro configuraciones sobre quince archivos de texto con acciones sencillas, en Windows 11 con CPython 3.12.9 y Git 2.55. No se midió ningún sandbox del sistema operativo, ningún escape, ningún enlace simbólico ni ningún proceso hijo. El siguiente paso, `SE-583`, trata cómo decidir qué cambios se aceptan: las compuertas de verificación y un menú único que agente y persona ejecutan igual.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Dominio](../d/dominio.md), [Operación](../o/operacion.md), [Región](../r/region.md), [Aislamiento del sistema operativo](../a/aislamiento-del-sistema-operativo.md), [Alcance](../a/alcance.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), [SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Saltzer y Schroeder](https://doi.org/10.1109/PROC.1975.9939) — mínimo privilegio y protección de la información; autoridad: Proceedings of the IEEE, 1975.
- [Claude Code: permisos](https://code.claude.com/docs/en/permissions) — orden de evaluación, órdenes compuestas y fragilidad de los patrones sobre argumentos; autoridad: documentación de Anthropic.
- [Claude Code: aislamiento (sandbox)](https://code.claude.com/docs/en/sandboxing) — aislamiento de sistema de archivos y red a nivel del sistema operativo; autoridad: documentación de Anthropic.
- [OWASP Top 10 para aplicaciones con LLM](https://genai.owasp.org/llm-top-10/) — riesgos, entre ellos la agencia excesiva; autoridad: proyecto OWASP GenAI.

---

[↑ Glosario](../../README.md) · [← Configuración y precedencia](./configuracion-y-precedencia.md) · [Confinamiento de rutas →](./confinamiento-de-rutas.md)
