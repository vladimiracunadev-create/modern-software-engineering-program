# Frontera entre capas

[↑ Glosario](../../README.md) · [← Frontera de validación](./frontera-de-validacion.md) · [Fronteras entre modelos →](./fronteras-entre-modelos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Punto donde el código compartido se comunica con el de una plataforma y cada cruce serializa, copia y cambia de contexto.

Definición de trabajo de [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md).

## Por qué importa

En [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), el tema «Frontera entre capas» importa porque cruzar de código compartido a código de plataforma cuesta por cruce, no solo por dato.

## Cómo funciona

Según [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), en la sección «Frontera entre capas»:

Los enfoques con capa compartida y capa de plataforma tienen una frontera: cada cruce serializa, copia y cambia de contexto. Cuando se cruza mucho y con mensajes pequeños, el coste domina. La regla práctica es agrupar el trabajo en el lado donde ocurre y cruzar con mensajes gruesos y poco frecuentes, y medir en el marco concreto antes de confiar en ella.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md):

El equipo del cliente documenta la elección en cuatro artefactos enlazados: la tabla de criterios con puntuaciones y su fuente, el análisis de sensibilidad (frecuencia con que gana cada opción al sortear pesos), un prototipo de la frontera más sensible (la que cruza más veces por segundo) con su medición, y la lista de capacidades que el cliente necesita y que cada opción ofrece, como disponibles, opcionales o ausentes.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md)) son:

- **La tabla de decisión elige la opción del autor de la tabla** — causa: los pesos se escogieron conociendo el ganador deseado. Corrección: fijar pesos antes de puntuar y mostrar la sensibilidad.
- **La decisión cambia al cambiar una puntuación en un punto** — causa: las puntuaciones son juicios con incertidumbre no declarada. Corrección: perturbar las puntuaciones y reportar la estabilidad.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Como proxy de una frontera entre capas se mide solo la serialización: 2000 mensajes pequeños se leen directamente, se serializan y se leen uno a uno con JSON, o se serializan juntos en un lote. ([SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Plataforma](../p/plataforma.md), [Análisis de sensibilidad](../a/analisis-de-sensibilidad.md), [Capacidad opcional](../c/capacidad-opcional.md), [Enfoque de construcción](../e/enfoque-de-construccion.md), [Intersección de capacidades](../i/interseccion-de-capacidades.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Flutter, «Architectural overview»](https://docs.flutter.dev/resources/architectural-overview) — capas de un marco multiplataforma con interfaz propia; autoridad: Google.
- [React Native, «Architecture overview»](https://reactnative.dev/architecture/overview) — arquitectura con interfaz nativa y código compartido; autoridad: Meta.
- [Capacitor, documentación](https://capacitorjs.com/docs) — aplicación web empaquetada con acceso a capacidades nativas; autoridad: Ionic.
- [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform.html) — código compartido con interfaz y capacidades por plataforma; autoridad: JetBrains.
- [MDN, «Progressive web apps»](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps) — aplicaciones web instalables y sus capacidades; autoridad: Mozilla.

---

[↑ Glosario](../../README.md) · [← Frontera de validación](./frontera-de-validacion.md) · [Fronteras entre modelos →](./fronteras-entre-modelos.md)
