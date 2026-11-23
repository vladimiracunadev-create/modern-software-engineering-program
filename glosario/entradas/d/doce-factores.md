# Doce factores

[↑ Glosario](../../README.md) · [← Doble validez](./doble-validez.md) · [Documentación como código →](./documentacion-como-codigo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Conjunto de prácticas para escribir aplicaciones portables, escalables y fáciles de operar.

Definición de trabajo de [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md).

## Por qué importa

La clase donde se define, [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), existe con este propósito: la clase existe para que puedas leer los doce factores como un conjunto de propiedades verificables de una aplicación y no como una lista de buenas prácticas.

## Cómo funciona

Según [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md):

Los doce factores son: una base de código con muchos despliegues; dependencias declaradas explícitamente; configuración en el entorno; servicios de apoyo tratados como recursos adjuntos; separación estricta entre construir, publicar y ejecutar; procesos sin estado; servicios exportados por vinculación de puertos; concurrencia escalando por procesos; desechabilidad (arranque rápido y parada limpia); paridad entre desarrollo y producción; registros como flujo de eventos; y procesos administrativos como tareas puntuales del mismo artefacto. Agrupados por lo que protegen, cuatro cubren la reproducibilidad (código, dependencias, construir-publicar-ejecutar, procesos administrativos), tres cubren la portabilidad entre entornos (configuración, servicios de apoyo, paridad) y cinco cubren la elasticidad y la recuperación (procesos, concurrencia, desechabilidad, vinculación de puertos, registros). La clase mide los factores de las dos últimas agrupaciones, que son los que se pueden comprobar con un experimento.

Según [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md):

Antes de crear las celdas de `SE-344`, el equipo de *Avisos* audita la aplicación contra los doce factores. De las doce filas, siete cumplen, tres incumplen y dos no aplican. Los incumplimientos son los de siempre: las sesiones viven en memoria, los registros van a un archivo y los umbrales están en un archivo de configuración dentro de la imagen. Antes de crear la primera celda corrigen los tres. Mueven las sesiones a un almacén externo (y añaden a las alertas la salud de ese almacén), cambian los registros a la salida estándar y leen los umbrales de variables de entorno con fallo inmediato si faltan. Después ejecutan la prueba de sesiones con tres instancias y matan una a mitad de la prueba: cero peticiones fallidas.

## Ejemplo

Ejemplo de [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md) (sección «Ejemplo profesional»):

Antes de crear las celdas de `SE-344`, el equipo de *Avisos* audita la aplicación contra los doce factores. De las doce filas, siete cumplen, tres incumplen y dos no aplican. Los incumplimientos son los de siempre: las sesiones viven en memoria, los registros van a un archivo y los umbrales están en un archivo de configuración dentro de la imagen. Antes de crear la primera celda corrigen los tres. Mueven las sesiones a un almacén externo (y añaden a las alertas la salud de ese almacén), cambian los registros a la salida estándar y leen los umbrales de variables de entorno con fallo inmediato si faltan.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md)) son: El linter y las simulaciones son de juguete; no se auditó una aplicación real ni se ejecutó un orquestador. El arranque se midió en una máquina Windows y cambia con el sistema. El siguiente paso, `SE-346`, trata la migración de un estilo a otro: cómo se reemplaza un módulo sin detener el servicio, qué se compara mientras conviven y cómo se decide cuándo avanzar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Práctica](../p/practica.md), [Artefacto inmutable](../a/artefacto-inmutable.md), [Concurrencia](../c/concurrencia.md), [Desechabilidad](./desechabilidad.md), [Drenaje](./drenaje.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md), [SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Doble validez](./doble-validez.md) · [Documentación como código →](./documentacion-como-codigo.md)
