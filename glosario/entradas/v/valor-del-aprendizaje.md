# Valor del aprendizaje

[↑ Glosario](../../README.md) · [← Valor definido](./valor-definido.md) · [Valor esperado →](./valor-esperado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Mejora esperada de una decisión gracias a información obtenida antes de decidir, menos el costo de obtenerla.

Definición de trabajo de [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md).

## Por qué importa

En [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), el tema «Valor del aprendizaje» importa porque una prueba barata puede evitar construir lo que no funciona; una cara o poco fiable no compensa.

## Cómo funciona

Según [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), en la sección «Valor del aprendizaje»:

Construir un ítem con 35 % de probabilidad de éxito, ganancia de 100 y coste de 40 tiene un valor esperado de −5. Una prueba previa que cuesta 5 y acierta el 90 % de las veces convierte esa apuesta en una decisión informada: se construye solo si la prueba sale positiva, y el valor esperado neto sube a +11,3. Si la prueba cuesta 15 y acierta solo el 70 %, vale −8,1 y conviene no hacerla. El valor de aprender depende de tres cosas: cuánta incertidumbre hay, cuánto cuesta equivocarse y cuánto cuesta la prueba. Es un cálculo con supuestos, pero hace explícito por qué aprender a veces es lo más rentable.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md):

En la plataforma de entregas, el registro de priorización conserva por cada ítem: identificador, regla aplicada, valores de entrada con su fuente y fecha, quién los estimó, puntuación base, probabilidad de top 3 bajo perturbación y estado (construir, probar, esperar, descartar). El contrato es que ningún ítem sube de puesto sin que cambie una entrada o su fuente, y que el orden se recalcula cuando se resuelve un experimento.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md)) son:

- **El primer puesto cambia en cada reunión** — causa: el ranking no resiste la incertidumbre de sus entradas. Corrección: calcular la probabilidad de primer puesto y tratar como empatados los ítems que comparten más del 25 %.
- **El equipo hace primero lo más valioso y todo lo demás se retrasa** — causa: no se consideró la duración ni el coste del retraso. Corrección: comparar con WSJF sobre las permutaciones relevantes y elegir el orden de menor coste total.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se priorizó un backlog real, la perturbación es independiente y el modelo de aprender antes usa parámetros ilustrativos. La siguiente clase revisa qué aprendizaje es éticamente aceptable y cómo proteger a quienes participan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Coste del retraso](../c/coste-del-retraso.md), [Decisión revisable](../d/decision-revisable.md), [Riesgo y confianza](../r/riesgo-y-confianza.md), [Valor y esfuerzo](./valor-y-esfuerzo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-182](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Intercom: RICE, simple prioritization for product managers](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/) — definición de los cuatro factores de RICE; autoridad: Intercom (fuente del autor del método).
- [Scaled Agile Framework: Weighted Shortest Job First](https://scaledagileframework.com/wsjf/) — definición de WSJF y su relación con el coste del retraso; autoridad: Scaled Agile, Inc.
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — valor de la información y cuantificación de la incertidumbre; autoridad: Hubbard Decision Research.
- [Product Talk: Opportunity Solution Tree](https://www.producttalk.org/opportunity-solution-tree/) — estructura para conectar oportunidades, soluciones y experimentos; autoridad: Teresa Torres (fuente del autor).
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado como unidad de progreso; autoridad: Eric Ries (fuente del autor).

---

[↑ Glosario](../../README.md) · [← Valor definido](./valor-definido.md) · [Valor esperado →](./valor-esperado.md)
