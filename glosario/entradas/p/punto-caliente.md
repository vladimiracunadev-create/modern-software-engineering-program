# Punto caliente

[↑ Glosario](../../README.md) · [← Pull request](./pull-request.md) · [Punto ciego →](./punto-ciego.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Archivo o módulo que concentra una parte desproporcionada de los cambios o de las correcciones.

Definición de trabajo de [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md).

## Por qué importa

En [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), el tema «Puntos calientes» importa porque concentran el riesgo y el trabajo preventivo con mejor retorno.

## Cómo funciona

Según [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md):

La mayor parte del cambio y de los defectos suele concentrarse en una minoría de archivos. Esa concentración es la que hace rentable priorizar: dedicar el trabajo preventivo a treinta archivos de trescientos es más barato que repartirlo. Tres criterios compiten. Ordenar por **tamaño** supone que lo grande es lo arriesgado; ordenar por **frecuencia de cambio** supone que lo que cambia más es donde ocurren los problemas; el **producto** de frecuencia por tamaño supone que el riesgo requiere ambas condiciones, algo que cambia mucho y que además es costoso de entender. Nagappan y Ball encontraron en software industrial que las medidas relativas de churn predicen densidad de defectos; eso respalda usar la frecuencia, no que la frecuencia sea suficiente.

## Ejemplo

Ejemplo de [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) (sección «Caso conductor»):

El módulo de calificaciones es el caso conductor de la [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md). Esta clase deja el segundo artefacto: el mapa de riesgo (puntos calientes, huérfanos y candidatos a código muerto). `SE-519` preguntará cómo se protegen los comportamientos de esos puntos calientes antes de modificarlos, y `SE-520` cómo se mide el riesgo que acumulan las dependencias. Cambia después un solo dato, la rotación mensual de 2 % a 0,5 %, y observa a partir de qué horizonte los huérfanos dejan de ser un problema.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md)) son:

- **Se prioriza el archivo más grande y no mejora nada** — causa: el tamaño no predice dónde se corrige. Corrección: combinar frecuencia de cambio, correcciones y tamaño.
- **El ranking cambia tras un formateo masivo** — causa: el commit de formato infla la frecuencia. Corrección: excluir commits mecánicos del análisis.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un punto caliente no es automáticamente un mal diseño; puede ser el lugar donde el negocio cambia más, como las reglas de calificación, y en ese caso el trabajo preventivo es hacerlo más fácil de cambiar. ([SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Módulo](../m/modulo.md), [Archivo huérfano](../a/archivo-huerfano.md), [Churn](../c/churn.md), [Código muerto](../c/codigo-muerto.md), [Factor de camión](../f/factor-de-camion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Puntos calientes».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nagappan y Ball, «Use of relative code churn measures to predict system defect density»](https://doi.org/10.1145/1062455.1062514) — churn relativo y densidad de defectos; autoridad: ICSE 2005.
- [Avelino et al., «A novel approach for estimating Truck Factors»](https://doi.org/10.1109/ICPC.2016.7503718) — factor de camión estimado desde la autoría; autoridad: ICPC 2016.
- [Registros de decisión de arquitectura (ADR)](https://adr.github.io/) — formato ligero para dejar por escrito contexto, decisión y consecuencias; autoridad: comunidad ADR.

---

[↑ Glosario](../../README.md) · [← Pull request](./pull-request.md) · [Punto ciego →](./punto-ciego.md)
