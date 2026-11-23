# Verificación de comportamiento

[↑ Glosario](../../README.md) · [← Verificación](./verificacion.md) · [Verificación de contenido →](./verificacion-de-contenido.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Aserción sobre las llamadas que el sujeto hizo.

Definición de trabajo de [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md).

## Por qué importa

La clase donde se define, [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md), existe con este propósito: la clase existe para que elijas con criterio qué comprueba una prueba: el **resultado** que el servicio deja en el mundo o las **llamadas** que hace a sus colaboradores.

## Cómo funciona

Según [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md):

La **verificación de estado** comprueba qué quedó en el mundo tras ejecutar: qué mensajes entregó el canal, qué envíos registró el repositorio. La **verificación de comportamiento** comprueba cómo el servicio trató a sus colaboradores: que llamó a `send` una vez, con tal argumento, antes de llamar a `mark_sent`. La primera es sobre lo observable desde fuera; la segunda, sobre la conversación interna. Una puede ser la misma que la otra cuando el colaborador es el canal que entrega el mensaje (la llamada **es** el efecto), y diferente cuando el colaborador es una consulta (pedir las entregas pendientes no es un efecto, es un detalle).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md)) son: Las dos suites son del autor sobre un servicio pequeño; no se midió ningún equipo ni se cubren los efectos de cada estilo sobre el diseño. El siguiente paso, `SE-544`, pasa del programador a la conversación: BDD escribe los ejemplos con el vocabulario del negocio y los ejecuta como pruebas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Aserción](../a/asercion.md), [Sobre](../s/sobre.md), [Sujeto](../s/sujeto.md), [Cambio de contrato](../c/cambio-de-contrato.md), [Doble](../d/doble.md), [Fake / doble con estado](../f/fake-doble-con-estado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Verificación](./verificacion.md) · [Verificación de contenido →](./verificacion-de-contenido.md)
