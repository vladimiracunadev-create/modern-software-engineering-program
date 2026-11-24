# Issue

[↑ Glosario](../../README.md) · [← ISBN](./isbn.md) · [Iterable →](./iterable.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

En el programa, un **issue** es un problema que ya ocurrió y requiere acción, con responsable, fecha y criterio de cierre ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md)). [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) usa el mismo término en el sentido de la plataforma de colaboración: un registro con identificador estable de un problema, una propuesta o una decisión pendiente. Los dos sentidos convergen en que el issue es un registro con dueño; esta entrada desarrolla ambos y marca la diferencia con el riesgo.

## Por qué importa

Distinguir un issue de un riesgo cambia cómo se gestiona. Un riesgo es algo que puede ocurrir y se gestiona con probabilidad y respuesta; un issue ya ocurrió y se gestiona con responsable, fecha y cierre. La confusión habitual es llamar «riesgo» a todo lo que preocupa y dejar los issues en una hoja sin dueño: nadie los cierra.

## Cómo funciona

[SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) describe el issue como un problema presente (el entorno de pruebas se cayó, un contrato se rompió) que **no tiene probabilidad, solo impacto**. Necesita tres cosas: un responsable, una fecha y un criterio de cierre. La transición clave es la de **riesgo materializado → issue**: cuando un riesgo ocurre, pasa al registro de issues, y esa transición se anota, porque es la señal de que el disparador funcionó o de que no existía.

El ejemplo de [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) reorganiza una hoja de 23 filas en cuatro registros: riesgos (seis, con causa, efecto, probabilidad, impacto, disparador, respuesta y responsable), supuestos (cinco, con quién los afirma, evidencia y fecha de validación), issues (cuatro, con responsable y fecha) y decisiones (siete, con contexto y disparador). Cada tipo tiene su propio ciclo.

En la plataforma de colaboración ([SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md)), el issue es la unidad de seguimiento y se enlaza con el código: una palabra clave en el mensaje de la integración (por ejemplo «closes #12») cierra el issue automáticamente. Dos fallos con causa conocida: el issue no se cierra al integrar porque la sintaxis no es la reconocida o falta la palabra por cada número (corrección: repetir la palabra clave para cada número y usar la forma documentada); y el issue se cierra sin que el defecto desaparezca porque no hay una prueba que falle antes y pase después (corrección: añadir la prueba de regresión como criterio de cierre).

## Ejemplo

El equipo de la plataforma registra: «Issue 3: el entorno de pruebas no responde desde el martes. Responsable: infraestructura. Fecha: jueves. Cierre: la suite completa corre en el entorno». Antes era un riesgo («el entorno podría caerse»); al ocurrir pasa a issue y se anota que el disparador funcionó o no existía. (Redacción ilustrativa.)

## Errores y confusiones comunes

- **Llamar riesgo a todo**: los problemas presentes quedan sin dueño.
- **Issues sin criterio de cierre**: se cierran por cansancio, no por verificación.
- **Cerrar sin prueba de regresión**: el defecto puede volver.
- **Confundir issue con tarea**: una tarea es trabajo planificado; un issue es un problema o decisión registrada.

## Límites y cuándo no aplica

En muchos equipos la plataforma llama «issue» a cualquier ítem (también ideas, preguntas, tareas); el sentido estricto de [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) conviene como disciplina de gestión pero no siempre coincide con el uso de la herramienta. Para trabajo de una sola persona y corta duración, un registro formal puede ser exceso.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ventana de gracia](../v/ventana-de-gracia.md), [Problemas](../p/problemas.md), [Registro](../r/registro.md), [Exposición](../e/exposicion.md), [Huérfano](../h/huerfano.md), [Pie de commit](../p/pie-de-commit.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (14 clases más lo mencionan; las que más):

[SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md), [SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md), [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Therac-25](../../../casos/fallo/therac-25.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Issues».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: vincular un PR con un issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) — palabras clave, sintaxis y condiciones; autoridad: GitHub Docs.
- [GitHub: plantillas de issues y PR](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates) — plantillas para pedir contexto; autoridad: GitHub Docs.
- [Boehm, «Software risk management: principles and practices» (IEEE Software, 1991)](https://doi.org/10.1109/52.62930) — identificación y priorización de riesgos de proyecto; autoridad: IEEE Software.
- [Nygard, «Documenting architecture decisions» (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registros breves de decisiones; autoridad: autor de la práctica.
- [Architectural Decision Records](https://adr.github.io/) — plantillas y vocabulario de registros de decisión; autoridad: comunidad ADR.

---

[↑ Glosario](../../README.md) · [← ISBN](./isbn.md) · [Iterable →](./iterable.md)
