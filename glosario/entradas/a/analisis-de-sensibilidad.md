# Análisis de sensibilidad

[↑ Glosario](../../README.md) · [← Análisis de impacto](./analisis-de-impacto.md) · [Análisis de sensibilidad global →](./analisis-de-sensibilidad-global.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

El **análisis de sensibilidad** estudia cuánto cambia el resultado de un modelo al variar uno de sus parámetros. [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) es la clase donde se define, aplicado a la decisión de reescribir o evolucionar. El programa lo usa con matices: en [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) es repetir una decisión variando sus supuestos para medir con qué frecuencia el resultado se mantiene; en [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) es estudiar cuánto deben moverse pesos o supuestos para que otra alternativa gane.

## Por qué importa

Convierte una discusión de preferencias en una pregunta medible. [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) existe para que la pregunta «¿reescribimos o seguimos?» no se decida por cansancio, por entusiasmo tecnológico o por quien habla más fuerte, sino con un modelo de costos explícito, con incertidumbre y con las condiciones en que la respuesta cambia. El análisis dice *qué parámetro vale la pena medir antes de comprometerse*.

## Cómo funciona

Un modelo con siete parámetros inciertos no es igual de sensible a todos. La versión más simple, según [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

1. Se toma cada parámetro por separado y se mueve entre un valor bajo y uno alto.
2. Los demás conservan sus distribuciones.
3. Se mide cuánto cambia la diferencia entre las opciones.

El parámetro con mayor recorrido domina la decisión. La utilidad es práctica: en vez de discutir qué opción es mejor, se discute cuánto costará construir, pregunta que se responde con una estimación mejor, un prototipo o el historial. Si el parámetro dominante no puede medirse hasta empezar, la decisión debe diseñarse para poder abandonarse cuando se mida.

En [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) la variante mueve los pesos de una matriz de decisión; en [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), repite la decisión muchas veces con supuestos variados y cuenta cuántas veces gana la misma opción.

## Ejemplo

Escenario hipotético de [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), sin datos reales. El equipo toma de su historial que la última reescritura costó 1,8 veces su presupuesto y duró 1,5 veces lo previsto, mide un crecimiento del costo del módulo de 9 % anual y cuenta las peticiones que tocaron el módulo antiguo. Al simular, el análisis muestra que el costo de construir domina; deciden hacer un prototipo de una rebanada ([SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md)) para medirlo antes de comprometer el resto.

## Errores y confusiones comunes

- **Aprobar una reescritura con un solo número** ([SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md)): una estimación puntual oculta qué parámetro la sostiene.
- **Mover todos los parámetros a la vez** y no poder atribuir el efecto.
- **Confundirlo con un intervalo de confianza:** el análisis no mide el error de estimación, mide la influencia de cada entrada.

## Límites y cuándo no aplica

Mover un parámetro cada vez ignora interacciones entre parámetros. El resultado es tan bueno como el modelo: si falta un costo, ninguna variación lo revela. Los datos de [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) son un escenario construido para la clase. Y cuando la decisión es barata o reversible, el análisis cuesta más que equivocarse.

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
