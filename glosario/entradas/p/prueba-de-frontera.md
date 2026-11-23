# Prueba de frontera

[↑ Glosario](../../README.md) · [← Prueba de estrés](./prueba-de-estres.md) · [Prueba de integración →](./prueba-de-integracion.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Caso de ejemplo en el borde de una regla (medianoche, límites de rango).

Definición de trabajo de [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md).

## Por qué importa

La clase donde se define, [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md), existe con este propósito: el taller existe para que practiques lo que hace valiosa a una persona de datos en una emergencia: encontrar por qué un número está mal y arreglarlo sin romper otra cosa.

## Cómo funciona

Según [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md):

Con ocho comprobaciones (conciliar filas con el origen, conciliar importe, unicidad, frescura, repetir la ejecución, prueba de frontera de día, esquema de entrada, importe medio por día en banda), D1 solo lo ve repetir la ejecución. D2 lo ven la prueba de frontera y el importe medio. D3, las dos conciliaciones. D4 y D5, las conciliaciones y el importe medio. D6, solo la conciliación exacta de importe. D7, la conciliación de importe, el esquema de entrada y el importe medio. D8, las dos conciliaciones. La conciliación del importe ve siete de los ocho; la unicidad y la frescura no ven ninguno, y es correcto: no corresponden a estos defectos, y un fallo de otra clase (un duplicado de clave, una carga atrasada) sí las dispararía.

Según [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md):

El equipo de *Avisos* recibe la queja de finanzas y sigue el método. Reproduce con un día de datos y una réplica pequeña. Concilia filas y importe de cada capa contra el origen: las filas del hecho son un 2 % menos que las del origen, y el importe, un 3 % menos. Las filas faltantes son pedidos sin cliente (unión interna). Corrige solo eso y vuelve a medir: ahora sobran filas el lunes, por una dimensión sin vigencia. Corrige la unión y la diferencia baja a cero filas pero el importe por día sigue sin coincidir: los pedidos de medianoche están en el día equivocado. Cada paso lo registra con el antes y el después.

## Ejemplo

Ejemplo de [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) (sección «Ejemplo mínimo»):

La prueba de frontera que habría atrapado el defecto D2:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con ocho comprobaciones (conciliar filas con el origen, conciliar importe, unicidad, frescura, repetir la ejecución, prueba de frontera de día, esquema de entrada, importe medio por día en banda), D1 solo lo ve repetir la ejecución. ([SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Borde](../b/borde.md), [Límite](../l/limite.md), [Rango](../r/rango.md), [Regla](../r/regla.md), [Acotar](../a/acotar.md), [Conciliación](../c/conciliacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md), [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Prueba de estrés](./prueba-de-estres.md) · [Prueba de integración →](./prueba-de-integracion.md)
