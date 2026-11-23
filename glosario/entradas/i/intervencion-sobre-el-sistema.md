# Intervención sobre el sistema

[↑ Glosario](../../README.md) · [← Intervalo de Wilson](./intervalo-de-wilson.md) · [Introspección →](./introspeccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Cambio en una variable que determina el comportamiento del flujo (capacidad, lotes, variabilidad, límite de trabajo), no en el esfuerzo individual.

Definición de trabajo de [SE-190 — Retrospectivas y mejora del sistema de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md).

## Por qué importa

La clase donde se define, [SE-190 — Retrospectivas y mejora del sistema de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md), existe con este propósito: la clase existe para que una retrospectiva produzca cambios que se terminan y se pueden evaluar, y no una lista de buenos propósitos: sabrás elegir cuántas acciones acordar según tu capacidad de mejora, cuántos datos necesitas para saber si una mejora funcionó y qué intervenciones mueven el sistema y cuáles solo piden más esfuerzo.

## Cómo funciona

Según [SE-190 — Retrospectivas y mejora del sistema de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md):

Traslada el análisis a otra práctica de mejora (por ejemplo, la revisión posterior a un incidente): cambia la capacidad, el efecto esperado y la señal, y conserva el procedimiento de limitar acciones, fijar el plazo de evaluación y comparar intervenciones sobre el sistema. La transferencia está lograda cuando puedes explicar qué parte del método dependía del tipo de mejora y cuál no, no cuando el código se parece.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-190 — Retrospectivas y mejora del sistema de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md):

El equipo de la plataforma de entregas cambia su retrospectiva. Antes de la reunión, quien facilita prepara el tablero de `SE-189` y la hoja de acciones previas con su estado. La reunión dedica diez minutos a evaluar el cambio anterior con su señal, 20 a identificar qué parte del sistema produce el plazo largo (con la cola y la ley de Little como lentes), y 15 a elegir una acción, máximo dos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-190 — Retrospectivas y mejora del sistema de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md)) son:

- **Las acciones pendientes crecen cada sprint** — causa: se acuerdan más de las que caben. Corrección: limitar a la capacidad y evaluar antes de agregar.
- **Se declara fracaso a las dos semanas** — causa: muestra insuficiente para detectar la mejora. Corrección: fijar de antemano el plazo de evaluación según el tamaño del efecto.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-190 — Retrospectivas y mejora del sistema de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se observó ninguna retrospectiva ni se evaluó un cambio real: la capacidad de mejora, el beneficio por acción, el efecto del 15 %, la dispersión y la cola de un servidor son construcciones del autor, y la prueba de rangos se implementó con aproximación normal.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Flujo](../f/flujo.md), [Límite](../l/limite.md), [Lote](../l/lote.md), [Capacidad de mejora](../c/capacidad-de-mejora.md), [Mirada repetida](../m/mirada-repetida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-190 — Retrospectivas y mejora del sistema de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — la retrospectiva como evento de inspección y adaptación; autoridad: Scrum.org y Scrum Inc. (autores de la guía).
- [Principios del Manifiesto Ágil](https://agilemanifesto.org/principles.html) — reflexión periódica sobre cómo ser más efectivos; autoridad: autores del manifiesto.
- [Edmondson, «Psychological safety and learning behavior in work teams» (Administrative Science Quarterly, 1999)](https://doi.org/10.2307/2666999) — seguridad psicológica y aprendizaje; autoridad: Administrative Science Quarterly.
- [Mann y Whitney, «On a test of whether one of two random variables is stochastically larger than the other» (Annals of Mathematical Statistics, 1947)](https://doi.org/10.1214/aoms/1177730491) — prueba de rangos; autoridad: Annals of Mathematical Statistics.
- [Little, «A proof for the queuing formula: L = λW» (Operations Research, 1961)](https://doi.org/10.1287/opre.9.3.383) — base de las intervenciones sobre el flujo; autoridad: Operations Research.

---

[↑ Glosario](../../README.md) · [← Intervalo de Wilson](./intervalo-de-wilson.md) · [Introspección →](./introspeccion.md)
