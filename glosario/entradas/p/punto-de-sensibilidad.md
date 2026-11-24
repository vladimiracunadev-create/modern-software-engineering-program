# Punto de sensibilidad

[↑ Glosario](../../README.md) · [← Punto de no retorno](./punto-de-no-retorno.md) · [Puntuación de Brier →](./puntuacion-de-brier.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Un **punto de sensibilidad** es un parámetro cuyo cambio pequeño invierte la decisión o cambia mucho una medida ([SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md)). En la evaluación de arquitecturas con métodos como ATAM, [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) lo define como un parámetro del que depende de forma notable un atributo de calidad.

## Por qué importa

Una recomendación de arquitectura sale de un modelo con supuestos. Saber **cuáles** de esos supuestos deciden el resultado permite saber dónde conviene invertir en medir y dónde da igual. La decisión que cambia es dónde se pone la atención: en los pocos parámetros que mueven la decisión, no en los muchos que no.

## Cómo funciona

[SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) calcula la utilidad de varios candidatos (monolito modular, microservicios, celdas) variando el tamaño de la organización de 2 a 30 equipos. Resultado del modelo de la clase: con cliente dominante, la celda gana en todos los tamaños (su utilidad baja de 0,813 con 2 equipos a 0,696 con 30 y sigue por encima del monolito y de los microservicios). Sin cliente dominante, el monolito modular gana hasta 25 equipos y los microservicios desde 26: la utilidad del monolito cae con la coordinación (0,807 con 2 equipos, 0,668 con 30), mientras la de los microservicios se mantiene en 0,670 porque su coordinación es cero.

El punto de sensibilidad respecto de los equipos es **26**: ahí se invierte la decisión. En [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), ATAM concluye con tres clases de hallazgo: **riesgos** (decisiones que pueden causar problemas), **puntos de sensibilidad** (parámetros de los que depende mucho un atributo) y **compromisos** (decisiones que mejoran un atributo a costa de otro). Cada hallazgo se apoya en un escenario concreto, lo que lo hace discutible y repetible.

Su utilidad práctica: indica qué dato vale la pena medir con precisión. Si la decisión cambia con 26 equipos, importa saber si la organización está cerca de ese valor.

## Ejemplo

Con el modelo de [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), una organización con 24 equipos sin cliente dominante elegiría el monolito modular, pero está a dos equipos del punto de inversión. Saber que el punto es 26 le dice que debe vigilar el crecimiento y preparar las fronteras para una separación posterior, no que deba migrar hoy.

## Errores y confusiones comunes

- **Tomar el valor como regla general**: [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) advierte que «separa cuando hay más de unos 25 equipos» sale de ese modelo y no de un estudio.
- **Confundirlo con un riesgo**: el punto de sensibilidad es un parámetro; el riesgo, una decisión que puede causar problemas.
- **Ignorar que cambia al cambiar los supuestos**: es una propiedad del modelo.
- **Buscarlo sin escenarios**: sin un atributo de calidad concreto no hay sensibilidad que medir.

## Límites y cuándo no aplica

La cifra de 26 depende de todos los supuestos del modelo de la clase (pesos, coordinación, utilidades), que son del autor. Cambiar un peso mueve el punto. El análisis de sensibilidad solo cubre los parámetros que el modelo incluye; un factor omitido no aparece. Sirve para decidir dónde mirar, no para sustituir la medición de la organización real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributos de calidad](../a/atributos-de-calidad.md), [Atributo](../a/atributo.md), [Medida](../m/medida.md), [Parámetro](./parametro.md), [Árbol de utilidad](../a/arbol-de-utilidad.md), [Compromiso](../c/compromiso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-347 — Taller: seleccionar un estilo con escenarios de calidad](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — evaluación de arquitectura contra escenarios; autoridad: Software Engineering Institute (Carnegie Mellon).
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — características de calidad del producto; autoridad: ISO.
- [Kruchten, «The 4+1 View Model of Architecture» (IEEE Software, 1995)](https://doi.org/10.1109/52.469759) — escenarios que unen las vistas; autoridad: IEEE Software.
- [Google SRE, «Embracing Risk»](https://sre.google/sre-book/embracing-risk/) — riesgo aceptable y presupuesto de error; autoridad: Google SRE.
- [Python: `copy`](https://docs.python.org/3/library/copy.html) — copias profundas para la sensibilidad; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Punto de no retorno](./punto-de-no-retorno.md) · [Puntuación de Brier →](./puntuacion-de-brier.md)
