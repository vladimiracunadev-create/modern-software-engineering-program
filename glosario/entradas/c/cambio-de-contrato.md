# Cambio de contrato

[↑ Glosario](../../README.md) · [← Cambio compatible](./cambio-compatible.md) · [Cambio de plan →](./cambio-de-plan.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Alteración de la interfaz de un colaborador; no es un refactor.

Definición de trabajo de [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md).

## Por qué importa

En [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md), el tema «Cambio de contrato» importa porque renombrar un puerto no es un refactor; rompe ambos estilos.

## Cómo funciona

Según [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md):

Un **refactor** cambia la estructura interna y conserva el comportamiento observable. Un **cambio de contrato** altera la interfaz de un colaborador: renombrar un puerto, añadir un parámetro obligatorio. Rompe cualquier prueba que use esa interfaz, con independencia del estilo. Es importante clasificar bien: cuando una prueba se rompe tras un cambio de contrato no hay nada que corregir en la prueba salvo adaptarla, y quien lo llama «refactor» induce a error en la revisión.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Es importante clasificar bien: cuando una prueba se rompe tras un cambio de contrato no hay nada que corregir en la prueba salvo adaptarla, y quien lo llama «refactor» induce a error en la revisión. ([SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Refactor](../r/refactor.md).
- **Ver también:** [Interfaz](../i/interfaz.md), [Doble](../d/doble.md), [Fake / doble con estado](../f/fake-doble-con-estado.md), [Simulado](../s/simulado.md), [Verificación de comportamiento](../v/verificacion-de-comportamiento.md), [Verificación de estado](../v/verificacion-de-estado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md), [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cambio compatible](./cambio-compatible.md) · [Cambio de plan →](./cambio-de-plan.md)
