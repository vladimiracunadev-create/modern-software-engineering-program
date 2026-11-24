# Capacidad de mejora

[↑ Glosario](../../README.md) · [← Capacidad](./capacidad.md) · [Capacidad opcional →](./capacidad-opcional.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

La **capacidad de mejora** es el tiempo que el equipo dedica en cada ciclo a cambiar su propio sistema de trabajo ([SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md)). Es un presupuesto, como la capacidad de entrega, pero aplicado a mejorar el proceso en lugar de producir producto.

## Por qué importa

Limita cuántas acciones de mejora se terminan, sin importar cuántas se acuerden. Mejorar el proceso compite con entregar producto: cada hora dedicada a una cosa no se dedica a la otra. Cambia lo que se hace en una retrospectiva: acordar menos acciones, pero terminarlas, en lugar de producir una lista larga que nadie cumple.

## Cómo funciona

[SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md) lo muestra con una cuenta simple: un equipo con **dos días de capacidad de mejora por sprint** termina, como máximo, unas ocho o nueve acciones de costo medio de dos días y medio en un trimestre (12 sprints × 2 días = 24 días; 24 / 2,5 ≈ 9,6 acciones, y menos si hay interrupciones), **sin importar cuántas acuerde**. Acordar más no acelera: crea un inventario de pendientes.

Ese inventario tiene un costo propio: erosiona la credibilidad de la retrospectiva («¿para qué proponer si no se hace?»). La gente deja de proponer o de creer que algo cambiará. La política sana es **acordar tan pocas acciones como la capacidad permita terminar**, y declarar la capacidad. Es la misma lógica de un límite de trabajo en curso: una cola sin límite crece sin avanzar.

La clase propone un fragmento de código que calcula cuántas acciones caben, y pide predecir cuántas acciones de 2,5 días de costo medio se terminan en 12 sprints con 2 días por sprint. La capacidad se complementa con un criterio de **evaluación**: cada acción se evalúa con una señal y un plazo fijado de antemano según el tamaño del efecto esperado; declarar fracaso a las dos semanas, con muestra insuficiente, es otro error que [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md) señala.

## Ejemplo

El equipo de la plataforma tiene 2 días de capacidad de mejora por sprint. En una retrospectiva surgen diez ideas. Con la cuenta anterior, caben unas nueve acciones en todo el trimestre; si el equipo acuerda las diez en un solo sprint, ocho quedarán pendientes tres meses. En cambio, acuerda una o dos, las termina y evalúa antes de añadir. (Cuenta ilustrativa basada en las cifras de [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md).)

## Errores y confusiones comunes

- **Las acciones pendientes crecen cada sprint**: se acuerdan más de las que caben; corrección: limitar a la capacidad y evaluar antes de agregar.
- **Declarar fracaso a las dos semanas**: muestra insuficiente; corrección: fijar de antemano el plazo de evaluación.
- **No reservar tiempo**: la mejora «si sobra tiempo» nunca ocurre.
- **Confundirla con la capacidad de entrega.**

## Límites y cuándo no aplica

La cuenta supone costos medios estables y capacidad constante; en la práctica ambos varían. No dice qué mejoras valen la pena, solo cuántas caben. En un equipo con deuda urgente, la capacidad puede ampliarse temporalmente, pero entonces debe declararse y acotarse.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ciclo](./ciclo.md), [Trabajo](../t/trabajo.md), [Intervención sobre el sistema](../i/intervencion-sobre-el-sistema.md), [Mirada repetida](../m/mirada-repetida.md), [Potencia](../p/potencia.md), [Retrospectiva](../r/retrospectiva.md).
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

[↑ Glosario](../../README.md) · [← Capacidad](./capacidad.md) · [Capacidad opcional →](./capacidad-opcional.md)
