# Ruta crítica

[↑ Glosario](../../README.md) · [← Ruta canónica](./ruta-canonica.md) · [Ruta vertical →](./ruta-vertical.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

La **ruta crítica** es el camino más largo de pasos dependientes que determina el tiempo total. El programa la usa en cuatro contextos con el mismo núcleo: en [SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) (trazas distribuidas), el camino de *spans* que determina la latencia total de una petición; en [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) (rendimiento web), la cadena más larga de recursos dependientes que decide el tiempo hasta la primera pintura; en [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), el camino de dependencias más largo en datos, que fija el tiempo de entrega; y en [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), la cadena de dependencias de mayor duración, que fija el mínimo de tiempo con cualquier número de trabajadores.

## Por qué importa

Solo importa lo que está en la cadena más larga; lo demás no cambia el total. Optimizar fuera de la ruta crítica no mejora la petición ni la entrega. Es la razón por la que medir antes de optimizar es una regla de trabajo, no un consejo.

## Cómo funciona

[SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md): en una traza con ramas paralelas, la latencia de la petición no es la suma de los spans sino el camino más largo desde la entrada hasta la salida. La identificación es mecánica:

- En un nodo con hijos **paralelos**, el hijo de mayor duración pertenece a la ruta.
- En un nodo con hijos **secuenciales**, todos pertenecen.

Consecuencias:

- Acelerar un span fuera de la ruta no cambia nada, porque la rama que domina tarda lo mismo. El ahorro es cero hasta que alcanza a la rama competidora.
- Acelerar uno dentro de la ruta ayuda, pero con un tope: cuando otra rama pasa a dominar, la ganancia termina.

En [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), la ruta crítica del plan de tareas fija el mínimo de tiempo con cualquier número de trabajadores: añadir personas no acorta lo que depende de una cadena secuencial.

## Ejemplo

Ilustración numérica propia: una petición llama en paralelo a A (120 ms) y B (80 ms), y luego a C (50 ms). La latencia es 120 + 50 = 170 ms; la ruta crítica es A → C. Reducir B de 80 a 40 ms no cambia nada. Reducir A a 90 ms baja el total a 140 ms; pero si A baja de 80 ms, B pasa a dominar y la mejora se detiene.

## Errores y confusiones comunes

- **Sumar los spans en paralelo** como si fueran secuenciales.
- **Optimizar el span más lento sin comprobar que esté en la ruta.**
- **Pensar que más trabajadores acortan siempre** un plan ([SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md)).
- **Confundirla con el camino más frecuente:** la ruta crítica es la más larga, no la más usada.

## Límites y cuándo no aplica

La ruta crítica cambia entre ejecuciones (una rama que hoy es corta puede ser larga mañana); conviene mirar muchas trazas. Con ramas de duración similar, varias son casi críticas. Y ignora recursos compartidos que alargan ramas paralelas por competencia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Latencia](../l/latencia.md), [Recurso](./recurso.md), [Span](../s/span.md), [Atribución de costos](../a/atribucion-de-costos.md), [Byte](../b/byte.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-370 — Costos y operación de plataformas de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.
- [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MDN: ruta crítica de renderizado](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Critical_rendering_path) — pasos hasta la primera pintura; autoridad: MDN.
- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — formato y reglas de `traceparent`; autoridad: Recomendación del W3C.
- [OpenTelemetry: propagación de contexto](https://opentelemetry.io/docs/concepts/context-propagation/) — cómo viaja el contexto; autoridad: proyecto OpenTelemetry (CNCF).
- [OpenTelemetry: muestreo](https://opentelemetry.io/docs/concepts/sampling/) — muestreo de cabeza y de cola; autoridad: proyecto OpenTelemetry (CNCF).
- [Sigelman et al., «Dapper»](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/) — trazado distribuido de bajo coste; autoridad: informe técnico de Google Research.

---

[↑ Glosario](../../README.md) · [← Ruta canónica](./ruta-canonica.md) · [Ruta vertical →](./ruta-vertical.md)
