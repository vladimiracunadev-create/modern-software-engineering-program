# Condición de revisión

[↑ Glosario](../../README.md) · [← Condición de parada](./condicion-de-parada.md) · [Condición de salida →](./condicion-de-salida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Evento o umbral que reabre una decisión.

Definición de trabajo de [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md): Hecho o medida que cambiaría una decisión.

## Por qué importa

La clase donde se define, [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md), existe con este propósito: el proyecto existe para que entregues, para un sistema con LLM que elijas, **la evidencia con que otra persona decidiría ponerlo en producción**: qué patrón usa y por qué, cómo se mide su calidad, cuánto cuesta y tarda en el caso malo, qué ataque lo rompe y cómo se contiene, qué pasa si se interrumpe a mitad y cómo degrada.

## Cómo funciona

Según [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md):

La decisión de entrar a producción no es definitiva. Cada decisión lleva su **condición de revisión**: un cambio de proveedor o de modelo, una tasa de escalado superior a un umbral, una caída del acuerdo del juez con personas, un incidente de seguridad, una desviación del costo mensual. La puerta se vuelve a ejecutar con cada cambio de versión y cada fallo relevante se convierte en un caso (`SE-597`). Operar es sostener esa disciplina.

Según [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md):

**Corrección.** Se elimina el campo de texto libre del esquema y se valida con una lista de valores permitidos. Se añade el caso a la evaluación, se reduce el tráfico al 10 % durante una semana y la condición de revisión incorpora «cualquier fuga de datos entre estudiantes reabre la decisión». El incidente se registra con su causa y el cambio de puerta.

## Ejemplo

Caso medido en la sección «La condición de revisión» de [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md):

La decisión de entrar a producción no es definitiva. Cada decisión lleva su **condición de revisión**: un cambio de proveedor o de modelo, una tasa de escalado superior a un umbral, una caída del acuerdo del juez con personas, un incidente de seguridad, una desviación del costo mensual. La puerta se vuelve a ejecutar con cada cambio de versión y cada fallo relevante se convierte en un caso (`SE-597`). Operar es sostener esa disciplina.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Define dos candidatos, escribe la puerta antes de medir, mide al menos calidad, costo, latencia y una prueba de seguridad, declara qué no mediste y decide con una condición de revisión. ([SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Hecho](../h/hecho.md), [Medida](../m/medida.md), [Alcance](../a/alcance.md), [Batería hostil](../b/bateria-hostil.md), [Candidato](./candidato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), [SE-533](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Condición de parada](./condicion-de-parada.md) · [Condición de salida →](./condicion-de-salida.md)
