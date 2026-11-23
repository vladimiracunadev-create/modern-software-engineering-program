# Enfoque de construcción

[↑ Glosario](../../README.md) · [← Energía](./energia.md) · [Engineering Manager →](./engineering-manager.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Forma de producir el cliente que determina dónde corre la interfaz, quién la dibuja y qué capa de código se comparte entre plataformas.

Definición de trabajo de [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md).

## Por qué importa

En [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), el tema «Enfoques de construcción» importa porque cada enfoque decide dónde corre la interfaz y quién la dibuja, y de eso derivan acceso, rendimiento y coste.

## Cómo funciona

Según [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), en la sección «Enfoques de construcción»:

El enfoque nativo escribe cada cliente con las herramientas de su plataforma. El multiplataforma con interfaz propia, como el que describe la arquitectura de Flutter, dibuja la interfaz con un motor propio. El que usa elementos nativos gobernados desde código compartido, como describe React Native, delega el dibujo a la plataforma. El híbrido en contenedor ejecuta una web dentro de una aplicación, y la web instalable corre en el navegador con capacidades limitadas. Son categorías de enfoque, no veredictos sobre marcas: dentro de cada una hay mucha variedad.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md):

El equipo del cliente documenta la elección en cuatro artefactos enlazados: la tabla de criterios con puntuaciones y su fuente, el análisis de sensibilidad (frecuencia con que gana cada opción al sortear pesos), un prototipo de la frontera más sensible (la que cruza más veces por segundo) con su medición, y la lista de capacidades que el cliente necesita y que cada opción ofrece, como disponibles, opcionales o ausentes.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md)) son:

- **La tabla de decisión elige la opción del autor de la tabla** — causa: los pesos se escogieron conociendo el ganador deseado. Corrección: fijar pesos antes de puntuar y mostrar la sensibilidad.
- **La decisión cambia al cambiar una puntuación en un punto** — causa: las puntuaciones son juicios con incertidumbre no declarada. Corrección: perturbar las puntuaciones y reportar la estabilidad.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo los tiempos. No se evaluó ningún marco ni producto: las puntuaciones son del autor y la frontera es un proxy. La siguiente clase decide dónde vive el estado y cómo se sincroniza.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](../c/capa.md), [Interfaz](../i/interfaz.md), [Plataforma](../p/plataforma.md), [Análisis de sensibilidad](../a/analisis-de-sensibilidad.md), [Capacidad opcional](../c/capacidad-opcional.md), [Frontera entre capas](../f/frontera-entre-capas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Enfoques de construcción».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Flutter, «Architectural overview»](https://docs.flutter.dev/resources/architectural-overview) — capas de un marco multiplataforma con interfaz propia; autoridad: Google.
- [React Native, «Architecture overview»](https://reactnative.dev/architecture/overview) — arquitectura con interfaz nativa y código compartido; autoridad: Meta.
- [Capacitor, documentación](https://capacitorjs.com/docs) — aplicación web empaquetada con acceso a capacidades nativas; autoridad: Ionic.
- [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform.html) — código compartido con interfaz y capacidades por plataforma; autoridad: JetBrains.
- [MDN, «Progressive web apps»](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps) — aplicaciones web instalables y sus capacidades; autoridad: Mozilla.

---

[↑ Glosario](../../README.md) · [← Energía](./energia.md) · [Engineering Manager →](./engineering-manager.md)
