# Condición

[↑ Glosario](../../README.md) · [← Concurrencia, paralelismo e intercalación](./concurrencia-paralelismo-e-intercalacion.md) · [Condición de aborto →](./condicion-de-aborto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Expresión interpretada para elegir control.

Definición de trabajo de [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md).

## Por qué importa

En [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), el tema «Condiciones» importa porque filtros y uniones deciden qué filas llegan.

## Cómo funciona

Según [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md):

El linaje de tablas dice «`mart_city` depende de `fact_sales`». El de columnas, «`mart_city.total_clp` se calcula desde `fact_sales.amount_clp`». El de condiciones añade «`fact_sales` solo contiene filas cuyo `status` no es `cancelled`». Cada nivel responde algo distinto: el primero, «qué se recalcula si cambia esta tabla» (`SE-364`); el segundo, «qué columnas ven esta columna»; el tercero, «qué filas llegan». La respuesta a «¿es seguro quitar esta columna?» necesita los tres.

Según [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md):

El equipo de *Avisos* quiere retirar tres columnas antiguas de la tabla de lecturas. Con el linaje de tablas, el catálogo dice que veinte activos dependen de ella, demasiado para revisar. Con linaje de columnas y condiciones, dos de las tres columnas no tienen consumidores y la tercera aparece en un filtro de un informe de finanzas. El equipo ejecuta la prueba de perturbación sobre la tercera en una copia: cambia cuatro columnas de salida de dos informes. Avisa a los dos dueños con la lista exacta, fija una fecha de retiro de seis semanas y retira las dos columnas sin consumidores esa misma semana. El catálogo registra la decisión y la fecha y comprueba que, al llegar la fecha, el uso en el registro de consultas sea cero.

## Ejemplo

Ejemplo de [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) (sección «Ejemplo mínimo»):

Aristas de valor y de condición en un solo `SELECT`:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El de condiciones añade «`fact_sales` solo contiene filas cuyo `status` no es `cancelled`». ([SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Control](./control.md), [Expresión](../e/expresion.md), [Arista de condición](../a/arista-de-condicion.md), [Arista de valor](../a/arista-de-valor.md), [Catálogo de datos](./catalogo-de-datos.md), [Contrato](./contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (336 clases más lo mencionan; las que más):

[SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md), [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Condiciones».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Concurrencia, paralelismo e intercalación](./concurrencia-paralelismo-e-intercalacion.md) · [Condición de aborto →](./condicion-de-aborto.md)
