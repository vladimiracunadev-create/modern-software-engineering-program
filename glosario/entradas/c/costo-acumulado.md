# Costo acumulado

[↑ Glosario](../../README.md) · [← Costo](./costo.md) · [Costo cognitivo y operativo →](./costo-cognitivo-y-operativo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Suma, durante un horizonte, de todos los costos de una opción (construcción, mantenimiento e inversiones) en las mismas unidades.

Definición de trabajo de [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md).

## Por qué importa

La clase donde se define, [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), existe con este propósito: la clase existe para que la pregunta «¿reescribimos o seguimos con esto?» deje de decidirse por cansancio, por entusiasmo por una tecnología o por quien habla más fuerte, y se decida con un modelo de costos explícito, con incertidumbre y con las condiciones en que la respuesta cambia.

## Cómo funciona

Según [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

El modelo mide el costo acumulado a diez años en unidades del costo anual actual de mantener el legado (1 = ese costo). El costo del legado crece a una tasa anual entre el 3 % y el 15 %. **Evolucionar** invierte 1,0 repartido en dos años y reduce después el crecimiento al 30 % de esa tasa.

Según [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** a mitad de la reescritura el costo acumulado supera lo presupuestado y el sistema nuevo no alcanza al antiguo. **Hipótesis rivales:** (a) el equipo es lento; (b) el alcance estaba mal estimado; (c) el sistema antiguo siguió cambiando y no se presupuestó replicarlo. **Prueba:** cuenta los cambios del sistema antiguo durante la construcción y súmalos como fracción del alcance; si son del orden del 15 % por año, el costo efectivo ya es 1,375 veces el presupuesto a 2,5 años. **Conclusión:** la deriva no estaba en el presupuesto. **Regresión:** añade a la plantilla de decisión los términos «mantener el legado», «deriva» y «probabilidad de abandono» como campos obligatorios.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo no discute las dos propuestas: las convierte en parámetros. Del historial de la empresa obtiene que la última reescritura costó 1,8 veces su presupuesto y duró 1,5 veces lo previsto; mide el crecimiento del costo del módulo en los últimos tres años (un 9 % anual); revisa cuántas peticiones modificaron el módulo antiguo en el último año para estimar la deriva.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md)) son:

- **Se aprueba una reescritura con un solo número** — causa: falta incertidumbre y términos ocultos. Corrección: modelar con distribuciones y todos los términos.
- **El costo real duplica el presupuesto** — causa: no se presupuestó la deriva ni el legado paralelo. Corrección: añadir esos términos y medir la deriva.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Síntoma:** a mitad de la reescritura el costo acumulado supera lo presupuestado y el sistema nuevo no alcanza al antiguo. ([SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](./costo.md), [Mantenimiento](../m/mantenimiento.md), [Opción](../o/opcion.md), [Análisis de sensibilidad](../a/analisis-de-sensibilidad.md), [Criterio de abandono](./criterio-de-abandono.md), [Deriva del alcance](../d/deriva-del-alcance.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spolsky, «Things You Should Never Do, Part I»](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) — argumento contra reescribir desde cero; autoridad: ensayo de un autor reconocido, de opinión.
- [Brooks, «No Silver Bullet»](https://doi.org/10.1109/MC.1987.1663532) — complejidad esencial y accidental; autoridad: IEEE Computer, 1987.
- [Lehman, «Programs, life cycles, and laws of software evolution»](https://doi.org/10.1109/PROC.1980.11805) — evolución de sistemas en uso; autoridad: Proceedings of the IEEE, 1980.
- [Fowler, «TechnicalDebt»](https://martinfowler.com/bliki/TechnicalDebt.html) — principal e intereses; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Costo](./costo.md) · [Costo cognitivo y operativo →](./costo-cognitivo-y-operativo.md)
