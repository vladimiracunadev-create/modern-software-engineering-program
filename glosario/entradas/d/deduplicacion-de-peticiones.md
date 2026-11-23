# Deduplicación de peticiones

[↑ Glosario](../../README.md) · [← Deduplicación](./deduplicacion.md) · [Defecto de forma →](./defecto-de-forma.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Reutilización de una petición en vuelo por varias partes que piden el mismo recurso.

Definición de trabajo de [SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md).

## Por qué importa

La clase donde se define, [SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md), existe con este propósito: la clase existe para que decidas dónde vive cada dato de una interfaz (en un componente, compartido, en el servidor, en la URL o derivado de otro) y sepas qué falla cuando lo guardas dos veces, lo identificas mal o aceptas respuestas en el orden en que llegan, de modo que «la pantalla muestra algo raro» tenga una causa que se pueda buscar.

## Cómo funciona

[SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para esta clase y deben contrastarse con la documentación enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md):

La lista de entregas de la plataforma usa el identificador de entrega como clave, deriva el total de adjuntos y el estado «con comentarios pendientes» de la lista, y obtiene los datos de un cliente que comparte una sola petición entre los componentes que la necesitan. El buscador asocia a cada consulta un contador y una señal de cancelación: la respuesta solo se aplica si su contador es el mayor visto. El comentario a medias vive en el estado local de la fila, que sigue al identificador.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md)) son:

- **El texto escrito aparece en otra fila tras reordenar** — causa: clave igual a la posición. Corrección: usar un identificador estable como clave.
- **El total de la cabecera no coincide con la lista** — causa: valor guardado aparte y una rama que no lo actualiza. Corrección: derivarlo de la lista.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con la documentación enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún marco real ni se midió una aplicación: el reconciliador es mínimo y las probabilidades de olvido y las latencias son construcciones del autor. La siguiente clase pregunta cómo se capturan y validan los datos que la persona escribe, y qué le decimos cuando algo falla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-231](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Carrera entre peticiones](../c/carrera-entre-peticiones.md), [Clave de lista](../c/clave-de-lista.md), [Estado derivado](../e/estado-derivado.md), [Fuente de verdad](../f/fuente-de-verdad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [React: Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state) — estado asociado a posición y clave; autoridad: documentación de React.
- [React: Choosing the State Structure](https://react.dev/learn/choosing-the-state-structure) — evitar el estado duplicado y derivar valores; autoridad: documentación de React.
- [React: You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect) — derivar en lugar de sincronizar con efectos; autoridad: documentación de React.
- [MDN: AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) — cancelación de peticiones; autoridad: MDN.
- [Redux: Normalizing State Shape](https://redux.js.org/usage/structuring-reducers/normalizing-state-shape) — entidades por identificador; autoridad: documentación de Redux.

---

[↑ Glosario](../../README.md) · [← Deduplicación](./deduplicacion.md) · [Defecto de forma →](./defecto-de-forma.md)
