# Ruta vertical

[↑ Glosario](../../README.md) · [← Ruta crítica](./ruta-critica.md) · [Rutina de interrupción →](./rutina-de-interrupcion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Seguimiento de una capacidad a través de capas.

Definición de trabajo de [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md).

## Por qué importa

La clase donde se define, [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), existe con este propósito: la clase existe para integrar las capas del computador en una explicación causal que separe observación, inferencia e hipótesis.

## Cómo funciona

[SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Una ruta vertical conecta causa y consecuencia» de [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md):

**Cómo leer la figura.** Cada fila sigue el mismo evento sintético por una capa: la columna central contiene un valor *realmente observado* en una ejecución de ejemplo, y la última dice qué no puede concluirse de ese valor. Por ejemplo, el hash de la entrada canónica demuestra que dos corridas procesan el mismo contenido serializado, no que otra serialización produzca el mismo valor. **Dónde deja de valer:** son los valores de un equipo y una versión (CPython 3.12.9, AMD64); otra versión cambiará el número de instrucciones de bytecode y otro equipo, los tiempos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md)) son:

- **colección de capturas** — causa: falta pregunta y ruta. Corrección: enlaza evidencia a transición.
- **variante produce otro resultado** — causa: invariante no comprobado. Corrección: verifica hash antes de comparar recursos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md)) son: No observa energía, contadores físicos ni producción. `SE-024` exige diseñar una investigación propia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](../c/capa.md), [Capacidad](../c/capacidad.md), [Fixture](../f/fixture.md), [Instrumento](../i/instrumento.md), [Invariante](../i/invariante.md), [Procedencia](../p/procedencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Ruta crítica](./ruta-critica.md) · [Rutina de interrupción →](./rutina-de-interrupcion.md)
