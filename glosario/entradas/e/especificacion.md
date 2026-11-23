# Especificación

[↑ Glosario](../../README.md) · [← Especialidad](./especialidad.md) · [Especificación del experimento →](./especificacion-del-experimento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Texto acordado de lo que el sistema debe hacer, escrito para que pueda construirse, probarse y auditarse sin preguntar a su autor.

Definición de trabajo de [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md): Documento versionado que declara qué comportamiento observable debe tener un sistema y por qué, con requisitos identificables y criterios comprobables.
- En [SE-060 — Proyecto: especificación y solución contrastable](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md): Descripción verificable de comportamiento y restricciones.

## Por qué importa

En [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), el tema «Especificación» importa porque fija un texto que otra persona puede implementar y probar sin preguntar.

En [SE-010 — Cómo leer estándares, documentación y literatura técnica](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md), el tema «Especificación» importa porque contrato preciso e interoperabilidad

## Cómo funciona

Según [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), en la sección «Especificación»:

Especificar es escribir lo acordado de forma que sirva a quien construye, a quien prueba y a quien audita. Zave y Jackson separan tres cosas que suelen mezclarse: el requisito (lo que se quiere en el mundo: «la estudiante recupera su trabajo»), los supuestos del dominio (lo que se cree del mundo: «la sesión dura 30 minutos y el navegador conserva el almacenamiento local») y la especificación (lo que el sistema hará: «guardará el borrador cada 30 s»). El programa satisface el requisito solo si especificación y supuestos, juntos, lo implican. Si el supuesto es falso —el navegador de la estudiante borra el almacenamiento al cerrar—, la especificación puede cumplirse al pie de la letra y el requisito, no.

## Ejemplo

Ejemplo de [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) (sección «Ejemplo profesional»):

Compara con el caso del interesado que pide algo que otro prohíbe, el requisito que se cumple con el supuesto falso, y el borrador que contiene datos de otra persona. Una especificación es apropiada cuando esas diferencias quedan visibles y localizadas; es peligrosa cuando se compila en una sola frase («guardará los borradores de forma segura»).

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La especificación está completa y el sistema decepciona a quienes lo usan** — causa: solo se entrevistó a quien paga; el conocimiento tácito no se elicitó. Corrección: añadir observación del trabajo real y validar con la persona usuaria, no solo con el cliente. ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md))
- **El sistema cumple la especificación y falla en producción** — causa: un supuesto del dominio era falso y nadie lo había escrito. Corrección: listar los supuestos con responsable y una forma de comprobarlos. ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md))
- **Las pruebas pasan pero el comportamiento es otro** — causa: las pruebas las escribió quien implementó, a partir de su propia lectura. Corrección: escribir los criterios en la especificación antes de implementar. ([SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El programa satisface el requisito solo si especificación y supuestos, juntos, lo implican. ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md))
- Un documento de requisitos que nadie compara con el sistema es una especificación en el nombre, no en la práctica. ([SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md))

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
