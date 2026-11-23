# Instrumento

[↑ Glosario](../../README.md) · [← Instrucciones en conflicto](./instrucciones-en-conflicto.md) · [Integración continua →](./integracion-continua.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Mecanismo que produce una observación con alcance.

Definición de trabajo de [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md).

## Por qué importa

La clase donde se define, [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), existe con este propósito: la clase existe para integrar las capas del computador en una explicación causal que separe observación, inferencia e hipótesis.

## Cómo funciona

Según [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md):

**Cómo leer la figura.** Cada fila sigue el mismo evento sintético por una capa: la columna central contiene un valor *realmente observado* en una ejecución de ejemplo, y la última dice qué no puede concluirse de ese valor. Por ejemplo, el hash de la entrada canónica demuestra que dos corridas procesan el mismo contenido serializado, no que otra serialización produzca el mismo valor. **Dónde deja de valer:** son los valores de un equipo y una versión (CPython 3.12.9, AMD64); otra versión cambiará el número de instrucciones de bytecode y otro equipo, los tiempos. Lo que se conserva en cualquier entorno es la *estructura*: capa, instrumento, valor y límite.

Según [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md):

Aplica el protocolo a una CLI propia de otro lenguaje y sustituye instrumentos manteniendo preguntas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md):

Un reporte de regresión incluye commit, runtime, carga, muestras y perfil. El equipo puede repetir y decidir; una captura de “antes/después” no ofrece ese contrato.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md)) son:

- **colección de capturas** — causa: falta pregunta y ruta. Corrección: enlaza evidencia a transición.
- **variante produce otro resultado** — causa: invariante no comprobado. Corrección: verifica hash antes de comparar recursos.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo que se conserva en cualquier entorno es la *estructura*: capa, instrumento, valor y límite. ([SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Observación](../o/observacion.md).
- **Ver también:** [Alcance](../a/alcance.md), [Mecanismo](../m/mecanismo.md), [Fixture](../f/fixture.md), [Invariante](./invariante.md), [Procedencia](../p/procedencia.md), [Recurso](../r/recurso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (28 clases más lo mencionan; las que más):

[SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md), [SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Instrucciones en conflicto](./instrucciones-en-conflicto.md) · [Integración continua →](./integracion-continua.md)
