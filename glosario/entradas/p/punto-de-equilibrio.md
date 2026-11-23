# Punto de equilibrio

[↑ Glosario](../../README.md) · [← Punto de entrada](./punto-de-entrada.md) · [Punto de equilibrio de costo →](./punto-de-equilibrio-de-costo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Nivel de actividad en que los ingresos igualan a los costos.

Definición de trabajo de [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md).

## Por qué importa

La clase donde se define, [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md), existe con este propósito: la clase existe para que traduzcas una decisión técnica a dinero y tiempo sin engañarte con una sola cifra.

## Cómo funciona

Según [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md):

Un servicio con costo fijo mensual F, costo variable v por persona usuaria y precio p por persona tiene un **punto de equilibrio** en F/(p − v) personas. Por debajo, cada persona adicional reduce la pérdida; por encima, genera margen. El equilibrio es útil como pregunta («¿cuántas personas hacen falta?») y peligroso como promesa, porque el crecimiento es incierto: dos servicios con el mismo equilibrio y distinta base inicial tienen probabilidades muy distintas de alcanzarlo en un año. El costo por usuario también orienta decisiones técnicas: un costo variable alto por persona (una consulta cara) cambia el precio mínimo, y un costo fijo alto empuja a buscar escala.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo estima el costo de demora de sus doce iniciativas con quienes las piden: la que evita una multa semanal vale 40 por semana y dura dos semanas; otra, un rediseño de portal, vale 6 por semana y dura ocho. La razón entre costo y duración (20 y 0,75) coloca la primera al inicio, aunque la dirección había pedido el rediseño primero.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md)) son:

- **Se ejecutan primero las iniciativas más antiguas** — causa: orden por llegada. Corrección: ordenar por costo de demora entre duración.
- **Se elige el proyecto de mayor suma** — causa: no se descontó el tiempo. Corrección: reportar VAN a varias tasas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md)) son: Las definiciones son operativas para el equipo de plataforma educativa. No convierten términos con una historia más amplia en sinónimos, no son asesoría contable y deben contrastarse con las fuentes primarias enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ninguna inversión ni se aplicó ninguna norma contable a un caso real; los costos de demora, las duraciones, los flujos, las tasas, los costos de infraestructura y el crecimiento son construcciones del autor, y el modelo supone iniciativas independientes y flujos conocidos con certeza.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-536](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actividad](../a/actividad.md), [Costo](../c/costo.md), [CAPEX y OPEX](../c/capex-y-opex.md), [Costo de demora](../c/costo-de-demora.md), [Tasa interna de retorno](../t/tasa-interna-de-retorno.md), [Valor presente neto](../v/valor-presente-neto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), [SE-598](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Smith, «Various optimizers for single-stage production»](https://doi.org/10.1002/nav.3800030106) — orden óptimo por razón entre peso y duración; autoridad: Naval Research Logistics Quarterly.
- [Reinertsen, *The Principles of Product Development Flow*](https://openlibrary.org/isbn/9781935401001) — costo de demora como base económica; autoridad: libro de referencia.
- [SAFe, WSJF](https://scaledagileframework.com/wsjf/) — priorización por costo de demora entre tamaño; autoridad: Scaled Agile.
- [Brealey, Myers y Allen, *Principles of Corporate Finance*](https://openlibrary.org/isbn/9781260013900) — valor presente neto y retorno; autoridad: libro de texto de referencia.
- [FinOps Framework](https://www.finops.org/framework/) — gestión del costo de la nube; autoridad: FinOps Foundation.

---

[↑ Glosario](../../README.md) · [← Punto de entrada](./punto-de-entrada.md) · [Punto de equilibrio de costo →](./punto-de-equilibrio-de-costo.md)
