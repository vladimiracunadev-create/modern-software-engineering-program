# Frontera entre capas

[↑ Glosario](../../README.md) · [← Frontera de validación](./frontera-de-validacion.md) · [Fronteras entre modelos →](./fronteras-entre-modelos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

La **frontera entre capas** es el punto donde el código compartido se comunica con el de una plataforma, y donde cada cruce serializa, copia y cambia de contexto. Es el sentido de [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) (nativo, híbrido, web wrapper y cross-platform). No es la frontera arquitectónica genérica entre módulos, sino la costura concreta entre, por ejemplo, la capa de lógica multiplataforma y las interfaces nativas del sistema.

## Por qué importa

Cruzar de código compartido a código de plataforma cuesta *por cruce*, no solo por dato. Dos diseños con los mismos datos pueden diferir mucho si uno cruza mil veces con mensajes pequeños y el otro una con un mensaje grueso. Es la parte del diseño cuyo costo más se subestima cuando se elige un enfoque de construcción.

## Cómo funciona

Los enfoques con capa compartida y capa de plataforma tienen esta frontera. Cada cruce:

1. **Serializa** los datos a una forma que ambos lados entienden.
2. **Copia** los bytes entre espacios de memoria o entornos.
3. **Cambia de contexto** de ejecución (otro hilo, otro motor, otro runtime).

El costo por cruce es en gran medida fijo, de modo que cuando se cruza mucho y con mensajes pequeños, el costo domina. La regla práctica de [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) es agrupar el trabajo en el lado donde ocurre y cruzar con mensajes gruesos y poco frecuentes, y *medir en el marco concreto antes de confiar en la regla*. Por eso la clase pide un prototipo de la frontera más sensible, es decir, la que cruza más veces por segundo.

## Ejemplo

El equipo del cliente de entregas documenta ([SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md)) un prototipo de la frontera más sensible con su medición. Ilustración propia: dibujar una lista animada elemento a elemento, enviando cada posición del desplazamiento por la frontera, produce miles de cruces por segundo; calcular la animación completa en el lado de la plataforma y enviar solo el estado final produce uno.

## Errores y confusiones comunes

- **Cruzar la frontera en un bucle,** un elemento por mensaje.
- **Aceptar la tabla de decisión que elige la opción del autor:** los pesos se escogieron conociendo el ganador deseado; la corrección es fijar pesos antes de puntuar y mostrar sensibilidad ([SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md)).
- **Suponer que el costo es el mismo en todo marco:** depende de cada uno, por eso se mide.
- **Confundirla con el costo de red,** que es otra frontera con otras propiedades.

## Límites y cuándo no aplica

No existe en el enfoque nativo puro, donde todo el código está de un lado (aunque hay otras fronteras, como llamadas al sistema). Y en una aplicación que cruza poco (formularios estáticos), el costo es irrelevante. La regla de agrupar tiene excepciones cuando la latencia de un mensaje grueso resulta inaceptable.

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
