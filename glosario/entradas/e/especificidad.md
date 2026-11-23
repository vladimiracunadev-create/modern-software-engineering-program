# Especificidad

[↑ Glosario](../../README.md) · [← Especificación semiformal](./especificacion-semiformal.md) · [Espera →](./espera.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Tupla que mide cuánto se concentra un selector en identificadores, clases y tipos y que decide entre declaraciones de igual origen y capa.

Definición de trabajo de [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md).

## Por qué importa

En [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md), el tema «Cascada, capas y especificidad» importa porque quien gana una declaración se decide por origen, capa, especificidad y orden; ignorarlo produce escaladas.

## Cómo funciona

Según [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md):

Cuando varias declaraciones compiten, la cascada decide en este orden: origen e importancia (agente de usuario, usuario, autor, `!important`), capa (`@layer`), especificidad y, por último, orden de aparición. La especificidad es una tupla (identificadores, clases/atributos/pseudoclases, tipos/pseudoelementos): `#a` supera a `.a.b.c.d`, no se suman como un número decimal. `:where()` suma cero y `:is()` y `:not()` suman su argumento más específico. Una consecuencia práctica: quien no puede ganar por orden gana subiendo la especificidad, y la siguiente persona debe subirla más. Las capas rompen esa carrera, porque una capa posterior gana a una anterior sin importar la especificidad.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md):

El formulario de entrega del caso conductor se publica con una estructura revisable: un `header` con `nav`, un `main` con un único `h1` («Entregar tarea») y `h2` por bloque, un `form` con dos campos, cada uno con su `label for`, un `button type="submit"` y un mensaje de estado en una región con `role="status"`. Los colores salen de variables CSS con la razón de contraste anotada junto a cada par. La hoja usa `@layer base, componentes, utilidades;` de modo que un ajuste puntual no necesita subir selectores.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un componente se estiliza «a la fuerza» con selectores cada vez más largos** — causa: carrera de especificidad por no ordenar con capas. Corrección: introducir `@layer` y mover las reglas a la capa que les corresponde. ([SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una consecuencia práctica: quien no puede ganar por orden gana subiendo la especificidad, y la siguiente persona debe subirla más. ([SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](../c/capa.md), [Origen](../o/origen.md), [Tipo](../t/tipo.md), [Capa de cascada](../c/capa-de-cascada.md), [Elemento semántico](./elemento-semantico.md), [Nombre accesible](../n/nombre-accesible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md), [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [CSS Selectors Level 4: Specificity (W3C)](https://www.w3.org/TR/selectors-4/#specificity-rules) — cálculo de especificidad; autoridad: W3C.
- [WCAG 2.2 (W3C)](https://www.w3.org/TR/WCAG22/) — criterios de contraste, reflujo y contenido no textual; autoridad: W3C.
- [Understanding SC 1.4.3 Contrast (Minimum) (W3C)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — fórmula de la razón de contraste y umbrales; autoridad: W3C WAI.
- [HTML Standard (WHATWG)](https://html.spec.whatwg.org/multipage/) — elementos, roles de contenido y comportamiento nativo; autoridad: WHATWG.
- [CSS Cascading and Inheritance Level 5: Layering (W3C)](https://www.w3.org/TR/css-cascade-5/#layering) — orden de la cascada y capas; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Especificación semiformal](./especificacion-semiformal.md) · [Espera →](./espera.md)
