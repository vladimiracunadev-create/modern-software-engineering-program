# Fuente de verdad

[↑ Glosario](../../README.md) · [← Fronteras entre modelos](./fronteras-entre-modelos.md) · [Fuente de verdad y transformación →](./fuente-de-verdad-y-transformacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Lugar único donde vive un dato y desde el que se obtienen sus copias.

Definición de trabajo de [SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md): Artefacto autorizado para una afirmación concreta.

## Por qué importa

La clase donde se define, [SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md), existe con este propósito: la clase existe para que decidas dónde vive cada dato de una interfaz (en un componente, compartido, en el servidor, en la URL o derivado de otro) y sepas qué falla cuando lo guardas dos veces, lo identificas mal o aceptas respuestas en el orden en que llegan, de modo que «la pantalla muestra algo raro» tenga una causa que se pueda buscar.

## Cómo funciona

[SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para esta clase y deben contrastarse con la documentación enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md):

La lista de entregas de la plataforma usa el identificador de entrega como clave, deriva el total de adjuntos y el estado «con comentarios pendientes» de la lista, y obtiene los datos de un cliente que comparte una sola petición entre los componentes que la necesitan. El buscador asocia a cada consulta un contador y una señal de cancelación: la respuesta solo se aplica si su contador es el mayor visto. El comentario a medias vive en el estado local de la fila, que sigue al identificador.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una acción cambia datos en tres sitios y uno se queda viejo** — causa: varias fuentes de verdad para el mismo dato. Corrección: elegir una fuente y derivar el resto. ([SE-232](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con la documentación enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún marco real ni se midió una aplicación: el reconciliador es mínimo y las probabilidades de olvido y las latencias son construcciones del autor. La siguiente clase pregunta cómo se capturan y validan los datos que la persona escribe, y qué le decimos cuando algo falla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Artefacto](../a/artefacto.md), [Carrera entre peticiones](../c/carrera-entre-peticiones.md), [Clave de lista](../c/clave-de-lista.md), [Contrato](../c/contrato.md), [Deduplicación de peticiones](../d/deduplicacion-de-peticiones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-232 — Estado, componentes y gestión de datos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (27 clases más lo mencionan; las que más):

[SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md), [SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

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

[↑ Glosario](../../README.md) · [← Fronteras entre modelos](./fronteras-entre-modelos.md) · [Fuente de verdad y transformación →](./fuente-de-verdad-y-transformacion.md)
