# Deriva del alcance

[↑ Glosario](../../README.md) · [← Deriva de los datos](./deriva-de-los-datos.md) · [Deriva del contrato →](./deriva-del-contrato.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Crecimiento de lo que el sistema nuevo debe replicar porque el antiguo sigue cambiando durante la construcción.

Definición de trabajo de [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md).

## Por qué importa

La clase donde se define, [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), existe con este propósito: la clase existe para que la pregunta «¿reescribimos o seguimos con esto?» deje de decidirse por cansancio, por entusiasmo por una tecnología o por quien habla más fuerte, y se decida con un modelo de costos explícito, con incertidumbre y con las condiciones en que la respuesta cambia.

## Cómo funciona

Según [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

El presupuesto de una reescritura suele contener el costo de construir el sistema nuevo. Hay al menos cuatro términos más. Primero, el **costo de mantener el sistema antiguo durante la construcción**, que no se detiene: sigue habiendo incidencias, adaptaciones con fecha y peticiones. Segundo, la **deriva del alcance**: el sistema antiguo sigue cambiando, y el nuevo tiene que alcanzar un objetivo que se mueve; cuanto más dura la construcción, más cambios hay que replicar. Tercero, el **conocimiento incrustado**: las reglas sin documentar del sistema antiguo (los redondeos, los casos de borde, las correcciones acumuladas) se redescubren con errores en producción. Cuarto, el **riesgo de abandono**: una fracción de las reescrituras se cancela a mitad de camino, y entonces se ha gastado una parte del presupuesto sin obtener un sistema.

Según [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

Reproduce el fallo clásico de la clase: **una reescritura aprobada con el presupuesto de construcción solamente**. Calcula el costo efectivo con la deriva del alcance y compara con el presupuesto.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo no discute las dos propuestas: las convierte en parámetros. Del historial de la empresa obtiene que la última reescritura costó 1,8 veces su presupuesto y duró 1,5 veces lo previsto; mide el crecimiento del costo del módulo en los últimos tres años (un 9 % anual); revisa cuántas peticiones modificaron el módulo antiguo en el último año para estimar la deriva.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md)) son:

- **Se aprueba una reescritura con un solo número** — causa: falta incertidumbre y términos ocultos. Corrección: modelar con distribuciones y todos los términos.
- **El costo real duplica el presupuesto** — causa: no se presupuestó la deriva ni el legado paralelo. Corrección: añadir esos términos y medir la deriva.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con simulaciones sintéticas en Windows y Ubuntu (WSL2) con resultados idénticos. Todos los parámetros y distribuciones son construcciones del autor, el modelo ignora interacciones, riesgos de seguridad, costo de oportunidad, moral y rotación del equipo, y trata el sistema nuevo como un destino único y no como un conjunto de rebanadas. No se analizó ninguna reescritura real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Análisis de sensibilidad](../a/analisis-de-sensibilidad.md), [Costo acumulado](../c/costo-acumulado.md), [Criterio de abandono](../c/criterio-de-abandono.md), [Horizonte de equilibrio](../h/horizonte-de-equilibrio.md), [Sensibilidad](../s/sensibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spolsky, «Things You Should Never Do, Part I»](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) — argumento contra reescribir desde cero; autoridad: ensayo de un autor reconocido, de opinión.
- [Brooks, «No Silver Bullet»](https://doi.org/10.1109/MC.1987.1663532) — complejidad esencial y accidental; autoridad: IEEE Computer, 1987.
- [Lehman, «Programs, life cycles, and laws of software evolution»](https://doi.org/10.1109/PROC.1980.11805) — evolución de sistemas en uso; autoridad: Proceedings of the IEEE, 1980.
- [Fowler, «TechnicalDebt»](https://martinfowler.com/bliki/TechnicalDebt.html) — principal e intereses; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Deriva de los datos](./deriva-de-los-datos.md) · [Deriva del contrato →](./deriva-del-contrato.md)
