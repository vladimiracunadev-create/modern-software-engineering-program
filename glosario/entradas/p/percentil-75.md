# Percentil 75

[↑ Glosario](../../README.md) · [← Percentil](./percentil.md) · [Percentil 85 →](./percentil-85.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Valor por debajo del cual está el 75 % de las visitas; se usa para evaluar métricas de experiencia.

Definición de trabajo de [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md): Valor bajo el cual queda el 75 % de las cargas; es el indicador de campo recomendado para el LCP.

## Por qué importa

La clase donde se define, [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), existe con este propósito: la clase existe para que conviertas «la página es lenta» en una decisión medible: qué métrica, con qué muestra, contra qué presupuesto y en qué cadena de recursos está el tiempo, de modo que optimizar deje de ser aplicar recetas y pase a ser cortar el tramo que realmente decide el resultado.

## Cómo funciona

Según [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md):

Las mediciones de **laboratorio** (un dispositivo y una red controlados) son reproducibles y sirven para encontrar la causa; las de **campo** (visitas reales) dicen qué experimentan las personas, con toda su variedad de dispositivos y redes. Las métricas de experiencia del usuario se evalúan en el percentil 75 de las visitas: el valor bajo el cual está el 75 % de ellas. El promedio engaña porque los tiempos tienen cola larga: unas pocas visitas muy lentas lo suben y ocultan que la mayoría está bien, o al revés.

Según [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md):

El equipo fija presupuestos para la página de entrega: 170 KB de JavaScript comprimido en la ruta de entrada, 15 peticiones y LCP de 2,5 s en el percentil 75 de visitas reales desde un móvil de gama media. Cada cambio pasa un comprobador que falla si el paquete lo supera. El análisis de la cascada muestra que la cadena HTML → script → datos decide el tiempo, así que se envían los datos iniciales en el primer HTML y se pre-carga la fuente; el CSS en línea se descarta por no mover la ruta crítica. Los datos de campo se leen con al menos 300 visitas por segmento.

## Ejemplo

Ejemplo de [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) (sección «Ejemplo mínimo»):

Estima el percentil 75 de una lista de tiempos y compáralo con el promedio; predice cuál es mayor.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md)) son:

- **La mejora no se nota en el móvil** — causa: optimización fuera de la ruta crítica. Corrección: medir la cadena y actuar sobre su eslabón más largo.
- **Se declara que se cumple con diez mediciones** — causa: muestra pequeña con falsa conformidad frecuente. Corrección: usar datos de campo con cientos de visitas e informar el intervalo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un presupuesto de rendimiento es un límite explícito (kilobytes de JavaScript, número de peticiones, LCP en el percentil 75) que se comprueba en cada cambio. ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md))
- Las métricas de experiencia se evalúan en el percentil 75 para que reflejen a casi todas las visitas sin que los extremos las dominen. ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Indicador](../i/indicador.md), [Métrica](../m/metrica.md), [Valor](../v/valor.md), [Byte](../b/byte.md), [Deriva](../d/deriva.md), [Medición de campo](../m/medicion-de-campo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [web.dev: umbrales de Core Web Vitals](https://web.dev/articles/defining-core-web-vitals-thresholds) — umbrales y percentil 75; autoridad: Google web.dev.
- [web.dev: Performance budgets 101](https://web.dev/articles/performance-budgets-101) — qué son los presupuestos y cómo comprobarlos; autoridad: Google web.dev.
- [web.dev: precargar recursos críticos](https://web.dev/articles/preload-critical-assets) — pistas de precarga; autoridad: Google web.dev.
- [MDN: ruta crítica de renderizado](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Critical_rendering_path) — pasos hasta la primera pintura; autoridad: MDN.
- [RFC 9113: HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) — multiplexación de peticiones; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Percentil](./percentil.md) · [Percentil 85 →](./percentil-85.md)
