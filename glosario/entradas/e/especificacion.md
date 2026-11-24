# Especificación

[↑ Glosario](../../README.md) · [← Especialidad](./especialidad.md) · [Especificación del experimento →](./especificacion-del-experimento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Una **especificación** es el texto acordado de lo que el sistema debe hacer, escrito para que pueda construirse, probarse y auditarse sin preguntar a su autor ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)). [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) la precisa para el trabajo con agentes: documento versionado que declara qué comportamiento observable debe tener un sistema y por qué, con requisitos identificables y criterios comprobables. [SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md) la reduce a una descripción verificable de comportamiento y restricciones.

## Por qué importa

Es el punto donde un deseo se vuelve contrato. Sin ella, quien construye, quien prueba y quien audita trabajan con tres lecturas distintas. Con agentes que implementan ([SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)) importa más: lo que no está especificado lo decide la máquina, y la entrega puede «funcionar» y no ser lo pedido.

## Cómo funciona

[SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), siguiendo a Zave y Jackson, separa tres cosas que suelen mezclarse:

- **Requisito:** lo que se quiere en el mundo («la estudiante recupera su trabajo»).
- **Supuestos del dominio:** lo que se cree del mundo («la sesión dura 30 minutos y el navegador conserva el almacenamiento local»).
- **Especificación:** lo que el sistema hará («guardará el borrador cada 30 s»).

El programa satisface el requisito solo si especificación y supuestos, juntos, lo implican. Si un supuesto es falso (el navegador borra el almacenamiento al cerrar), la especificación puede cumplirse al pie de la letra y el requisito no. De ahí dos prácticas: listar los supuestos con responsable y forma de comprobarlos, y escribir los criterios en la especificación *antes* de implementar ([SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)).

## Ejemplo

Requisito: la estudiante recupera su trabajo. Supuesto: el almacenamiento local persiste. Especificación: guardado cada 30 s en el servidor y en el navegador. Si el supuesto falla, el servidor sigue conservando el borrador: la especificación cubre el caso porque no depende de un solo supuesto. Ilustración de criterio comprobable:

```text
REQ-12: tras cerrar y reabrir, el borrador coincide con el último guardado (<= 30 s de antigüedad).
```

## Errores y confusiones comunes

- **Especificación completa y sistema que decepciona.** Causa: solo se entrevistó a quien paga y no se elicitó el conocimiento tácito; corrección: observar el trabajo real y validar con quien usa ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)).
- **Cumple la especificación y falla en producción.** Causa: un supuesto falso que nadie escribió; corrección: listar supuestos ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)).
- **Pruebas que pasan con otro comportamiento.** Causa: las escribió quien implementó, desde su propia lectura; corrección: criterios en la especificación antes de implementar ([SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)).

## Límites y cuándo no aplica

Un documento de requisitos que nadie compara con el sistema es una especificación en el nombre, no en la práctica ([SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)). En exploración temprana, especificar en detalle algo que se está descubriendo cuesta más de lo que protege. Y ninguna especificación es completa: dónde se detiene es una decisión, y lo omitido queda delegado.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Documento](../d/documento.md), [Restricciones](../r/restricciones.md), [Versionado](../v/versionado.md), [Cita de proximidad](../c/cita-de-proximidad.md), [Dominio](../d/dominio.md), [Edición](./edicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-010 — Cómo leer estándares, documentación y literatura técnica](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-060 — Proyecto: especificación y solución contrastable](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (156 clases más lo mencionan; las que más):

[SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md), [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Zave y Jackson: Four dark corners of requirements engineering (1997)](https://doi.org/10.1145/237432.237434) — relación entre requisitos, supuestos del dominio y especificación; autoridad: ACM Transactions on Software Engineering and Methodology.
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — significado de DEBE, NO DEBE y DEBERÍA en especificaciones; autoridad: IETF.
- [Nuseibeh y Easterbrook: Requirements engineering, a roadmap (2000)](https://doi.org/10.1145/336512.336523) — panorama de las actividades de la disciplina; autoridad: ACM, The Future of Software Engineering.
- [Boehm: Verifying and validating software requirements and design specifications (1984)](https://doi.org/10.1109/MS.1984.233702) — validación frente a verificación; autoridad: IEEE Software.
- [Fagan: Design and code inspections to reduce errors in program development (1976)](https://doi.org/10.1147/sj.153.0182) — inspección estructurada con roles; autoridad: IBM Systems Journal.

---

[↑ Glosario](../../README.md) · [← Especialidad](./especialidad.md) · [Especificación del experimento →](./especificacion-del-experimento.md)
