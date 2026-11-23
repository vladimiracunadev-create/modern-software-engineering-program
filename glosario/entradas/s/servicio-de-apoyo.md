# Servicio de apoyo

[↑ Glosario](../../README.md) · [← Servicio](./servicio.md) · [Servidor MCP →](./servidor-mcp.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Recurso externo (base de datos, cola, caché) que se engancha por configuración.

Definición de trabajo de [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md).

## Por qué importa

En [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), el tema «Servicios de apoyo» importa porque el estado vive fuera y se trata como recurso adjunto.

## Cómo funciona

Según [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md):

Los doce factores son: una base de código con muchos despliegues; dependencias declaradas explícitamente; configuración en el entorno; servicios de apoyo tratados como recursos adjuntos; separación estricta entre construir, publicar y ejecutar; procesos sin estado; servicios exportados por vinculación de puertos; concurrencia escalando por procesos; desechabilidad (arranque rápido y parada limpia); paridad entre desarrollo y producción; registros como flujo de eventos; y procesos administrativos como tareas puntuales del mismo artefacto. Agrupados por lo que protegen, cuatro cubren la reproducibilidad (código, dependencias, construir-publicar-ejecutar, procesos administrativos), tres cubren la portabilidad entre entornos (configuración, servicios de apoyo, paridad) y cinco cubren la elasticidad y la recuperación (procesos, concurrencia, desechabilidad, vinculación de puertos, registros). La clase mide los factores de las dos últimas agrupaciones, que son los que se pueden comprobar con un experimento.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Agrupados por lo que protegen, cuatro cubren la reproducibilidad (código, dependencias, construir-publicar-ejecutar, procesos administrativos), tres cubren la portabilidad entre entornos (configuración, servicios de apoyo, paridad) y cinco cubren la elasticidad y la recuperación (procesos, concurrencia, desechabilidad, vinculación de puertos, registros). ([SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Recurso](../r/recurso.md), [Artefacto inmutable](../a/artefacto-inmutable.md), [Concurrencia](../c/concurrencia.md), [Desechabilidad](../d/desechabilidad.md), [Doce factores](../d/doce-factores.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Servicios de apoyo».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Servicio](./servicio.md) · [Servidor MCP →](./servidor-mcp.md)
