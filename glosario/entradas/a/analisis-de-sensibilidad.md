# Análisis de sensibilidad

[↑ Glosario](../../README.md) · [← Análisis de impacto](./analisis-de-impacto.md) · [Análisis de sensibilidad global →](./analisis-de-sensibilidad-global.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Estudio de cuánto cambia el resultado de un modelo al variar uno de sus parámetros.

Definición de trabajo de [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md): Repetición de una decisión variando sus supuestos para medir con qué frecuencia el resultado se mantiene.
- En [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md): Estudio de cuánto cambian los pesos o los supuestos para que otra alternativa gane.

## Por qué importa

La clase donde se define, [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), existe con este propósito: la clase existe para que la pregunta «¿reescribimos o seguimos con esto?» deje de decidirse por cansancio, por entusiasmo por una tecnología o por quien habla más fuerte, y se decida con un modelo de costos explícito, con incertidumbre y con las condiciones en que la respuesta cambia.

## Cómo funciona

Según [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

Cuando un modelo tiene siete parámetros inciertos, no todos pesan lo mismo en el resultado. El análisis de sensibilidad más simple mueve un parámetro cada vez entre un valor bajo y uno alto, deja los demás con sus distribuciones y mide cuánto cambia la diferencia entre las opciones. El parámetro con mayor recorrido es el que domina la decisión y el que merece medirse antes de comprometerse. La utilidad es práctica: en lugar de discutir qué opción es mejor, se discute cuánto costará construir, y esa pregunta se puede responder con una estimación mejor, con un prototipo o con el historial de proyectos previos. Si el parámetro dominante no se puede medir hasta empezar, la decisión debe diseñarse para poder abandonarla cuando se mida.

Según [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo no discute las dos propuestas: las convierte en parámetros. Del historial de la empresa obtiene que la última reescritura costó 1,8 veces su presupuesto y duró 1,5 veces lo previsto; mide el crecimiento del costo del módulo en los últimos tres años (un 9 % anual); revisa cuántas peticiones modificaron el módulo antiguo en el último año para estimar la deriva. Con eso ejecuta la simulación: el análisis de sensibilidad dice que el costo de construir domina, así que decide hacer un prototipo de una rebanada (`SE-521`) para medirlo antes de comprometer el resto.

## Ejemplo

Ejemplo de [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo no discute las dos propuestas: las convierte en parámetros. Del historial de la empresa obtiene que la última reescritura costó 1,8 veces su presupuesto y duró 1,5 veces lo previsto; mide el crecimiento del costo del módulo en los últimos tres años (un 9 % anual); revisa cuántas peticiones modificaron el módulo antiguo en el último año para estimar la deriva. Con eso ejecuta la simulación: el análisis de sensibilidad dice que el costo de construir domina, así que decide hacer un prototipo de una rebanada (`SE-521`) para medirlo antes de comprometer el resto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md)) son:

- **Se aprueba una reescritura con un solo número** — causa: falta incertidumbre y términos ocultos. Corrección: modelar con distribuciones y todos los términos.
- **El costo real duplica el presupuesto** — causa: no se presupuestó la deriva ni el legado paralelo. Corrección: añadir esos términos y medir la deriva.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El análisis de sensibilidad más simple mueve un parámetro cada vez entre un valor bajo y uno alto, deja los demás con sus distribuciones y mide cuánto cambia la diferencia entre las opciones. ([SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Parámetro](../p/parametro.md), [Repetición](../r/repeticion.md), [Resultado](../r/resultado.md), [ADR](./adr.md), [Capacidad opcional](../c/capacidad-opcional.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spolsky, «Things You Should Never Do, Part I»](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) — argumento contra reescribir desde cero; autoridad: ensayo de un autor reconocido, de opinión.
- [Brooks, «No Silver Bullet»](https://doi.org/10.1109/MC.1987.1663532) — complejidad esencial y accidental; autoridad: IEEE Computer, 1987.
- [Lehman, «Programs, life cycles, and laws of software evolution»](https://doi.org/10.1109/PROC.1980.11805) — evolución de sistemas en uso; autoridad: Proceedings of the IEEE, 1980.
- [Fowler, «TechnicalDebt»](https://martinfowler.com/bliki/TechnicalDebt.html) — principal e intereses; autoridad: autor del texto.
- [Flutter, «Architectural overview»](https://docs.flutter.dev/resources/architectural-overview) — capas de un marco multiplataforma con interfaz propia; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Análisis de impacto](./analisis-de-impacto.md) · [Análisis de sensibilidad global →](./analisis-de-sensibilidad-global.md)
