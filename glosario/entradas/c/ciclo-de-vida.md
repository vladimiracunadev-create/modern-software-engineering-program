# Ciclo de vida

[↑ Glosario](../../README.md) · [← Ciclo de trabajo](./ciclo-de-trabajo.md) · [CIDR →](./cidr.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Secuencia de estados por los que pasa una aplicación (primer plano, segundo plano, suspendido, terminado) y de transiciones que el sistema o la persona provocan.

Definición de trabajo de [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md).

## Por qué importa

En [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), el tema «Ciclo de vida» importa porque reparte responsabilidades y puntos de falla.

## Cómo funciona

[SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md)) son: Las cuatro fallas, su magnitud, el efecto del recordatorio y la regla son construcciones del autor sobre datos sintéticos; los números muestran que las causas son distintas y que el bucle existe, no su frecuencia en ningún sistema real. No se evaluó ninguna plataforma de MLOps. El siguiente paso, `SE-602`, abre el primer eslabón: cómo se construyen los datos, las etiquetas y las características para que no mientan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Secuencia](../s/secuencia.md), [Transición](../t/transicion.md), [Bucle de realimentación](../b/bucle-de-realimentacion.md), [Deriva de concepto](../d/deriva-de-concepto.md), [Deriva de covariables](../d/deriva-de-covariables.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (91 clases más lo mencionan; las que más):

[SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md).

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

[↑ Glosario](../../README.md) · [← Ciclo de trabajo](./ciclo-de-trabajo.md) · [CIDR →](./cidr.md)
