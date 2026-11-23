# Referencia externa

[↑ Glosario](../../README.md) · [← Referencia débil](./referencia-debil.md) · [Referencia externa única →](./referencia-externa-unica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Huella del último evento de un registro guardada en otro lugar con otros controles de acceso.

Definición de trabajo de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md).

## Por qué importa

La clase donde se define, [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), existe con este propósito: la clase existe para que dejes de pensar la seguridad de un agente como el problema de que alguien le escriba algo malicioso y la pienses como el problema de que el agente lee texto de fuentes que no controlas y puede hacer cosas con lo que lee.

## Cómo funciona

Según [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md):

Un registro en texto plano se puede editar sin dejar rastro. Una **cadena de huellas** hace que cada evento incluya el hash del anterior: cambiar, borrar o reordenar un evento rompe todos los siguientes y la verificación lo detecta. Tiene dos límites que la clase mide. El primero es que quien puede reescribir el registro también puede recalcular la cadena desde el punto modificado, de modo que el resultado es una cadena válida; el segundo es que cortar los últimos eventos deja una cadena válida más corta. Ambos se resuelven con una **referencia externa**: la huella del último evento guardada en otro lugar, con otro control de acceso, o firmada. La cadena detecta lo que cambia en el medio; la referencia, lo que se corta o se reescribe entero.

Según [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md):

Traslada el análisis a otro dominio (por ejemplo, un agente que lee correos de proveedores y registra facturas): cambia las fuentes, los datos y las herramientas y conserva el procedimiento de marcar las tres capacidades, romper una, tratar el filtro como señal y registrar con una cadena de huellas y una referencia externa. La transferencia está lograda cuando puedes decir qué forma de esconder una orden no detectaría tu filtro y qué limita el daño cuando ocurre, no cuando la tabla se parece a la de *Avisos*.

## Ejemplo

Ejemplo de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) (sección «Caso conductor»):

El servicio *Avisos* es el caso conductor de la [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md). Esta clase deja el décimo artefacto: el modelo de amenazas con las tres capacidades, la política que rompe una, el filtro como señal y el registro de auditoría con su referencia externa. `SE-575` reúne todo en un taller: detener un agente que se descontrola, recuperarlo y evaluarlo con rigor. Cambia después un solo dato, la proporción de tareas que necesitan las tres capacidades, y observa a partir de qué valor la aprobación humana en el paso de salida se convierte en el cuello de botella.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El registro «verifica» pero está manipulado** — causa: sin referencia externa. Corrección: guardar la huella final fuera, con otros permisos. ([SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: los filtros, el análisis de capacidades y la cadena de huellas son código real sobre datos sintéticos con semilla fija. No se invocó ningún modelo, no se midió la tasa de éxito de ninguna inyección, no se usó ninguna técnica efectiva contra ningún sistema y la orden de prueba es una palabra inocua.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Huella](../h/huella.md), [Registro](./registro.md), [Agente en cuarentena](../a/agente-en-cuarentena.md), [Cadena de huellas](../c/cadena-de-huellas.md), [Contenido no confiable](../c/contenido-no-confiable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Greshake et al., «Not what you've signed up for»](https://arxiv.org/abs/2302.12173) — inyección indirecta en aplicaciones reales; autoridad: preimpresión en arXiv, 2023.
- [Willison, «The lethal trifecta for AI agents»](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — regla de las tres capacidades; autoridad: ensayo de un autor reconocido.
- [Especificación MCP: buenas prácticas de seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) — ataques a sistemas con herramientas; autoridad: mantenedores de MCP.

---

[↑ Glosario](../../README.md) · [← Referencia débil](./referencia-debil.md) · [Referencia externa única →](./referencia-externa-unica.md)
