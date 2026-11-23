# Dependencia nominal

[↑ Glosario](../../README.md) · [← Dependencia funcional](./dependencia-funcional.md) · [Dependencia sin soporte →](./dependencia-sin-soporte.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Dependencia declarada en el tipo, aunque el cliente no use todos sus métodos.

Definición de trabajo de [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md).

## Por qué importa

En [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), el tema «Segregación de interfaces» importa porque reduce la dependencia nominal de cada cliente.

## Cómo funciona

Según [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md):

Un cliente no debe depender de métodos que no usa. Una interfaz ancha obliga a cada cliente a revisar, recompilar o doblar métodos ajenos, y vuelve incierto qué cambio afecta a quién. La segregación crea interfaces por rol (leer tarifa, calcular recargo, cobrar). Reduce la dependencia nominal, no la real: si el cambio es en un método que sí usan, el cliente se afecta igual.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md):

El equipo no aplica los cinco principios a la vez: elige por cambio. Para los descuentos, que marketing añade cada trimestre, introduce el registro de reglas y deja la política de combinación (el máximo) escrita en un solo lugar con una prueba. Para `TarifaExpress`, escribe la prueba de contrato de `Tarifa`, la ejecuta contra todas las subclases y convierte la restricción de 20 kilos en una validación explícita que ningún cliente espera de una `Tarifa` general.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md)) son:

- **Cada regla nueva reabre la misma función** — causa: cadena de condicionales sin punto de extensión. Corrección: registrar reglas y escribir la política de combinación en un solo sitio.
- **Una subclase pasa los ejemplos y falla con datos reales** — causa: contrato no escrito como prueba, o probado solo con camino feliz. Corrección: ejecutar una prueba de contrato con azar y bordes contra todas las subclases.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Reduce la dependencia nominal, no la real: si el cambio es en un método que sí usan, el cliente se afecta igual. ([SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](./dependencia.md), [Tipo](../t/tipo.md), [Contrato](../c/contrato.md), [Prueba de contrato](../p/prueba-de-contrato.md), [Punto de extensión](../p/punto-de-extension.md), [Razón de cambio](../r/razon-de-cambio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Liskov y Wing, «A behavioral notion of subtyping» (ACM TOPLAS, 1994)](https://doi.org/10.1145/197320.197383) — subtipos que preservan el comportamiento; autoridad: ACM Transactions on Programming Languages and Systems.
- [Martin, «The Open-Closed Principle» (2014)](https://blog.cleancoder.com/uncle-bob/2014/05/12/TheOpenClosedPrinciple.html) — formulación del principio abierto/cerrado; autoridad: su autor.
- [Martin, «The Single Responsibility Principle» (2014)](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html) — responsabilidad única como razón de cambio; autoridad: su autor.
- [PEP 544, protocolos](https://peps.python.org/pep-0544/) — tipos estructurales en Python; autoridad: Python Enhancement Proposals.
- [Python: `abc`](https://docs.python.org/3/library/abc.html) — clases abstractas; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Dependencia funcional](./dependencia-funcional.md) · [Dependencia sin soporte →](./dependencia-sin-soporte.md)
