# Generación

[↑ Glosario](../../README.md) · [← Gemelo simulado](./gemelo-simulado.md) · [Generación determinista →](./generacion-determinista.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Producción de código nuevo a partir de una descripción.

Definición de trabajo de [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md).

## Por qué importa

En [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md), el tema «Generación» importa porque introduce código que nadie conocía: exige comprenderlo antes de integrarlo

## Cómo funciona

Según [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md):

El **autocompletado** propone la continuación de lo que escribes, normalmente una línea o un bloque corto, a una frecuencia alta; su riesgo es la aceptación automática, porque cada sugerencia exige una micro-decisión que el cansancio convierte en un reflejo. El **chat** conversa sobre el código; no cambia nada por sí mismo, así que su riesgo es de comprensión: una explicación errónea sobre el sistema, expresada con aplomo (`SE-553`). La **edición** propone modificar archivos existentes, a veces varios a la vez; su riesgo es el alcance, porque el cambio es tan fiable como la lectura que se haga de su diff. La **generación** produce código nuevo; su riesgo es la propiedad, porque aparece código que nadie del equipo escribió ni entiende y que hay que mantener.

Según [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones asigna modo y política a diez tareas. «Cambiar una condición de frontera» va por edición dirigida con parche mínimo y obligación de correr las pruebas antes de aceptar. «Entender cómo se calcula el redondeo» va por chat, con la función en el contexto y la respuesta contrastada con el código. «Escribir el cuerpo de una función con firma y pruebas dadas» va por autocompletado, con prohibición de aceptar líneas que contengan comparaciones de frontera, consultas o permisos sin ejecutar. «Crear un módulo de exportación nuevo» va por generación, con lectura completa por una segunda persona y las mismas pruebas que el código escrito a mano.

## Ejemplo

Ejemplo de [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones asigna modo y política a diez tareas. «Cambiar una condición de frontera» va por edición dirigida con parche mínimo y obligación de correr las pruebas antes de aceptar. «Entender cómo se calcula el redondeo» va por chat, con la función en el contexto y la respuesta contrastada con el código. «Escribir el cuerpo de una función con firma y pruebas dadas» va por autocompletado, con prohibición de aceptar líneas que contengan comparaciones de frontera, consultas o permisos sin ejecutar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se integra un módulo generado que nadie entiende** — causa: generación sin lectura. Corrección: lectura completa y explicación antes de integrar. ([SE-556](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de aceptación, una medición real de diff con `difflib` sobre un archivo generado y una traza de pulsaciones determinista.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producción](../p/produccion.md), [Autocompletado](../a/autocompletado.md), [Edición](../e/edicion.md), [Edición asistida](../e/edicion-asistida.md), [Retardo antes de pedir](../r/retardo-antes-de-pedir.md), [Sesgo de automatización](../s/sesgo-de-automatizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (48 clases más lo mencionan; las que más):

[SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md), [SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md), [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

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

[↑ Glosario](../../README.md) · [← Gemelo simulado](./gemelo-simulado.md) · [Generación determinista →](./generacion-determinista.md)
