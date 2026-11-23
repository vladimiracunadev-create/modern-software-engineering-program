# Contrato de salida

[↑ Glosario](../../README.md) · [← Contrato de puerto](./contrato-de-puerto.md) · [Contrato del consumidor →](./contrato-del-consumidor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Descripción de la forma y los valores válidos de la respuesta, comprobable por un programa.

Definición de trabajo de [SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md).

## Por qué importa

En [SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md), el tema «Formato y contratos de salida» importa porque permite que la salida entre en un proceso automático

## Cómo funciona

Según [SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md):

Un formato estructurado convierte la salida en algo que un programa puede validar. JSON Schema permite declarar tipos, campos obligatorios, rangos y enumeraciones; un validador que lo aplique rechaza lo que no cumple sin intervención humana. Hay dos precauciones. La primera: el formato es una restricción sobre la forma, no sobre la verdad, y un documento perfectamente válido puede contener una nota equivocada. La segunda: pedir «solo JSON» no garantiza que el modelo no antepondrá una frase explicativa; el validador debe rechazar esa salida y la rutina debe decidir si reintenta, extrae el JSON o escala. Por eso el contrato de salida se redacta en el encargo y se **comprueba fuera del modelo**: un esquema declarativo y un script que lo aplica.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo reescribe el encargo para «calcular la nota final» con los seis componentes. Objetivo: función `nota_final(trabajos, examen)` que devuelve nota y estado. Contexto: módulo de calificaciones, Python 3.12, sin dependencias. Restricciones: no modificar otras funciones; lanzar `ValueError` ante lista vacía de trabajos. Formato: un parche unificado más un archivo de pruebas. Ejemplos: cinco casos, entre ellos la frontera 4,0 y un promedio con medio punto de redondeo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El JSON llega con texto delante** — causa: el contrato de salida no se comprueba. Corrección: validar fuera del modelo y rechazar o extraer con regla. ([SE-554](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de requisitos con semilla fija, un validador real aplicado a salidas sintéticas y un cálculo exacto de conflictos. No se llamó a ningún modelo real; las probabilidades de cumplimiento, los seis tipos de defecto, su reparto uniforme y la tasa de conflicto son construcciones del autor, y el validador se escribió sabiendo qué defectos se inyectaban.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](../v/valor.md), [Criterio de aceptación](./criterio-de-aceptacion.md), [Encargo](../e/encargo.md), [Instrucciones en conflicto](../i/instrucciones-en-conflicto.md), [Validación por capas](../v/validacion-por-capas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-065](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md), [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: prompt engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) — claridad, ejemplos y criterios de éxito antes de iterar; autoridad: documentación de Anthropic.
- [JSON Schema](https://json-schema.org/specification) — validación de la estructura de documentos JSON; autoridad: especificación del proyecto JSON Schema.
- [Wallace et al., «The Instruction Hierarchy»](https://arxiv.org/abs/2404.13208) — jerarquía de instrucciones por nivel de privilegio; autoridad: preprint de OpenAI.
- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — evaluación de código por pruebas; autoridad: preprint de OpenAI.
- [Python: json](https://docs.python.org/3/library/json.html) — análisis de JSON; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Contrato de puerto](./contrato-de-puerto.md) · [Contrato del consumidor →](./contrato-del-consumidor.md)
