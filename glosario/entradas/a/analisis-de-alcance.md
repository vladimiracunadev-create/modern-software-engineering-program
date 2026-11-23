# Análisis de alcance

[↑ Glosario](../../README.md) · [← Análisis confirmatorio y exploratorio](./analisis-confirmatorio-y-exploratorio.md) · [Análisis de impacto →](./analisis-de-impacto.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Determinación de los elementos que un cambio obliga a revisar, a partir de las dependencias y los enlaces.

Definición de trabajo de [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md).

## Por qué importa

En [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), el tema «Análisis de alcance» importa porque estima el costo y el riesgo de un cambio antes de aprobarlo.

## Cómo funciona

Según [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), en la sección «Análisis de alcance»:

El alcance de un cambio es el conjunto de elementos que habría que revisar: requisitos que dependen del modificado, criterios y pruebas enlazados, módulos, documentación y obligaciones. Con el grafo de `SE-151` se obtiene recorriendo las dependencias hacia quienes dependen del cambiado. Un cambio con alcance cero es un ajuste local; uno con muchos dependientes transitivos es una decisión de arquitectura de los requisitos y merece más cuidado.

## Ejemplo

Caso medido en la sección «Análisis de alcance» de [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md):

El alcance de un cambio es el conjunto de elementos que habría que revisar: requisitos que dependen del modificado, criterios y pruebas enlazados, módulos, documentación y obligaciones. Con el grafo de `SE-151` se obtiene recorriendo las dependencias hacia quienes dependen del cambiado. Un cambio con alcance cero es un ajuste local; uno con muchos dependientes transitivos es una decisión de arquitectura de los requisitos y merece más cuidado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md)) son:

- **Nadie sabe cuál era la versión acordada** — causa: no hay línea base identificada. Corrección: etiquetar cada versión acordada y registrar su hash normalizado.
- **Un cambio «pequeño» rompe media especificación** — causa: no se calculó el alcance. Corrección: recorrer las dependencias antes de aprobar y registrar el resultado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos y una demostración con `git` en Windows y Ubuntu (WSL2) con resultados idénticos. No se analizó ningún proyecto real, los grafos y las llegadas son sintéticos y la normalización es una de varias posibles. La siguiente clase busca los defectos que los cambios parciales introducen: ambigüedad, contradicción e incompletitud.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Comité y cadencia](../c/comite-y-cadencia.md), [Identidad de una versión](../i/identidad-de-una-version.md), [Línea base](../l/linea-base.md), [Solicitud de cambio](../s/solicitud-de-cambio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), [SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md).

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

[↑ Glosario](../../README.md) · [← Análisis confirmatorio y exploratorio](./analisis-confirmatorio-y-exploratorio.md) · [Análisis de impacto →](./analisis-de-impacto.md)
