# Archivo huérfano

[↑ Glosario](../../README.md) · [← Archivo generado](./archivo-generado.md) · [Arco →](./arco.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Archivo sin ninguna persona activa asociada por autoría que pueda explicarlo.

Definición de trabajo de [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md).

## Por qué importa

En [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), el tema «Conocimiento tácito y archivos huérfanos» importa porque un archivo sin persona conocedora es un riesgo que no figura en ninguna métrica de código.

## Cómo funciona

Según [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md):

**Cómo leer la figura.** El eje horizontal son los meses y el vertical, los archivos huérfanos de 300; la línea verde es la mediana de 200 simulaciones y la coral, el percentil 90. Mira primero cómo ambas suben sin frenarse y que a los 60 meses la mediana ya es de dos tercios de los archivos. **Dónde deja de valer:** la rotación, el 35 % de archivos compartidos y la asignación al azar de archivos a personas son supuestos del autor; en equipos reales los archivos se agrupan por área y la rotación depende del contexto. La simulación no distingue entre conocimiento activo y archivos sin importancia.

## Ejemplo

Caso medido en la sección «Conocimiento tácito y archivos huérfanos» de [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md):

El conocimiento de un sistema vive en personas, en documentos y en el código. Cuando una persona se va, se lleva la parte que solo vivía en su cabeza: por qué existe una regla, qué pasa si se cambia, qué se probó y falló.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md)) son:

- **Se prioriza el archivo más grande y no mejora nada** — causa: el tamaño no predice dónde se corrige. Corrección: combinar frecuencia de cambio, correcciones y tamaño.
- **El ranking cambia tras un formateo masivo** — causa: el commit de formato infla la frecuencia. Corrección: excluir commits mecánicos del análisis.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Churn](../c/churn.md), [Código muerto](../c/codigo-muerto.md), [Factor de camión](../f/factor-de-camion.md), [Punto caliente](../p/punto-caliente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nagappan y Ball, «Use of relative code churn measures to predict system defect density»](https://doi.org/10.1145/1062455.1062514) — churn relativo y densidad de defectos; autoridad: ICSE 2005.
- [Avelino et al., «A novel approach for estimating Truck Factors»](https://doi.org/10.1109/ICPC.2016.7503718) — factor de camión estimado desde la autoría; autoridad: ICPC 2016.
- [Registros de decisión de arquitectura (ADR)](https://adr.github.io/) — formato ligero para dejar por escrito contexto, decisión y consecuencias; autoridad: comunidad ADR.

---

[↑ Glosario](../../README.md) · [← Archivo generado](./archivo-generado.md) · [Arco →](./arco.md)
