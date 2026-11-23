# ODD

[↑ Glosario](../../README.md) · [← Ocurrió antes de](./ocurrio-antes-de.md) · [Offline-first →](./offline-first.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Flujo de trabajo para agentes de código descrito por el proyecto Gentle AI.

Definición de trabajo de [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md).

## Por qué importa

La clase donde se define, [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md), existe con este propósito: la clase existe para que sepas leer un **flujo de trabajo para agentes de código** como lo que es: un conjunto de reglas con una razón cada una y con evidencia de distinta calidad.

## Cómo funciona

Según [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md):

Según la documentación de Gentle AI, ODD empieza por decidir si la petición autoriza un cambio: explicar e investigar se quedan en lectura; el agente explora el código existente, pregunta solo por decisiones que no puede tomar con seguridad e implementa el trabajo autorizado con las comprobaciones aplicables. La regla es una frontera de permiso, no un hallazgo técnico: separa «entender» de «cambiar» con el mismo cuidado con que un sistema de permisos separa lectura de escritura (`SE-569`). Su valor depende de que el agente la cumpla, y eso es verificable solo con un registro de qué hizo en cada petición.

Según [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md):

El equipo adopta tres reglas de ODD sin instalar nada: toda petición de un agente se clasifica en lectura o cambio al empezar (una línea en el registro de la sesión); todo trabajo de más de un archivo tiene un documento de tarea creado antes del primer cambio; y la integración continua rechaza un pull request con más de 400 líneas modificadas en un commit, salvo que el commit lleve la etiqueta «generado» o «movimiento». Añade una comprobación de dos líneas que verifica que el documento exista antes del primer commit con código. Tras un mes mide: el tamaño medio de commit baja a 90 líneas; un agente ya no propone cambios en peticiones de explicación; y retomar un trabajo en otra sesión toma minutos.

## Ejemplo

Ejemplo de [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md) (sección «Ejemplo profesional»):

El equipo adopta tres reglas de ODD sin instalar nada: toda petición de un agente se clasifica en lectura o cambio al empezar (una línea en el registro de la sesión); todo trabajo de más de un archivo tiene un documento de tarea creado antes del primer cambio; y la integración continua rechaza un pull request con más de 400 líneas modificadas en un commit, salvo que el commit lleve la etiqueta «generado» o «movimiento». Añade una comprobación de dos líneas que verifica que el documento exista antes del primer commit con código.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Según la documentación de Gentle AI, ODD empieza por decidir si la petición autoriza un cambio: explicar e investigar se quedan en lectura; el agente explora el código existente, pregunta solo por decisiones que no puede tomar con seguridad e implementa el trabajo autorizado con las comprobaciones aplicables. ([SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md), [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Flujo](../f/flujo.md), [Trabajo](../t/trabajo.md), [Decisión de entrega](../d/decision-de-entrega.md), [Documento de tarea](../d/documento-de-tarea.md), [Rojo y verde](../r/rojo-y-verde.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «desarrollo orgánico».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Ocurrió antes de](./ocurrio-antes-de.md) · [Offline-first →](./offline-first.md)
