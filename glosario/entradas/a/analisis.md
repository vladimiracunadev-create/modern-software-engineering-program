# Análisis

[↑ Glosario](../../README.md) · [← Amplitud](./amplitud.md) · [Análisis confirmatorio y exploratorio →](./analisis-confirmatorio-y-exploratorio.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Tratamiento del conjunto recogido para encontrar duplicados, conflictos, dependencias y huecos y convertirlos en decisiones o preguntas.

Definición de trabajo de [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md).

## Por qué importa

En [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), el tema «Análisis» importa porque detecta conflictos, dependencias y huecos antes de comprometer diseño.

## Cómo funciona

Según [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), en la sección «Análisis»:

Analizar es tratar lo recogido como un conjunto, no como una lista. Se buscan duplicados (dos personas piden lo mismo con palabras distintas), conflictos (dos personas piden cosas incompatibles), dependencias (un requisito solo tiene sentido si otro existe) y huecos (una situación que nadie contempló). El resultado no es un texto más bonito sino una lista de preguntas pendientes con nombre y apellido: «Auditoría exige 730 días y Privacidad 365; ¿quién decide?». Un análisis que no produce preguntas probablemente no analizó nada.

## Ejemplo

Ejemplo de [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) (sección «Preguntas frecuentes»):

No. Hablar con el cliente es una técnica de elicitación entre varias, y en la simulación solo llega hasta 77 % de la cobertura aunque se hablara con todos. El análisis empieza cuando lo recogido se trata como conjunto: allí aparecen los conflictos que cada persona, por separado, no ve.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)) son:

- **La especificación está completa y el sistema decepciona a quienes lo usan** — causa: solo se entrevistó a quien paga; el conocimiento tácito no se elicitó. Corrección: añadir observación del trabajo real y validar con la persona usuaria, no solo con el cliente.
- **Dos equipos discuten una frase durante una hora** — causa: la frase mezcla un requisito y una solución, y los interesados entienden cosas distintas. Corrección: separar necesidad, requisito y supuesto, y registrar el origen de cada uno.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un análisis que no produce preguntas probablemente no analizó nada. ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md))
- El análisis empieza cuando lo recogido se trata como conjunto: allí aparecen los conflictos que cada persona, por separado, no ve. ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md))

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
