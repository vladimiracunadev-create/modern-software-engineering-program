# K-anonimato

[↑ Glosario](../../README.md) · [← Just transition](../j/just-transition.md) · [Kappa de Cohen →](./kappa-de-cohen.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Un conjunto de datos cumple **k-anonimato** cuando cada combinación de **cuasi-identificadores** (atributos que no identifican por sí solos, como ciudad, plan o año de nacimiento, pero que juntos pueden señalar a una persona) aparece en al menos *k* registros. Dicho de otro modo, ninguna persona es distinguible de al menos otras *k − 1* por esos atributos. El programa usa el sentido de Sweeney (2002), tal como lo presentan [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) y [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md); [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) y [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) lo aplican a telemetría y a entornos de vista previa con datos reducidos.

## Por qué importa

Quitar el nombre y el identificador de una tabla no la anonimiza: [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) muestra que un agregado liberado con atributos que, juntos, identifican puede señalar a una persona aunque cada atributo sea inocuo. El k-anonimato convierte esa intuición en una medida que se puede calcular antes de publicar, compartir telemetría o poblar un entorno de pruebas, y obliga a decidir cuánta utilidad se sacrifica a cambio de privacidad.

## Cómo funciona

El mecanismo es contar y generalizar. Se eligen los cuasi-identificadores, se agrupan los registros por cada combinación y se mide el tamaño del grupo más pequeño: ese es el *k* real del conjunto. Si es menor que el objetivo, se actúa sobre los atributos ([SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md)):

1. **Generalizar:** reducir la precisión (año a década o a tramos de cinco años, comuna a región) o quitar atributos.
2. **Suprimir:** eliminar los registros raros que quedan en grupos pequeños.
3. Volver a medir hasta que el grupo más pequeño alcance *k*.

Cada paso reduce la unicidad y también la utilidad. Con *k* de 5, [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) agrupa 5 000 personas por ciudad (6 grupos, ninguno pequeño), por ciudad y plan (18 grupos, ninguno pequeño) y por ciudad, plan y año de nacimiento (1 004 grupos, de los cuales 441 tienen menos de 5 personas y dejan a 1 310 personas expuestas); al generalizar el año a década, quedan 108 grupos y ninguno pequeño. La causa es combinatoria: cada atributo que se añade multiplica los grupos y deja menos personas en cada uno.

## Ejemplo

En [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md), el conjunto del experimento se generaliza con tramos de cinco años, macrozona y sin género: queda en 12 grupos con un *k* mínimo de 63. Es una protección fuerte, y el precio es que el conjunto sirve para contar por macrozona y poco más. Los datos son sintéticos de la clase, y el ejemplo ilustra el compromiso, no una recomendación de qué *k* usar.

## Errores y confusiones comunes

- **Creer que sin nombre ya es anónimo.** El problema son los atributos en conjunto (cuasi-identificadores), no el identificador directo.
- **Confundir k-anonimato con seudonimización.** Seudonimizar sustituye el identificador por otro reversible con una clave; el k-anonimato actúa sobre la combinación de atributos. Son técnicas distintas.
- **Fijar el *k* sin decidir los cuasi-identificadores.** El valor de *k* solo tiene sentido respecto de los atributos elegidos: un atributo olvidado deshace la garantía.
- **Medir una sola vez.** Cada versión nueva de los datos puede cambiar los grupos; hay que volver a medir al publicar.

## Límites y cuándo no aplica

[SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) lo llama condición necesaria y no suficiente. [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) precisa tres límites: no protege cuando todos los miembros de un grupo comparten el valor del atributo sensible (si las 63 personas de un grupo abandonaron el servicio, saber el grupo revela el abandono); no protege frente a quien conoce un dato más; y no resiste que se publiquen varias versiones del mismo conjunto, porque se pueden cruzar. Tampoco es una garantía legal: la minimización y los plazos de retención dependen de la norma aplicable, que las clases citan de fuentes oficiales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cuasi-identificador](../c/cuasi-identificador.md), [Atributo](../a/atributo.md), [Combinación](../c/combinacion.md), [Conjunto](../c/conjunto.md), [Consentimiento](../c/consentimiento.md), [Evento de telemetría](../e/evento-de-telemetria.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Sweeney, 2002](https://doi.org/10.1142/S0218488502001648) — k-anonimato; autoridad: International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems.
- [k-Anonymity: A Model for Protecting Privacy (Sweeney, 2002)](https://epic.org/wp-content/uploads/privacy/reidentification/Sweeney_Article.pdf) — la reidentificación por combinación de atributos y el criterio de k-anonimato; autoridad: artículo académico (International Journal on Uncertainty, Fuzziness and Knowledge-based Systems).
- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — principios de minimización y plazo, protección desde el diseño y seudonimización; autoridad: Unión Europea.
- [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — protección y tratamiento de datos personales en Chile; autoridad: Biblioteca del Congreso Nacional de Chile.
- [Dwork y Roth, 2014](https://doi.org/10.1561/0400000042) — privacidad diferencial; autoridad: Foundations and Trends in Theoretical Computer Science.

---

[↑ Glosario](../../README.md) · [← Just transition](../j/just-transition.md) · [Kappa de Cohen →](./kappa-de-cohen.md)
