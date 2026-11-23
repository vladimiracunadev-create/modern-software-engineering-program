# Cobertura estructural

[↑ Glosario](../../README.md) · [← Cobertura del verificador](./cobertura-del-verificador.md) · [Cobertura por pares →](./cobertura-por-pares.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Medida de qué partes del código ejecutaron las pruebas.

Definición de trabajo de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md).

## Por qué importa

En [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), el tema «Cobertura estructural» importa porque encuentra lo que las pruebas no ejercitaron.

## Cómo funciona

Según [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

En la práctica aeronáutica, cada función del sistema tiene condiciones de fallo clasificadas por su efecto en la aeronave y las personas (desde «sin efecto» hasta «catastrófica»). De esa clasificación sale un nivel de garantía de desarrollo para el software y el hardware que implementan la función: a mayor gravedad, más objetivos de verificación, más independencia entre quien desarrolla y quien verifica y mayor profundidad de la cobertura estructural. La evaluación que fija esos niveles la hacen los procesos de sistema y de seguridad (ARP4754A y ARP4761), no el equipo de software. El número exacto de objetivos por nivel pertenece a la norma de pago y no se reproduce.

## Ejemplo

Ejemplo de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) (sección «Ejemplo mínimo»):

Las dos pruebas «de requisitos» pasan y la sentencia de la puerta trasera no se ejecuta. Es el hallazgo que la cobertura estructural existe para producir.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- De esa clasificación sale un nivel de garantía de desarrollo para el software y el hardware que implementan la función: a mayor gravedad, más objetivos de verificación, más independencia entre quien desarrolla y quien verifica y mayor profundidad de la cobertura estructural. ([SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](../m/medida.md), [Calificación de herramienta](./calificacion-de-herramienta.md), [Código muerto](./codigo-muerto.md), [Código no previsto](./codigo-no-previsto.md), [Condición de fallo](./condicion-de-fallo.md), [Prueba basada en requisitos](../p/prueba-basada-en-requisitos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cobertura del verificador](./cobertura-del-verificador.md) · [Cobertura por pares →](./cobertura-por-pares.md)
