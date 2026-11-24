# Razón de contraste

[↑ Glosario](../../README.md) · [← Razón de cambio](./razon-de-cambio.md) · [ReAct →](./react.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

La **razón de contraste** es el cociente (L1 + 0,05) / (L2 + 0,05) entre las luminancias relativas del color más claro (L1) y del más oscuro (L2) ([SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md), [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md), [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md)). Mide cuánto se distinguen dos colores, típicamente texto y fondo, y va de 1:1 (idénticos) a 21:1 (negro sobre blanco).

## Por qué importa

Convierte «que se lea bien» en un número que se puede exigir y vigilar. Elegir colores a ojo falla a menudo: lo que parece legible para quien diseña no lo es con baja visión, con sol en la pantalla o en una impresión en gris. Cambia la decisión de diseño: se calcula y se comprueba, y el umbral pasa a ser parte del presupuesto de accesibilidad.

## Cómo funciona

La **luminancia relativa** L de un color se calcula a partir de sus componentes rojo, verde y azul linealizados y ponderados según la sensibilidad del ojo: el verde pesa mucho más que el azul. Con L1 la del color más claro y L2 la del más oscuro, la razón es (L1 + 0,05) / (L2 + 0,05); el 0,05 modela la luz ambiente y evita la división por cero con negro.

[SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) recoge los **mínimos**: **4,5:1** para texto normal y **3:1** para texto grande y componentes de interfaz (bordes de campos, iconos). Son los criterios de las pautas de accesibilidad web. [SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) añade una regla complementaria: el **color no puede ser la única señal** de un estado; un error indicado solo en rojo no se distingue para personas con daltonismo ni en una impresión en gris, de modo que se acompaña con texto o un icono.

[SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) incluye la razón de contraste entre los **presupuestos** de una página: un límite medible con dueño, un umbral con una razón, una medición automática y una acción al superarlo. A diferencia del peso o del tiempo de carga, el contraste es determinista y se comprueba en integración continua sobre la hoja de estilos. El presupuesto captura una parte de la experiencia (la legibilidad del color) y deja fuera otras (tamaño de letra, espaciado, foco), que requieren otras medidas.

## Ejemplo

Texto gris medio sobre fondo blanco: si la luminancia del gris es L2 = 0,2 y la del blanco L1 = 1, la razón es (1 + 0,05) / (0,2 + 0,05) = 4,2: no alcanza el 4,5:1 para texto normal, aunque «se vea bien» en un monitor nuevo. Oscurecer el gris hasta L2 = 0,18 da 4,57 y cumple. (Cálculo propio con la fórmula de [SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md); las luminancias son de ejemplo.)

## Errores y confusiones comunes

- **Elegir colores sin calcular.**
- **Usar solo el color para señalar un estado.**
- **Aplicar el umbral de texto normal a texto grande o al revés.**
- **Medir contraste sobre imágenes o degradados** con un único valor.

## Límites y cuándo no aplica

La razón es una aproximación de la percepción: no capta toda la legibilidad (tipografía, tamaño, espaciado) ni condiciones como el modo oscuro. Cumplir el mínimo no certifica accesibilidad: es una condición necesaria. En logotipos y elementos decorativos las pautas no exigen un contraste mínimo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Criterio de éxito](../c/criterio-de-exito.md), [Declaración de alcance](../d/declaracion-de-alcance.md), [Distancia de color ΔE](../d/distancia-de-color-e.md), [Reflujo](./reflujo.md), [Señal redundante](../s/senal-redundante.md), [Tecnología de apoyo](../t/tecnologia-de-apoyo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-106](../../../classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C: Understanding SC 1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — razón de contraste y fórmula; autoridad: W3C.
- [web.dev: Largest Contentful Paint](https://web.dev/articles/lcp) — definición del LCP y umbral recomendado; autoridad: Google, documentación de web.dev.
- [web.dev: performance budgets 101](https://web.dev/articles/performance-budgets-101) — presupuestos de rendimiento; autoridad: Google, documentación de web.dev.
- [W3C: Understanding SC 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) — contraste de componentes y gráficos; autoridad: W3C.
- [Nielsen Norman Group: Response Times, the 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/) — límites de tiempo de respuesta; autoridad: Nielsen Norman Group.

---

[↑ Glosario](../../README.md) · [← Razón de cambio](./razon-de-cambio.md) · [ReAct →](./react.md)
