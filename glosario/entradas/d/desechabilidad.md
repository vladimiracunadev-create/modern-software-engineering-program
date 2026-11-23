# Desechabilidad

[↑ Glosario](../../README.md) · [← Descubrimiento, formulación, automatización](./descubrimiento-formulacion-automatizacion.md) · [Desechabilidad y persistencia →](./desechabilidad-y-persistencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Capacidad de arrancar rápido y terminar limpiamente en cualquier momento.

Definición de trabajo de [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md).

## Por qué importa

En [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), el tema «Desechabilidad» importa porque permite parar y arrancar sin pérdida.

## Cómo funciona

Según [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md):

Los doce factores son: una base de código con muchos despliegues; dependencias declaradas explícitamente; configuración en el entorno; servicios de apoyo tratados como recursos adjuntos; separación estricta entre construir, publicar y ejecutar; procesos sin estado; servicios exportados por vinculación de puertos; concurrencia escalando por procesos; desechabilidad (arranque rápido y parada limpia); paridad entre desarrollo y producción; registros como flujo de eventos; y procesos administrativos como tareas puntuales del mismo artefacto. Agrupados por lo que protegen, cuatro cubren la reproducibilidad (código, dependencias, construir-publicar-ejecutar, procesos administrativos), tres cubren la portabilidad entre entornos (configuración, servicios de apoyo, paridad) y cinco cubren la elasticidad y la recuperación (procesos, concurrencia, desechabilidad, vinculación de puertos, registros). La clase mide los factores de las dos últimas agrupaciones, que son los que se pueden comprobar con un experimento.

## Ejemplo

Caso medido en la sección «Desechabilidad: arranque rápido y parada limpia» de [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md):

Un proceso desechable arranca rápido y termina bien cuando se lo piden. El arranque se midió con procesos Python reales: un intérprete vacío tardó una mediana de 116 ms y uno que importa `sqlite3`, `json`, `http.server` y `hashlib`, 249 ms (diez ejecuciones en una máquina Windows; el valor cambia con el equipo y la caché del sistema). El arranque de una aplicación real incluye conectar a servicios y calentar cachés, y el presupuesto es el que permite sustituir instancias sin que se note.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Agrupados por lo que protegen, cuatro cubren la reproducibilidad (código, dependencias, construir-publicar-ejecutar, procesos administrativos), tres cubren la portabilidad entre entornos (configuración, servicios de apoyo, paridad) y cinco cubren la elasticidad y la recuperación (procesos, concurrencia, desechabilidad, vinculación de puertos, registros). ([SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Artefacto inmutable](../a/artefacto-inmutable.md), [Concurrencia](../c/concurrencia.md), [Doce factores](./doce-factores.md), [Drenaje](./drenaje.md), [Paridad](../p/paridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Descubrimiento, formulación, automatización](./descubrimiento-formulacion-automatizacion.md) · [Desechabilidad y persistencia →](./desechabilidad-y-persistencia.md)
