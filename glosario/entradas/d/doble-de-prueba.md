# Doble de prueba

[↑ Glosario](../../README.md) · [← Doble](./doble.md) · [Doble escritura →](./doble-escritura.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Un **doble de prueba** es un sustituto de un componente real que se usa durante una prueba para hacerla más rápida, aislada o determinista. Es la definición de [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md) y [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md); [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) añade la condición que lo hace legítimo: un adaptador sustituto debe cumplir el mismo contrato que el real. [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) nombra tres variantes habituales: *stub*, *mock* y *fake*.

## Por qué importa

Probar contra un proveedor real puede ser lento, caro o imposible de controlar (una red, un reloj, un cobro). El doble quita esa dependencia y permite repetir la misma condición cuantas veces haga falta. Pero [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) señala el costo oculto: **el doble encarna la creencia del consumidor sobre el proveedor**, y cuando el proveedor cambia, el doble sigue diciendo lo mismo, de modo que las pruebas pasan sobre una realidad que ya no existe.

## Cómo funciona

El doble ocupa el lugar de una dependencia detrás de una interfaz y responde según lo que quien escribe la prueba decidió. [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) nombra tres variantes habituales (*stub*, *mock* y *fake*) y [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) amplía el abanico a bases en memoria, contenedores y máquinas virtuales: lo que se reemplaza en una prueba es una decisión que se paga en **fidelidad**, en **acoplamiento a la implementación** y en **diferencias de entorno** que cambian el resultado. La frase de [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) lo resume: todo doble es una apuesta, porque ahorra tiempo y aislamiento a cambio de dejar de comprobar algo.

La defensa contra la deriva es **verificar el doble contra el proveedor real**, de modo que cada afirmación del doble sea una afirmación comprobada; esa es la idea de fondo de las pruebas de contrato ([SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md)). [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) lo aplica a un producto con dos plataformas: un contrato de adaptadores impide que los dobles de prueba prometan lo que la plataforma real no cumple.

## Ejemplo

[SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) presenta el riesgo desde el consumidor: el doble dice lo que el consumidor cree, y si el proveedor cambia, las pruebas del consumidor siguen pasando sobre una realidad que ya no existe. La corrección que propone la clase es comprobar el doble contra el proveedor real. [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) la aplica con un contrato de adaptadores que obliga al adaptador sustituto y al real a cumplir lo mismo.

## Errores y confusiones comunes

- **Confiar en el doble sin verificarlo.** Cuando el proveedor cambia, el doble sigue diciendo lo mismo ([SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md)).
- **Ignorar el costo de fidelidad y de acoplamiento.** Cada doble deja de comprobar algo y puede atar la prueba a la implementación ([SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md)).
- **Tomar un doble por un contrato.** Un doble describe lo que el consumidor espera; el contrato se verifica contra el proveedor ([SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)).

## Límites y cuándo no aplica

Un doble no prueba el sistema real: prueba el consumidor frente a una creencia. [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) lo trata como herramienta legítima con un riesgo concreto, y la mitigación (verificarlo contra el proveedor) tiene un costo de mantenimiento. No sustituye a las pruebas de integración con el proveedor real en el nivel donde se necesite comprobar el comportamiento de verdad, ni a la observación en producción.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Adaptador](../a/adaptador.md), [Componente](../c/componente.md), [Contrato](../c/contrato.md), [Dependencia](./dependencia.md), [Contrato de consumidor](../c/contrato-de-consumidor.md), [Contrato de puerto](../c/contrato-de-puerto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md), [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Dobles de prueba», «doble de pruebas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Test Double»](https://martinfowler.com/bliki/TestDouble.html) — tipos de dobles de prueba; autoridad: Martin Fowler.
- [Fowler: Consumer-Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html) — contratos que expresan lo que cada consumidor usa; autoridad: martinfowler.com.
- [Pact documentation](https://docs.pact.io/) — implementación del enfoque dirigido por el consumidor; autoridad: proyecto Pact.
- [Claessen y Hughes, «QuickCheck» (ICFP, 2000)](https://doi.org/10.1145/351240.351266) — pruebas basadas en propiedades y reducción; autoridad: ACM SIGPLAN ICFP.
- [Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de pruebas de propiedades para Python con reducción; autoridad: proyecto Hypothesis.

---

[↑ Glosario](../../README.md) · [← Doble](./doble.md) · [Doble escritura →](./doble-escritura.md)
