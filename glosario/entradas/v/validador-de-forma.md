# Validador de forma

[↑ Glosario](../../README.md) · [← Validador de estructura](./validador-de-estructura.md) · [Validador de paquete →](./validador-de-paquete.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Un **validador de forma** es un programa que comprueba la estructura y las referencias de un dosier, no su sentido. [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) (proyecto: plataforma mínima reproducible) lo define como un comprobador que decide si un paquete está completo y es coherente en su estructura, sin interpretar su contenido; [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) lo describe como un programa que comprueba la estructura de un documento sin entender su sentido; [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) lo usa en el dosier de arquitectura.

## Por qué importa

Impide dosieres rotos sin pretender evaluarlos. Es barato y se ejecuta en cada cambio. Pero conviene no confundir un validador en verde con un dosier correcto: detecta lo estructural y deja pasar lo que exige interpretar.

## Cómo funciona

[SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) enumera reglas típicas de un validador:

- Identificadores únicos.
- Referencias que existen.
- Umbrales numéricos con unidad.
- Al menos dos alternativas por ADR.
- Estados válidos.
- Vistas con los mismos componentes.
- **Cobertura:** todo driver tiene un escenario, todo escenario una decisión, y todo escenario alto una función de aptitud o una excepción.

Son reglas locales y de referencia que un programa puede comprobar mecánicamente. Su límite está en el nombre: valida la *forma*. No sabe si un umbral es razonable, si una función de aptitud comprueba lo que dice o si una decisión contradice a otra. Para esas cosas hace falta revisión humana. Esta división de trabajo (máquina para lo estructural, personas para el sentido) es la que sostiene la entrega.

## Ejemplo

En [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), el equipo entrega `architecture-dossier/` con un `modelo.yaml` del que se generan las cuatro vistas, doce escenarios y cuatro ADR. El validador comprueba que cada driver tenga escenario y que cada escenario alto tenga función de aptitud. En [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), el paquete del dispositivo pasa su validador y aun así puede fallar en la flota si falta una regla de sentido.

## Errores y confusiones comunes

- **El paquete pasa el validador y falla en la flota:** validador de forma sin reglas de sentido; corrección, reglas de sentido y revisión humana ([SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md)).
- **Tomar «validado» por «correcto».**
- **Un dosier completo con afirmaciones sin evidencia** ([SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)).
- **Añadir reglas que parecen de sentido pero solo comprueban presencia.**

## Límites y cuándo no aplica

Cuanto más rica la estructura, más útil el validador; para documentos sin estructura formal, no hay mucho que comprobar. Y no sustituye las pruebas del comportamiento del sistema descrito. Agregar reglas de sentido tiene un límite: lo que requiere juicio queda en manos de personas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Estructura](../e/estructura.md), [Paquete](../p/paquete.md), [Referencia](../r/referencia.md), [Dossier de arquitectura](../d/dossier-de-arquitectura.md), [Gemelo simulado](../g/gemelo-simulado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [arc42](https://arc42.org/) — plantilla de documentación de arquitectura; autoridad: arc42.
- [Ford, Parsons y Kua, «Building Evolutionary Architectures» (O'Reilly)](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/) — funciones de aptitud continuas; autoridad: O'Reilly Media.
- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — evaluación de arquitectura contra escenarios; autoridad: Software Engineering Institute (Carnegie Mellon).
- [Nygard, «Documenting Architecture Decisions»](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registros de decisión; autoridad: Michael Nygard.
- [C4 model](https://c4model.com/) — niveles de diagramas de arquitectura; autoridad: Simon Brown.

---

[↑ Glosario](../../README.md) · [← Validador de estructura](./validador-de-estructura.md) · [Validador de paquete →](./validador-de-paquete.md)
