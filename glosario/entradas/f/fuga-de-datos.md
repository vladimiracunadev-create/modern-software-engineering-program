# Fuga de datos

[↑ Glosario](../../README.md) · [← Fuerzas del problema](./fuerzas-del-problema.md) · [Fuga de información →](./fuga-de-informacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Presencia en los datos de entrenamiento o prueba de información que no estará disponible en el momento de predecir y que infla el rendimiento estimado.

Definición de trabajo de [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md).

## Por qué importa

La clase donde se define, [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md), existe con este propósito: la clase existe para que trates un modelo de aprendizaje automático como un componente con contrato, límites y fallos propios dentro de un producto, y no como una caja que «tiene una exactitud».

## Cómo funciona

[SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el aviso de riesgo. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md):

El equipo de la plataforma redefine el aviso como una decisión: «cada lunes, listar a los estudiantes con riesgo alto, con el motivo, para que el docente decida si escribe». Fija una línea base (sin entregas en dos semanas) y exige que el modelo la supere en sensibilidad con el mismo número de avisos. Separa entrenamiento y prueba por fecha, revisa cada variable con la pregunta de la fuga (descarta «nota final» y «fecha de baja»), reporta sensibilidad, valor predictivo y prevalencia, y documenta la tarjeta del modelo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md)) son:

- **Exactitud excelente en prueba y mala en uso** — causa: fuga o partición que no imita el uso. Corrección: separar por fecha y revisar cada variable con la pregunta de existencia.
- **«Avisa por casi todos»** — causa: prevalencia baja con umbral por defecto. Corrección: reportar valor predictivo y elegir el umbral por coste de errores.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md)) son: Las definiciones son operativas para el aviso de riesgo. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se entrenó ningún modelo real, no se usó ninguna biblioteca de aprendizaje automático y no se midió ninguna población: los casos, el clasificador por umbral y las distribuciones son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Rendimiento](../r/rendimiento.md), [Deriva de los datos](../d/deriva-de-los-datos.md), [Prevalencia](../p/prevalencia.md), [Tarjeta de modelo](../t/tarjeta-de-modelo.md), [Valor predictivo positivo](../v/valor-predictivo-positivo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kaufman et al., «Leakage in Data Mining» (ACM TKDD, 2012)](https://doi.org/10.1145/2382577.2382579) — formulación de la fuga de datos; autoridad: ACM Transactions on Knowledge Discovery from Data.
- [Sculley et al., «Hidden Technical Debt in Machine Learning Systems» (NeurIPS, 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — deuda técnica específica de sistemas de aprendizaje automático; autoridad: NeurIPS.
- [Mitchell et al., «Model Cards for Model Reporting» (FAT*, 2019)](https://doi.org/10.1145/3287560.3287596) — documentación de uso previsto y límites de un modelo; autoridad: ACM FAT*.
- [Google, «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — prácticas de ingeniería de aprendizaje automático en producción; autoridad: Google Developers.
- [NIST, AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — marco de gestión del riesgo de sistemas de inteligencia artificial; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Fuerzas del problema](./fuerzas-del-problema.md) · [Fuga de información →](./fuga-de-informacion.md)
