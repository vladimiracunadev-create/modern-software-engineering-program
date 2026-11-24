# Análisis de alcance

[↑ Glosario](../../README.md) · [← Análisis confirmatorio y exploratorio](./analisis-confirmatorio-y-exploratorio.md) · [Análisis de impacto →](./analisis-de-impacto.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

El **análisis de alcance** determina los elementos que un cambio obliga a revisar, a partir de las dependencias y los enlaces entre artefactos ([SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md)). No debe confundirse con definir el «alcance del proyecto» (qué entra y qué no): aquí el alcance es el conjunto de lo afectado por un cambio concreto. Es muy cercano al análisis de impacto, que [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) y [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) formulan con el mismo mecanismo.

## Por qué importa

Estima el costo y el riesgo de un cambio antes de aprobarlo. Un cambio aparentemente pequeño en una especificación puede obligar a tocar media especificación; saberlo antes permite decidir con información. Sin análisis, el síntoma que [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) describe es un cambio «pequeño» que rompe media especificación porque nadie calculó el alcance.

## Cómo funciona

El alcance de un cambio es el conjunto de elementos que habría que revisar: los **requisitos que dependen del modificado**, los **criterios y pruebas enlazados**, los módulos, la documentación y las obligaciones. Con el grafo de enlaces de [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) se obtiene **recorriendo las dependencias hacia quienes dependen del cambiado**: se parte del elemento que cambia y se sigue cada arista hacia sus consumidores, de forma transitiva.

El tamaño del resultado informa la decisión. Un cambio con alcance cero es un ajuste local. Uno con muchos dependientes transitivos es una decisión de arquitectura de los requisitos y merece más cuidado: revisión específica, aviso a los dueños de lo afectado y, a menudo, una solicitud de cambio formal contra la línea base. [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) pide registrar el resultado en la solicitud de cambio, de modo que quien decide vea el alcance y quien revisa sepa qué mirar.

El análisis es tan bueno como el grafo: si faltan enlaces, el alcance se subestima; si se enlazó todo con todo, se sobrestima. Por eso va de la mano de una granularidad de enlaces que responda a las preguntas reales.

## Ejemplo

Cambiar el tope de penalización por entrega tardía. Recorriendo las dependencias: las pruebas de frontera de esa regla, el módulo de cálculo de la nota, las vistas que muestran el descuento al estudiante, al docente y a secretaría, y el texto de la política publicada. Esa lista es el alcance; con ella se estima el trabajo y se avisa a quienes mantienen cada pieza. Si el cambio solo toca un texto de ayuda sin dependientes, el alcance es cero. (Ilustración sobre el escenario de la plataforma.)

## Errores y confusiones comunes

- **Un cambio «pequeño» rompe media especificación**: no se calculó el alcance; corrección: recorrer las dependencias antes de aprobar y registrar el resultado.
- **Nadie sabe cuál era la versión acordada**: sin línea base no hay contra qué calcular el cambio.
- **Confundirlo con «alcance del proyecto».**
- **Tratar la lista como lo que hay que modificar**: es lo que hay que revisar.

## Límites y cuándo no aplica

Solo ve dependencias enlazadas; las implícitas (datos compartidos, configuración) quedan fuera. El resultado es una cota superior, no una predicción. En un sistema pequeño con pocos artefactos, la revisión directa suele bastar.

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
