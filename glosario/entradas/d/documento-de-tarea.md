# Documento de tarea

[↑ Glosario](../../README.md) · [← Documento de límites](./documento-de-limites.md) · [Documento embebido →](./documento-embebido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Archivo con alcance, tareas, evidencia y siguiente paso, creado antes de tocar el código.

Definición de trabajo de [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md).

## Por qué importa

En [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md), el tema «Documento de tarea» importa porque es la memoria entre sesiones y el registro del alcance.

## Cómo funciona

Según [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md):

SDD (`SE-548`) ataca la pregunta de qué fuente manda: la especificación. ODD ataca la pregunta de cómo se autoriza, se acota y se retoma el trabajo de un agente. Se pueden usar juntos: una especificación define el qué; un documento de tarea, el avance de una sesión concreta. Un artículo de terceros presenta ODD como sucesor del SDD que ese ecosistema usaba; la documentación oficial no hace esa comparación, de modo que se toma como una opinión por contrastar. Lo que sí se puede decir con precisión es qué artefacto produce cada uno: SDD, una especificación que vive con el sistema; ODD, un documento por tarea que vive con la rama.

Según [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md):

El equipo adopta tres reglas de ODD sin instalar nada: toda petición de un agente se clasifica en lectura o cambio al empezar (una línea en el registro de la sesión); todo trabajo de más de un archivo tiene un documento de tarea creado antes del primer cambio; y la integración continua rechaza un pull request con más de 400 líneas modificadas en un commit, salvo que el commit lleve la etiqueta «generado» o «movimiento». Añade una comprobación de dos líneas que verifica que el documento exista antes del primer commit con código. Tras un mes mide: el tamaño medio de commit baja a 90 líneas; un agente ya no propone cambios en peticiones de explicación; y retomar un trabajo en otra sesión toma minutos.

## Ejemplo

Ejemplo de [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md) (sección «Ejemplo mínimo»):

Un documento de tarea de cinco líneas útiles:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md)) son: No se ejecutó Gentle AI ni se midió el efecto de ODD en equipos; los historiales son sintéticos y las reglas son las que la documentación declara. El siguiente paso, `SE-551`, es el taller: el mismo cambio, silenciar un curso, con cinco metodologías, medido con los mismos mutantes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md), [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Siguiente paso](../s/siguiente-paso.md), [Alcance](../a/alcance.md), [Evidencia](../e/evidencia.md), [Tarea](../t/tarea.md), [Decisión de entrega](./decision-de-entrega.md), [ODD](../o/odd.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Documento de límites](./documento-de-limites.md) · [Documento embebido →](./documento-embebido.md)
