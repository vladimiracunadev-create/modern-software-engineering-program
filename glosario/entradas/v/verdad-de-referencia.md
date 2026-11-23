# Verdad de referencia

[↑ Glosario](../../README.md) · [← Ventana de reversión limpia](./ventana-de-reversion-limpia.md) · [Verde →](./verde.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Resultado correcto calculado de forma independiente.

Definición de trabajo de [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md).

## Por qué importa

En [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md), el tema «Verdad de referencia» importa porque sin ella no hay diagnóstico.

## Cómo funciona

Según [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md):

Toma un informe de tu organización cuyo número alguien haya puesto en duda. Escribe su verdad de referencia, concilia por capa hasta encontrar la primera diferencia y registra cada paso con su medida. Deja al final la comprobación que lo habría detectado el primer día.

## Ejemplo

Caso medido en la sección «El pipeline y la verdad de referencia» de [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md):

El pipeline lee 20 000 pedidos (identificador, cliente, marca de tiempo en UTC, importe y día de llegada), los carga en un hecho, los une con una dimensión de clientes con historia y calcula, por día local (UTC−3), el número de pedidos y el importe. La referencia calcula lo mismo directamente sobre los pedidos: 20 000 filas, un importe total de 912 729 905 y 15 días (de −1 a 13, por el desfase horario). Cualquier diferencia contra esa referencia es un defecto.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md)) son: Los pedidos, los defectos, las comprobaciones y el orden de corrección son construcciones del autor; los ocho defectos se probaron aislados y en conjunto con un único reintento. No se midió la frecuencia de ninguno de ellos en la práctica ni se evaluó ninguna herramienta. El siguiente paso, `SE-372`, integra comprobaciones, contratos, linaje, privacidad y costo en una plataforma mínima con un control que decide si algo se publica.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Acotar](../a/acotar.md), [Conciliación](../c/conciliacion.md), [Defecto enmascarado](../d/defecto-enmascarado.md), [Importe en unidad mínima](../i/importe-en-unidad-minima.md), [Prueba de frontera](../p/prueba-de-frontera.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Ventana de reversión limpia](./ventana-de-reversion-limpia.md) · [Verde →](./verde.md)
