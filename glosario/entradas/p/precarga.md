# Precarga

[↑ Glosario](../../README.md) · [← Práctica deliberada](./practica-deliberada.md) · [Precedencia →](./precedencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Pista que hace que el navegador pida un recurso antes de descubrirlo por sí mismo.

Definición de trabajo de [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md).

## Por qué importa

En [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), el tema «Caché y prioridad» importa porque un recurso en caché no cuesta una petición; una pista de precarga adelanta el inicio de otra.

## Cómo funciona

Según [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md):

El navegador no puede pintar hasta tener el HTML y los recursos que bloquean el renderizado (hojas de estilo, scripts síncronos); y hay recursos que solo se descubren al procesar otros (una fuente que declara el CSS, unos datos que pide el JavaScript). La **ruta crítica** es la cadena más larga de dependencias: acortar cualquier otra no cambia el tiempo total. Se acorta con menos bytes en la cadena, con menos eslabones (incluir lo necesario en el primer HTML) y con pistas que adelantan el inicio de un recurso (`preload`).

Según [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** tras poner el CSS en línea, la página tarda lo mismo en un móvil lento. **Hipótesis rivales:** (a) el CSS en línea no se aplicó; (b) la ruta crítica pasa por otra cadena. **Prueba:** calcula la cadena más larga del modelo y comprueba que es HTML → script → datos; evalúa la variante con preload y observa que baja el total. **Conclusión:** la causa es optimizar fuera de la ruta crítica. **Regresión:** añade al comprobador un cálculo de la ruta crítica y exige que cada optimización indique en qué eslabón actúa. No cambies a la vez el CSS y los datos: no sabrás qué mejoró el total.

## Ejemplo

Ejemplo de [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) (sección «Caso conductor»):

La aplicación de entregas con conectividad irregular fija en esta clase el presupuesto de la página de entrega y el orden de los recursos. Ese presupuesto es el que `SE-237` usa para decidir qué precarga el service worker, `SE-238` para los metadatos de la página y `SE-239` para el taller de integración. Cambia después una sola decisión, el nivel de gzip de 6 a 9, y calcula cuánto ahorra y cuánto cuesta en tiempo de construcción.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md)) son:

- **La mejora no se nota en el móvil** — causa: optimización fuera de la ruta crítica. Corrección: medir la cadena y actuar sobre su eslabón más largo.
- **Se declara que se cumple con diez mediciones** — causa: muestra pequeña con falsa conformidad frecuente. Corrección: usar datos de campo con cientos de visitas e informar el intervalo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Poner el CSS en línea no cambia el total porque la ruta más larga es HTML → script → datos, y el preload la acorta al sacar los datos de detrás del script. ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Byte](../b/byte.md), [Minificación](../m/minificacion.md), [Percentil 75](./percentil-75.md), [Presupuesto](./presupuesto.md), [Presupuesto de rendimiento](./presupuesto-de-rendimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «preload».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [web.dev: precargar recursos críticos](https://web.dev/articles/preload-critical-assets) — pistas de precarga; autoridad: Google web.dev.
- [web.dev: umbrales de Core Web Vitals](https://web.dev/articles/defining-core-web-vitals-thresholds) — umbrales y percentil 75; autoridad: Google web.dev.
- [web.dev: Performance budgets 101](https://web.dev/articles/performance-budgets-101) — qué son los presupuestos y cómo comprobarlos; autoridad: Google web.dev.
- [MDN: ruta crítica de renderizado](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Critical_rendering_path) — pasos hasta la primera pintura; autoridad: MDN.
- [RFC 9113: HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) — multiplexación de peticiones; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Práctica deliberada](./practica-deliberada.md) · [Precedencia →](./precedencia.md)
