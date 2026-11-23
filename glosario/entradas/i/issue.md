# Issue

[↑ Glosario](../../README.md) · [← ISBN](./isbn.md) · [Iterable →](./iterable.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Problema que ya ocurrió y requiere acción, con responsable, fecha y criterio de cierre.

Definición de trabajo de [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md): Registro con identificador estable de un problema, una propuesta o una decisión pendiente.

## Por qué importa

En [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), el tema «Issues» importa porque ya ocurrieron: necesitan responsable y fecha, no probabilidad.

## Cómo funciona

Según [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), en la sección «Issues»:

Un issue es un problema que ya ocurrió y requiere acción: el entorno de pruebas se cayó, un contrato se rompió. No tiene probabilidad, solo impacto presente. Necesita un responsable, una fecha y un criterio de cierre. La confusión habitual es llamar «riesgo» a todo lo que preocupa y dejar los issues en una hoja sin dueño. Un riesgo materializado se convierte en issue, y esa transición debe registrarse: es la señal de que el disparador funcionó o de que no existía.

## Ejemplo

Ejemplo de [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma de entregas reorganiza su hoja de 23 filas en cuatro registros. En riesgos quedan seis, cada uno con causa, efecto, probabilidad, impacto, disparador, respuesta y responsable; dos de ellos comparten causa (la salida de una persona clave) y se registran juntos para estimar la contingencia por percentil. En supuestos quedan cinco, con quién los afirma, evidencia y fecha de validación, ordenados por coste de fallar sobre coste de comprobar. Los cuatro issues tienen responsable y fecha. Las siete decisiones tomadas en el trimestre se registran con contexto y disparador de revisión.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El issue no se cierra al integrar** — causa: la sintaxis no es la reconocida o falta la palabra por cada issue. Corrección: repetir la palabra clave para cada número y usar la forma documentada. ([SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md))
- **El issue se cierra sin que el defecto desaparezca** — causa: no hay prueba que falle antes y pase después. Corrección: añadir la prueba de regresión como criterio de cierre. ([SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un issue es un problema que ya ocurrió y requiere acción: el entorno de pruebas se cayó, un contrato se rompió. ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md))
- Mezclar varios problemas en un issue impide cerrarlos por separado, y un issue sin criterio de cierre queda abierto para siempre. ([SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md))

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
