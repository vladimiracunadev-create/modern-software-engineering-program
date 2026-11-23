# Microtarea

[↑ Glosario](../../README.md) · [← Microservicio](./microservicio.md) · [MicroVM →](./microvm.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Continuación pendiente (promesa o `queueMicrotask`) que se ejecuta por completo antes de la siguiente tarea.

Definición de trabajo de [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md).

## Por qué importa

La clase donde se define, [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), existe con este propósito: la clase existe para que entiendas el modelo de ejecución del navegador (un hilo, colas de tareas y de microtareas, renderizado entre tareas) y el flujo de eventos del DOM, de modo que un manejador no «a veces funcione»: sepas qué corre cuándo, quién recibe el clic y cuánto tiempo le dejas al navegador para responder.

## Cómo funciona

Según [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md):

El navegador ejecuta el código de la página en un hilo principal con un bucle de eventos: toma una tarea de una cola (un temporizador vencido, un evento de usuario, la carga de un recurso), la ejecuta hasta vaciar la pila y, antes de tomar la siguiente, vacía **todas** las microtareas pendientes (las continuaciones de promesas y `queueMicrotask`). Solo entre tareas puede el navegador actualizar el renderizado. Consecuencia: `Promise.then` corre antes que un `setTimeout(0)` programado antes, y un bucle síncrono largo o una cadena infinita de microtareas dejan sin turno al resto.

Según [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md):

Porque programa una tarea para el futuro: antes corren el código síncrono en curso y todas las microtareas pendientes. Y los navegadores aplican un retraso mínimo a temporizadores anidados.

## Ejemplo

Ejemplo de [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) (sección «Ejemplo mínimo»):

La salida es 1, 2, 3, 4: el código síncrono termina, se vacían las microtareas y solo entonces corre el temporizador. Registra versión de Node y salida; si anidas otra microtarea dentro de la primera, predice dónde queda respecto del temporizador.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md)) son:

- **Los botones de filas nuevas no responden** — causa: manejador registrado por elemento solo en la carga inicial. Corrección: delegar en el contenedor o registrar al crear cada fila.
- **El manejador delegado ignora clics en el icono** — causa: se compara `target` con el botón en lugar de usar `closest`. Corrección: buscar el ancestro con `closest` y comprobar que pertenece al contenedor.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- `Promise.then` corre antes que un `setTimeout(0)` programado antes, y un bucle síncrono largo o una cadena infinita de microtareas dejan sin turno al resto. ([SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md))
- Porque programa una tarea para el futuro: antes corren el código síncrono en curso y todas las microtareas pendientes. ([SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tarea](../t/tarea.md), [Debounce](../d/debounce.md), [Delegación de eventos](../d/delegacion-de-eventos.md), [Throttle](../t/throttle.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HTML Standard: bucles de eventos (WHATWG)](https://html.spec.whatwg.org/multipage/webappapis.html#event-loops) — tareas, microtareas y renderizado; autoridad: WHATWG.
- [Node.js: el bucle de eventos](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick) — orden entre microtareas y temporizadores en Node; autoridad: OpenJS Foundation.
- [DOM Standard: eventos (WHATWG)](https://dom.spec.whatwg.org/#events) — fases de captura, destino y burbuja; autoridad: WHATWG.
- [MDN: Introducción a los eventos](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events) — burbuja, captura y delegación con ejemplos; autoridad: MDN.
- [web.dev: Interaction to Next Paint](https://web.dev/articles/inp) — latencia de interacción y tareas largas; autoridad: Google web.dev.

---

[↑ Glosario](../../README.md) · [← Microservicio](./microservicio.md) · [MicroVM →](./microvm.md)
