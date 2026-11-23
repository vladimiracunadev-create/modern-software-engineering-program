# Playbook

[↑ Glosario](../../README.md) · [← Platform Engineer](./platform-engineer.md) · [Plazo →](./plazo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Guía de respuesta con preguntas y criterios de decisión para situaciones abiertas o poco conocidas.

Definición de trabajo de [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md).

## Por qué importa

En [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md), el tema «Runbook y playbook» importa porque uno se ejecuta, el otro se piensa; confundirlos da procedimientos rígidos para casos abiertos.

## Cómo funciona

Según [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md):

Un runbook es un procedimiento para una situación que ya se conoce: «la cola de importación está atascada y el servicio responde». Un playbook es una guía de respuesta para situaciones más abiertas: «el servicio devuelve errores y no sabemos por qué»; contiene preguntas, criterios de decisión y quién llamar. La diferencia práctica es el grado de libertad: el runbook pide ejecutar, el playbook pide pensar con una estructura. Confundirlos produce procedimientos que parecen precisos y se aplican a situaciones que no son las suyas. Un buen playbook lleva a un runbook cuando la situación se reconoce, y a escalar cuando no.

Según [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md):

La plataforma de entregas mantiene tres runbooks (cola de importación atascada, certificado próximo a expirar, base de datos sin espacio) y un playbook («el servicio responde con errores»). Cada paso lleva precondición, acción, verificación y reversión, y está marcado como idempotente o no. Una integración continua ejecuta el linter en cada cambio y falla ante órdenes destructivas sin confirmación o secretos. Tras cada incidente, la revisión posterior registra qué paso falló o faltaba y si el síntoma estaba cubierto.

## Ejemplo

Ejemplo de [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) (sección «Ejemplo profesional»):

La plataforma de entregas mantiene tres runbooks (cola de importación atascada, certificado próximo a expirar, base de datos sin espacio) y un playbook («el servicio responde con errores»). Cada paso lleva precondición, acción, verificación y reversión, y está marcado como idempotente o no. Una integración continua ejecuta el linter en cada cambio y falla ante órdenes destructivas sin confirmación o secretos. Tras cada incidente, la revisión posterior registra qué paso falló o faltaba y si el síntoma estaba cubierto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un incidente nuevo deja a la guardia sin guía** — causa: solo hay runbooks, no playbook. Corrección: escribir un playbook de preguntas y criterios de escalada. ([SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de las guías de manejo de incidentes enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se operó ningún servicio ni se midió el tiempo de resolución de nadie: el estado es un diccionario, el reparto de incidentes y el 8 % de tipos nuevos son supuestos, y el linter se afinó con los casos que luego se usaron para probarlo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-210](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Idempotencia](../i/idempotencia.md), [Retroceso](../r/retroceso.md), [Runbook](../r/runbook.md), [Verificación](../v/verificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-210](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md), [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md).

**Aparece en los casos de estudio:** [TSB Bank](../../../casos/fallo/tsb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE, «Managing Incidents»](https://sre.google/sre-book/managing-incidents/) — gestión de incidentes con roles y comunicación; autoridad: Google SRE.
- [Google SRE, «Emergency Response»](https://sre.google/sre-book/emergency-response/) — respuesta a emergencias y lecciones de casos; autoridad: Google SRE.
- [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) — ciclo de manejo de incidentes de seguridad; autoridad: NIST.
- [PagerDuty, guía de respuesta a incidentes](https://response.pagerduty.com/) — proceso de respuesta publicado en abierto; autoridad: PagerDuty.
- [RFC 9110, semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — define los métodos idempotentes y su significado; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Platform Engineer](./platform-engineer.md) · [Plazo →](./plazo.md)
