# Razón de cambio

[↑ Glosario](../../README.md) · [← Raw data](./raw-data.md) · [Razón de contraste →](./razon-de-contraste.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Decisión o grupo de personas cuya petición obliga a modificar un módulo.

Definición de trabajo de [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md).

## Por qué importa

La clase donde se define, [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), existe con este propósito: la clase existe para que uses los cinco principios SOLID como preguntas que se contrastan con un cambio y una prueba, y para que sepas cuándo cada uno deja de pagar: un principio aplicado sin un cambio que lo justifique es estructura que se lee, se prueba y se mantiene sin comprar nada.

## Cómo funciona

[SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md):

El equipo no aplica los cinco principios a la vez: elige por cambio. Para los descuentos, que marketing añade cada trimestre, introduce el registro de reglas y deja la política de combinación (el máximo) escrita en un solo lugar con una prueba. Para `TarifaExpress`, escribe la prueba de contrato de `Tarifa`, la ejecuta contra todas las subclases y convierte la restricción de 20 kilos en una validación explícita que ningún cliente espera de una `Tarifa` general.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md)) son:

- **Cada regla nueva reabre la misma función** — causa: cadena de condicionales sin punto de extensión. Corrección: registrar reglas y escribir la política de combinación en un solo sitio.
- **Una subclase pasa los ejemplos y falla con datos reales** — causa: contrato no escrito como prueba, o probado solo con camino feliz. Corrección: ejecutar una prueba de contrato con azar y bordes contra todas las subclases.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis con código de ejemplo y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna base de código real ni la frecuencia de cada problema; los contratos, las subclases y los clientes son construcciones del autor. La siguiente clase compara herencia, composición y delegación como formas de reutilizar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Módulo](../m/modulo.md), [Contrato](../c/contrato.md), [Dependencia nominal](../d/dependencia-nominal.md), [Prueba de contrato](../p/prueba-de-contrato.md), [Punto de extensión](../p/punto-de-extension.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Martin, «The Single Responsibility Principle» (2014)](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html) — responsabilidad única como razón de cambio; autoridad: su autor.
- [Liskov y Wing, «A behavioral notion of subtyping» (ACM TOPLAS, 1994)](https://doi.org/10.1145/197320.197383) — subtipos que preservan el comportamiento; autoridad: ACM Transactions on Programming Languages and Systems.
- [Martin, «The Open-Closed Principle» (2014)](https://blog.cleancoder.com/uncle-bob/2014/05/12/TheOpenClosedPrinciple.html) — formulación del principio abierto/cerrado; autoridad: su autor.
- [PEP 544, protocolos](https://peps.python.org/pep-0544/) — tipos estructurales en Python; autoridad: Python Enhancement Proposals.
- [Python: `abc`](https://docs.python.org/3/library/abc.html) — clases abstractas; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Raw data](./raw-data.md) · [Razón de contraste →](./razon-de-contraste.md)
