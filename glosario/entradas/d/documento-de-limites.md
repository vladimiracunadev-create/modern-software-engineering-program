# Documento de límites

[↑ Glosario](../../README.md) · [← Documento](./documento.md) · [Documento de tarea →](./documento-de-tarea.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Declaración de lo que no se midió y de los supuestos de lo medido.

Definición de trabajo de [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md).

## Por qué importa

La clase donde se define, [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md), existe con este propósito: el proyecto existe para que entregues, para un sistema con LLM que elijas, **la evidencia con que otra persona decidiría ponerlo en producción**: qué patrón usa y por qué, cómo se mide su calidad, cuánto cuesta y tarda en el caso malo, qué ataque lo rompe y cómo se contiene, qué pasa si se interrumpe a mitad y cómo degrada.

## Cómo funciona

Según [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md):

La última parte del proyecto es un documento de **límites**: qué se midió con datos reales y qué con simulación, qué tamaño tiene el conjunto de casos, qué proveedor y versión de modelo se usó, qué ataques se probaron y cuáles no, qué escalones de degradación se ensayaron y cuáles solo existen en papel. La honestidad de ese documento es lo que permite a la persona que decide ponderar el riesgo. Un sistema con «todo verde» y un documento de límites vacío es una señal de alerta.

Según [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md):

El equipo de *Avisos* entrega un dossier de nueve páginas a una comisión de revisión. La primera página es la puerta con sus umbrales y sus justificaciones, firmada antes de medir. Las páginas siguientes presentan los cuatro candidatos medidos con 400 casos (250 reales anonimizados, 100 difíciles y 50 adversariales) y tres repeticiones; el híbrido gobernado pasa las cinco columnas, con calidad 98,1 % (intervalo del 96,9 % al 99,0 %). La comisión pregunta por el ataque que no se probó y el equipo responde con el documento de límites: se probaron 40 correos hostiles, no se probó contenido en otro idioma ni documentos adjuntos. Se acuerda publicar con un 10 % del tráfico, una alarma de escalado por encima del 12 % y una revisión a los 30 días.

## Ejemplo

Ejemplo de [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* entrega un dossier de nueve páginas a una comisión de revisión. La primera página es la puerta con sus umbrales y sus justificaciones, firmada antes de medir. Las páginas siguientes presentan los cuatro candidatos medidos con 400 casos (250 reales anonimizados, 100 difíciles y 50 adversariales) y tres repeticiones; el híbrido gobernado pasa las cinco columnas, con calidad 98,1 % (intervalo del 96,9 % al 99,0 %). La comisión pregunta por el ataque que no se probó y el equipo responde con el documento de límites: se probaron 40 correos hostiles, no se probó contenido en otro idioma ni documentos adjuntos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La última parte del proyecto es un documento de **límites**: qué se midió con datos reales y qué con simulación, qué tamaño tiene el conjunto de casos, qué proveedor y versión de modelo se usó, qué ataques se probaron y cuáles no, qué escalones de degradación se ensayaron y cuáles solo existen en papel. ([SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md))
- Declara en el documento de límites qué es simulado. ([SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md), [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Supuestos](../s/supuestos.md), [Candidato](../c/candidato.md), [Condición de revisión](../c/condicion-de-revision.md), [Durabilidad](./durabilidad.md), [Gobierno](../g/gobierno.md), [Puerta de entrada a producción](../p/puerta-de-entrada-a-produccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Documento](./documento.md) · [Documento de tarea →](./documento-de-tarea.md)
