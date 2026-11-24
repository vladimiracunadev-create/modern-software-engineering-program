# Retroceso

[↑ Glosario](../../README.md) · [← Retroalimentación específica](./retroalimentacion-especifica.md) · [Retroceso catastrófico →](./retroceso-catastrofico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

El **retroceso** (*rollback*) es el conjunto de acciones que devuelve el sistema al estado anterior a un paso ([SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md)). Según la clase, es la vuelta a la versión anterior tras detectar un defecto ([SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md), [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md)), a una versión anterior ya validada ([SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md)) o la operación que restituye el sistema al estado previo a la inyección de una falla y cuyo tiempo se mide ([SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md)). Tiene un sentido distinto en algoritmos (*backtracking*, retroceder ante un conflicto, como hace el resolvedor de [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md)); esta entrada trata el retroceso operativo.

## Por qué importa

Un cambio solo es seguro si se puede deshacer rápido. Cuánto tarda el retroceso acota el daño de un despliegue o de un experimento. Cambia lo que se exige antes de cambiar algo en producción: un camino de vuelta probado.

## Cómo funciona

[SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) (ingeniería del caos) lo trata con precisión: abortar un experimento significa que algo deja de inyectar; si la falla es una regla de red, un proceso detenido o una configuración modificada, el retroceso es una operación que **puede fallar**: la regla no se elimina, el proceso no reinicia, la configuración vieja ya no existe. Por eso el retroceso:

- se **prueba antes**;
- se ejecuta con **un solo comando**;
- **no depende** del componente que se está dañando;
- se **mide**: cuánto tarda en volver el indicador a su banda.

En despliegues ([SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md)), el *blue-green* mantiene dos entornos completos y el retroceso es redirigir el tráfico; pero el cambio expone a todas las personas a la vez y el costo es doble infraestructura. Otras estrategias (canario, bandera) trazan otros compromisos. En ML ([SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md)), retroceder es volver a un modelo ya validado.

## Ejemplo

[SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), como caso hipotético: la especificación del experimento «almacenamiento con 20 % de errores» define un radio de 2 % del tráfico durante 10 minutos, aborto si el grupo experimental falla más de 50 % en 10 s o si el servicio global baja de 99,5 % en 30 s, y reversión «quitar la regla del proxy», probada la víspera con un tiempo de 4 s.

```bash
./quitar_toxico.sh && ./verificar_indicador.sh --espera 10
```

## Errores y confusiones comunes

- **La falla no se detiene al abortar.** Causa: reversión no probada o dependiente del componente dañado; corrección: probar la reversión antes y ejecutarla desde fuera ([SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md)).
- **Suponer que siempre se puede retroceder.** Un cambio de esquema que borra columnas o una migración de datos pueden no ser reversibles.
- **Confundir retroceso con retiro.** El retroceso vuelve a un estado anterior; el retiro elimina una capacidad.

## Límites y cuándo no aplica

El retroceso solo restituye lo que el cambio tocó: los efectos externos (mensajes enviados, cobros) no se deshacen. Los datos escritos por la versión nueva pueden ser ilegibles para la anterior; por eso se prefieren cambios compatibles hacia atrás. Y un retroceso que nunca se ensayó es una esperanza.

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

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md), [Cloudflare](../../../casos/exito/cloudflare.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md).

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
