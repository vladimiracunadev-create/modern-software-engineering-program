# Tasa interna de retorno

[↑ Glosario](../../README.md) · [← Tasa de fallos de los cambios](./tasa-de-fallos-de-los-cambios.md) · [Tasa monótona →](./tasa-monotona.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Tasa de descuento que hace nulo el valor presente neto de un proyecto.

Definición de trabajo de [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md).

## Por qué importa

La clase donde se define, [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md), existe con este propósito: la clase existe para que traduzcas una decisión técnica a dinero y tiempo sin engañarte con una sola cifra.

## Cómo funciona

Según [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md):

Un peso que llega en cinco años vale menos que uno de hoy, porque podría haberse invertido (el costo de oportunidad). La **tasa de descuento** r convierte el flujo futuro F del año t en su valor presente F/(1+r)^t. El **valor presente neto** (VAN) suma los flujos descontados, incluida la inversión inicial negativa; un VAN positivo significa que el proyecto rinde más que la tasa exigida. La **tasa interna de retorno** (TIR) es la tasa que hace nulo el VAN. El **período de recuperación** cuenta cuántos años hacen falta para recuperar la inversión sin descontar.

Según [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo estima el costo de demora de sus doce iniciativas con quienes las piden: la que evita una multa semanal vale 40 por semana y dura dos semanas; otra, un rediseño de portal, vale 6 por semana y dura ocho. La razón entre costo y duración (20 y 0,75) coloca la primera al inicio, aunque la dirección había pedido el rediseño primero. Calcula el costo de la espera del orden por llegada frente al propuesto y lo presenta como rango, porque las estimaciones son inciertas.

## Ejemplo

Ejemplo de [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md) (sección «Ejemplo mínimo»):

Imprime `46.3` y `-7.9`: a una tasa del 10 % el proyecto vale 46,3; a una del 25 %, vale −7,9. El signo cambia porque los beneficios son tardíos: cuanto más se descuenta, menos pesan. La tasa interna de retorno está entre ambas. Registra versión de Python, comando y salida.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md)) son:

- **Se ejecutan primero las iniciativas más antiguas** — causa: orden por llegada. Corrección: ordenar por costo de demora entre duración.
- **Se elige el proyecto de mayor suma** — causa: no se descontó el tiempo. Corrección: reportar VAN a varias tasas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada medida responde una pregunta distinta, y ordenan los proyectos de modo diferente porque pesan el tiempo distinto: la recuperación ignora todo lo posterior; la TIR supone que los flujos intermedios se reinvierten a la misma tasa; el VAN depende de la tasa elegida. ([SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-536](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor presente neto](../v/valor-presente-neto.md), [Valor](../v/valor.md), [CAPEX y OPEX](../c/capex-y-opex.md), [Costo de demora](../c/costo-de-demora.md), [Punto de equilibrio](../p/punto-de-equilibrio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «TIR».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Smith, «Various optimizers for single-stage production»](https://doi.org/10.1002/nav.3800030106) — orden óptimo por razón entre peso y duración; autoridad: Naval Research Logistics Quarterly.
- [Reinertsen, *The Principles of Product Development Flow*](https://openlibrary.org/isbn/9781935401001) — costo de demora como base económica; autoridad: libro de referencia.
- [SAFe, WSJF](https://scaledagileframework.com/wsjf/) — priorización por costo de demora entre tamaño; autoridad: Scaled Agile.
- [Brealey, Myers y Allen, *Principles of Corporate Finance*](https://openlibrary.org/isbn/9781260013900) — valor presente neto y retorno; autoridad: libro de texto de referencia.
- [FinOps Framework](https://www.finops.org/framework/) — gestión del costo de la nube; autoridad: FinOps Foundation.

---

[↑ Glosario](../../README.md) · [← Tasa de fallos de los cambios](./tasa-de-fallos-de-los-cambios.md) · [Tasa monótona →](./tasa-monotona.md)
