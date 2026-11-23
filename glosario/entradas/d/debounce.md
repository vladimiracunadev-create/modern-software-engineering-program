# Debounce

[↑ Glosario](../../README.md) · [← Debilidad sistémica](./debilidad-sistemica.md) · [Debugger, adapter y runtime →](./debugger-adapter-y-runtime.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Técnica que retrasa una llamada hasta que pasa un tiempo sin nuevos eventos.

Definición de trabajo de [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md).

## Por qué importa

En [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), el tema «Ritmo y respuesta» importa porque debounce y throttle no son intercambiables; las tareas largas cuestan interactividad.

## Cómo funciona

Según [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md):

Los eventos de entrada continuos (teclas, desplazamiento, redimensión) pueden llegar más rápido de lo que conviene reaccionar. **Debounce** espera a que cese la actividad y responde una vez, con el último valor; **throttle** responde como mucho una vez por intervalo y deja pasar valores intermedios. Para animaciones, `requestAnimationFrame` sincroniza con el pintado. Una tarea larga (más de 50 ms, como orientación de la plataforma) bloquea el hilo y demora el siguiente evento: se fragmenta cediendo el control entre trozos o se mueve a un trabajador.

Según [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md):

La lista de adjuntos de la plataforma se rehace con un único manejador en el contenedor que usa `evento.target.closest("button.borrar")`, comprueba que el botón pertenece a la lista y llama a una función pura que decide qué borrar a partir de `data-id`. El manejador de búsqueda de entregas usa debounce de 300 ms y lanza una única petición por ráfaga. La actualización de la barra de progreso de subida se agrupa con `requestAnimationFrame`, y el cálculo del resumen de 5000 filas se divide en trozos de 5 ms que ceden el control entre sí.

## Ejemplo

Ejemplo de [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) (sección «Ejemplo profesional»):

La lista de adjuntos de la plataforma se rehace con un único manejador en el contenedor que usa `evento.target.closest("button.borrar")`, comprueba que el botón pertenece a la lista y llama a una función pura que decide qué borrar a partir de `data-id`. El manejador de búsqueda de entregas usa debounce de 300 ms y lanza una única petición por ráfaga. La actualización de la barra de progreso de subida se agrupa con `requestAnimationFrame`, y el cálculo del resumen de 5000 filas se divide en trozos de 5 ms que ceden el control entre sí.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una búsqueda lanza una petición por pulsación** — causa: ausencia de debounce en un evento de entrada continua. Corrección: aplicar debounce y cancelar la petición anterior. ([SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El motor es V8 en Node, no un navegador; el modelo de DOM es una simplificación del algoritmo y las pulsaciones son construcciones del autor. La siguiente clase pregunta dónde conviene calcular y construir el documento: en el navegador, en un servidor o antes de publicar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Delegación de eventos](./delegacion-de-eventos.md), [Microtarea](../m/microtarea.md), [Tarea](../t/tarea.md), [Throttle](../t/throttle.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-556](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HTML Standard: bucles de eventos (WHATWG)](https://html.spec.whatwg.org/multipage/webappapis.html#event-loops) — tareas, microtareas y renderizado; autoridad: WHATWG.
- [DOM Standard: eventos (WHATWG)](https://dom.spec.whatwg.org/#events) — fases de captura, destino y burbuja; autoridad: WHATWG.
- [MDN: Introducción a los eventos](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events) — burbuja, captura y delegación con ejemplos; autoridad: MDN.
- [web.dev: Interaction to Next Paint](https://web.dev/articles/inp) — latencia de interacción y tareas largas; autoridad: Google web.dev.
- [web.dev: Optimizar tareas largas](https://web.dev/articles/optimize-long-tasks) — fragmentar el trabajo y ceder el control; autoridad: Google web.dev.

---

[↑ Glosario](../../README.md) · [← Debilidad sistémica](./debilidad-sistemica.md) · [Debugger, adapter y runtime →](./debugger-adapter-y-runtime.md)
