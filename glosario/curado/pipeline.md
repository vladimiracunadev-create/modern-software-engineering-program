# Pipeline

## Definición

Un **pipeline** (tubería) conecta la salida de una etapa con la entrada de la siguiente (`SE-029`). En arquitectura de procesadores, `SE-017` lo usa como el solapamiento de etapas de ejecución de instrucciones. Los dos usos comparten la idea de etapas encadenadas que trabajan sobre un flujo; esta entrada trata el de línea de comandos y menciona el de estilos de arquitectura (`SE-339`, véase *flujo*).

## Por qué importa

Permite componer herramientas pequeñas sin guardar resultados intermedios. Pero tiene una trampa frecuente: el estado final del pipeline depende del shell y de su configuración (`SE-029`). Un pipeline puede tener éxito aparente aunque una etapa intermedia haya fallado. La decisión que cambia es qué se toma como criterio de éxito de una cadena.

## Cómo funciona

Cada etapa lee de su entrada estándar y escribe en su salida estándar; el shell conecta las etapas y las ejecuta a la vez. Un productor lento y un consumidor rápido se sincronizan por el buffer de la tubería.

Las diferencias entre shells son semánticas, no de sintaxis (`SE-029`):

- En Bash, el código de salida de un pipeline es por defecto el de la última etapa; `pipefail` modifica qué fallos se propagan.
- En PowerShell, el pipeline transporta **objetos** dentro del entorno PowerShell y **texto** al cruzar a procesos nativos.

Por eso debe verificarse la semántica del shell en uso en lugar de extrapolarla.

## Ejemplo

`SE-029`: un pipeline de exportación transforma miles de registros. La etapa inicial falla tras diez, pero la última herramienta termina correctamente con entrada parcial. La política de propagación detiene la entrega y conserva stderr correlacionado; el éxito visual del último comando deja de ser el criterio.

```bash
set -o pipefail
exportar | transformar | cargar     # falla si cualquier etapa falla
```

## Errores y confusiones comunes

- **Un pipeline grande se bloquea.** Causa: no se consumen ambos flujos o se almacena todo; corrección: procesar en streaming y drenar canales (`SE-029`).
- **Usar el código del último comando como criterio.** Una etapa anterior puede haber fallado sin que se note.
- **Suponer que Bash y PowerShell se comportan igual.** El primero mueve texto; el segundo, objetos.

## Límites y cuándo no aplica

Un pipeline no sirve cuando las etapas necesitan resultados completos, no flujos (como en una canalización de CI, donde cada paso recibe artefactos). La composición por tuberías oculta el estado intermedio, lo que dificulta depurar. Y para procesos largos y críticos, una etapa que falle a mitad debe dejar un rastro recuperable, no solo un código de salida.
