# Límite declarado

[↑ Glosario](../../README.md) · [← Límite de trabajo en curso](./limite-de-trabajo-en-curso.md) · [Límites de lenguajes declarativos →](./limites-de-lenguajes-declarativos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Un **límite declarado** es la afirmación explícita de lo que un artefacto no cubre o no demuestra: lo que ni el modelo ni el validador ven ([SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md)), lo que un paquete no probó ([SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md)) o la lista de lo que no se midió, no se probó o se supuso, escrita en el propio dossier ([SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md)). Es la parte honesta de un documento técnico.

## Por qué importa

Un dossier o paquete sin límites parece más sólido, pero solo es más opaco: quien lo lee no sabe qué comprobar antes de confiar. La decisión que cambia es qué se entrega junto con el resultado: además de lo que se afirma, lo que no se afirma. [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) lo dice con claridad: un paquete sin límites declarados no es más seguro, solo más opaco.

## Cómo funciona

[SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) agrupa los límites en tres:

1. **Lo que el validador no ve**: el sentido de los umbrales, funciones de aptitud triviales, contradicciones entre ADR.
2. **Lo que el modelo no ve**: degradación parcial, reintentos, colas reales, seguridad, correlaciones de fallos.
3. **Lo que nadie ha medido**: latencias reales, disponibilidades reales, carga real.

Cada límite lleva un **responsable** y una **señal para dejar de ser un supuesto** (una prueba de carga, un mes de telemetría). Eso lo vuelve un compromiso verificable, no una disculpa genérica.

[SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) lo concreta en un archivo, `LIMITES.md`, que declara qué no se probó (un motor distinto, el tiempo de restauración con el volumen real, el cifrado, el proveedor), qué se supuso (plazos de retención, volúmenes, popularidad de las claves) y qué ningún validador ve (las cuatro familias de mutación de sentido). Una lista así permite a quien opera el paquete decidir qué comprobar antes de confiar y a quien lo revisa saber qué exigir. [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md) lo lleva al nivel de gestión: la lista de lo que no se midió ni se probó va en el propio dossier.

## Ejemplo

Un paquete de recuperación de datos incluye una prueba de restauración con una base pequeña. Su `LIMITES.md` dice: no se probó el tiempo de restauración con el volumen real; se supuso un plazo de retención de 30 días; el validador no ve mutaciones que cambian el sentido de un umbral. Para cada uno, un responsable y la señal que lo cerraría (por ejemplo, una restauración con datos del tamaño real). Basado en la estructura de [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md).

## Errores y confusiones comunes

- **El comité pregunta por una caída y no hay respuesta**: documento sin escenarios ni modelo; se corrige con escenarios medibles y un modelo que los evalúa.
- **Los diagramas se contradicen**: vistas mantenidas a mano; se corrige generándolas desde un modelo único.
- **Declarar límites genéricos** («puede haber errores»): no dicen qué comprobar.
- **Creer que declarar límites debilita el trabajo**: es lo que permite cuestionarlo con precisión.

## Límites y cuándo no aplica

Declarar un límite no lo resuelve: lo hace visible. Una lista de límites sin responsable ni señal de cierre se vuelve un descargo de responsabilidad. Y no hace falta para entregables triviales y desechables; su valor crece con el costo de equivocarse al confiar en el artefacto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Artefacto](../a/artefacto.md), [Modelo](../m/modelo.md), [Bitácora de cambios](../b/bitacora-de-cambios.md), [Dossier de arquitectura](../d/dossier-de-arquitectura.md), [Impacto de una decisión](../i/impacto-de-una-decision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (20 clases más lo mencionan; las que más):

[SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), [SE-538](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-538-portafolio-entrevistas-y-defensa-profesional/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «límites declarados».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [arc42](https://arc42.org/) — plantilla de documentación de arquitectura; autoridad: arc42.
- [Ford, Parsons y Kua, «Building Evolutionary Architectures» (O'Reilly)](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/) — funciones de aptitud continuas; autoridad: O'Reilly Media.
- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — evaluación de arquitectura contra escenarios; autoridad: Software Engineering Institute (Carnegie Mellon).
- [Nygard, «Documenting Architecture Decisions»](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registros de decisión; autoridad: Michael Nygard.
- [C4 model](https://c4model.com/) — niveles de diagramas de arquitectura; autoridad: Simon Brown.

---

[↑ Glosario](../../README.md) · [← Límite de trabajo en curso](./limite-de-trabajo-en-curso.md) · [Límites de lenguajes declarativos →](./limites-de-lenguajes-declarativos.md)
