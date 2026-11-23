# Validador de forma

[↑ Glosario](../../README.md) · [← Validador de estructura](./validador-de-estructura.md) · [Validador de paquete →](./validador-de-paquete.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Programa que comprueba la estructura y las referencias de un dossier, no su sentido.

Definición de trabajo de [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md): Comprobador que decide si un paquete está completo y es coherente en su estructura, sin interpretar su contenido.
- En [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md): Programa que comprueba la estructura de un documento sin entender su sentido.

## Por qué importa

En [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), el tema «Validador de forma» importa porque impide dossiers rotos sin pretender evaluarlos.

En [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), el tema «Validador de forma» importa porque detecta lo estructural y deja pasar lo que exige interpretar.

## Cómo funciona

Según [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), en la sección «Validador de forma»:

Un validador comprueba reglas locales y de referencia: identificadores únicos, referencias que existen, umbrales numéricos con unidad, al menos dos alternativas por ADR, estados válidos, vistas con los mismos componentes, y cobertura (todo driver tiene un escenario, todo escenario una decisión, todo escenario alto una función de aptitud o una excepción). Es barato y se ejecuta en cada cambio. Su límite está en el nombre: valida la *forma*. No sabe si un umbral es razonable, si una función de aptitud comprueba lo que dice o si una decisión contradice a otra.

## Ejemplo

Ejemplo de [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) (sección «Ejemplo profesional»):

El equipo entrega `architecture-dossier/` con un `modelo.yaml` del que se generan las cuatro vistas, doce escenarios, cuatro ADR y seis funciones de aptitud que corren en CI (dominio sin importaciones de infraestructura, p95 del recorrido de entrega, capacidad del pico, presupuesto de disponibilidad, uso por unidad y fallo inyectado del antivirus). El validador de forma corre en cada cambio y rechaza referencias rotas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El paquete pasa el validador y falla en la flota** — causa: validador de forma sin reglas de sentido. Corrección: añadir reglas de sentido y una revisión humana. ([SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres análisis con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se desplegó ni se midió ningún sistema: el dossier, las mutaciones, las caídas, el 30 % de causa común, los picos y el grafo de impacto son construcciones del autor, y el validador se escribió mirando las mismas mutaciones que lo evalúan.

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
