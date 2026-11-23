# Expandir, migrar y contraer

[↑ Glosario](../../README.md) · [← Expandir y contraer](./expandir-y-contraer.md) · [Expansión del trabajo →](./expansion-del-trabajo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Secuencia de tres fases para cambiar una interfaz o un dato.

Definición de trabajo de [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md).

## Por qué importa

La clase donde se define, [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), existe con este propósito: la clase existe para que conviertas la relación entre quien produce un conjunto de datos y quien lo consume en un acuerdo escrito, comprobable y versionado, y para que sepas qué cambios de esquema rompen a los consumidores y cuáles no.

## Cómo funciona

Según [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), en la sección «Expandir, migrar y contraer»:

Cuando un cambio es incompatible, se divide en pasos que cada lector sobrevive. Expandir: añadir lo nuevo sin quitar lo viejo. Migrar: escribir en las dos formas, rellenar lo antiguo y mover a los lectores uno a uno. Contraer: quitar lo viejo cuando ya nadie lo lee. En el experimento, un lector viejo suma `fee_cents` y uno nuevo `amount_cents`. Un renombre de golpe rompe al viejo al instante (`no such column`). En tres pasos: expandir añade `amount_cents` y el lector viejo sigue leyendo 14 950, pero el nuevo devuelve un nulo sin error (la columna existe y está vacía); al escribir en las dos y rellenar, los dos leen 14 950; al contraer (quitar `fee_cents`) el viejo falla.

## Ejemplo

Caso medido en la sección «Expandir, migrar y contraer» de [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md):

Cuando un cambio es incompatible, se divide en pasos que cada lector sobrevive. Expandir: añadir lo nuevo sin quitar lo viejo. Migrar: escribir en las dos formas, rellenar lo antiguo y mover a los lectores uno a uno. Contraer: quitar lo viejo cuando ya nadie lo lee. En el experimento, un lector viejo suma `fee_cents` y uno nuevo `amount_cents`. Un renombre de golpe rompe al viejo al instante (`no such column`).

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md)) son: Los esquemas, las reglas de promoción y los registros son construcciones del autor; el verificador es una simplificación y no cubre tipos anidados, enumeraciones ni uniones. No se ejecutó ningún registro de esquemas ni se midió el costo de un cambio incompatible en una organización. El siguiente paso, `SE-367`, construye el linaje y el catálogo que dicen quién consume cada campo.

## Relación con otros conceptos

- **Prerrequisito:** [Interfaz](../i/interfaz.md).
- **Ver también:** [Secuencia](../s/secuencia.md), [Abstracción de rama](../a/abstraccion-de-rama.md), [Cambio semántico](../c/cambio-semantico.md), [Compatibilidad hacia adelante](../c/compatibilidad-hacia-adelante.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Contrato de datos](../c/contrato-de-datos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Expandir y contraer](./expandir-y-contraer.md) · [Expansión del trabajo →](./expansion-del-trabajo.md)
