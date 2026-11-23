# Hidratación

[↑ Glosario](../../README.md) · [← Híbrido](./hibrido.md) · [HIL →](./hil.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Adjuntar comportamiento en el cliente a un HTML ya construido por el servidor, reproduciendo el mismo árbol.

Definición de trabajo de [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md).

## Por qué importa

En [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md), el tema «Hidratación y determinismo» importa porque el cliente debe reproducir lo que construyó el servidor; la zona horaria o un azar lo rompen.

## Cómo funciona

Según [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md):

Se tomaron 2000 marcas de tiempo sintéticas de 2026 y se formatearon con el mismo formato `dd/mm/aaaa hh:mm` en una zona (servidor en UTC) y en otra (cliente). Si el cliente está en la **misma** zona, 0 de 2000 textos difieren; si está en UTC−3 o en UTC+9, **los 2000 difieren**. Si solo se muestra el día, difieren **239** (UTC−3) y **742** (UTC+9). Un valor aleatorio sin semilla generado en el render difirió en **2000 de 2000** hidrataciones.

Según [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** al cargar, las fechas «parpadean» y la consola avisa de un desajuste de hidratación. **Hipótesis rivales:** (a) un componente se renderiza dos veces; (b) el texto de la fecha difiere entre servidor y cliente. **Prueba:** compara el texto del HTML recibido con el del árbol tras hidratar para una misma marca; comprueba que difieren por la hora. **Conclusión:** la causa es formatear con la zona del entorno en la primera pasada. **Regresión:** envía el instante en ISO, formatea solo en el cliente tras la hidratación y añade una prueba que renderice la lista bajo tres zonas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md):

La plataforma divide sus páginas por contenido: la portada y la ayuda se generan al publicar; el catálogo de cursos usa regeneración cada hora; la lista de entregas de una persona se renderiza en servidor después de identificarla, con las fechas enviadas como instantes ISO que el cliente formatea en su zona tras hidratar; y el formulario de entrega se hidrata como componente aislado. Cada página declara en el repositorio su estrategia, su caducidad y qué dato obsoleto sería inaceptable.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md)) son:

- **La página queda en blanco varios segundos en un móvil lento** — causa: todo el contenido depende de un paquete grande y de una petición en cadena. Corrección: enviar el contenido principal en el primer HTML o reducir la cadena.
- **Aviso de desajuste al hidratar** — causa: valores que dependen de zona, región, reloj o azar. Corrección: pasar el valor desde el servidor o renderizarlo solo en el cliente.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un valor aleatorio sin semilla generado en el render difirió en **2000 de 2000** hidrataciones. ([SE-231](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Árbol](../a/arbol.md), [Generación estática](../g/generacion-estatica.md), [Regeneración incremental](../r/regeneracion-incremental.md), [Renderizado en cliente](../r/renderizado-en-cliente.md), [Renderizado en servidor](../r/renderizado-en-servidor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-231 — Renderizado cliente, servidor, estático e híbrido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-232](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `datetime`](https://docs.python.org/3/library/datetime.html) — zonas horarias fijas usadas en el experimento de hidratación.
- [web.dev: Rendering on the Web](https://web.dev/articles/rendering-on-the-web) — estrategias de renderizado y sus compromisos; autoridad: Google web.dev.
- [React: hydrateRoot](https://react.dev/reference/react-dom/client/hydrateRoot) — coincidencia entre HTML del servidor y árbol del cliente; autoridad: documentación de React.
- [RFC 5861: HTTP Cache-Control Extensions for Stale Content](https://www.rfc-editor.org/rfc/rfc5861) — `stale-while-revalidate` y `stale-if-error`; autoridad: IETF.
- [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — frescura, caducidad y revalidación; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Híbrido](./hibrido.md) · [HIL →](./hil.md)
