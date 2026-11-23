# Tres capacidades

[↑ Glosario](../../README.md) · [← Trazas comparables](./trazas-comparables.md) · [Triage y contención →](./triage-y-contencion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Acceso a datos privados, exposición a contenido no confiable y capacidad de comunicación hacia fuera.

Definición de trabajo de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md).

## Por qué importa

En [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), el tema «Las tres capacidades» importa porque su coincidencia hace posible la fuga; romper una la evita.

## Cómo funciona

Según [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md):

Reproduce el fallo clásico de la clase: **un agente con las tres capacidades que obedece una orden escondida en un contenido**. Ejecuta el filtro de frase fija sobre las cuarenta órdenes de prueba.

Según [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md):

Traslada el análisis a otro dominio (por ejemplo, un agente que lee correos de proveedores y registra facturas): cambia las fuentes, los datos y las herramientas y conserva el procedimiento de marcar las tres capacidades, romper una, tratar el filtro como señal y registrar con una cadena de huellas y una referencia externa. La transferencia está lograda cuando puedes decir qué forma de esconder una orden no detectaría tu filtro y qué limita el daño cuando ocurre, no cuando la tabla se parece a la de *Avisos*.

## Ejemplo

Ejemplo de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) (sección «Caso conductor»):

El servicio *Avisos* es el caso conductor de la [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md). Esta clase deja el décimo artefacto: el modelo de amenazas con las tres capacidades, la política que rompe una, el filtro como señal y el registro de auditoría con su referencia externa. `SE-575` reúne todo en un taller: detener un agente que se descontrola, recuperarlo y evaluarlo con rigor. Cambia después un solo dato, la proporción de tareas que necesitan las tres capacidades, y observa a partir de qué valor la aprobación humana en el paso de salida se convierte en el cuello de botella.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una nota hace que el agente envíe un correo** — causa: las tres capacidades coinciden. Corrección: romper una o exigir aprobación en la salida. ([SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Regresión:** añade una prueba que inserte la orden de prueba en una nota y exija que no se envíe ningún correo sin aprobación, y rompe una de las tres capacidades. ([SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contenido no confiable](../c/contenido-no-confiable.md), [Capacidad](../c/capacidad.md), [Exposición](../e/exposicion.md), [Agente en cuarentena](../a/agente-en-cuarentena.md), [Cadena de huellas](../c/cadena-de-huellas.md), [Inyección indirecta de instrucciones](../i/inyeccion-indirecta-de-instrucciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md), [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-598](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Willison, «The lethal trifecta for AI agents»](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — regla de las tres capacidades; autoridad: ensayo de un autor reconocido.
- [Greshake et al., «Not what you've signed up for»](https://arxiv.org/abs/2302.12173) — inyección indirecta en aplicaciones reales; autoridad: preimpresión en arXiv, 2023.
- [Especificación MCP: buenas prácticas de seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) — ataques a sistemas con herramientas; autoridad: mantenedores de MCP.

---

[↑ Glosario](../../README.md) · [← Trazas comparables](./trazas-comparables.md) · [Triage y contención →](./triage-y-contencion.md)
