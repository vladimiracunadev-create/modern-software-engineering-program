# Renderizado en servidor

[↑ Glosario](../../README.md) · [← Renderizado en cliente](./renderizado-en-cliente.md) · [Rendimiento →](./rendimiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Construcción del HTML completo en cada petición antes de enviarlo.

Definición de trabajo de [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md).

## Por qué importa

La clase donde se define, [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md), existe con este propósito: la clase existe para que decidas, página por página, dónde se produce el HTML (en el navegador, en un servidor, antes de publicar o con regeneración periódica), sabiendo qué se paga en bytes, en tiempo de CPU del dispositivo, en obsolescencia y en riesgo de que el servidor y el cliente no coincidan, de modo que «usar el marco de moda» deje de ser un argumento.

## Cómo funciona

Según [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md):

En el **renderizado en cliente**, el servidor entrega un documento mínimo y un paquete de JavaScript; el navegador lo descarga, lo ejecuta, pide los datos y construye la página. En el **renderizado en servidor**, cada petición produce el HTML completo con los datos incluidos. En el **estático**, el HTML se produce antes de publicar y se sirve desde una caché. En la **regeneración incremental** se sirve lo estático y se reconstruye al caducar. Ninguna es mejor en abstracto: el cliente ahorra servidor y paga dispositivo y red; el servidor paga cómputo por visita; el estático paga obsolescencia.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md):

La plataforma divide sus páginas por contenido: la portada y la ayuda se generan al publicar; el catálogo de cursos usa regeneración cada hora; la lista de entregas de una persona se renderiza en servidor después de identificarla, con las fechas enviadas como instantes ISO que el cliente formatea en su zona tras hidratar; y el formulario de entrega se hidrata como componente aislado. Cada página declara en el repositorio su estrategia, su caducidad y qué dato obsoleto sería inaceptable.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md)) son:

- **La página queda en blanco varios segundos en un móvil lento** — causa: todo el contenido depende de un paquete grande y de una petición en cadena. Corrección: enviar el contenido principal en el primer HTML o reducir la cadena.
- **Aviso de desajuste al hidratar** — causa: valores que dependen de zona, región, reloj o azar. Corrección: pasar el valor desde el servidor o renderizarlo solo en el cliente.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con renderizado en servidor el contenido llega en el primer HTML y la página es visible antes de que se ejecute el JavaScript; hasta que este se carga y se «hidrata», los controles pueden no responder. ([SE-231](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Generación estática](../g/generacion-estatica.md), [Hidratación](../h/hidratacion.md), [Regeneración incremental](./regeneracion-incremental.md), [Renderizado en cliente](./renderizado-en-cliente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [web.dev: Rendering on the Web](https://web.dev/articles/rendering-on-the-web) — estrategias de renderizado y sus compromisos; autoridad: Google web.dev.
- [React: hydrateRoot](https://react.dev/reference/react-dom/client/hydrateRoot) — coincidencia entre HTML del servidor y árbol del cliente; autoridad: documentación de React.
- [RFC 5861: HTTP Cache-Control Extensions for Stale Content](https://www.rfc-editor.org/rfc/rfc5861) — `stale-while-revalidate` y `stale-if-error`; autoridad: IETF.
- [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — frescura, caducidad y revalidación; autoridad: IETF.
- [web.dev: Largest Contentful Paint](https://web.dev/articles/lcp) — métrica de primer contenido útil; autoridad: Google web.dev.

---

[↑ Glosario](../../README.md) · [← Renderizado en cliente](./renderizado-en-cliente.md) · [Rendimiento →](./rendimiento.md)
