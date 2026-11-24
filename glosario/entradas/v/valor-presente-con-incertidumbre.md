# Valor presente con incertidumbre

[↑ Glosario](../../README.md) · [← Valor predictivo positivo](./valor-predictivo-positivo.md) · [Valor presente neto →](./valor-presente-neto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

El **valor presente con incertidumbre** es la distribución del valor presente neto (VPN) que resulta de muestrear los rangos de los supuestos de un caso de viabilidad ([SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md)). En lugar de un número obtenido con valores centrales, es una distribución de la que se informa la mediana, el intervalo del 5 al 95 por ciento y la probabilidad de que el valor sea positivo.

## Por qué importa

Un punto cercano a cero con una cola amplia es un caso muy distinto de uno ancho y positivo, y un solo número no lo distingue. Cambia la decisión de inversión: aprobar un proyecto por un VPN puntual positivo sin ver que el 40 % de los escenarios son negativos es comprar riesgo sin saberlo.

## Cómo funciona

[SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) define el valor presente a 36 meses como la suma de los **márgenes mensuales descontados menos el costo de construcción**. Cada supuesto (tamaño de los centros, costo de construcción, conversión, tasa de descuento) tiene un rango (mínimo, moda, máximo). Se muestrea muchas veces cada rango, se calcula el VPN de cada muestra y se obtiene una distribución. Con rangos, el resultado no es un número sino una **distribución**.

Lo que se informa es la **mediana**, el **intervalo del 5 al 95 por ciento** y la **probabilidad de VPN positivo**; el punto con valores centrales es un caso entre muchos y a menudo no el más representativo, porque las relaciones no lineales hacen que el valor con entradas centrales no coincida con el centro de la distribución.

La clase añade el paso siguiente: calcular la **oscilación por supuesto** (sensibilidad) y medir primero el que más mueve el resultado. Un error típico: el equipo mide el costo de construcción, que es fácil de conocer, y no el tamaño de los centros, que es lo que más mueve el VPN. La corrección es ordenar los supuestos por oscilación y medir el primero.

## Ejemplo

[SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) describe un caso aprobado con un valor presente de 34 mil que luego falla: se informó solo el punto. Con la distribución, el informe habría dicho, por ejemplo (cifras ilustrativas): mediana 20 mil, intervalo del 5 al 95 por ciento de −60 a 110 mil, probabilidad de VPN positivo de 62 %. Con ese informe, la decisión pasa a ser «¿aceptamos un 38 % de probabilidad de pérdida a cambio de este potencial?», y no «es positivo».

## Errores y confusiones comunes

- **Aprobar con un VPN puntual**: falla porque solo se informó el punto; corrección: informar intervalo y probabilidad de valor positivo.
- **Medir lo fácil**: el costo de construcción y no el tamaño de los centros.
- **Tratar los rangos como certezas**: los rangos son supuestos del autor.
- **Muestrear supuestos independientes cuando están correlacionados**: subestima la cola.

## Límites y cuándo no aplica

La distribución solo es tan buena como los rangos y la forma que se les da; [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) declara que los costos, la distribución y las tasas son supuestos del autor, de modo que muestran el método. No incorpora riesgos que no se modelaron. Con supuestos casi desconocidos, el resultado es amplio y debe leerse como una señal de qué investigar antes de decidir.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor presente neto](./valor-presente-neto.md), [Rango](../r/rango.md), [Supuestos](../s/supuestos.md), [Valor](./valor.md), [Caso de viabilidad](../c/caso-de-viabilidad.md), [Compuerta de abandono](../c/compuerta-de-abandono.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HM Treasury: The Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-governent/the-green-book-2020) — evaluación de opciones, descuento, sensibilidad y sesgo de optimismo; autoridad: HM Treasury (Reino Unido).
- [GOV.UK Service Manual: How the beta phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works) — fases con puntos de decisión y evidencia; autoridad: Government Digital Service.
- [GOV.UK Service Manual: How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works) — probar incertidumbres antes de construir; autoridad: Government Digital Service.
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — indicadores con cálculo, fuente y uso; autoridad: Government Digital Service.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — economía de la ingeniería de software, riesgo e incertidumbre; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Valor predictivo positivo](./valor-predictivo-positivo.md) · [Valor presente neto →](./valor-presente-neto.md)
