# Enfoque de construcción

[↑ Glosario](../../README.md) · [← Energía](./energia.md) · [Engineering Manager →](./engineering-manager.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Un **enfoque de construcción** es la forma de producir el cliente de una aplicación: determina dónde corre la interfaz, quién la dibuja y qué capa de código se comparte entre plataformas. Es el término con que [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) (nativo, híbrido, web wrapper y cross-platform) organiza las opciones. Son categorías de enfoque, no veredictos sobre marcas: dentro de cada una hay mucha variedad.

## Por qué importa

De esa elección derivan el acceso a las capacidades del dispositivo, el rendimiento y el costo de mantener varios clientes. [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) pide documentarla y no tomarla por moda: cada enfoque decide dónde corre la interfaz y quién la dibuja.

## Cómo funciona

[SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) distingue cinco enfoques:

1. **Nativo:** cada cliente con las herramientas de su plataforma. Máximo acceso y adaptación, a costa de mantener un código por plataforma.
2. **Multiplataforma con interfaz propia:** un motor propio dibuja la interfaz, como describe la arquitectura de Flutter. Mismo aspecto en todas partes; la interfaz no usa los elementos nativos.
3. **Multiplataforma con elementos nativos gobernados desde código compartido:** como describe React Native; delega el dibujo a la plataforma.
4. **Híbrido en contenedor:** una web dentro de una aplicación; accede a capacidades vía un puente.
5. **Web instalable:** corre en el navegador con capacidades limitadas.

La pregunta técnica útil es dónde están las **fronteras** entre el código compartido y el de la plataforma, y cuántas veces por segundo se cruzan: la frontera más sensible es la que cruza más veces.

## Ejemplo

El equipo del cliente documenta la elección en cuatro artefactos enlazados ([SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md)): la tabla de criterios con puntuaciones y su fuente; el análisis de sensibilidad, que cuenta con qué frecuencia gana cada opción al sortear pesos; un prototipo de la frontera más sensible con su medición; y la lista de capacidades que el cliente necesita, marcadas como disponibles, opcionales o ausentes en cada opción.

## Errores y confusiones comunes

- **Elegir por marca o por tendencia** en lugar de por criterios con fuente.
- **Tomar una sola puntuación sin analizar su sensibilidad** a los pesos.
- **Suponer que «multiplataforma» significa una sola base sin trabajo nativo:** casi siempre hay capacidades que exigen código de plataforma.
- **Confundir enfoque con modelo de aplicación,** que trata del ciclo de vida del proceso ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md)).

## Límites y cuándo no aplica

La tabla de criterios codifica supuestos del equipo y de la fecha: los enfoques evolucionan. Un prototipo mide una frontera concreta, no el producto completo. Y cuando el producto es solo contenido web, la discusión de enfoques de cliente pierde sentido.

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
