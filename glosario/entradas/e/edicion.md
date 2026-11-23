# Edición

[↑ Glosario](../../README.md) · [← ECE](./ece.md) · [Edición asistida →](./edicion-asistida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Versión formal de una publicación.

Definición de trabajo de [SE-010 — Cómo leer estándares, documentación y literatura técnica](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md).

## Por qué importa

En [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md), el tema «Edición» importa porque cambia código existente: el tamaño del diff condiciona la revisión

## Cómo funciona

Según [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md):

El **autocompletado** propone la continuación de lo que escribes, normalmente una línea o un bloque corto, a una frecuencia alta; su riesgo es la aceptación automática, porque cada sugerencia exige una micro-decisión que el cansancio convierte en un reflejo. El **chat** conversa sobre el código; no cambia nada por sí mismo, así que su riesgo es de comprensión: una explicación errónea sobre el sistema, expresada con aplomo (`SE-553`). La **edición** propone modificar archivos existentes, a veces varios a la vez; su riesgo es el alcance, porque el cambio es tan fiable como la lectura que se haga de su diff. La **generación** produce código nuevo; su riesgo es la propiedad, porque aparece código que nadie del equipo escribió ni entiende y que hay que mantener.

Según [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones asigna modo y política a diez tareas. «Cambiar una condición de frontera» va por edición dirigida con parche mínimo y obligación de correr las pruebas antes de aceptar. «Entender cómo se calcula el redondeo» va por chat, con la función en el contexto y la respuesta contrastada con el código. «Escribir el cuerpo de una función con firma y pruebas dadas» va por autocompletado, con prohibición de aceptar líneas que contengan comparaciones de frontera, consultas o permisos sin ejecutar. «Crear un módulo de exportación nuevo» va por generación, con lectura completa por una segunda persona y las mismas pruebas que el código escrito a mano.

## Ejemplo

Ejemplo de [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md) (sección «Ejemplo mínimo»):

El fragmento mide cuántas líneas cambia una edición frente a una regeneración. Antes de ejecutarlo, predice el número de líneas distintas de cada una.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **“según ISO” sin edición** — causa: se omitieron vigencia y alcance. Corrección: añade identificador, año, modelo usado y límite. ([SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La práctica que se deduce es pedir parches mínimos, separar los cambios cosméticos y rechazar una edición cuyo diff no corresponde a la petición. ([SE-556](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Versión](../v/version.md), [Autocompletado](../a/autocompletado.md), [Cita de proximidad](../c/cita-de-proximidad.md), [Edición asistida](./edicion-asistida.md), [Especificación](./especificacion.md), [Generación](../g/generacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-010 — Cómo leer estándares, documentación y literatura técnica](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (63 clases más lo mencionan; las que más):

[SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Therac-25](../../../casos/fallo/therac-25.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Peng et al., «The Impact of AI on Developer Productivity: Evidence from GitHub Copilot»](https://arxiv.org/abs/2302.06590) — experimento controlado con una tarea acotada; autoridad: preprint de investigadores de GitHub y Microsoft.
- [METR, «Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity»](https://arxiv.org/abs/2507.09089) — ensayo aleatorizado con desarrolladores expertos; autoridad: METR.
- [Parasuraman y Manzey, «Complacency and Bias in Human Use of Automation»](https://doi.org/10.1177/0018720810376055) — complacencia y sesgo de automatización; autoridad: Human Factors.
- [Perry et al., «Do Users Write More Insecure Code with AI Assistants?»](https://arxiv.org/abs/2211.03622) — estudio de usuarios sobre código inseguro con asistente; autoridad: ACM CCS 2023.
- [Bacchelli y Bird](https://doi.org/10.1109/ICSE.2013.6606617) — revisión de código moderna; autoridad: ICSE 2013.

---

[↑ Glosario](../../README.md) · [← ECE](./ece.md) · [Edición asistida →](./edicion-asistida.md)
