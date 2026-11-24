# Solicitud de cambio

[↑ Glosario](../../README.md) · [← Solape](./solape.md) · [Solicitud de cobertura →](./solicitud-de-cobertura.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Una **solicitud de cambio** es la propuesta registrada de modificar la línea base, con motivo, alcance y decisión ([SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md)). Convierte una modificación en un objeto con autor, motivo y alcance.

## Por qué importa

Evita cambios silenciosos, obliga a nombrar el motivo y deja un historial que explica por qué el sistema es como es. Sin solicitudes, la línea base se edita sin que nadie lo sepa, y la pregunta «¿esto está dentro de lo acordado?» deja de tener respuesta. Cambia cómo se gestiona la especificación: los cambios pasan por un registro, no por conversaciones sueltas.

## Cómo funciona

[SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) enumera el contenido: **qué cambia**, **quién lo pide**, **por qué**, **qué elementos alcanza** y **qué decisión se tomó**. El **alcance** se obtiene con el análisis de alcance: recorriendo las dependencias desde el elemento modificado para listar los requisitos, criterios, pruebas y documentos afectados. La decisión (aceptar, rechazar, aplazar) tiene un responsable y una fecha.

Registrarla sirve a tres cosas, dice la clase: **evita cambios silenciosos**, **obliga a nombrar el motivo** y **deja un historial**. Un cambio urgente puede saltarse la espera, pero **no el registro**: se registra después, lo antes posible. Esto conserva el principio sin convertirlo en burocracia que paralice.

La solicitud opera sobre una línea base con identidad estable (etiqueta y hash normalizado). Al aprobarse, se crea una nueva línea base con su propia identidad. Una prueba de regresión puede verificar el hash normalizado de la línea base y fallar si cambia sin una solicitud registrada, de modo que el proceso se hace cumplir. Dos síntomas que previene: nadie sabe cuál era la versión acordada (no hay línea base identificada) y un cambio «pequeño» rompe media especificación (no se calculó el alcance).

[SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) muestra una solicitud de cambio con su análisis y su decisión sobre la línea base 1: propone un cambio, lista lo que alcanza, y registra la decisión.

## Ejemplo

SC-014. Qué cambia: el tope de penalización pasa del 50 % al 30 %. Quién: coordinación académica. Por qué: reclamos por descuentos excesivos. Alcance: regla BR-07, requisito REQ-12, pruebas de frontera TST-31 a TST-34, texto de política publicado. Decisión: aceptada el 4 de marzo, responsable: producto. Resultado: línea base 2. (Solicitud ilustrativa en el formato de [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md).)

## Errores y confusiones comunes

- **Nadie sabe cuál era la versión acordada**: no hay línea base identificada.
- **Un cambio «pequeño» rompe media especificación**: no se calculó el alcance.
- **Registrar solo los cambios grandes.**
- **Saltarse el registro por urgencia.**

## Límites y cuándo no aplica

En un proyecto exploratorio con requisitos que cambian a diario, una solicitud formal por cada cambio frena el aprendizaje; se usa una línea base ligera por iteración. El registro no garantiza que el cambio sea bueno, solo que sea visible y atribuible.

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
