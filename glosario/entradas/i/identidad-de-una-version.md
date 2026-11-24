# Identidad de una versión

[↑ Glosario](../../README.md) · [← Identidad de carga de trabajo](./identidad-de-carga-de-trabajo.md) · [Identidad federada →](./identidad-federada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La **identidad de una versión** es un identificador estable (una etiqueta, un identificador de commit o un hash del contenido) que permite saber de qué versión se habla ([SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md)). Es la propiedad que permite que dos personas, o una persona y una prueba, se refieran sin ambigüedad a la misma versión de una especificación o de un artefacto.

## Por qué importa

Sin identidad estable, «la versión acordada» es una expresión que cada quien interpreta como quiere, y la pregunta «¿esto está dentro del alcance?» no tiene respuesta. Con ella, un cambio se evalúa contra una versión concreta y una discrepancia se resuelve comparando identificadores, no recuerdos. [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) la sitúa como parte del contrato de la línea base.

## Cómo funciona

Hay tres formas de dar identidad, con compromisos distintos. Una **etiqueta** (`baseline-1`) es legible, pero depende de que nadie la mueva. Un **identificador de commit** es preciso e inmutable dentro del repositorio. Un **hash del contenido** identifica los bytes mismos, con independencia de dónde vivan.

El detalle técnico que [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) destaca es qué se hashea. Un hash del **texto crudo** cambia con cualquier byte: un espacio al final, un salto de línea distinto (los de Windows y Linux difieren), así que confunde formato con contenido y dispara falsos cambios. Un hash de un **texto normalizado** cambia solo cuando cambia lo que importa. El precio es que la normalización debe quedar escrita (qué se descarta: espacios, saltos de línea, mayúsculas) y que, si se normaliza mal, se ocultan cambios reales. Por eso la regla de normalización es parte de la identidad y se versiona.

La consecuencia práctica se vuelve una prueba de regresión: una comprobación que calcula el hash normalizado de la línea base y falla si cambia sin una solicitud de cambio registrada.

## Ejemplo

El equipo etiqueta la especificación acordada como `baseline-1` y registra su hash normalizado. Más tarde, un editor reformatea el archivo (cambia los saltos de línea y quita espacios). El hash crudo cambia y la alarma suena sin motivo; el hash normalizado no cambia y la comprobación pasa. Si alguien cambia «10 MB» por «25 MB», el hash normalizado sí cambia y la prueba exige una solicitud de cambio. (Ilustración del mecanismo de [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md).)

## Errores y confusiones comunes

- **Nadie sabe cuál era la versión acordada**: no hay línea base identificada; corrección: etiquetar cada versión acordada y registrar su hash normalizado.
- **Un cambio «pequeño» rompe media especificación**: no se calculó el alcance; corrección: recorrer las dependencias antes de aprobar.
- **Usar el hash crudo** y alarmar por cambios de formato.
- **Normalizar de más** y ocultar cambios reales (por ejemplo, ignorar diferencias de números).

## Límites y cuándo no aplica

La identidad dice cuál versión, no si es la correcta ni quién la aprobó; eso lo registran el proceso de cambio y la línea base. Un hash solo identifica contenido idéntico: dos versiones semánticamente equivalentes tendrán hashes distintos si difieren en lo normalizado. En documentos de vida muy corta, una etiqueta o la fecha pueden bastar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Etiqueta](../e/etiqueta.md), [Huella](../h/huella.md), [Versión](../v/version.md), [Análisis de alcance](../a/analisis-de-alcance.md), [Comité y cadencia](../c/comite-y-cadencia.md), [Línea base](../l/linea-base.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO 10007:2017](https://www.iso.org/standard/70400.html) — gestión de la configuración: identificación, control de cambios, registro de estado y auditoría; autoridad: ISO.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de la configuración y control de cambios; autoridad: IEEE Computer Society.
- [Nuseibeh y Easterbrook: Requirements engineering, a roadmap (2000)](https://doi.org/10.1145/336512.336523) — evolución de los requisitos; autoridad: ACM, The Future of Software Engineering.
- [Git: git-tag](https://git-scm.com/docs/git-tag) — etiquetas anotadas; autoridad: proyecto Git.
- [Git: git-diff](https://git-scm.com/docs/git-diff) — comparación entre revisiones; autoridad: proyecto Git.

---

[↑ Glosario](../../README.md) · [← Identidad de carga de trabajo](./identidad-de-carga-de-trabajo.md) · [Identidad federada →](./identidad-federada.md)
