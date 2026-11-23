# Throttle

[↑ Glosario](../../README.md) · [← Texto alternativo](./texto-alternativo.md) · [Throughput →](./throughput.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Técnica que limita una llamada a como mucho una por intervalo.

Definición de trabajo de [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md).

## Por qué importa

En [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), el tema «Ritmo y respuesta» importa porque debounce y throttle no son intercambiables; las tareas largas cuestan interactividad.

## Cómo funciona

Según [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md):

Los eventos de entrada continuos (teclas, desplazamiento, redimensión) pueden llegar más rápido de lo que conviene reaccionar. **Debounce** espera a que cese la actividad y responde una vez, con el último valor; **throttle** responde como mucho una vez por intervalo y deja pasar valores intermedios. Para animaciones, `requestAnimationFrame` sincroniza con el pintado. Una tarea larga (más de 50 ms, como orientación de la plataforma) bloquea el hilo y demora el siguiente evento: se fragmenta cediendo el control entre trozos o se mueve a un trabajador.

Según [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md):

Para reaccionar mientras se desplaza (barra de progreso, carga diferida) conviene limitar la frecuencia con throttle o `requestAnimationFrame`; para reaccionar al terminar (guardar la posición) conviene debounce. La pregunta es si el valor intermedio sirve.

## Ejemplo

Ejemplo de [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) (sección «Preguntas frecuentes»):

Para reaccionar mientras se desplaza (barra de progreso, carga diferida) conviene limitar la frecuencia con throttle o `requestAnimationFrame`; para reaccionar al terminar (guardar la posición) conviene debounce. La pregunta es si el valor intermedio sirve.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md)) son:

- **Los botones de filas nuevas no responden** — causa: manejador registrado por elemento solo en la carga inicial. Corrección: delegar en el contenedor o registrar al crear cada fila.
- **El manejador delegado ignora clics en el icono** — causa: se compara `target` con el botón en lugar de usar `closest`. Corrección: buscar el ancestro con `closest` y comprobar que pertenece al contenedor.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Del total de 92 pausas de al menos 300 ms, en **66** el throttle de 300 ms no atendió el último evento de la ráfaga. ([SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intervalo](../i/intervalo.md), [Debounce](../d/debounce.md), [Delegación de eventos](../d/delegacion-de-eventos.md), [Microtarea](../m/microtarea.md), [Tarea](./tarea.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

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

[↑ Glosario](../../README.md) · [← Texto alternativo](./texto-alternativo.md) · [Throughput →](./throughput.md)
