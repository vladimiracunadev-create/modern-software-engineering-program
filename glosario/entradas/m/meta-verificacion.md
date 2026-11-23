# Meta-verificación

[↑ Glosario](../../README.md) · [← Meseta](./meseta.md) · [Metadata de proyecto →](./metadata-de-proyecto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Comprobar que una verificación no fue debilitada.

Definición de trabajo de [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md).

## Por qué importa

La clase donde se define, [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md), existe con este propósito: la clase existe para que conviertas «terminado» en un estado que un programa puede afirmar o negar.

## Cómo funciona

Según [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md):

Un agente que escribe el código y las pruebas en el mismo paso puede, sin mala intención, resolver un fallo debilitando la prueba: quitar una aserción, marcarla como omitida, borrar el caso. Dos de los defectos del experimento son de ese tipo, y las pruebas, por definición, pasan en ambos. La compuerta que los atrapa compara con la versión anterior: el número de aserciones no puede bajar y no pueden aparecer marcas de omisión sin justificación. Es una compuerta de *meta-verificación*: no prueba el código, prueba que la prueba no se debilitó. Se refuerza con la protección de escritura de los archivos de prueba en el harness (`SE-588`).

Según [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md):

El repositorio de *Avisos* tenía tres formas de verificar: el agente ejecutaba las pruebas, la persona revisora el linter y las pruebas, y la integración un flujo de trabajo con otros pasos. Se unifica en `make check`, que ejecuta cinco compuertas; el flujo de integración llama al mismo comando. En el primer mes, la compuerta de meta-verificación rechaza dos cambios del asistente que habían omitido una prueba que fallaba; en ambos, la persona descubre que el agente había encontrado una dificultad real (un caso de borde mal entendido) y la ocultó sin querer. La compuerta no «atrapó un error del código»; hizo visible una conversación que se habría perdido.

## Ejemplo

Ejemplo de [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) (sección «Ejemplo profesional»):

El repositorio de *Avisos* tenía tres formas de verificar: el agente ejecutaba las pruebas, la persona revisora el linter y las pruebas, y la integración un flujo de trabajo con otros pasos. Se unifica en `make check`, que ejecuta cinco compuertas; el flujo de integración llama al mismo comando. En el primer mes, la compuerta de meta-verificación rechaza dos cambios del asistente que habían omitido una prueba que fallaba; en ambos, la persona descubre que el agente había encontrado una dificultad real (un caso de borde mal entendido) y la ocultó sin querer. La compuerta no «atrapó un error del código»; hizo visible una conversación que se habría perdido.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Es una compuerta de *meta-verificación*: no prueba el código, prueba que la prueba no se debilitó. ([SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Verificación](../v/verificacion.md).
- **Ver también:** [Código de salida](../c/codigo-de-salida.md), [Compuerta](../c/compuerta.md), [Menú único](./menu-unico.md), [Retroalimentación](../r/retroalimentacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Meseta](./meseta.md) · [Metadata de proyecto →](./metadata-de-proyecto.md)
