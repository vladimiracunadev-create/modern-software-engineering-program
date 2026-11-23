# Sesgo de participación

[↑ Glosario](../../README.md) · [← Sesgo de lo ya sabido](./sesgo-de-lo-ya-sabido.md) · [Sesgo de posición →](./sesgo-de-posicion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Diferencia entre quienes aceptan ser medidos y la población que se quiere conocer.

Definición de trabajo de [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md).

## Por qué importa

En [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), el tema «Sesgo de participación» importa porque quien acepta no es representativo de quien no.

## Cómo funciona

[SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md):

`notas` es opt-in: la primera ejecución no envía nada y, si la persona lo pide, `notas telemetria activar` muestra la lista exacta de eventos y campos antes de aceptar; `notas telemetria estado` y `desactivar` están siempre disponibles. Los eventos son tres: arranque (versión mayor, sistema, código de resultado), subcomando usado (su nombre, sin argumentos) y error (código, sin mensaje). La compuerta respeta `DO_NOT_TRACK=1` y los entornos de CI aunque haya consentimiento.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md)) son:

- **La telemetría está activa sin que nadie la pidiera** — causa: valor por defecto activado. Corrección: opt-in explícito y estado visible.
- **Se envían datos con `DO_NOT_TRACK=1`** — causa: la compuerta ignora las señales del entorno. Corrección: respetar las señales y probarlas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Las poblaciones, los atributos, las tasas de aceptación y de adopción y los seis defectos son supuestos del autor; no se midió ninguna telemetría real, no se evaluó el cumplimiento de ninguna norma y no se pidió consentimiento a nadie. La siguiente clase aplica todo lo anterior al endurecimiento de una automatización frágil.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Consentimiento](../c/consentimiento.md), [Identificabilidad](../i/identificabilidad.md), [K-anonimato](../k/k-anonimato.md), [Mínimo necesario](../m/minimo-necesario.md), [Opt-in](../o/opt-in.md), [Privacidad diferencial](../p/privacidad-diferencial.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Sweeney, «k-anonymity: a model for protecting privacy» (2002)](https://doi.org/10.1142/S0218488502001648) — k-anonimato; autoridad: International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems.
- [Eckersley, «How Unique Is Your Web Browser?» (2010)](https://doi.org/10.1007/978-3-642-14527-8_1) — unicidad de configuraciones de navegador; autoridad: PETS 2010.
- [Dwork y Roth, «The Algorithmic Foundations of Differential Privacy»](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf) — privacidad diferencial y mecanismo de Laplace; autoridad: Foundations and Trends in Theoretical Computer Science.
- [EDPB: Directrices 05/2020 sobre el consentimiento](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en) — condiciones del consentimiento válido; autoridad: Comité Europeo de Protección de Datos.
- [Console Do Not Track](https://consoledonottrack.com/) — convención `DO_NOT_TRACK`; autoridad: proyecto comunitario.

---

[↑ Glosario](../../README.md) · [← Sesgo de lo ya sabido](./sesgo-de-lo-ya-sabido.md) · [Sesgo de posición →](./sesgo-de-posicion.md)
