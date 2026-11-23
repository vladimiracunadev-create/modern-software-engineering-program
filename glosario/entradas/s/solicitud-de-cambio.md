# Solicitud de cambio

[↑ Glosario](../../README.md) · [← Solape](./solape.md) · [Solicitud de cobertura →](./solicitud-de-cobertura.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Propuesta registrada de modificar la línea base, con motivo, alcance y decisión.

Definición de trabajo de [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md).

## Por qué importa

En [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), el tema «Solicitud de cambio» importa porque convierte una modificación en un objeto con autor, motivo y alcance.

## Cómo funciona

Según [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), en la sección «Solicitud de cambio»:

Una solicitud de cambio es la propuesta de modificar la línea base: qué cambia, quién lo pide, por qué, qué elementos alcanza y qué decisión se tomó. Registrarla sirve a tres cosas: evita cambios silenciosos, obliga a nombrar el motivo y deja un historial que explica por qué el sistema es como es. Un cambio urgente puede saltarse la espera, pero no el registro.

## Ejemplo

Ejemplo de [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) (sección «Ejemplo profesional»):

Una solicitud de cambio con su análisis y su decisión, sobre la línea base 1:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md)) son:

- **Nadie sabe cuál era la versión acordada** — causa: no hay línea base identificada. Corrección: etiquetar cada versión acordada y registrar su hash normalizado.
- **Un cambio «pequeño» rompe media especificación** — causa: no se calculó el alcance. Corrección: recorrer las dependencias antes de aprobar y registrar el resultado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos y una demostración con `git` en Windows y Ubuntu (WSL2) con resultados idénticos. No se analizó ningún proyecto real, los grafos y las llegadas son sintéticos y la normalización es una de varias posibles. La siguiente clase busca los defectos que los cambios parciales introducen: ambigüedad, contradicción e incompletitud.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Línea base](../l/linea-base.md), [Alcance](../a/alcance.md), [Base](../b/base.md), [Análisis de alcance](../a/analisis-de-alcance.md), [Comité y cadencia](../c/comite-y-cadencia.md), [Identidad de una versión](../i/identidad-de-una-version.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md).

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

[↑ Glosario](../../README.md) · [← Solape](./solape.md) · [Solicitud de cobertura →](./solicitud-de-cobertura.md)
