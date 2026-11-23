# Telemetría

[↑ Glosario](../../README.md) · [← TEE](./tee.md) · [Temperatura →](./temperatura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Datos de uso o de funcionamiento enviados por una herramienta a quien la mantiene.

Definición de trabajo de [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md).

## Por qué importa

La clase donde se define, [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), existe con este propósito: la clase existe para decidir qué se mide de una herramienta que corre en equipos ajenos, con qué consentimiento y cuánto se puede aprender sin identificar a nadie: una compuerta de consentimiento que se pueda probar, un conjunto mínimo de datos y una lectura honesta de lo que quienes aceptan no representan.

## Cómo funciona

Según [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md):

La telemetría empieza por la pregunta, no por el dato: «¿qué subcomandos se usan?» pide un contador por subcomando, no el historial de comandos con argumentos; «¿arranca bien el lanzamiento?» pide un evento de arranque con la versión y un código de resultado, no la ruta de trabajo. Un inventario de eventos con tres columnas —pregunta, campos, quién decide qué hacer con la respuesta— elimina de entrada la mitad de lo que se pensaba recoger. Y cada campo tiene una vida: cuánto se conserva y quién puede verlo.

Según [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md):

`notas` es opt-in: la primera ejecución no envía nada y, si la persona lo pide, `notas telemetria activar` muestra la lista exacta de eventos y campos antes de aceptar; `notas telemetria estado` y `desactivar` están siempre disponibles. Los eventos son tres: arranque (versión mayor, sistema, código de resultado), subcomando usado (su nombre, sin argumentos) y error (código, sin mensaje). La compuerta respeta `DO_NOT_TRACK=1` y los entornos de CI aunque haya consentimiento. Los datos se agregan por semana, se descartan los grupos con menos de 20 instalaciones y el informe lleva siempre la nota «solo instalaciones con telemetría activada». Una suite de ocho escenarios con un servidor local cuenta las peticiones y falla si aparece una ruta o un usuario en la carga.

## Ejemplo

Ejemplo de [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) (sección «Ejemplo profesional»):

`notas` es opt-in: la primera ejecución no envía nada y, si la persona lo pide, `notas telemetria activar` muestra la lista exacta de eventos y campos antes de aceptar; `notas telemetria estado` y `desactivar` están siempre disponibles. Los eventos son tres: arranque (versión mayor, sistema, código de resultado), subcomando usado (su nombre, sin argumentos) y error (código, sin mensaje). La compuerta respeta `DO_NOT_TRACK=1` y los entornos de CI aunque haya consentimiento. Los datos se agregan por semana, se descartan los grupos con menos de 20 instalaciones y el informe lleva siempre la nota «solo instalaciones con telemetría activada».

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La telemetría está activa sin que nadie la pidiera** — causa: valor por defecto activado. Corrección: opt-in explícito y estado visible. ([SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La telemetría empieza por la pregunta, no por el dato: ([SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Consentimiento](../c/consentimiento.md), [Identificabilidad](../i/identificabilidad.md), [K-anonimato](../k/k-anonimato.md), [Mínimo necesario](../m/minimo-necesario.md), [Opt-in](../o/opt-in.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (41 clases más lo mencionan; las que más):

[SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md), [SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Command Line Interface Guidelines](https://clig.dev/) — recomendaciones sobre telemetría en herramientas; autoridad: guía de autores.
- [Sweeney, «k-anonymity: a model for protecting privacy» (2002)](https://doi.org/10.1142/S0218488502001648) — k-anonimato; autoridad: International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems.
- [Eckersley, «How Unique Is Your Web Browser?» (2010)](https://doi.org/10.1007/978-3-642-14527-8_1) — unicidad de configuraciones de navegador; autoridad: PETS 2010.
- [Dwork y Roth, «The Algorithmic Foundations of Differential Privacy»](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf) — privacidad diferencial y mecanismo de Laplace; autoridad: Foundations and Trends in Theoretical Computer Science.
- [EDPB: Directrices 05/2020 sobre el consentimiento](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en) — condiciones del consentimiento válido; autoridad: Comité Europeo de Protección de Datos.

---

[↑ Glosario](../../README.md) · [← TEE](./tee.md) · [Temperatura →](./temperatura.md)
