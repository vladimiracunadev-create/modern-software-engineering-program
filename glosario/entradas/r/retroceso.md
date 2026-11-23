# Retroceso

[↑ Glosario](../../README.md) · [← Retroalimentación específica](./retroalimentacion-especifica.md) · [Retroceso catastrófico →](./retroceso-catastrofico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Operación que restituye el sistema al estado previo a la inyección y cuyo tiempo se mide.

Definición de trabajo de [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md): Vuelta a una versión anterior ya validada.
- En [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md): Vuelta a la versión anterior tras detectar un defecto.
- En [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md): Vuelta a la versión anterior tras detectar un problema.
- En [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md): Conjunto de acciones que devuelve el sistema al estado anterior a un paso.

## Por qué importa

En [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), el tema «Reversión» importa porque abortar no sirve si no se sabe volver.

En [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), el tema «Rollback» importa porque limita el daño y debe estar ensayado.

En [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md), el tema «Reversión» importa porque sin versión anterior, una actualización mala es irreversible.

## Cómo funciona

Según [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md):

Abortar significa que algo deja de inyectar. Si la falla es una regla de red, un proceso detenido o una configuración modificada, la reversión es una operación que puede fallar: la regla no se elimina, el proceso no reinicia, la configuración vieja ya no existe. Por eso la reversión se **prueba antes**, se ejecuta con un solo comando, no depende del componente que se está dañando y se mide: ¿cuánto tarda en volver el indicador a su banda? En la API de entregas, una falla inyectada con un proxy se revierte quitando el tóxico; una caída de proceso, reiniciando el servicio; una pérdida de capacidad, devolviendo los hilos.

Según [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md):

Supón, como caso hipotético y no como medición, que el equipo escribe la especificación del experimento «almacenamiento con 20 % de errores»: radio de 2 % del tráfico durante 10 minutos, aborto si el grupo experimental falla más de 50 % en 10 s o si el servicio global baja de 99,5 % en 30 s, reversión «quitar la regla del proxy» probada la víspera con un tiempo de 4 s, responsable la guardia de la API, ventana de martes a jueves de 10:00 a 16:00 y nunca en una semana de cierre de plazo.

## Ejemplo

Ejemplo de [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético y no como medición, que el equipo escribe la especificación del experimento «almacenamiento con 20 % de errores»: radio de 2 % del tráfico durante 10 minutos, aborto si el grupo experimental falla más de 50 % en 10 s o si el servicio global baja de 99,5 % en 30 s, reversión «quitar la regla del proxy» probada la víspera con un tiempo de 4 s, responsable la guardia de la API, ventana de martes a jueves de 10:00 a 16:00 y nunca en una semana de cierre de plazo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La falla no se detiene al abortar** — causa: reversión no probada o dependiente del componente dañado. Corrección: probar la reversión antes y ejecutarla desde fuera. ([SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si la falla es una regla de red, un proceso detenido o una configuración modificada, la reversión es una operación que puede fallar: la regla no se elimina, el proceso no reinicia, la configuración vieja ya no existe. ([SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md))
- **Blue-green** mantiene dos entornos completos; el tráfico se dirige a uno, y el otro recibe la versión nueva y se prueba sin usuarios; el cambio es instantáneo y el retroceso, volver a dirigir el tráfico, pero el cambio expone a todas las personas a la vez y el coste es doble infraestructura. ([SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Imagen](../i/imagen.md).
- **Ver también:** [Conjunto](../c/conjunto.md), [Estado](../e/estado.md), [Inyección](../i/inyeccion.md), [Operación](../o/operacion.md), [Cambio mínimo](../c/cambio-minimo.md), [Estado inicial](../e/estado-inicial.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (107 clases más lo mencionan; las que más):

[SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md), [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Reversión», «reversión».

**Forma en inglés o término técnico original:** «rollback».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Release Engineering](https://sre.google/sre-book/release-engineering/) — entrega y retroceso; autoridad: Google.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — minimizar el radio de explosión; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Netflix: «ChAP: Chaos Automation Platform»](https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f) — tamaño de experimento, control y experimento, interruptor del experimento; autoridad: blog de ingeniería de Netflix.
- [AWS FIS: stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html) — condiciones de parada basadas en alarmas; autoridad: documentación de Amazon Web Services.
- [Chaos Mesh: Define the Scope of Chaos Experiments](https://chaos-mesh.org/docs/define-chaos-experiment-scope/) — selectores y radio de explosión; autoridad: documentación del proyecto Chaos Mesh.

---

[↑ Glosario](../../README.md) · [← Retroalimentación específica](./retroalimentacion-especifica.md) · [Retroceso catastrófico →](./retroceso-catastrofico.md)
