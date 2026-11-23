# Defecto enmascarado

[↑ Glosario](../../README.md) · [← Defecto dormido](./defecto-dormido.md) · [Defecto latente →](./defecto-latente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Defecto cuyo efecto lo compensa otro.

Definición de trabajo de [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md).

## Por qué importa

La clase donde se define, [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md), existe con este propósito: el taller existe para que practiques lo que hace valiosa a una persona de datos en una emergencia: encontrar por qué un número está mal y arreglarlo sin romper otra cosa.

## Cómo funciona

Según [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md):

**Corrección.** Se añade la condición de vigencia a la unión, se agrega la prueba de unicidad del identificador de pedido al hecho y se registra la medida antes y después. La lección es que un error de filas de más tras corregir otros defectos no es un fallo de la corrección anterior sino un defecto enmascarado hasta entonces.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La lección es que un error de filas de más tras corregir otros defectos no es un fallo de la corrección anterior sino un defecto enmascarado hasta entonces. ([SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Acotar](../a/acotar.md), [Conciliación](../c/conciliacion.md), [Importe en unidad mínima](../i/importe-en-unidad-minima.md), [Prueba de frontera](../p/prueba-de-frontera.md), [Réplica pequeña](../r/replica-pequena.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Defecto dormido](./defecto-dormido.md) · [Defecto latente →](./defecto-latente.md)
