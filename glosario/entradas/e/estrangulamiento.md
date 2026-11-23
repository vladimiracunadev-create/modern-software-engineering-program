# Estrangulamiento

[↑ Glosario](../../README.md) · [← Estimación puntual](./estimacion-puntual.md) · [Estrategia →](./estrategia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Reemplazo de un sistema desviando su funcionalidad, rebanada por rebanada, hacia uno nuevo detrás de una fachada.

Definición de trabajo de [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md): Reemplazo gradual de un sistema desviando su funcionalidad a uno nuevo a través de una fachada.

## Por qué importa

En [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), el tema «Estrangulamiento y rebanadas» importa porque reduce el daño por paso y permite revertir.

## Cómo funciona

Según [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md):

Cuando la sustitución es interna al programa y no se puede interponer una fachada de red: una biblioteca, un algoritmo, un acceso a datos. El estrangulamiento actúa en las fronteras del sistema; la rama por abstracción, dentro.

Según [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md):

El patrón del estrangulamiento coloca delante del sistema antiguo una fachada que, para cada petición, decide si la atiende el antiguo o el nuevo. Se empieza con todo al antiguo y se desvían rutas, inquilinos o tipos de operación hacia el nuevo, una a una. Cuando el último tramo se ha movido y el antiguo no recibe tráfico, se retira. El nombre viene de una planta que crece alrededor de un árbol hasta reemplazarlo. La fachada es la pieza clave y es también un componente compartido (como el enrutador de `SE-344`): debe ser simple, versionada y con un camino de retroceso inmediato.

## Ejemplo

Ejemplo de [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) (sección «Preguntas frecuentes»):

Cuando la sustitución es interna al programa y no se puede interponer una fachada de red: una biblioteca, un algoritmo, un acceso a datos. El estrangulamiento actúa en las fronteras del sistema; la rama por abstracción, dentro.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md)) son:

- **El corte se pospone una y otra vez** — causa: el paso es demasiado grande para verificarse. Corrección: dividir en rebanadas con retroceso independiente.
- **La sombra no muestra diferencias y hay error en producción** — causa: la ventana no incluye el tráfico raro. Corrección: elegir la ventana por calendario y reproducir tráfico grabado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se migró ningún sistema ni se comparó tráfico real; el 10 % de rutas con regresión, los dos días hasta decidir, la eficacia de la sombra, el calendario de cuatro semanas de cierre y las anomalías de los 5 000 registros son construcciones del autor, y el modelo supone rutas de igual peso.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fachada](../f/fachada.md), [Rebanada](../r/rebanada.md), [Reemplazo](../r/reemplazo.md), [Abstracción de rama](../a/abstraccion-de-rama.md), [Capa anticorrupción](../c/capa-anticorrupcion.md), [Comparación en sombra](../c/comparacion-en-sombra.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «strangler fig».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «StranglerFigApplication»](https://martinfowler.com/bliki/StranglerFigApplication.html) — el patrón de estrangulamiento; autoridad: autor del texto.
- [Microsoft Azure Architecture Center: Strangler Fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) — fachada y migración incremental; autoridad: documentación de Microsoft.
- [Microsoft Azure Architecture Center: Anti-corruption Layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — traducción entre modelos; autoridad: documentación de Microsoft.
- [Fowler, «DarkLaunching»](https://martinfowler.com/bliki/DarkLaunching.html) — ejecutar con tráfico real sin exponer el resultado; autoridad: autor del texto.
- [Fowler, «FeatureToggle»](https://martinfowler.com/bliki/FeatureToggle.html) — banderas de funcionalidad y su costo; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Estimación puntual](./estimacion-puntual.md) · [Estrategia →](./estrategia.md)
