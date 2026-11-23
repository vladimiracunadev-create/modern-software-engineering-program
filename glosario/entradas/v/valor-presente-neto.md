# Valor presente neto

[↑ Glosario](../../README.md) · [← Valor presente con incertidumbre](./valor-presente-con-incertidumbre.md) · [Valor y esfuerzo →](./valor-y-esfuerzo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Suma de los flujos futuros descontados a una tasa, menos la inversión inicial.

Definición de trabajo de [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md): Suma de los flujos descontados a una tasa declarada; depende del juicio sobre la tasa.

## Por qué importa

La clase donde se define, [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md), existe con este propósito: la clase existe para que traduzcas una decisión técnica a dinero y tiempo sin engañarte con una sola cifra.

## Cómo funciona

Según [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md):

Un peso que llega en cinco años vale menos que uno de hoy, porque podría haberse invertido (el costo de oportunidad). La **tasa de descuento** r convierte el flujo futuro F del año t en su valor presente F/(1+r)^t. El **valor presente neto** (VAN) suma los flujos descontados, incluida la inversión inicial negativa; un VAN positivo significa que el proyecto rinde más que la tasa exigida. La **tasa interna de retorno** (TIR) es la tasa que hace nulo el VAN. El **período de recuperación** cuenta cuántos años hacen falta para recuperar la inversión sin descontar.

Según [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo estima el costo de demora de sus doce iniciativas con quienes las piden: la que evita una multa semanal vale 40 por semana y dura dos semanas; otra, un rediseño de portal, vale 6 por semana y dura ocho. La razón entre costo y duración (20 y 0,75) coloca la primera al inicio, aunque la dirección había pedido el rediseño primero. Calcula el costo de la espera del orden por llegada frente al propuesto y lo presenta como rango, porque las estimaciones son inciertas.

## Ejemplo

Ejemplo de [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el valor presente neto de un proyecto a dos tasas. Antes de ejecutarlo, predice si el signo cambia entre ambas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se elige el proyecto de mayor suma** — causa: no se descontó el tiempo. Corrección: reportar VAN a varias tasas. ([SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada medida responde una pregunta distinta, y ordenan los proyectos de modo diferente porque pesan el tiempo distinto: la recuperación ignora todo lo posterior; la TIR supone que los flujos intermedios se reinvierten a la misma tasa; el VAN depende de la tasa elegida. ([SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md))
- Calcula la suma sin descontar y el VAN a 20 % de los tres proyectos y compara los órdenes. ([SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Flujo](../f/flujo.md), [Sobre](../s/sobre.md), [CAPEX y OPEX](../c/capex-y-opex.md), [Costo de construir](../c/costo-de-construir.md), [Costo de demora](../c/costo-de-demora.md), [Costo de operar y mantener](../c/costo-de-operar-y-mantener.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «VAN».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Brealey, Myers y Allen, *Principles of Corporate Finance*](https://openlibrary.org/isbn/9781260013900) — valor presente neto y retorno; autoridad: libro de texto de referencia.
- [Smith, «Various optimizers for single-stage production»](https://doi.org/10.1002/nav.3800030106) — orden óptimo por razón entre peso y duración; autoridad: Naval Research Logistics Quarterly.
- [Reinertsen, *The Principles of Product Development Flow*](https://openlibrary.org/isbn/9781935401001) — costo de demora como base económica; autoridad: libro de referencia.
- [SAFe, WSJF](https://scaledagileframework.com/wsjf/) — priorización por costo de demora entre tamaño; autoridad: Scaled Agile.
- [FinOps Framework](https://www.finops.org/framework/) — gestión del costo de la nube; autoridad: FinOps Foundation.

---

[↑ Glosario](../../README.md) · [← Valor presente con incertidumbre](./valor-presente-con-incertidumbre.md) · [Valor y esfuerzo →](./valor-y-esfuerzo.md)
