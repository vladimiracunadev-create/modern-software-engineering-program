# Reloj vectorial

[↑ Glosario](../../README.md) · [← Reloj monotónico](./reloj-monotonico.md) · [Reloj, repetición y distribución →](./reloj-repeticion-y-distribucion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Marca con un contador por nodo que permite decidir si dos sucesos están ordenados o son concurrentes.

Definición de trabajo de [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md).

## Por qué importa

La clase donde se define, [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md), existe con este propósito: la clase existe para que dejes de usar la hora como si fuera un orden: que sepas cuándo basta un reloj monotónico para medir una duración, cuándo una marca de tiempo de pared ordena mal los sucesos de dos máquinas y qué ofrece cada reloj lógico (Lamport, vectorial, híbrido) para decidir qué ocurrió antes de qué, y qué sucesos son simplemente concurrentes.

## Cómo funciona

Según [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md):

Un **reloj vectorial** guarda un contador por nodo en cada suceso. La marca de *a* es menor o igual que la de *b* en todas las posiciones, y distinta, solo si *a* ocurrió antes que *b*; si ninguna es menor, son concurrentes. Es la herramienta exacta para detectar conflictos: dos versiones de un dato con vectores incomparables son escrituras concurrentes que hay que reconciliar, no una más antigua que otra. El precio es el tamaño: un contador por nodo en cada marca, que crece con el número de participantes y obliga a podar o a usar variantes.

## Ejemplo

Ejemplo de [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra que un reloj vectorial detecta concurrencia donde Lamport no. Antes de ejecutarlo, predice si `a` y `b` son concurrentes.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Todos los pares aparecen ordenados en el registro** — causa: se leyó Lamport como causalidad. Corrección: reloj vectorial para detectar concurrencia. ([SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2); los conteos fueron idénticos y la resolución de los relojes difirió, como se declara. No se midió ningún servicio de tiempo ni la deriva real de relojes: los eventos, los desfases y el ajuste de −80 ms son construcciones del autor. La siguiente clase aborda el otro lado del problema: qué se sabe cuando una respuesta no llega.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contador](../c/contador.md), [Ocurrió antes de](../o/ocurrio-antes-de.md), [Reloj de pared](./reloj-de-pared.md), [Reloj monotónico](./reloj-monotonico.md), [Sucesos concurrentes](../s/sucesos-concurrentes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lamport, «Time, clocks, and the ordering of events…»](https://doi.org/10.1145/359545.359563) — orden parcial y relojes lógicos; autoridad: artículo original (1978).
- [Kulkarni et al., «Logical Physical Clocks»](https://cse.buffalo.edu/tech-reports/2014-04.pdf) — reloj híbrido; autoridad: informe técnico de los autores.
- [RFC 5905: NTP versión 4](https://www.rfc-editor.org/rfc/rfc5905) — sincronización de relojes y su error; autoridad: IETF.
- [Python: time](https://docs.python.org/3/library/time.html) — relojes y resolución; autoridad: documentación de Python.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — pérdida de escrituras con marcas de pared; autoridad: autor del libro.

---

[↑ Glosario](../../README.md) · [← Reloj monotónico](./reloj-monotonico.md) · [Reloj, repetición y distribución →](./reloj-repeticion-y-distribucion.md)
