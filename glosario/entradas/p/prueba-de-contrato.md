# Prueba de contrato

[↑ Glosario](../../README.md) · [← Prueba de carga](./prueba-de-carga.md) · [Prueba de contrato dirigida por el consumidor →](./prueba-de-contrato-dirigida-por-el-consumidor.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Prueba que se ejecuta contra todas las implementaciones de una interfaz para comprobar que cumplen lo mismo.

Definición de trabajo de [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md): Batería común que debe pasar toda implementación de una interfaz.
- En [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md): Prueba que ejecuta la herramienta como lo haría un consumidor y comprueba código, flujos y efectos.
- En [SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md): Prueba escrita contra un puerto y ejecutada contra todas sus implementaciones.
- En [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md): Batería de comprobaciones que se ejecuta contra el doble y contra la implementación real.

## Por qué importa

La clase donde se define, [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), existe con este propósito: la clase existe para que uses los cinco principios SOLID como preguntas que se contrastan con un cambio y una prueba, y para que sepas cuándo cada uno deja de pagar: un principio aplicado sin un cambio que lo justifique es estructura que se lee, se prueba y se mantiene sin comprar nada.

## Cómo funciona

Según [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md):

Donde se espera una `Tarifa` debe poder usarse cualquier subclase sin que el cliente lo note. Eso fija un **contrato**: precondiciones (qué acepta), postcondiciones (qué devuelve) e invariantes (qué se mantiene). Una subclase puede aceptar más y prometer más; si acepta menos (rechaza pesos altos), devuelve menos (pierde monotonía) o lanza excepciones nuevas, rompe al cliente. El lenguaje no lo comprueba: lo comprueba una prueba de contrato que se ejecuta contra todas las subclases.

Según [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md):

El equipo no aplica los cinco principios a la vez: elige por cambio. Para los descuentos, que marketing añade cada trimestre, introduce el registro de reglas y deja la política de combinación (el máximo) escrita en un solo lugar con una prueba. Para `TarifaExpress`, escribe la prueba de contrato de `Tarifa`, la ejecuta contra todas las subclases y convierte la restricción de 20 kilos en una validación explícita que ningún cliente espera de una `Tarifa` general. Para el servicio con la interfaz de doce métodos, define dos protocolos, `LeeTarifa` y `CalculaRecargo`, con `typing.Protocol`. Y para el redondeo, que se usa una vez, deja una función.

## Ejemplo

Ejemplo de [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) (sección «Ejemplo profesional»):

El equipo no aplica los cinco principios a la vez: elige por cambio. Para los descuentos, que marketing añade cada trimestre, introduce el registro de reglas y deja la política de combinación (el máximo) escrita en un solo lugar con una prueba. Para `TarifaExpress`, escribe la prueba de contrato de `Tarifa`, la ejecuta contra todas las subclases y convierte la restricción de 20 kilos en una validación explícita que ningún cliente espera de una `Tarifa` general. Para el servicio con la interfaz de doce métodos, define dos protocolos, `LeeTarifa` y `CalculaRecargo`, con `typing.Protocol`. Y para el redondeo, que se usa una vez, deja una función.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una subclase pasa los ejemplos y falla con datos reales** — causa: contrato no escrito como prueba, o probado solo con camino feliz. Corrección: ejecutar una prueba de contrato con azar y bordes contra todas las subclases. ([SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El lenguaje no lo comprueba: lo comprueba una prueba de contrato que se ejecuta contra todas las subclases. ([SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md))

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
