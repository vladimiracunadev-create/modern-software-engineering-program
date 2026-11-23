# Deriva de los datos

[↑ Glosario](../../README.md) · [← Deriva de distribución](./deriva-de-distribucion.md) · [Deriva del alcance →](./deriva-del-alcance.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Cambio en la distribución de las entradas respecto de la de entrenamiento.

Definición de trabajo de [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md).

## Por qué importa

La clase donde se define, [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md), existe con este propósito: la clase existe para que trates un modelo de aprendizaje automático como un componente con contrato, límites y fallos propios dentro de un producto, y no como una caja que «tiene una exactitud».

## Cómo funciona

Según [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md):

La población cambia: otro formato de curso, otra época del año, otro canal de entrada. La **deriva** de los datos de entrada se detecta comparando la distribución reciente con la de referencia; una medida habitual es el índice de estabilidad de población (PSI), que agrupa la variable en tramos y suma las diferencias de proporciones ponderadas por su logaritmo. Por convención, valores sobre 0,1 piden atención y sobre 0,2 acción, pero son convenciones, no leyes. Detectar deriva en la entrada no es lo mismo que detectar que el modelo empeoró: eso exige etiquetas que pueden llegar tarde. El monitoreo combina ambos y declara cuánto retraso tiene cada señal.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md):

El equipo de la plataforma redefine el aviso como una decisión: «cada lunes, listar a los estudiantes con riesgo alto, con el motivo, para que el docente decida si escribe». Fija una línea base (sin entregas en dos semanas) y exige que el modelo la supere en sensibilidad con el mismo número de avisos. Separa entrenamiento y prueba por fecha, revisa cada variable con la pregunta de la fuga (descarta «nota final» y «fecha de baja»), reporta sensibilidad, valor predictivo y prevalencia, y documenta la tarjeta del modelo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md)) son:

- **Exactitud excelente en prueba y mala en uso** — causa: fuga o partición que no imita el uso. Corrección: separar por fecha y revisar cada variable con la pregunta de existencia.
- **«Avisa por casi todos»** — causa: prevalencia baja con umbral por defecto. Corrección: reportar valor predictivo y elegir el umbral por coste de errores.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md)) son: Las definiciones son operativas para el aviso de riesgo. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se entrenó ningún modelo real, no se usó ninguna biblioteca de aprendizaje automático y no se midió ninguna población: los casos, el clasificador por umbral y las distribuciones son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fuga de datos](../f/fuga-de-datos.md), [Prevalencia](../p/prevalencia.md), [Tarjeta de modelo](../t/tarjeta-de-modelo.md), [Valor predictivo positivo](../v/valor-predictivo-positivo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Sculley et al., «Hidden Technical Debt in Machine Learning Systems» (NeurIPS, 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — deuda técnica específica de sistemas de aprendizaje automático; autoridad: NeurIPS.
- [Kaufman et al., «Leakage in Data Mining» (ACM TKDD, 2012)](https://doi.org/10.1145/2382577.2382579) — formulación de la fuga de datos; autoridad: ACM Transactions on Knowledge Discovery from Data.
- [Mitchell et al., «Model Cards for Model Reporting» (FAT*, 2019)](https://doi.org/10.1145/3287560.3287596) — documentación de uso previsto y límites de un modelo; autoridad: ACM FAT*.
- [Google, «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — prácticas de ingeniería de aprendizaje automático en producción; autoridad: Google Developers.
- [NIST, AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — marco de gestión del riesgo de sistemas de inteligencia artificial; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Deriva de distribución](./deriva-de-distribucion.md) · [Deriva del alcance →](./deriva-del-alcance.md)
