# Prueba de contrato

[↑ Glosario](../../README.md) · [← Prueba de carga](./prueba-de-carga.md) · [Prueba de contrato dirigida por el consumidor →](./prueba-de-contrato-dirigida-por-el-consumidor.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Una **prueba de contrato** es una prueba, o una batería de pruebas, escrita contra una interfaz o un puerto y ejecutada contra todas sus implementaciones, para comprobar que cumplen lo mismo. [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) la define como la batería común que debe pasar toda implementación de una interfaz, [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) como la prueba que se ejecuta contra todas las implementaciones y [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md) como la escrita contra un puerto y ejecutada contra todas sus implementaciones. [SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) la usa con otro matiz: ejecutar la herramienta como lo haría un consumidor y comprobar código de salida, flujos y efectos. El núcleo común es comprobar lo que un consumidor puede esperar.

## Por qué importa

Sin ella, cada implementación es una promesa privada. [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) lo ilustra con el patrón adaptador: la prueba de contrato es la pieza que mantiene honesto al patrón, porque obliga a que cualquier adaptador nuevo pase la misma batería. También protege a los dobles de prueba: un doble que no se contrasta con la implementación real acaba diciendo algo falso.

## Cómo funciona

Se escribe una sola batería contra el contrato (la interfaz o el puerto) y se parametriza por implementación. En [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), la aplicación *Avisos* integra dos proveedores: uno expone `enviar(to, body)` y devuelve un diccionario con `id` y `status`; el otro, `push(destinatario, texto, prioridad)` y devuelve una tupla `(id, código HTTP)`. Dos adaptadores presentan a ambos la interfaz única `send(to, body)` que devuelve `(id, aceptado)`, y la prueba de contrato comprueba que con una misma llamada ambos devuelven la misma forma. La causa de su utilidad es que el contrato queda ejecutable: un cambio en un proveedor rompe la prueba y no al usuario.

## Ejemplo

[SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md): con una misma llamada, los adaptadores devuelven `('a1', True)` y `('b1', True)`: forma idéntica, valores propios de cada proveedor. Si un tercer adaptador devolviera otra forma, la batería común lo detectaría antes de integrarlo. En [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), una subclase pasa los ejemplos y falla con datos reales; la corrección es ejecutar una prueba de contrato con azar y bordes contra todas las subclases.

## Errores y confusiones comunes

- **Contrato no escrito como prueba, o probado solo con el camino feliz.** Una subclase pasa los ejemplos y falla con datos reales ([SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md)).
- **Cada adaptador con su propia prueba.** Es una promesa privada sin una batería común ([SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md)).
- **Confundirla con una prueba del consumidor.** [SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) y [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) usan el término del lado del consumidor; lo común es que el contrato sea verificable.

## Límites y cuándo no aplica

La prueba de contrato comprueba lo que el contrato dice: si el contrato omite un comportamiento, ninguna implementación será juzgada por él. Los ejemplos de las clases son sintéticos (dos proveedores de mensajería ficticios). Y como el término se usa en sentidos cercanos (entre implementaciones, entre consumidor y proveedor, de una herramienta), conviene confirmar cuál aplica en cada clase.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Doble](../d/doble.md), [Efecto](../e/efecto.md), [Flujo](../f/flujo.md), [Herramientas](../h/herramientas.md), [Contrato](../c/contrato.md), [Decisión humana abierta](../d/decision-humana-abierta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (34 clases más lo mencionan; las que más):

[SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md), [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), [SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md), [SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

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

[↑ Glosario](../../README.md) · [← Prueba de carga](./prueba-de-carga.md) · [Prueba de contrato dirigida por el consumidor →](./prueba-de-contrato-dirigida-por-el-consumidor.md)
