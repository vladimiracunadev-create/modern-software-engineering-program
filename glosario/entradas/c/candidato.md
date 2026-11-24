# Candidato

[↑ Glosario](../../README.md) · [← Candidata](./candidata.md) · [Candidato descartado →](./candidato-descartado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

En la evaluación de sistemas con modelos, un **candidato** es una configuración del sistema que se somete a la puerta ([SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md)).

## Por qué importa

Elegir entre configuraciones (un workflow, un agente, un híbrido) exige medir cada una con los mismos criterios y decidir con una puerta fijada antes de medir.

## Cómo funciona

Cada candidato se mide en varias columnas con su método: la **calidad** con el conjunto de casos de [SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) (pareada, con repeticiones y puerta estadística); los **tokens** y la **latencia p95** con los modelos de costo y de cadena de llamadas de [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md) y [SE-598](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md); y una prueba de seguridad. En el experimento, los candidatos van de 85,0 % de calidad (workflow solo) a 99,0 % (híbrido), con 774 tokens el workflow, 1 862 el agente y 1 421 el híbrido.

## Ejemplo

[SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md): el equipo de *Avisos* entrega un dossier a una comisión; la primera página es la puerta con umbrales, firmada antes de medir; luego cuatro candidatos medidos con 400 casos y tres repeticiones; el híbrido gobernado pasa las cinco columnas con calidad 98,1 % (intervalo 96,9 % a 99,0 %).

## Errores y confusiones comunes

Fijar umbrales después de ver los resultados; comparar candidatos en conjuntos distintos.

## Límites y cuándo no aplica

Los números son de un experimento sintético; el dossier debe declarar lo que no se midió y la condición de revisión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md), [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Puerta](../p/puerta.md), [Condición de revisión](./condicion-de-revision.md), [Documento de límites](../d/documento-de-limites.md), [Durabilidad](../d/durabilidad.md), [Gobierno](../g/gobierno.md), [Puerta de entrada a producción](../p/puerta-de-entrada-a-produccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (61 clases más lo mencionan; las que más):

[SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Candidata](./candidata.md) · [Candidato descartado →](./candidato-descartado.md)
