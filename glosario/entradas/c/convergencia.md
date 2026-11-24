# Convergencia

[↑ Glosario](../../README.md) · [← Convención de mensajes](./convencion-de-mensajes.md) · [Copia consistente →](./copia-consistente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

La **convergencia** es el estado en que un verificador independiente no encuentra ningún criterio de la especificación sin cumplir ([SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md)). Es la única condición de parada «feliz» de un bucle de agente.

## Por qué importa

«El agente dice haber terminado» no es convergencia. Para que lo sea, el veredicto debe venir de un verificador distinto del propio agente, con criterios ejecutables previos.

## Cómo funciona

[SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) define el bucle: el agente trabaja, el verificador revisa los criterios, y el bucle acaba cuando no queda ninguno abierto. Las otras condiciones (máximo de pasadas, sin progreso, presupuesto, regresión) detienen sin convergencia y llaman a una persona. El valor de la convergencia depende de la **cobertura del verificador**: si no mira un criterio, no puede declararlo cumplido, por lo que la clase pide publicar la cobertura y medir su capacidad de detección con variantes defectuosas.

## Ejemplo

[SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) (asistente de *Avisos*): un agente migra textos de una intranet a otro formato. Sin verificador independiente, declara haber terminado y la revisión encuentra incumplimientos. Con criterios ejecutables previos, la convergencia significa que el verificador recorrió todos y no halló ninguno abierto.

## Errores y confusiones comunes

**El agente dice haber terminado y la revisión encuentra incumplimientos.** Verificador del propio agente o con cobertura parcial; criterios ejecutables previos y cobertura publicada.

## Límites y cuándo no aplica

La convergencia es tan fiable como el verificador: una variante defectuosa que ningún criterio detecta pasa. Por eso se mide con variantes y se declara qué criterios no detectarían un defecto concreto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Verificador independiente](../v/verificador-independiente.md), [Especificación](../e/especificacion.md), [Estado](../e/estado.md), [Verificador](../v/verificador.md), [Cobertura del verificador](./cobertura-del-verificador.md), [Condición de parada](./condicion-de-parada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), [SE-531](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-531-comunicacion-facilitacion-y-conflicto/README.md), [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spec Kit — referencia del proceso agentic](https://github.github.io/spec-kit/reference/agentic-sdd.html) — implementar por fases y converger solo añadiendo tareas; autoridad: GitHub y mantenedores de la comunidad.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — verdad del entorno y condiciones de parada en bucles de agente; autoridad: Anthropic, artículo de ingeniería.
- [Jia y Harman](https://doi.org/10.1109/TSE.2010.62) — prueba de mutación como medida de la detección; autoridad: IEEE Transactions on Software Engineering.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — medir y gestionar el riesgo de sistemas de IA; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Convención de mensajes](./convencion-de-mensajes.md) · [Copia consistente →](./copia-consistente.md)
