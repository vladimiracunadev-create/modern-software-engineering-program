# Perturbación

[↑ Glosario](../../README.md) · [← Personas y promedios](./personas-y-promedios.md) · [Petición condicional →](./peticion-condicional.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Cambio deliberado de una entrada para ver qué salidas se alteran.

Definición de trabajo de [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md).

## Por qué importa

La clase donde se define, [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), existe con este propósito: la clase existe para que puedas responder dos preguntas que una plataforma de datos recibe todos los días y que casi nadie puede contestar con certeza:

## Cómo funciona

Según [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md):

El equipo de *Avisos* quiere retirar tres columnas antiguas de la tabla de lecturas. Con el linaje de tablas, el catálogo dice que veinte activos dependen de ella, demasiado para revisar. Con linaje de columnas y condiciones, dos de las tres columnas no tienen consumidores y la tercera aparece en un filtro de un informe de finanzas. El equipo ejecuta la prueba de perturbación sobre la tercera en una copia: cambia cuatro columnas de salida de dos informes. Avisa a los dos dueños con la lista exacta, fija una fecha de retiro de seis semanas y retira las dos columnas sin consumidores esa misma semana. El catálogo registra la decisión y la fecha y comprueba que, al llegar la fecha, el uso en el registro de consultas sea cero.

Según [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md):

Una herramienta captura lo que sus conectores ven. Mide su cobertura con una prueba de perturbación sobre columnas conocidas y declara lo que no cubre. Sin esa medición, un grafo bonito es una opinión.

## Ejemplo

Ejemplo de [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* quiere retirar tres columnas antiguas de la tabla de lecturas. Con el linaje de tablas, el catálogo dice que veinte activos dependen de ella, demasiado para revisar. Con linaje de columnas y condiciones, dos de las tres columnas no tienen consumidores y la tercera aparece en un filtro de un informe de finanzas. El equipo ejecuta la prueba de perturbación sobre la tercera en una copia: cambia cuatro columnas de salida de dos informes. Avisa a los dos dueños con la lista exacta, fija una fecha de retiro de seis semanas y retira las dos columnas sin consumidores esa misma semana.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Mide su cobertura con una prueba de perturbación sobre columnas conocidas y declara lo que no cubre. ([SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Arista de condición](../a/arista-de-condicion.md), [Arista de valor](../a/arista-de-valor.md), [Catálogo de datos](../c/catalogo-de-datos.md), [Condición](../c/condicion.md), [Impacto](../i/impacto.md), [Linaje](../l/linaje.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-098](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md), [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Personas y promedios](./personas-y-promedios.md) · [Petición condicional →](./peticion-condicional.md)
