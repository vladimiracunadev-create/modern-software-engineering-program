# Ruta crítica

[↑ Glosario](../../README.md) · [← Ruta canónica](./ruta-canonica.md) · [Ruta vertical →](./ruta-vertical.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Camino de spans que determina la latencia total de una petición.

Definición de trabajo de [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md): Cadena más larga de recursos dependientes que decide el tiempo hasta la primera pintura.
- En [SE-370 — Costos y operación de plataformas de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md): Camino de dependencias más largo; fija el tiempo de entrega.
- En [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md): Cadena de dependencias de mayor duración; fija el mínimo de tiempo con cualquier número de trabajadores.

## Por qué importa

En [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), el tema «Ruta crítica» importa porque optimizar fuera de ella no mejora la petición.

En [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), el tema «Ruta crítica» importa porque solo importa lo que está en la cadena más larga; lo demás no cambia el total.

En [SE-370 — Costos y operación de plataformas de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), el tema «Ruta crítica» importa porque fija la hora de entrega.

## Cómo funciona

Según [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), en la sección «Ruta crítica»:

En una traza con ramas paralelas, la latencia de la petición no es la suma de los spans sino el camino más largo desde la entrada hasta la salida: la **ruta crítica**. Un span fuera de ella puede acelerarse sin que la petición cambie, porque la rama paralela que la domina sigue tardando lo mismo. La identificación es mecánica: en cada nodo con hijos paralelos, el hijo cuya duración es la mayor pertenece a la ruta; en uno con hijos secuenciales, todos pertenecen. El ahorro de optimizar un span fuera de la ruta es cero hasta que alcanza al de la rama competidora, y la ganancia de optimizar uno dentro de ella tiene un tope cuando otra rama pasa a dominar.

Según [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), en la sección «Ruta crítica»:

El navegador no puede pintar hasta tener el HTML y los recursos que bloquean el renderizado (hojas de estilo, scripts síncronos); y hay recursos que solo se descubren al procesar otros (una fuente que declara el CSS, unos datos que pide el JavaScript). La **ruta crítica** es la cadena más larga de dependencias: acortar cualquier otra no cambia el tiempo total. Se acorta con menos bytes en la cadena, con menos eslabones (incluir lo necesario en el primer HTML) y con pistas que adelantan el inicio de un recurso (`preload`).

## Ejemplo

Ejemplo de [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) (sección «Preguntas frecuentes»):

Se puede, y a veces funciona, pero en uno de cada cinco casos de este experimento el span más largo no cambiaba la latencia. La ruta crítica es la que dice si el esfuerzo va a servir.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una traza está completa pero la mejora no llega** — causa: se optimizó un span fuera de la ruta crítica. Corrección: calcular la ruta crítica antes de elegir. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))
- **La mejora no se nota en el móvil** — causa: optimización fuera de la ruta crítica. Corrección: medir la cadena y actuar sobre su eslabón más largo. ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En una traza con ramas paralelas, la latencia de la petición no es la suma de los spans sino el camino más largo desde la entrada hasta la salida: la **ruta crítica**. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))
- Traslada el análisis a otro flujo (una compra con pago externo o un trabajo programado): inventaría las fronteras, calcula la fracción esperada de trazas completas y calcula la ruta crítica de una ejecución. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))

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
