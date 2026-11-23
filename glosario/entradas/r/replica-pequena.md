# Réplica pequeña

[↑ Glosario](../../README.md) · [← Réplica asíncrona](./replica-asincrona.md) · [Replicación →](./replicacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Muestra que reproduce el defecto con poco costo.

Definición de trabajo de [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md).

## Por qué importa

La clase donde se define, [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md), existe con este propósito: el taller existe para que practiques lo que hace valiosa a una persona de datos en una emergencia: encontrar por qué un número está mal y arreglarlo sin romper otra cosa.

## Cómo funciona

Según [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md):

El equipo de *Avisos* recibe la queja de finanzas y sigue el método. Reproduce con un día de datos y una réplica pequeña. Concilia filas y importe de cada capa contra el origen: las filas del hecho son un 2 % menos que las del origen, y el importe, un 3 % menos. Las filas faltantes son pedidos sin cliente (unión interna). Corrige solo eso y vuelve a medir: ahora sobran filas el lunes, por una dimensión sin vigencia. Corrige la unión y la diferencia baja a cero filas pero el importe por día sigue sin coincidir: los pedidos de medianoche están en el día equivocado. Cada paso lo registra con el antes y el después.

Según [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md):

**Diagnóstico paso a paso.** (1) Se mide el cociente filas del hecho entre filas del origen: 1,99. (2) Se cuenta cuántas veces aparece cada identificador de pedido en el hecho: dos. (3) Se revisa la unión con la dimensión de clientes: el cliente tiene dos versiones y no se filtra por vigencia. (4) Se prueba la unión corregida sobre la réplica pequeña: las filas coinciden.

## Ejemplo

Ejemplo de [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* recibe la queja de finanzas y sigue el método. Reproduce con un día de datos y una réplica pequeña. Concilia filas y importe de cada capa contra el origen: las filas del hecho son un 2 % menos que las del origen, y el importe, un 3 % menos. Las filas faltantes son pedidos sin cliente (unión interna). Corrige solo eso y vuelve a medir: ahora sobran filas el lunes, por una dimensión sin vigencia. Corrige la unión y la diferencia baja a cero filas pero el importe por día sigue sin coincidir: los pedidos de medianoche están en el día equivocado.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md)) son: Los pedidos, los defectos, las comprobaciones y el orden de corrección son construcciones del autor; los ocho defectos se probaron aislados y en conjunto con un único reintento. No se midió la frecuencia de ninguno de ellos en la práctica ni se evaluó ninguna herramienta. El siguiente paso, `SE-372`, integra comprobaciones, contratos, linaje, privacidad y costo en una plataforma mínima con un control que decide si algo se publica.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Acotar](../a/acotar.md), [Conciliación](../c/conciliacion.md), [Defecto enmascarado](../d/defecto-enmascarado.md), [Importe en unidad mínima](../i/importe-en-unidad-minima.md), [Prueba de frontera](../p/prueba-de-frontera.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Réplica asíncrona](./replica-asincrona.md) · [Replicación →](./replicacion.md)
