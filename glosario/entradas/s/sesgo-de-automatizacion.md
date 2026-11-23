# Sesgo de automatización

[↑ Glosario](../../README.md) · [← Servidor MCP](./servidor-mcp.md) · [Sesgo de escritura →](./sesgo-de-escritura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Tendencia a aceptar la recomendación automatizada y a vigilar menos.

Definición de trabajo de [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md).

## Por qué importa

La clase donde se define, [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md), existe con este propósito: la clase existe para que dejes de hablar de «usar IA para programar» como si fuera una sola actividad y distingas cuatro modos de interacción con exigencias distintas: el autocompletado que sugiere mientras escribes, el chat que conversa sobre el código, la edición que propone un cambio sobre archivos existentes y la generación que produce código nuevo.

## Cómo funciona

Según [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md):

Parasuraman y Manzey describen el **sesgo de automatización**: la tendencia a aceptar la recomendación de un sistema automatizado y a reducir la vigilancia, que aumenta cuanto más fiable parece la ayuda. En programación el efecto es especialmente traicionero porque la mayoría de las sugerencias es correcta, de modo que la política «aceptar si parece bien» se refuerza con éxito hasta que falla una que parecía bien. Perry y sus coautores observaron que quienes tenían asistente escribieron código menos seguro y estaban más convencidos de que era seguro. La defensa no es desconfiar de todo, sino hacer proporcional la comprobación al riesgo: aceptar una cadena de texto no es lo mismo que aceptar una condición de frontera, una consulta SQL o una comprobación de permisos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones asigna modo y política a diez tareas. «Cambiar una condición de frontera» va por edición dirigida con parche mínimo y obligación de correr las pruebas antes de aceptar. «Entender cómo se calcula el redondeo» va por chat, con la función en el contexto y la respuesta contrastada con el código.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md)) son:

- **Se acepta una línea de frontera equivocada** — causa: aceptación a ciegas. Corrección: lista de líneas que no se aceptan sin ejecutar.
- **El diff es enorme para un cambio pequeño** — causa: se pidió el archivo regenerado. Corrección: pedir parches mínimos y separar los cambios cosméticos.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de aceptación, una medición real de diff con `difflib` sobre un archivo generado y una traza de pulsaciones determinista.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Autocompletado](../a/autocompletado.md), [Edición](../e/edicion.md), [Edición asistida](../e/edicion-asistida.md), [Generación](../g/generacion.md), [Retardo antes de pedir](../r/retardo-antes-de-pedir.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-556 — Autocompletado, chat, edición y generación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md), [SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Parasuraman y Manzey, «Complacency and Bias in Human Use of Automation»](https://doi.org/10.1177/0018720810376055) — complacencia y sesgo de automatización; autoridad: Human Factors.
- [Peng et al., «The Impact of AI on Developer Productivity: Evidence from GitHub Copilot»](https://arxiv.org/abs/2302.06590) — experimento controlado con una tarea acotada; autoridad: preprint de investigadores de GitHub y Microsoft.
- [METR, «Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity»](https://arxiv.org/abs/2507.09089) — ensayo aleatorizado con desarrolladores expertos; autoridad: METR.
- [Perry et al., «Do Users Write More Insecure Code with AI Assistants?»](https://arxiv.org/abs/2211.03622) — estudio de usuarios sobre código inseguro con asistente; autoridad: ACM CCS 2023.
- [Bacchelli y Bird](https://doi.org/10.1109/ICSE.2013.6606617) — revisión de código moderna; autoridad: ICSE 2013.

---

[↑ Glosario](../../README.md) · [← Servidor MCP](./servidor-mcp.md) · [Sesgo de escritura →](./sesgo-de-escritura.md)
