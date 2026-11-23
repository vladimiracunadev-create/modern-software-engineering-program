# Rama por abstracción

[↑ Glosario](../../README.md) · [← Raíz de confianza](./raiz-de-confianza.md) · [Rama protegida →](./rama-protegida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Técnica que introduce una abstracción para cambiar una implementación sin ramas largas, con una bandera que elige la implementación.

Definición de trabajo de [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md).

## Por qué importa

En [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), el tema «Rama por abstracción» importa porque cambia una implementación sin ramas largas ni congelar el desarrollo.

## Cómo funciona

Según [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), en la sección «Rama por abstracción»:

Cuando el código a reemplazar está dentro del mismo programa, la técnica equivalente es la **rama por abstracción**: se introduce una abstracción (una interfaz o una función) sobre el comportamiento a cambiar; el código existente pasa a ser una implementación; se desarrolla la nueva implementación detrás de la misma abstracción, con una bandera que decide cuál se usa; se cambia el valor de la bandera gradualmente y, cuando la nueva es la única en uso, se retira la antigua y la bandera. La técnica evita ramas largas de control de versiones, que acumulan conflictos, y permite integrar con frecuencia código que aún no está activo. La abstracción es una costura de objeto (`SE-519`) y la prueba de caracterización es la que garantiza que ambas implementaciones se comportan igual.

## Ejemplo

Ejemplo de [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) (sección «Preguntas frecuentes»):

Cuando la sustitución es interna al programa y no se puede interponer una fachada de red: una biblioteca, un algoritmo, un acceso a datos. El estrangulamiento actúa en las fronteras del sistema; la rama por abstracción, dentro.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md)) son:

- **El corte se pospone una y otra vez** — causa: el paso es demasiado grande para verificarse. Corrección: dividir en rebanadas con retroceso independiente.
- **La sombra no muestra diferencias y hay error en producción** — causa: la ventana no incluye el tráfico raro. Corrección: elegir la ventana por calendario y reproducir tráfico grabado.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se migró ningún sistema ni se comparó tráfico real; el 10 % de rutas con regresión, los dos días hasta decidir, la eficacia de la sombra, el calendario de cuatro semanas de cierre y las anomalías de los 5 000 registros son construcciones del autor, y el modelo supone rutas de igual peso.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Abstracción](../a/abstraccion.md), [Capa anticorrupción](../c/capa-anticorrupcion.md), [Comparación en sombra](../c/comparacion-en-sombra.md), [Estrangulamiento](../e/estrangulamiento.md), [Rebanada](./rebanada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «StranglerFigApplication»](https://martinfowler.com/bliki/StranglerFigApplication.html) — el patrón de estrangulamiento; autoridad: autor del texto.
- [Microsoft Azure Architecture Center: Strangler Fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) — fachada y migración incremental; autoridad: documentación de Microsoft.
- [Microsoft Azure Architecture Center: Anti-corruption Layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — traducción entre modelos; autoridad: documentación de Microsoft.
- [Fowler, «DarkLaunching»](https://martinfowler.com/bliki/DarkLaunching.html) — ejecutar con tráfico real sin exponer el resultado; autoridad: autor del texto.
- [Fowler, «FeatureToggle»](https://martinfowler.com/bliki/FeatureToggle.html) — banderas de funcionalidad y su costo; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Raíz de confianza](./raiz-de-confianza.md) · [Rama protegida →](./rama-protegida.md)
