# Regla de dependencia

[↑ Glosario](../../README.md) · [← Regla de decisión](./regla-de-decision.md) · [Regla de las tres condiciones →](./regla-de-las-tres-condiciones.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Las dependencias del código fuente apuntan hacia las políticas de alto nivel y no hacia los detalles.

Definición de trabajo de [SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md).

## Por qué importa

En [SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), el tema «Regla de dependencia» importa porque hace que lo que más cambia dependa de lo que menos cambia.

## Cómo funciona

Según [SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md):

La **regla de dependencia** (formulada por Martin en la arquitectura limpia) dice que las dependencias del código fuente solo apuntan hacia adentro: hacia las políticas de alto nivel, que cambian poco, y nunca hacia los detalles (base de datos, framework, proveedor), que cambian más. Se logra con inversión de dependencias: el dominio declara la interfaz que necesita y el detalle la implementa. El beneficio es un cambio acotado: reemplazar la base de datos toca el adaptador y el arranque, no el dominio. La regla es fácil de enunciar y fácil de violar; por eso se comprueba con una herramienta de análisis de importaciones, no con la memoria del equipo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md):

El equipo de la plataforma reorganiza el módulo de notas: `notas/dominio` contiene las reglas y el puerto `Repositorio`; `notas/aplicacion` los casos de uso; `notas/adaptadores` el adaptador SQLite y el doble en memoria. Un comprobador de importaciones (el de `SE-327`) falla si `dominio` importa `adaptadores`, `sqlite3` o el framework web. La suite de contrato corre contra el doble y contra SQLite en cada commit; las pruebas de regla usan el doble (0,01 ms) y solo una docena de pruebas de integración usan SQLite en archivo (100 ms).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md)) son:

- **Cambiar la base de datos toca decenas de módulos** — causa: el dominio depende de la infraestructura. Corrección: invertir la dependencia con un puerto y comprobar las importaciones.
- **Las capas existen en los nombres pero el código salta capas** — causa: no hay una regla comprobable. Corrección: añadir un comprobador de importaciones al CI.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **regla de dependencia** (formulada por Martin en la arquitectura limpia) dice que las dependencias del código fuente solo apuntan hacia adentro: hacia las políticas de alto nivel, que cambian poco, y nunca hacia los detalles (base de datos, framework, proveedor), que cambian más. ([SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Adaptador](../a/adaptador.md), [Doble de prueba](../d/doble-de-prueba.md), [Prueba de contrato](../p/prueba-de-contrato.md), [Puerto](../p/puerto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Martin, «The Clean Architecture»](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) — regla de dependencia; autoridad: Robert C. Martin.
- [Cockburn, «Hexagonal architecture»](https://alistair.cockburn.us/hexagonal-architecture/) — puertos y adaptadores; autoridad: Alistair Cockburn.
- [Fowler, «Test Double»](https://martinfowler.com/bliki/TestDouble.html) — tipos de dobles de prueba; autoridad: Martin Fowler.
- [Fowler, «Contract Test»](https://martinfowler.com/bliki/ContractTest.html) — pruebas que mantienen de acuerdo a un doble y a la implementación real; autoridad: Martin Fowler.
- [Python: `sqlite3`](https://docs.python.org/3/library/sqlite3.html) — base usada en la medición; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Regla de decisión](./regla-de-decision.md) · [Regla de las tres condiciones →](./regla-de-las-tres-condiciones.md)
