# Tapado

[↑ Glosario](../../README.md) · [← Tamaño y potencia](./tamano-y-potencia.md) · [Tarea →](./tarea.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Regresión que no se manifiesta porque otra protección la compensa.

Definición de trabajo de [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md).

## Por qué importa

La clase donde se define, [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), existe con este propósito: la clase trata el caos continuo: lo que se automatiza en el camino a producción y lo que se ejecuta de forma continua sobre el sistema en producción.

## Cómo funciona

[SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md):

Supón, como caso hipotético y no como medición, que el equipo de la API de entregas agrega a su pipeline una etapa de resiliencia con tres piezas. La lectura estática corre en cada commit y bloquea el cambio si falta alguna de cinco reglas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md)) son:

- **El pipeline aprueba un cambio que quita una protección** — causa: solo hay pruebas de camino feliz. Corrección: añadir una suite de fallas y reglas de configuración.
- **La suite falla al azar y se ignora** — causa: sin dobles de prueba ni reloj controlado. Corrección: aislar la suite, usar semillas y mayoría de ejecuciones.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md)) son: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se ejecutó ningún pipeline real; la configuración, las siete modificaciones, los cuatro escenarios, las ocho semillas y las reglas estáticas son construcciones del autor, las reglas se escribieron conociendo las regresiones y la suite se afinó con ellas, y la repetibilidad de la simulación no se traslada a un sistema real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regresión](../r/regresion.md), [Doble de prueba](../d/doble-de-prueba.md), [Falsa alarma](../f/falsa-alarma.md), [Lectura estática de la configuración](../l/lectura-estatica-de-la-configuracion.md), [Regresión de resiliencia](../r/regresion-de-resiliencia.md), [Suite dinámica de fallas](../s/suite-dinamica-de-fallas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md).

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

[↑ Glosario](../../README.md) · [← Tamaño y potencia](./tamano-y-potencia.md) · [Tarea →](./tarea.md)
