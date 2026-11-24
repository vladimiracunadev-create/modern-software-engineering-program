# Pipeline

[↑ Glosario](../../README.md) · [← Pila y disciplina lifo](./pila-y-disciplina-lifo.md) · [Pivote →](./pivote.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Un **pipeline** (tubería) conecta la salida de una etapa con la entrada de la siguiente ([SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md)). En arquitectura de procesadores, [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) lo usa como el solapamiento de etapas de ejecución de instrucciones. Los dos usos comparten la idea de etapas encadenadas que trabajan sobre un flujo; esta entrada trata el de línea de comandos y menciona el de estilos de arquitectura ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), véase *flujo*).

## Por qué importa

Permite componer herramientas pequeñas sin guardar resultados intermedios. Pero tiene una trampa frecuente: el estado final del pipeline depende del shell y de su configuración ([SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md)). Un pipeline puede tener éxito aparente aunque una etapa intermedia haya fallado. La decisión que cambia es qué se toma como criterio de éxito de una cadena.

## Cómo funciona

Cada etapa lee de su entrada estándar y escribe en su salida estándar; el shell conecta las etapas y las ejecuta a la vez. Un productor lento y un consumidor rápido se sincronizan por el buffer de la tubería.

Las diferencias entre shells son semánticas, no de sintaxis ([SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md)):

- En Bash, el código de salida de un pipeline es por defecto el de la última etapa; `pipefail` modifica qué fallos se propagan.
- En PowerShell, el pipeline transporta **objetos** dentro del entorno PowerShell y **texto** al cruzar a procesos nativos.

Por eso debe verificarse la semántica del shell en uso en lugar de extrapolarla.

## Ejemplo

[SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md): un pipeline de exportación transforma miles de registros. La etapa inicial falla tras diez, pero la última herramienta termina correctamente con entrada parcial. La política de propagación detiene la entrega y conserva stderr correlacionado; el éxito visual del último comando deja de ser el criterio.

```bash
set -o pipefail
exportar | transformar | cargar     # falla si cualquier etapa falla
```

## Errores y confusiones comunes

- **Un pipeline grande se bloquea.** Causa: no se consumen ambos flujos o se almacena todo; corrección: procesar en streaming y drenar canales ([SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md)).
- **Usar el código del último comando como criterio.** Una etapa anterior puede haber fallado sin que se note.
- **Suponer que Bash y PowerShell se comportan igual.** El primero mueve texto; el segundo, objetos.

## Límites y cuándo no aplica

Un pipeline no sirve cuando las etapas necesitan resultados completos, no flujos (como en una canalización de CI, donde cada paso recibe artefactos). La composición por tuberías oculta el estado intermedio, lo que dificulta depurar. Y para procesos largos y críticos, una etapa que falle a mitad debe dejar un rastro recuperable, no solo un código de salida.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Argumento](../a/argumento.md), [Código de salida](../c/codigo-de-salida.md), [Excepción](../e/excepcion.md), [Flujos estándar](../f/flujos-estandar.md), [Instrucción](../i/instruccion.md), [ISA](../i/isa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (40 clases más lo mencionan; las que más):

[SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md), [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md), [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GNU Bash Reference Manual 5.3](https://www.gnu.org/software/bash/manual/) — documenta parsing, expansión, quoting, pipelines y estado de salida en Bash.
- [Microsoft Learn — about_Pipelines](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pipelines) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Microsoft Learn — PowerShell documentation](https://learn.microsoft.com/powershell/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [The Open Group — Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.

---

[↑ Glosario](../../README.md) · [← Pila y disciplina lifo](./pila-y-disciplina-lifo.md) · [Pivote →](./pivote.md)
