# Restauración

[↑ Glosario](../../README.md) · [← Responsabilidad compartida](./responsabilidad-compartida.md) · [Restricción de integridad →](./restriccion-de-integridad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Lectura del estado guardado para reconstruir la aplicación tras un arranque en frío o una actualización.

Definición de trabajo de [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md).

## Por qué importa

En [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), el tema «Restauración y versiones» importa porque el estado guardado por la versión anterior es una entrada que la versión nueva debe leer.

## Cómo funciona

Según [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md):

Restaurar es leer un estado escrito por otra versión del código, y las versiones se suceden. Añadir un campo se resuelve con un valor por defecto; cambiar la forma de uno existente exige una migración que lo transforme. Rechazar por versión distinta, la política estricta, equivale a perder el estado en cada actualización. Una prueba que restaura un estado guardado por cada versión anterior es la única evidencia de que la restauración funciona.

Según [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md):

El equipo del cliente define la política de guardado en una tabla con tres columnas: qué estado (borrador, adjuntos pendientes, posición), cuándo se guarda (al editar tras una pausa de un segundo, al pasar a segundo plano) y cómo se restaura (con la versión de formato en el archivo). La restauración se prueba con un estado de cada versión anterior almacenado en el repositorio, y el arranque en frío se fuerza en las pruebas de integración. El guardado en el gancho solo escribe el borrador; los adjuntos se suben antes.

## Ejemplo

Ejemplo de [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) (sección «Ejemplo profesional»):

El equipo del cliente define la política de guardado en una tabla con tres columnas: qué estado (borrador, adjuntos pendientes, posición), cuándo se guarda (al editar tras una pausa de un segundo, al pasar a segundo plano) y cómo se restaura (con la versión de formato en el archivo). La restauración se prueba con un estado de cada versión anterior almacenado en el repositorio, y el arranque en frío se fuerza en las pruebas de integración. El guardado en el gancho solo escribe el borrador; los adjuntos se suben antes.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Las pruebas pasan y la restauración falla en uso real** — causa: nunca se probó el arranque en frío ni un estado antiguo. Corrección: forzar el arranque en frío y conservar un estado de cada versión. ([SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Resultado: la política estricta falla en **2000 de 2000** restauraciones con las versiones 2, 3 y 4; los valores por defecto funcionan con las versiones 2 y 3 (**0 fallos**) pero fallan en **2000 de 2000** con la 4, porque cambia la forma de un campo existente; las migraciones no fallan nunca. ([SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Arranque en frío](../a/arranque-en-frio.md).
- **Ver también:** [Estado](../e/estado.md), [Ciclo de vida](../c/ciclo-de-vida.md), [Escritura atómica](../e/escritura-atomica.md), [Gancho](../g/gancho.md), [Migración](../m/migracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (36 clases más lo mencionan; las que más):

[SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md).

**Aparece en los casos de estudio:** [TSB Bank](../../../casos/fallo/tsb.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Android Developers, «The activity lifecycle»](https://developer.android.com/guide/components/activities/activity-lifecycle) — estados y transiciones de una actividad; autoridad: Google.
- [Android Developers, «Save UI states»](https://developer.android.com/topic/libraries/architecture/saving-states) — qué estado guardar y dónde; autoridad: Google.
- [Android Developers, «Processes and app lifecycle»](https://developer.android.com/guide/components/activities/process-lifecycle) — prioridad de procesos y cuándo el sistema los termina; autoridad: Google.
- [Apple Developer, «Managing your app's life cycle»](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) — estados de una aplicación de iOS; autoridad: Apple.
- [Apple Developer, «Preserving your app's UI across launches»](https://developer.apple.com/documentation/uikit/view_controllers/preserving_your_app_s_ui_across_launches) — preservar y restaurar la interfaz; autoridad: Apple.

---

[↑ Glosario](../../README.md) · [← Responsabilidad compartida](./responsabilidad-compartida.md) · [Restricción de integridad →](./restriccion-de-integridad.md)
