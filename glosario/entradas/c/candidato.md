# Candidato

[↑ Glosario](../../README.md) · [← Candidata](./candidata.md) · [Candidato descartado →](./candidato-descartado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Configuración del sistema que se somete a la puerta.

Definición de trabajo de [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md).

## Por qué importa

La clase donde se define, [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md), existe con este propósito: el proyecto existe para que entregues, para un sistema con LLM que elijas, **la evidencia con que otra persona decidiría ponerlo en producción**: qué patrón usa y por qué, cómo se mide su calidad, cuánto cuesta y tarda en el caso malo, qué ataque lo rompe y cómo se contiene, qué pasa si se interrumpe a mitad y cómo degrada.

## Cómo funciona

Según [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md):

Cada columna tiene su método. La **calidad** se mide con el conjunto de casos de `SE-597`: pareada, con repeticiones y con la puerta estadística; en el experimento, los candidatos van de 85,0 % (workflow solo, que escala las incidencias) a 99,0 % (híbrido). Los **tokens** salen del modelo de costo de `SE-589` y `SE-598`: 774 el workflow, 1 862 el agente, 1 421 el híbrido. La **latencia p95** sale de la cadena de llamadas de `SE-598`: unas 6 s para el workflow (dos llamadas) y unas 18 s para los candidatos con agente (la cadena de ocho llamadas). Los **ataques** salen de la simulación de `SE-598`: 19,23 % sin defensa y 0,00 % con la política de no tener canal de salida junto a contenido no confiable.

Según [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md):

El equipo de *Avisos* entrega un dossier de nueve páginas a una comisión de revisión. La primera página es la puerta con sus umbrales y sus justificaciones, firmada antes de medir. Las páginas siguientes presentan los cuatro candidatos medidos con 400 casos (250 reales anonimizados, 100 difíciles y 50 adversariales) y tres repeticiones; el híbrido gobernado pasa las cinco columnas, con calidad 98,1 % (intervalo del 96,9 % al 99,0 %). La comisión pregunta por el ataque que no se probó y el equipo responde con el documento de límites: se probaron 40 correos hostiles, no se probó contenido en otro idioma ni documentos adjuntos. Se acuerda publicar con un 10 % del tráfico, una alarma de escalado por encima del 12 % y una revisión a los 30 días.

## Ejemplo

Ejemplo de [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* entrega un dossier de nueve páginas a una comisión de revisión. La primera página es la puerta con sus umbrales y sus justificaciones, firmada antes de medir. Las páginas siguientes presentan los cuatro candidatos medidos con 400 casos (250 reales anonimizados, 100 difíciles y 50 adversariales) y tres repeticiones; el híbrido gobernado pasa las cinco columnas, con calidad 98,1 % (intervalo del 96,9 % al 99,0 %). La comisión pregunta por el ataque que no se probó y el equipo responde con el documento de límites: se probaron 40 correos hostiles, no se probó contenido en otro idioma ni documentos adjuntos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** Cada tarjeta es un candidato con sus cinco medidas a la derecha y el criterio que incumple debajo: coral si no pasa la puerta y verde azulado si pasa. ([SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md))
- Define dos candidatos, escribe la puerta antes de medir, mide al menos calidad, costo, latencia y una prueba de seguridad, declara qué no mediste y decide con una condición de revisión. ([SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md))

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
