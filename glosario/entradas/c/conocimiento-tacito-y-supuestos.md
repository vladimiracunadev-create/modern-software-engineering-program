# Conocimiento tácito y supuestos

[↑ Glosario](../../README.md) · [← Conocimiento perdido](./conocimiento-perdido.md) · [Consecuencia →](./consecuencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Lo que quienes participan saben o creen sin decirlo, y lo que se da por cierto del mundo sin haberlo comprobado.

Definición de trabajo de [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md).

## Por qué importa

En [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), el tema «Conocimiento tácito y supuestos» importa porque lo que nadie dice y lo que se da por cierto sobre el mundo decide si el sistema funciona.

## Cómo funciona

Según [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), en la sección «Conocimiento tácito y supuestos»:

Hay requisitos que nadie enuncia porque parecen obvios (el borrador no debe mostrarse a otra estudiante) y supuestos que nadie cuestiona porque nunca han fallado (la hora del servidor es la misma que la del navegador). La clase los trata como categoría propia porque son los que producen los defectos más caros: no están en ningún documento, así que ninguna revisión de documentos los encuentra. La defensa no es preguntar más sino preguntar de otra manera: observar el trabajo real, pedir casos de excepción, y escribir los supuestos como una lista revisable con una persona responsable.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md):

En la plataforma de entregas, el requisito conductor se registra con su cadena completa:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)) son:

- **La especificación está completa y el sistema decepciona a quienes lo usan** — causa: solo se entrevistó a quien paga; el conocimiento tácito no se elicitó. Corrección: añadir observación del trabajo real y validar con la persona usuaria, no solo con el cliente.
- **Dos equipos discuten una frase durante una hora** — causa: la frase mezcla un requisito y una solución, y los interesados entienden cosas distintas. Corrección: separar necesidad, requisito y supuesto, y registrar el origen de cada uno.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se entrevistó a nadie, no se observó trabajo real y los porcentajes de tácitos, de recuerdo y de detección son supuestos del autor. La siguiente clase baja del ciclo al contenido de los requisitos funcionales y de las reglas de negocio que los sostienen.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Análisis](../a/analisis.md), [Elicitación](../e/elicitacion.md), [Especificación](../e/especificacion.md), [Validación](../v/validacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

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

[↑ Glosario](../../README.md) · [← Conocimiento perdido](./conocimiento-perdido.md) · [Consecuencia →](./consecuencia.md)
