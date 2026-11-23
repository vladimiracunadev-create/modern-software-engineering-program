# Código no previsto

[↑ Glosario](../../README.md) · [← Código muerto](./codigo-muerto.md) · [Coeficiente de variación →](./coeficiente-de-variacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Código ejecutable que no corresponde a ningún requisito.

Definición de trabajo de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md).

## Por qué importa

La clase donde se define, [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), existe con este propósito: la clase existe para que entiendas cómo la aviación civil organiza la confianza en el software de a bordo y por qué su pieza más característica, la **cobertura estructural del código medida contra pruebas basadas en requisitos**, es una herramienta para encontrar lo que nadie pidió y no un número que alcanzar.

## Cómo funciona

Según [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

Hay tres explicaciones y cada una tiene su respuesta. **Falta una prueba**: el requisito existe y su prueba no ejercita esa rama; se escribe. **Falta un requisito**: la conducta es deseable y nadie la pidió; se deriva, se revisa con seguridad y se prueba. **Código muerto o no previsto**: no hay requisito y no debería haberlo; se elimina o se justifica por escrito (por ejemplo, programación defensiva que no se puede activar con las entradas posibles) con una revisión. El código no previsto es el que más importa: una orden de depuración que se activa con un valor mágico es una función que nadie evaluó, y en un sistema crítico una función no evaluada es un peligro.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El código no previsto es el que más importa: una orden de depuración que se activa con un valor mágico es una función que nadie evaluó, y en un sistema crítico una función no evaluada es un peligro. ([SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Calificación de herramienta](./calificacion-de-herramienta.md), [Cobertura estructural](./cobertura-estructural.md), [Código muerto](./codigo-muerto.md), [Condición de fallo](./condicion-de-fallo.md), [Prueba basada en requisitos](../p/prueba-basada-en-requisitos.md), [Requisito derivado](../r/requisito-derivado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Código muerto](./codigo-muerto.md) · [Coeficiente de variación →](./coeficiente-de-variacion.md)
