# Riesgo aceptado

[↑ Glosario](../../README.md) · [← Riesgo](./riesgo.md) · [Riesgo arquitectónico →](./riesgo-arquitectonico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Riesgo conocido que se decide asumir, con responsable, motivo y condición de revisión.

Definición de trabajo de [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md): Riesgo registrado con dueño, escenario y señal de reapertura que el equipo decide no corregir ahora.

## Por qué importa

La clase donde se define, [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), existe con este propósito: el taller existe para que no empieces una modernización sobre un terreno que se mueve.

## Cómo funciona

Según [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md):

Estabilizar es dejar el sistema en un estado donde un cambio produce una señal interpretable. No es refactorizar ni reducir deuda en general: es lograr seis condiciones concretas, cada una con evidencia. **Construcción reproducible**: el mismo código produce el mismo artefacto. **Suite con rojo significativo**: cuando una prueba falla, es por un cambio y no por azar. **Caracterización de los puntos calientes**: el comportamiento de lo que más cambia está fijado (`SE-519`). **Camino de vuelta probado**: se ha desplegado y revertido al menos una vez de forma controlada. **Línea base de métricas**: se conoce el estado actual de la entrega y de las incidencias, con su incertidumbre. **Inventario**: se sabe de qué depende el sistema, quién lo conoce y quién responde por él.

Según [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo ejecuta el taller en seis estaciones durante dos semanas. Estación 1: construye el artefacto dos veces en máquinas distintas, encuentra que las fechas del empaquetado lo impiden, las fija y vuelve a comparar. Estación 2: ejecuta la suite cien veces sobre un commit sano, identifica 7 pruebas inestables de 412 y las pone en cuarentena con dueño y plazo; desactiva los reintentos automáticos de la integración. Estación 3: carga las pruebas de caracterización de los tres puntos calientes del mapa de riesgo. Estación 4: despliega y revierte una versión en el entorno de ensayo, con cronómetro.

## Ejemplo

Ejemplo de [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo ejecuta el taller en seis estaciones durante dos semanas. Estación 1: construye el artefacto dos veces en máquinas distintas, encuentra que las fechas del empaquetado lo impiden, las fija y vuelve a comparar. Estación 2: ejecuta la suite cien veces sobre un commit sano, identifica 7 pruebas inestables de 412 y las pone en cuarentena con dueño y plazo; desactiva los reintentos automáticos de la integración. Estación 3: carga las pruebas de caracterización de los tres puntos calientes del mapa de riesgo. Estación 4: despliega y revierte una versión en el entorno de ensayo, con cronómetro.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md)) son:

- **La suite sale roja y verde sin cambios** — causa: pruebas inestables. Corrección: cuarentena con dueño y plazo, y corregir la causa.
- **Un defecto intermitente llega a producción** — causa: reintentos globales que lo escondieron. Corrección: eliminar los reintentos globales y repetir solo lo nuevo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si una condición no se cumple y se decide entrar igualmente, se escribe como **riesgo aceptado**, con quién lo acepta, por qué y qué señal lo haría volver a estabilizar. ([SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición de revisión](../c/condicion-de-revision.md), [Condición](../c/condicion.md), [Escenario](../e/escenario.md), [Revisión](./revision.md), [Construcción reproducible](../c/construccion-reproducible.md), [Dossier de arquitectura](../d/dossier-de-arquitectura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Luo et al., «An empirical analysis of flaky tests»](https://doi.org/10.1145/2635868.2635920) — causas de las pruebas inestables; autoridad: FSE 2014.
- [Python: zipfile](https://docs.python.org/3/library/zipfile.html) — fechas y orden de los miembros de un archivo; autoridad: documentación de Python.
- [DORA: las cuatro claves](https://dora.dev/guides/dora-metrics-four-keys/) — métricas de entrega; autoridad: DORA.
- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo para una proporción; autoridad: Journal of the American Statistical Association.
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — gestión del riesgo con un presupuesto; autoridad: Google, libro de ingeniería de confiabilidad.

---

[↑ Glosario](../../README.md) · [← Riesgo](./riesgo.md) · [Riesgo arquitectónico →](./riesgo-arquitectonico.md)
