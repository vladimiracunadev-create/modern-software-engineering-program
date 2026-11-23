# Frontera de módulo

[↑ Glosario](../../README.md) · [← Frontera de equipo](./frontera-de-equipo.md) · [Frontera de Pareto →](./frontera-de-pareto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Límite que una regla comprobable impide cruzar salvo por la API pública.

Definición de trabajo de [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md).

## Por qué importa

La clase donde se define, [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), existe con este propósito: la clase existe para que compares tres formas de agrupar los mismos componentes (un monolito, un monolito modular y servicios) por lo que cuesta cruzar cada frontera y por lo que garantiza cada una sobre la consistencia, y no por la moda de cada época.

## Cómo funciona

[SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md):

El equipo de la plataforma mantiene el sistema como monolito modular y añade al CI un comprobador de fronteras que falla si un módulo importa algo que no sea la `api` de otro, y otro que prohíbe `importlib` y `__import__` con nombres de módulos internos. Mide que la operación «calificar» hace 14 llamadas entre `notas` y `entregas` y decide que, si algún día se separan, esas dos son una sola frontera mal puesta: primero deberían fusionarse o reducir las llamadas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md)) son:

- **Un cambio pequeño exige probar todo el sistema** — causa: monolito sin fronteras internas. Corrección: imponer API públicas y un comprobador de importaciones.
- **La latencia sube al separar un módulo** — causa: la frontera cruza muchas llamadas por operación. Corrección: medir llamadas por operación y fusionar o engrosar la API.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con Windows y Ubuntu (WSL2): dos simulaciones con datos sintéticos, idénticas en ambos sistemas, y una medición real de tiempos en bucle local cuyos valores difieren entre ejecuciones y sistemas y se dan como rangos. No se midió ninguna red, TLS, balanceador ni servicio real; las tasas de fallo y el proyecto sintético del comprobador son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [API pública](../a/api-publica.md), [Límite](../l/limite.md), [Regla](../r/regla.md), [Monolito](../m/monolito.md), [Monolito modular](../m/monolito-modular.md), [Saga](../s/saga.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler y Lewis, «Microservices»](https://martinfowler.com/articles/microservices.html) — características, ventajas y costes de los servicios; autoridad: Martin Fowler y James Lewis.
- [Fowler, «MonolithFirst»](https://martinfowler.com/bliki/MonolithFirst.html) — empezar por un monolito modular; autoridad: Martin Fowler.
- [Parnas, «On the criteria to be used in decomposing systems into modules» (CACM, 1972)](https://doi.org/10.1145/361598.361623) — ocultación de información como criterio de descomposición; autoridad: Communications of the ACM.
- [García-Molina y Salem, «Sagas» (SIGMOD, 1987)](https://doi.org/10.1145/38713.38742) — transacciones largas con compensación; autoridad: ACM SIGMOD.
- [Microsoft Learn, patrón Saga](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) — coordinación de transacciones distribuidas con compensaciones; autoridad: Microsoft.

---

[↑ Glosario](../../README.md) · [← Frontera de equipo](./frontera-de-equipo.md) · [Frontera de Pareto →](./frontera-de-pareto.md)
