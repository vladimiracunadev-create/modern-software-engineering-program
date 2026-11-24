# Análisis

[↑ Glosario](../../README.md) · [← Amplitud](./amplitud.md) · [Análisis confirmatorio y exploratorio →](./analisis-confirmatorio-y-exploratorio.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

En ingeniería de requisitos, **análisis** es el tratamiento del conjunto recogido para encontrar duplicados, conflictos, dependencias y huecos, y convertirlos en decisiones o preguntas. Es el sentido de [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), que lo sitúa tras la elicitación y antes de la especificación y la validación. «Análisis» tiene otros usos en el programa (análisis de impacto, estático, de datos); aquí se trata únicamente de lo que se hace con los requisitos ya recogidos.

## Por qué importa

Decide cuándo se descubren los conflictos: antes de comprometer diseño o después. Cada persona consultada ve su parte; solo quien trata lo recogido como conjunto ve que dos partes chocan. [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) lo ilustra con una simulación en la que hablar con todo el mundo cubre apenas el 77 % de lo necesario: recoger más no sustituye a analizar. Un conflicto hallado al analizar cuesta una conversación; hallado en producción cuesta un rediseño.

## Cómo funciona

Analizar es tratar lo recogido como un conjunto, no como una lista. [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) enumera cuatro búsquedas:

- **Duplicados:** dos personas piden lo mismo con palabras distintas.
- **Conflictos:** dos personas piden cosas incompatibles.
- **Dependencias:** un requisito solo tiene sentido si otro existe.
- **Huecos:** una situación que nadie contempló.

El producto del análisis no es un texto más pulido sino una lista de preguntas pendientes con responsable. La clase da el modelo: «Auditoría exige 730 días y Privacidad 365; ¿quién decide?». La pregunta nombra a las partes y obliga a que alguien con autoridad resuelva. Y la regla de cierre es práctica: un análisis que no produce preguntas probablemente no analizó nada.

## Ejemplo

En la plataforma de entregas de [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), los requisitos recogidos de docentes, estudiantes, secretaría y auditoría se cruzan. Retención de datos aparece con dos plazos incompatibles; la solución no la elige quien analiza, sino que se registra como pregunta dirigida a quien tiene la decisión. Mientras no se resuelva, el requisito queda marcado como en conflicto, no como aprobado con un valor arbitrario.

## Errores y confusiones comunes

- **Confundir elicitar con analizar.** Hablar con el cliente es una técnica de elicitación; el análisis empieza cuando lo recogido se trata como conjunto ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)).
- **Pulir la redacción en lugar de buscar conflictos.** Mejorar el texto no resuelve la contradicción de fondo.
- **Resolver el conflicto en silencio.** Elegir un valor sin que decida quien corresponde oculta el problema.
- **Mezclar requisito y solución.** Dos equipos discuten una frase una hora porque mezcla ambas cosas; la corrección es separar necesidad, requisito y supuesto y registrar el origen de cada uno.

## Límites y cuándo no aplica

El análisis solo encuentra lo que está en el conjunto: si la elicitación no recogió el conocimiento tácito (por ejemplo, porque solo se entrevistó a quien paga), el análisis no puede inventarlo, y la especificación saldrá «completa» pero decepcionará a quienes la usan. Tampoco decide por sí mismo: produce preguntas, no resoluciones. En proyectos muy pequeños puede hacerse en una conversación; la disciplina que importa es dejar escritas las preguntas y quién las responde.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conflicto](../c/conflicto.md), [Conjunto](../c/conjunto.md), [Dependencia](../d/dependencia.md), [Conocimiento tácito y supuestos](../c/conocimiento-tacito-y-supuestos.md), [Elicitación](../e/elicitacion.md), [Especificación](../e/especificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (364 clases más lo mencionan; las que más):

[SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nuseibeh y Easterbrook: Requirements engineering, a roadmap (2000)](https://doi.org/10.1145/336512.336523) — panorama de las actividades de la disciplina; autoridad: ACM, The Future of Software Engineering.
- [Zave y Jackson: Four dark corners of requirements engineering (1997)](https://doi.org/10.1145/237432.237434) — relación entre requisitos, supuestos del dominio y especificación; autoridad: ACM Transactions on Software Engineering and Methodology.
- [Boehm: Verifying and validating software requirements and design specifications (1984)](https://doi.org/10.1109/MS.1984.233702) — validación frente a verificación; autoridad: IEEE Software.
- [Fagan: Design and code inspections to reduce errors in program development (1976)](https://doi.org/10.1147/sj.153.0182) — inspección estructurada con roles; autoridad: IBM Systems Journal.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — procesos y elementos de información de la ingeniería de requisitos; autoridad: ISO, IEC e IEEE.

---

[↑ Glosario](../../README.md) · [← Amplitud](./amplitud.md) · [Análisis confirmatorio y exploratorio →](./analisis-confirmatorio-y-exploratorio.md)
