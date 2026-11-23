# Condición de fallo

[↑ Glosario](../../README.md) · [← Condición de carrera](./condicion-de-carrera.md) · [Condición de parada →](./condicion-de-parada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Efecto de un fallo de una función sobre la aeronave y sus ocupantes, clasificado por gravedad.

Definición de trabajo de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md).

## Por qué importa

En [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), el tema «Gravedad de la condición de fallo» importa porque fija el nivel de rigor de cada elemento.

## Cómo funciona

Según [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

En la práctica aeronáutica, cada función del sistema tiene condiciones de fallo clasificadas por su efecto en la aeronave y las personas (desde «sin efecto» hasta «catastrófica»). De esa clasificación sale un nivel de garantía de desarrollo para el software y el hardware que implementan la función: a mayor gravedad, más objetivos de verificación, más independencia entre quien desarrolla y quien verifica y mayor profundidad de la cobertura estructural. La evaluación que fija esos niveles la hacen los procesos de sistema y de seguridad (ARP4754A y ARP4761), no el equipo de software. El número exacto de objetivos por nivel pertenece a la norma de pago y no se reproduce.

Según [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

Es la contraparte para hardware electrónico complejo (lógica programable, circuitos integrados específicos): también deriva el rigor de la gravedad de la condición de fallo y exige requisitos, verificación y trazabilidad, con las particularidades del hardware.

## Ejemplo

Ejemplo de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) (sección «Preguntas frecuentes»):

Es la contraparte para hardware electrónico complejo (lógica programable, circuitos integrados específicos): también deriva el rigor de la gravedad de la condición de fallo y exige requisitos, verificación y trazabilidad, con las particularidades del hardware.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En la práctica aeronáutica, cada función del sistema tiene condiciones de fallo clasificadas por su efecto en la aeronave y las personas (desde «sin efecto» hasta «catastrófica»). ([SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Función](../f/funcion.md), [Gravedad](../g/gravedad.md), [Sobre](../s/sobre.md), [Calificación de herramienta](./calificacion-de-herramienta.md), [Cobertura estructural](./cobertura-estructural.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-058](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Condición de carrera](./condicion-de-carrera.md) · [Condición de parada →](./condicion-de-parada.md)
