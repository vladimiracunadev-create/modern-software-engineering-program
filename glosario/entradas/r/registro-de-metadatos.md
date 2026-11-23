# Registro de metadatos

[↑ Glosario](../../README.md) · [← Registro de intención](./registro-de-intencion.md) · [Registro de modelos →](./registro-de-modelos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Declaración versionada de lo que debería ser cada conjunto.

Definición de trabajo de [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md).

## Por qué importa

En [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), el tema «Registro de metadatos» importa porque es la declaración contra la que se verifica.

## Cómo funciona

Según [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md):

La plataforma tiene un costo que se estima con las fórmulas de `SE-370`: bytes leídos por consulta frecuente, frecuencia de refresco de cada conjunto, TB-mes por retención y duración del camino crítico. El registro de metadatos añade un campo de presupuesto por conjunto y el control, una regla futura: si la proyección mensual de un dueño supera su presupuesto, avisa. No se implementa aquí para no mezclar un parámetro inventado con una regla de gobierno; se declara como extensión.

Según [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md):

El equipo de *Avisos* convierte el proyecto en una práctica. Mantiene el registro de metadatos junto al código del pipeline y ejecuta el control en cada cambio y antes de cada publicación. Cada trimestre ejecuta las diez mutaciones como prueba del propio control: si un cambio de reglas deja de detectar alguna, la prueba falla y el cambio no entra. Un día añade una undécima mutación inspirada en un incidente real (un `JOIN` que duplicó filas) y ve que ninguna regla la detecta; añade entonces una regla de conciliación de filas contra la capa anterior y la matriz pasa a 11 de 11.

## Ejemplo

Ejemplo de [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* convierte el proyecto en una práctica. Mantiene el registro de metadatos junto al código del pipeline y ejecuta el control en cada cambio y antes de cada publicación. Cada trimestre ejecuta las diez mutaciones como prueba del propio control: si un cambio de reglas deja de detectar alguna, la prueba falla y el cambio no entra. Un día añade una undécima mutación inspirada en un incidente real (un `JOIN` que duplicó filas) y ve que ninguna regla la detecta; añade entonces una regla de conciliación de filas contra la capa anterior y la matriz pasa a 11 de 11.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md)) son: Los tres conjuntos, las siete reglas y las diez mutaciones son construcciones del autor, y la matriz mide qué familia de defectos ve cada regla, no la tasa de defectos de ninguna plataforma; el control solo corre sobre SQLite y no cubre catálogo, captura de linaje en ejecución, claves gestionadas ni costo. Que el control detecte 9 de 10 no dice que detecte 9 de 10 de los defectos reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Cobertura](../c/cobertura.md), [Control](../c/control.md), [Evidencia](../e/evidencia.md), [Evidencia de ejecución](../e/evidencia-de-ejecucion.md), [Mutación](../m/mutacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Registro de intención](./registro-de-intencion.md) · [Registro de modelos →](./registro-de-modelos.md)
