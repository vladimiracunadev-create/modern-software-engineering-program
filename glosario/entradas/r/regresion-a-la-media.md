# Regresión a la media

[↑ Glosario](../../README.md) · [← Regresión](./regresion.md) · [Regresión de resiliencia →](./regresion-de-resiliencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

La **regresión a la media** es la tendencia de los casos extremos de una medición ruidosa a acercarse al promedio en la siguiente medición ([SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md)). No es un efecto de ninguna intervención: es una propiedad estadística de medir con ruido. No debe confundirse con la «regresión» de pruebas (defecto que reaparece) ni con la regresión estadística como técnica de ajuste.

## Por qué importa

Hace que programas dirigidos a los peores casos parezcan funcionar aunque no hagan nada. Si se elige al peor decil por una primera medición y se compara con una segunda, el grupo habrá «mejorado» solo por el ruido. Quien evalúa «antes y después» atribuye esa mejora al programa. Cambia cómo se evalúa cualquier intervención sobre un grupo seleccionado por una métrica extrema.

## Cómo funciona

[SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) lo explica así: una medición es el **valor verdadero más ruido**. Cuando se selecciona a los peores por una primera medición, algunos están allí porque su valor verdadero es bajo y otros porque tuvieron mala suerte en esa medición. En la segunda medición, la mala suerte no se repite (es ruido independiente), y el grupo, en promedio, mejora sin intervención. Cuanto **menos fiable** la medición (más ruido en relación con la variación real entre casos), **mayor** la regresión.

La corrección que enseña la clase es de diseño: comparar con un **grupo seleccionado igual** (los peores del grupo de comparación, elegidos con el mismo criterio) o, mejor, asignar al azar entre los seleccionados. Así el efecto del ruido afecta a ambos grupos por igual y la diferencia entre ellos sí es atribuible al programa. [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) conecta esto con su formato de lectura de experimentos: unidad asignada, mecanismo de asignación, proporciones esperadas y observadas con control, población y ventana, métrica primaria con su contraria, efecto estimado con intervalo y límites; toda comparación observacional se rotula como tal.

## Ejemplo

Un programa de apoyo se ofrece al 10 % de estudiantes con peor nota en el primer parcial. En el segundo parcial, ese grupo sube en promedio 8 puntos. Pero sin ningún programa, un grupo equivalente (el 10 % peor de otra sección sin apoyo) sube 6 puntos por regresión: el efecto atribuible al programa es de 2, no de 8. (Cifras ilustrativas del mecanismo; [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) trabaja con datos sintéticos.)

## Errores y confusiones comunes

- **«El programa funcionó en el peor decil»**: regresión a la media; corrección: comparar con un grupo seleccionado igual.
- **Premiar o castigar por desempeño extremo** y creer que el cambio posterior fue causado por la intervención.
- **Creer que solo afecta a los peores**: también a los mejores, que tienden a bajar.
- **Confundir regresión a la media con tendencia real**: la primera no implica un cambio de fondo.

## Límites y cuándo no aplica

No hay regresión a la media si la medición es muy fiable (poco ruido) o si el valor verdadero es lo que cambia. Si la selección no se hizo por la medición extrema (se elige a todo el grupo), el efecto no aparece. Y el control adecuado no corrige otros sesgos de selección: hay que cuidar que los grupos sean comparables en lo demás.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Extremo](../e/extremo.md), [Medición](../m/medicion.md), [Asignación aleatoria](../a/asignacion-aleatoria.md), [Contrafactual](../c/contrafactual.md), [Desajuste de proporción de muestra](../d/desajuste-de-proporcion-de-muestra.md), [Sesgo de selección](../s/sesgo-de-seleccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Trustworthy Online Controlled Experiments](https://experimentguide.com/) — diseño, calidad y análisis de experimentos controlados en línea; autoridad: R. Kohavi, D. Tang y Y. Xu (Cambridge University Press).
- [Diagnosing Sample Ratio Mismatch in Online Controlled Experiments (KDD 2019)](https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf) — taxonomía y reglas para diagnosticar un desajuste de asignación; autoridad: A. Fabijan y colaboradores (Microsoft).
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — usar datos para decidir cómo mejorar un servicio; autoridad: Government Digital Service.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — medición y evidencia empírica en ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generadores con semilla.

---

[↑ Glosario](../../README.md) · [← Regresión](./regresion.md) · [Regresión de resiliencia →](./regresion-de-resiliencia.md)
