# Consentimiento

[↑ Glosario](../../README.md) · [← Consenso perezoso](./consenso-perezoso.md) · [Consentimiento informado →](./consentimiento-informado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Manifestación libre, específica, informada e inequívoca de una persona, retirable con facilidad.

Definición de trabajo de [SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md).

## Por qué importa

En [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), el tema «Consentimiento» importa porque debe ser una acción afirmativa, informada y revocable.

## Cómo funciona

Según [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md):

Un consentimiento válido es una acción afirmativa, específica e informada, y se puede retirar. Una casilla marcada de antemano, un silencio o «seguir usando» no lo son. En una herramienta de línea de comandos esto se traduce en **opt-in**: la telemetría está apagada hasta que la persona la activa explícitamente (`notas telemetria activar`), con un texto que dice qué se envía; se puede desactivar con la misma facilidad; y se respetan señales ajenas: la variable `DO_NOT_TRACK=1` y los entornos automáticos (integración continua) la apagan aunque haya consentimiento en un archivo de configuración. Todo esto es diseño, no asesoría jurídica.

Según [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md):

`notas` es opt-in: la primera ejecución no envía nada y, si la persona lo pide, `notas telemetria activar` muestra la lista exacta de eventos y campos antes de aceptar; `notas telemetria estado` y `desactivar` están siempre disponibles. Los eventos son tres: arranque (versión mayor, sistema, código de resultado), subcomando usado (su nombre, sin argumentos) y error (código, sin mensaje). La compuerta respeta `DO_NOT_TRACK=1` y los entornos de CI aunque haya consentimiento. Los datos se agregan por semana, se descartan los grupos con menos de 20 instalaciones y el informe lleva siempre la nota «solo instalaciones con telemetría activada». Una suite de ocho escenarios con un servidor local cuenta las peticiones y falla si aparece una ruta o un usuario en la carga.

## Ejemplo

Ejemplo de [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) (sección «Ejemplo profesional»):

`notas` es opt-in: la primera ejecución no envía nada y, si la persona lo pide, `notas telemetria activar` muestra la lista exacta de eventos y campos antes de aceptar; `notas telemetria estado` y `desactivar` están siempre disponibles. Los eventos son tres: arranque (versión mayor, sistema, código de resultado), subcomando usado (su nombre, sin argumentos) y error (código, sin mensaje). La compuerta respeta `DO_NOT_TRACK=1` y los entornos de CI aunque haya consentimiento. Los datos se agregan por semana, se descartan los grupos con menos de 20 instalaciones y el informe lleva siempre la nota «solo instalaciones con telemetría activada».

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La métrica de uso sube cuando baja el consentimiento** — causa: quedan quienes más usan. Corrección: informar la tasa de consentimiento y cautelar la comparación. ([SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una prueba que solo comprueba que «con consentimiento, se envía» deja pasar casi todos los defectos. ([SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md))
- Tendrías más datos y menos legitimidad: el silencio no es consentimiento, y las normas y las expectativas de quienes usan herramientas de línea de comandos van en sentido contrario. ([SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento de telemetría](../e/evento-de-telemetria.md), [Identificabilidad](../i/identificabilidad.md), [K-anonimato](../k/k-anonimato.md), [Minimización](../m/minimizacion.md), [Mínimo necesario](../m/minimo-necesario.md), [Opt-in](../o/opt-in.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (36 clases más lo mencionan; las que más):

[SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), [SE-009](../../../classes/part-00-ingenieria-de-software-como-profesion/se-009-sostenibilidad-inclusion-y-responsabilidad-social/README.md), [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md), [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [EDPB: Directrices 05/2020 sobre el consentimiento](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en) — condiciones del consentimiento válido; autoridad: Comité Europeo de Protección de Datos.
- [Sweeney, «k-anonymity: a model for protecting privacy» (2002)](https://doi.org/10.1142/S0218488502001648) — k-anonimato; autoridad: International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems.
- [Eckersley, «How Unique Is Your Web Browser?» (2010)](https://doi.org/10.1007/978-3-642-14527-8_1) — unicidad de configuraciones de navegador; autoridad: PETS 2010.
- [Dwork y Roth, «The Algorithmic Foundations of Differential Privacy»](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf) — privacidad diferencial y mecanismo de Laplace; autoridad: Foundations and Trends in Theoretical Computer Science.
- [Console Do Not Track](https://consoledonottrack.com/) — convención `DO_NOT_TRACK`; autoridad: proyecto comunitario.

---

[↑ Glosario](../../README.md) · [← Consenso perezoso](./consenso-perezoso.md) · [Consentimiento informado →](./consentimiento-informado.md)
