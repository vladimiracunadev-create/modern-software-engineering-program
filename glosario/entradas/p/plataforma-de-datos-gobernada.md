# Plataforma de datos gobernada

[↑ Glosario](../../README.md) · [← Plataforma como producto](./plataforma-como-producto.md) · [Plataforma de dos lados →](./plataforma-de-dos-lados.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Plataforma donde cada conjunto tiene dueño, contrato, comprobaciones, retención y dependencias verificables.

Definición de trabajo de [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md).

## Por qué importa

La clase donde se define, [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), existe con este propósito: el proyecto existe para que integres todo lo de la parte en una plataforma pequeña que se pueda ejecutar, auditar y romper a propósito: tres capas de datos (cruda, intermedia y analítica), un registro de metadatos con dueño, contrato, comprobaciones, retención y dependencias de cada conjunto, y un control de siete reglas que decide si algo se publica.

## Cómo funciona

[SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md)) son: Los tres conjuntos, las siete reglas y las diez mutaciones son construcciones del autor, y la matriz mide qué familia de defectos ve cada regla, no la tasa de defectos de ninguna plataforma; el control solo corre sobre SQLite y no cubre catálogo, captura de linaje en ejecución, claves gestionadas ni costo. Que el control detecte 9 de 10 no dice que detecte 9 de 10 de los defectos reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Contrato](../c/contrato.md), [Dependencia](../d/dependencia.md), [Plataforma](./plataforma.md), [Cobertura](../c/cobertura.md), [Control](../c/control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Plataforma como producto](./plataforma-como-producto.md) · [Plataforma de dos lados →](./plataforma-de-dos-lados.md)
