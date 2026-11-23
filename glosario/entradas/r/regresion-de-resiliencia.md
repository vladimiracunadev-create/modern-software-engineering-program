# Regresión de resiliencia

[↑ Glosario](../../README.md) · [← Regresión a la media](./regresion-a-la-media.md) · [Reidentificación →](./reidentificacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Cambio que empeora la capacidad de resistir una falla sin romper ninguna prueba funcional.

Definición de trabajo de [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md).

## Por qué importa

En [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), el tema «Regresión de resiliencia» importa porque una protección que se retira sin que ninguna prueba falle no estaba protegida.

## Cómo funciona

Según [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md):

Una **regresión de resiliencia** es un cambio que empeora la capacidad del sistema de resistir una falla sin romper ninguna prueba funcional. Ocurre porque las pruebas funcionales verifican lo que el sistema hace cuando todo va bien, y la protección solo se ejerce cuando algo va mal. Netflix lo explica al motivar la automatización de ChAP: cualquier cambio en el entorno de producción cambia la resiliencia del sistema, y con cientos de despliegues diarios, la confianza en un resultado experimental disminuye pronto; antes de integrar los experimentos con el sistema de entrega, una vulnerabilidad podía identificarse, corregirse y volver a aparecer causando un incidente. La respuesta fue ejecutar los experimentos de forma continua como parte del camino hacia producción, que es la idea de esta clase:

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md):

Supón, como caso hipotético y no como medición, que el equipo de la API de entregas agrega a su pipeline una etapa de resiliencia con tres piezas. La lectura estática corre en cada commit y bloquea el cambio si falta alguna de cinco reglas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md)) son:

- **El pipeline aprueba un cambio que quita una protección** — causa: solo hay pruebas de camino feliz. Corrección: añadir una suite de fallas y reglas de configuración.
- **La suite falla al azar y se ignora** — causa: sin dobles de prueba ni reloj controlado. Corrección: aislar la suite, usar semillas y mayoría de ejecuciones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **regresión de resiliencia** es un cambio que empeora la capacidad del sistema de resistir una falla sin romper ninguna prueba funcional. ([SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Doble de prueba](../d/doble-de-prueba.md), [Falsa alarma](../f/falsa-alarma.md), [Lectura estática de la configuración](../l/lectura-estatica-de-la-configuracion.md), [Suite dinámica de fallas](../s/suite-dinamica-de-fallas.md), [Tapado](../t/tapado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Netflix: ChAP: Chaos Automation Platform](https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f) — integración con el sistema de entrega continua y regresiones de resiliencia; autoridad: blog de ingeniería de Netflix.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — automatizar y ejecutar de forma continua; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — límites de repetibilidad de las pruebas estadísticas; autoridad: libro de ingeniería de confiabilidad de Google.
- [AWS Well-Architected: Use failure injection to test resiliency](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_failure_injection_resiliency.html) — inyección de fallas en las pruebas; autoridad: documentación de Amazon Web Services.
- [Martin Fowler: Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html) — patrón del cortacircuitos; autoridad: boletín de ingeniería de software de Martin Fowler.

---

[↑ Glosario](../../README.md) · [← Regresión a la media](./regresion-a-la-media.md) · [Reidentificación →](./reidentificacion.md)
