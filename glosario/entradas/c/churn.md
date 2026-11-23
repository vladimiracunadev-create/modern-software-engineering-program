# Churn

[↑ Glosario](../../README.md) · [← Checksum](./checksum.md) · [CI →](./ci.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Cantidad de código añadido, modificado o eliminado en un periodo, medida por archivo.

Definición de trabajo de [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md).

## Por qué importa

La clase donde se define, [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), existe con este propósito: la clase existe para que puedas entrar a un sistema que nadie entiende por completo y averiguar, con evidencia, dónde se concentra el riesgo, qué conocimiento se perdió y qué partes del código ya no hacen nada.

## Cómo funciona

Según [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md):

La mayor parte del cambio y de los defectos suele concentrarse en una minoría de archivos. Esa concentración es la que hace rentable priorizar: dedicar el trabajo preventivo a treinta archivos de trescientos es más barato que repartirlo. Tres criterios compiten. Ordenar por **tamaño** supone que lo grande es lo arriesgado; ordenar por **frecuencia de cambio** supone que lo que cambia más es donde ocurren los problemas; el **producto** de frecuencia por tamaño supone que el riesgo requiere ambas condiciones, algo que cambia mucho y que además es costoso de entender. Nagappan y Ball encontraron en software industrial que las medidas relativas de churn predicen densidad de defectos; eso respalda usar la frecuencia, no que la frecuencia sea suficiente.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo ejecuta `git log --since=2y --name-only` sobre el módulo y obtiene la frecuencia de cambio por archivo; cruza con el tamaño y con el número de correcciones identificadas por la convención de mensaje `fix:`. Tres archivos concentran el 48 % de las correcciones: el cierre de acta, el cálculo de la nota final y el exportador. De ellos, `cierre.py` solo tiene commits de dos personas que dejaron la empresa.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md)) son:

- **Se prioriza el archivo más grande y no mejora nada** — causa: el tamaño no predice dónde se corrige. Corrección: combinar frecuencia de cambio, correcciones y tamaño.
- **El ranking cambia tras un formateo masivo** — causa: el commit de formato infla la frecuencia. Corrección: excluir commits mecánicos del análisis.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Nagappan y Ball encontraron en software industrial que las medidas relativas de churn predicen densidad de defectos; eso respalda usar la frecuencia, no que la frecuencia sea suficiente. ([SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](../m/medida.md), [Archivo huérfano](../a/archivo-huerfano.md), [Código muerto](./codigo-muerto.md), [Factor de camión](../f/factor-de-camion.md), [Punto caliente](../p/punto-caliente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nagappan y Ball, «Use of relative code churn measures to predict system defect density»](https://doi.org/10.1145/1062455.1062514) — churn relativo y densidad de defectos; autoridad: ICSE 2005.
- [Avelino et al., «A novel approach for estimating Truck Factors»](https://doi.org/10.1109/ICPC.2016.7503718) — factor de camión estimado desde la autoría; autoridad: ICPC 2016.
- [Registros de decisión de arquitectura (ADR)](https://adr.github.io/) — formato ligero para dejar por escrito contexto, decisión y consecuencias; autoridad: comunidad ADR.

---

[↑ Glosario](../../README.md) · [← Checksum](./checksum.md) · [CI →](./ci.md)
