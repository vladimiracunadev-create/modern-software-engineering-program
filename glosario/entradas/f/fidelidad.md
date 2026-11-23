# Fidelidad

[↑ Glosario](../../README.md) · [← Ficha del modelo](./ficha-del-modelo.md) · [Fijación de sesión →](./fijacion-de-sesion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Grado en que un doble se comporta como la dependencia real en lo que las pruebas usan.

Definición de trabajo de [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md).

## Por qué importa

En [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md), el tema «Fidelidad de un doble» importa porque un doble infiel hace pasar pruebas que producción rechazaría.

## Cómo funciona

Según [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md):

Una base en memoria del mismo motor que producción (SQLite en memoria) tiene mucha más fidelidad que un diccionario y casi el mismo costo. Un contenedor desechable con el servicio real (una base de datos, un broker) da fidelidad alta con tiempo de arranque. Un entorno compartido de integración da fidelidad total y trae estado compartido, contención y fallos que dependen de otros. La decisión es de riesgo: cuanto más grave el defecto que solo la dependencia real revela, más cerca de lo real se prueba.

## Ejemplo

Caso medido en la sección «Fidelidad de un doble» de [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md):

Un doble es fiel en la medida en que se comporta como lo real en lo que las pruebas usan. No se mide por inspección: se escribe una batería de comportamientos (rechazar un duplicado, respetar un rango, ordenar los nulos de una forma, tratar mayúsculas) y se ejecuta contra la implementación real y contra el doble. Cada comprobación que el doble no supera es una situación en la que una prueba de servicio pasará con él y fallaría con la real. La batería de contrato es el mismo mecanismo que anclaba al doble en `SE-423`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md)) son:

- **Una prueba con doble pasa y con la dependencia real falla** — causa: el doble no reproduce una regla. Corrección: batería de contrato ejecutada contra ambos.
- **Un refactor sin cambios de comportamiento rompe pruebas** — causa: pruebas que verifican llamadas y orden. Corrección: pruebas de estado y verificación de interacción solo donde el efecto es lo único observable.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un entorno compartido de integración da fidelidad total y trae estado compartido, contención y fallos que dependen de otros. ([SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Doble](../d/doble.md), [Doble de prueba](../d/doble-de-prueba.md), [Espía](../e/espia.md), [Fake](./fake.md), [Prueba de contrato](../p/prueba-de-contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [xUnit Patterns: Test Double](http://xunitpatterns.com/Test%20Double.html) — taxonomía de dobles; autoridad: autor del libro.
- [Martin Fowler, «TestDouble»](https://martinfowler.com/bliki/TestDouble.html) — resumen de dobles; autoridad: autor del texto.
- [Martin Fowler, «Mocks Aren't Stubs»](https://martinfowler.com/articles/mocksArentStubs.html) — estado frente a comportamiento; autoridad: autor del texto.
- [Documentación de unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — dobles en Python; autoridad: documentación oficial de Python.
- [Testcontainers](https://testcontainers.com/) — dependencias reales en contenedores desechables; autoridad: sitio oficial del proyecto.

---

[↑ Glosario](../../README.md) · [← Ficha del modelo](./ficha-del-modelo.md) · [Fijación de sesión →](./fijacion-de-sesion.md)
