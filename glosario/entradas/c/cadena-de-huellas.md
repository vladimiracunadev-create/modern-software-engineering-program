# Cadena de huellas

[↑ Glosario](../../README.md) · [← Cadena de hashes](./cadena-de-hashes.md) · [Cadena de respuesta →](./cadena-de-respuesta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Registro en el que cada evento incorpora el hash del anterior, de modo que cambiar un evento invalida los siguientes.

Definición de trabajo de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md).

## Por qué importa

La clase donde se define, [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), existe con este propósito: la clase existe para que dejes de pensar la seguridad de un agente como el problema de que alguien le escriba algo malicioso y la pienses como el problema de que el agente lee texto de fuentes que no controlas y puede hacer cosas con lo que lee.

## Cómo funciona

Según [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md):

Un registro en texto plano se puede editar sin dejar rastro. Una **cadena de huellas** hace que cada evento incluya el hash del anterior: cambiar, borrar o reordenar un evento rompe todos los siguientes y la verificación lo detecta. Tiene dos límites que la clase mide. El primero es que quien puede reescribir el registro también puede recalcular la cadena desde el punto modificado, de modo que el resultado es una cadena válida; el segundo es que cortar los últimos eventos deja una cadena válida más corta. Ambos se resuelven con una **referencia externa**: la huella del último evento guardada en otro lugar, con otro control de acceso, o firmada. La cadena detecta lo que cambia en el medio; la referencia, lo que se corta o se reescribe entero.

Según [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* modela las amenazas de su agente que resume notas. Marca las capacidades: lee notas de docentes (contenido de terceros: N), accede a la base con datos de matrícula (D) y tiene una herramienta de envío de correos (E). Las tres coinciden. Rompe una: el resumen de notas pasa a un agente en cuarentena, sin base de datos ni correo, que devuelve un objeto con tres campos de valores acotados (tono, urgencia, un identificador de entrega); el agente con la base y el correo solo recibe ese objeto, nunca el texto de la nota. Añade un filtro normalizado que registra cada intento sospechoso sin bloquearlo, porque sirve para detectar campañas y no como defensa.

## Ejemplo

Ejemplo de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* modela las amenazas de su agente que resume notas. Marca las capacidades: lee notas de docentes (contenido de terceros: N), accede a la base con datos de matrícula (D) y tiene una herramienta de envío de correos (E). Las tres coinciden. Rompe una: el resumen de notas pasa a un agente en cuarentena, sin base de datos ni correo, que devuelve un objeto con tres campos de valores acotados (tono, urgencia, un identificador de entrega); el agente con la base y el correo solo recibe ese objeto, nunca el texto de la nota.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md)) son:

- **El filtro bloquea frases legítimas y deja pasar la orden** — causa: patrón amplio sin normalizar o patrón fijo. Corrección: usar el filtro como señal y no como control.
- **Una nota hace que el agente envíe un correo** — causa: las tres capacidades coinciden. Corrección: romper una o exigir aprobación en la salida.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: los filtros, el análisis de capacidades y la cadena de huellas son código real sobre datos sintéticos con semilla fija. No se invocó ningún modelo, no se midió la tasa de éxito de ninguna inyección, no se usó ninguna técnica efectiva contra ningún sistema y la orden de prueba es una palabra inocua.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Huella](../h/huella.md), [Registro](../r/registro.md), [Agente en cuarentena](../a/agente-en-cuarentena.md), [Contenido no confiable](./contenido-no-confiable.md), [Inyección indirecta de instrucciones](../i/inyeccion-indirecta-de-instrucciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Greshake et al., «Not what you've signed up for»](https://arxiv.org/abs/2302.12173) — inyección indirecta en aplicaciones reales; autoridad: preimpresión en arXiv, 2023.
- [Willison, «The lethal trifecta for AI agents»](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — regla de las tres capacidades; autoridad: ensayo de un autor reconocido.
- [Especificación MCP: buenas prácticas de seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) — ataques a sistemas con herramientas; autoridad: mantenedores de MCP.

---

[↑ Glosario](../../README.md) · [← Cadena de hashes](./cadena-de-hashes.md) · [Cadena de respuesta →](./cadena-de-respuesta.md)
