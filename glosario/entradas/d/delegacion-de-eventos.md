# Delegación de eventos

[↑ Glosario](../../README.md) · [← Delegación](./delegacion.md) · [Deliberate practice →](./deliberate-practice.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Registro de un manejador en un ancestro para atender eventos de descendientes presentes y futuros.

Definición de trabajo de [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md).

## Por qué importa

La clase donde se define, [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), existe con este propósito: la clase existe para que entiendas el modelo de ejecución del navegador (un hilo, colas de tareas y de microtareas, renderizado entre tareas) y el flujo de eventos del DOM, de modo que un manejador no «a veces funcione»: sepas qué corre cuándo, quién recibe el clic y cuánto tiempo le dejas al navegador para responder.

## Cómo funciona

[SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md):

La lista de adjuntos de la plataforma se rehace con un único manejador en el contenedor que usa `evento.target.closest("button.borrar")`, comprueba que el botón pertenece a la lista y llama a una función pura que decide qué borrar a partir de `data-id`. El manejador de búsqueda de entregas usa debounce de 300 ms y lanza una única petición por ráfaga.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md)) son:

- **Los botones de filas nuevas no responden** — causa: manejador registrado por elemento solo en la carga inicial. Corrección: delegar en el contenedor o registrar al crear cada fila.
- **El manejador delegado ignora clics en el icono** — causa: se compara `target` con el botón en lugar de usar `closest`. Corrección: buscar el ancestro con `closest` y comprobar que pertenece al contenedor.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El motor es V8 en Node, no un navegador; el modelo de DOM es una simplificación del algoritmo y las pulsaciones son construcciones del autor. La siguiente clase pregunta dónde conviene calcular y construir el documento: en el navegador, en un servidor o antes de publicar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Manejador](../m/manejador.md), [Registro](../r/registro.md), [Debounce](./debounce.md), [Microtarea](../m/microtarea.md), [Tarea](../t/tarea.md).
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

[↑ Glosario](../../README.md) · [← Delegación](./delegacion.md) · [Deliberate practice →](./deliberate-practice.md)
