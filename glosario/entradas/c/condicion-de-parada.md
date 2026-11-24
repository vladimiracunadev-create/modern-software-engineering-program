# Condición de parada

[↑ Glosario](../../README.md) · [← Condición de fallo](./condicion-de-fallo.md) · [Condición de revisión →](./condicion-de-revision.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Una **condición de parada** es una regla explícita que detiene un bucle de agente y define qué se hace después. Es la definición de [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) y [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md). Un sentido emparentado aparece en [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), en ingeniería del caos: la alarma que detiene un experimento si el sistema alcanza un estado inaceptable. En ambos, la idea es la misma: el fin del proceso no se deja al azar ni al agotamiento de recursos.

## Por qué importa

Un bucle sin condición de parada, dice [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), se detiene cuando se acaba el dinero o la paciencia. Es una decisión de diseño que cambia el riesgo: con parada explícita, el peor caso está acotado y es predecible; sin ella, un agente puede trabajar toda la noche sin avanzar ([SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md)) y la factura o el daño llegan antes que cualquier revisión.

## Cómo funciona

[SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) enumera cinco condiciones útiles, y cada una vigila una causa distinta de no terminar:

1. **Convergencia:** el verificador no encuentra nada y el trabajo acaba bien. Es la única salida «feliz».
2. **Máximo de pasadas:** tras N pasadas se detiene aunque haya criterios abiertos; es la condición que la guía de Anthropic cita como habitual para mantener el control.
3. **Sin progreso:** el número de criterios abiertos no baja en dos pasadas seguidas.
4. **Presupuesto:** tope de tokens, tiempo o dinero.
5. **Regresión:** una pasada reabre criterios ya cumplidos; indica que el agente deshace su propio trabajo.

Salvo la convergencia, la acción es la misma: **detener, guardar el estado y llamar a una persona** con la lista de lo abierto. Por eso la parada incluye el «qué se hace después»: una parada que solo mata el proceso pierde el contexto.

En ingeniería del caos ([SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md)), la condición es una alarma sobre el sistema: si una señal cruza un umbral definido de antemano, el experimento se aborta y el estado se restaura.

## Ejemplo

Un agente corrige fallos de un conjunto de criterios de aceptación. Pasada 1: abiertos 7. Pasada 2: abiertos 4. Pasada 3: abiertos 4. Pasada 4: abiertos 4 → *sin progreso* (dos pasadas seguidas sin bajar). El bucle se detiene, guarda el estado y entrega a una persona la lista de los 4 criterios abiertos y lo intentado. Si en la pasada 5 un criterio ya cumplido se reabriera, saltaría *regresión* aun antes. (Los números son ilustración, no datos de la clase.)

## Errores y confusiones comunes

- **El bucle no acaba nunca.** No hay condiciones de parada; corrección de [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md): máximo de pasadas, sin progreso, presupuesto y regresión.
- **Poner solo un máximo enorme.** [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) señala que un agente puede trabajar toda la noche sin avanzar; hay que añadir estado repetido y falta de avance, con presupuesto por tarea.
- **Parar sin guardar el estado.** Se pierde lo hecho y la persona no sabe qué falta.
- **Confundirla con el criterio de aceptación.** Este define cuándo el trabajo está bien; la condición de parada define cuándo dejar de intentarlo aunque no lo esté.

## Límites y cuándo no aplica

Las condiciones de no convergencia dependen de poder medir el progreso: si el verificador es débil, «sin progreso» o «convergencia» pueden ser engañosos (un verificador que no ve un defecto declara convergencia). Un máximo demasiado bajo corta trabajo legítimo; uno demasiado alto no protege. En un único paso de modelo sin bucle no hay nada que detener. Y en experimentos de caos, una alarma sobre una señal mal elegida puede no saltar a tiempo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Estado](../e/estado.md), [Regla](../r/regla.md), [Cobertura del verificador](./cobertura-del-verificador.md), [Convergencia](./convergencia.md), [Orquestador de caos](../o/orquestador-de-caos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md), [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Condiciones de parada».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — verdad del entorno y condiciones de parada en bucles de agente; autoridad: Anthropic, artículo de ingeniería.
- [Spec Kit — referencia del proceso agentic](https://github.github.io/spec-kit/reference/agentic-sdd.html) — implementar por fases y converger solo añadiendo tareas; autoridad: GitHub y mantenedores de la comunidad.
- [Jia y Harman](https://doi.org/10.1109/TSE.2010.62) — prueba de mutación como medida de la detección; autoridad: IEEE Transactions on Software Engineering.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — medir y gestionar el riesgo de sistemas de IA; autoridad: NIST.
- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — reanudar desde el punto del error, muestras pequeñas con efectos grandes y evaluación del estado final; autoridad: Anthropic.

---

[↑ Glosario](../../README.md) · [← Condición de fallo](./condicion-de-fallo.md) · [Condición de revisión →](./condicion-de-revision.md)
