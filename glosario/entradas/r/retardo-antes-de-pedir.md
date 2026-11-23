# Retardo antes de pedir

[↑ Glosario](../../README.md) · [← Resumen con pérdida](./resumen-con-perdida.md) · [Retardo de replicación →](./retardo-de-replicacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Espera tras la última pulsación antes de enviar una petición.

Definición de trabajo de [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md).

## Por qué importa

La clase donde se define, [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md), existe con este propósito: la clase existe para que dejes de hablar de «usar IA para programar» como si fuera una sola actividad y distingas cuatro modos de interacción con exigencias distintas: el autocompletado que sugiere mientras escribes, el chat que conversa sobre el código, la edición que propone un cambio sobre archivos existentes y la generación que produce código nuevo.

## Cómo funciona

Según [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md):

Una sugerencia útil debe llegar antes de que la persona continúe escribiendo; si llega tarde, estorba o se descarta. Pedir una sugerencia en cada pulsación genera muchas peticiones que se cancelan antes de ser leídas, con costo para el servicio y parpadeo para la persona. La técnica estándar es el **retardo antes de pedir** (*debounce*): esperar a que la escritura se detenga un momento. El retardo óptimo depende del ritmo de la persona y de la latencia del servicio, y no existe un valor universal. Tampoco hay que olvidar el costo de atención: cada sugerencia mostrada obliga a decidir, aun si se rechaza. Un buen diseño muestra menos sugerencias en los momentos en que es más probable que sean útiles, y la persona debe poder ajustarlo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones asigna modo y política a diez tareas. «Cambiar una condición de frontera» va por edición dirigida con parche mínimo y obligación de correr las pruebas antes de aceptar. «Entender cómo se calcula el redondeo» va por chat, con la función en el contexto y la respuesta contrastada con el código.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Mucho gasto y poca ayuda del autocompletado** — causa: petición en cada pulsación. Corrección: retardo antes de pedir ajustado al ritmo. ([SE-556](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de aceptación, una medición real de diff con `difflib` sobre un archivo generado y una traza de pulsaciones determinista.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Autocompletado](../a/autocompletado.md), [Edición](../e/edicion.md), [Edición asistida](../e/edicion-asistida.md), [Generación](../g/generacion.md), [Sesgo de automatización](../s/sesgo-de-automatizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «debounce».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Peng et al., «The Impact of AI on Developer Productivity: Evidence from GitHub Copilot»](https://arxiv.org/abs/2302.06590) — experimento controlado con una tarea acotada; autoridad: preprint de investigadores de GitHub y Microsoft.
- [METR, «Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity»](https://arxiv.org/abs/2507.09089) — ensayo aleatorizado con desarrolladores expertos; autoridad: METR.
- [Parasuraman y Manzey, «Complacency and Bias in Human Use of Automation»](https://doi.org/10.1177/0018720810376055) — complacencia y sesgo de automatización; autoridad: Human Factors.
- [Perry et al., «Do Users Write More Insecure Code with AI Assistants?»](https://arxiv.org/abs/2211.03622) — estudio de usuarios sobre código inseguro con asistente; autoridad: ACM CCS 2023.
- [Bacchelli y Bird](https://doi.org/10.1109/ICSE.2013.6606617) — revisión de código moderna; autoridad: ICSE 2013.

---

[↑ Glosario](../../README.md) · [← Resumen con pérdida](./resumen-con-perdida.md) · [Retardo de replicación →](./retardo-de-replicacion.md)
