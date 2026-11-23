# Evento de telemetría

[↑ Glosario](../../README.md) · [← Evento de dominio](./evento-de-dominio.md) · [Evento de uso →](./evento-de-uso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Registro estructurado de algo que ocurrió en el producto, con campos permitidos y justificados.

Definición de trabajo de [SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md).

## Por qué importa

La clase donde se define, [SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), existe con este propósito: la clase existe para decidir qué se mide de las personas, con qué permiso y con qué cuidado, de modo que la telemetría de producto aporte decisiones sin recoger más de lo necesario, sin identificar a nadie por combinación de campos y sin depender de un permiso que el código no respeta.

## Cómo funciona

[SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md):

En la plataforma, `telemetry-plan.md` contiene una fila por evento (nombre, momento, campos permitidos, decisión que informa, retención, base de recolección) y un diagrama de estados del consentimiento. El contrato es que todo campo nuevo exige una decisión asociada y una medición de unicidad antes de entrar al esquema, y que la puerta se prueba con mutantes en integración continua. Esa estructura permite que otra persona vea qué se recoge, por qué y con qué control.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md)) son:

- **Se envían eventos de personas que rechazaron** — causa: la puerta trata «desconocido» como «concedido» o no vacía el búfer. Corrección: probar los tres estados y las transiciones con mutantes.
- **El conjunto «anónimo» permite reidentificar** — causa: campos acumulados sin medir la unicidad. Corrección: medir grupos y fijar k mínimo; engrosar la granularidad.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se recogió ningún dato real, no se consultó a un especialista legal y los campos, las probabilidades de consentir y los once mutantes son supuestos o elecciones del autor. La siguiente clase usa estos eventos para estudiar experimentos, sesgos y causalidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro estructurado](../r/registro-estructurado.md), [Producto](../p/producto.md), [Registro](../r/registro.md), [Consentimiento](../c/consentimiento.md), [K-anonimato](../k/k-anonimato.md), [Minimización](../m/minimizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [EDPB: Guidelines 05/2020 on consent under Regulation 2016/679](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en) — condiciones del consentimiento válido y su retirada; autoridad: Comité Europeo de Protección de Datos.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — vocabulario para gestionar riesgo de privacidad; autoridad: NIST.
- [k-Anonymity: A Model for Protecting Privacy (Sweeney, 2002)](https://epic.org/wp-content/uploads/privacy/reidentification/Sweeney_Article.pdf) — la reidentificación por combinación de atributos y el criterio de k-anonimato; autoridad: artículo académico (International Journal on Uncertainty, Fuzziness and Knowledge-based Systems).
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — medir lo necesario para mejorar un servicio; autoridad: Government Digital Service.
- [Python: `collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) — conteo de grupos para la unicidad.

---

[↑ Glosario](../../README.md) · [← Evento de dominio](./evento-de-dominio.md) · [Evento de uso →](./evento-de-uso.md)
