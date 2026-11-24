# Diagnóstico incorporado

[↑ Glosario](../../README.md) · [← Diagnóstico](./diagnostico.md) · [Diagrama →](./diagrama.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

El **diagnóstico incorporado** es, en [SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), un comando del propio proyecto que **imprime versiones, ejecutable, plataforma y comprobaciones, sin secretos**, de modo que cualquiera pueda ver con qué entorno está trabajando y compartirlo al reportar un problema. Junto con él, la reproducción del defecto y su regresión viven **junto al proyecto**, no en la memoria de quien lo investigó. Es un término propio del programa, parecido a un `doctor` o `--version` ampliado.

## Por qué importa

Gran parte del tiempo de un diagnóstico se va en averiguar qué es distinto entre dos máquinas: qué versión del lenguaje, cuál ejecutable se está usando realmente, qué sistema. Sin una salida estándar, la persona que reporta tiene que adivinar qué comunicar, y quien investiga, preguntar. La decisión que cambia es quién produce la información del entorno: el proyecto, de forma uniforme y reproducible, y no cada persona a mano. Además, al excluir secretos por diseño, esa salida puede pegarse en una incidencia sin riesgo.

## Cómo funciona

Un buen comando de diagnóstico tiene cuatro rasgos:

- **Datos del entorno:** versión del lenguaje y de las dependencias clave, ruta del ejecutable que se está usando, sistema operativo y arquitectura.
- **Comprobaciones:** pequeñas verificaciones con resultado «ok» o «falla» y motivo (¿existe el archivo de datos? ¿responde el servicio local?).
- **Ausencia de secretos:** no imprime tokens ni rutas personales; las variables sensibles se omiten o se enmascaran.
- **Salidas separadas:** lo consumible por otros programas va a la **salida estándar** y el diagnóstico a la **salida de error**, y se usan **códigos de salida** para que un guion sepa si el entorno está sano.

La causa de que sirva es que convierte un problema de conversación («¿qué tienes instalado?») en un artefacto que se adjunta. [SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md) lo conecta con la reproducción: junto al comando viven el caso que reproduce el defecto y la prueba de regresión que lo cubre.

## Ejemplo

Para el entorno de diagnóstico de [SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), un comando `proyecto doctor` podría producir (ilustración; el nombre y el formato son inventados):

```text
python        3.12.4   /usr/local/bin/python3
plataforma    linux-x86_64
paquete       engineering_sdk 1.3.0 (instalado, no editable)
check datos   ok     (data/casos.json presente)
check puerto  falla  (8000 ocupado)
```

con código de salida distinto de cero si algún chequeo falla. Una persona que reporta pega esa salida y quien investiga ve de inmediato, por ejemplo, que se está ejecutando otro intérprete del esperado. Es la misma idea con la que la clase aborda un entorno que «no se reconstruye en otra máquina»: eliminar el paso manual no documentado.

## Errores y confusiones comunes

- **Imprimir variables de entorno completas.** Filtra tokens y rutas.
- **Mezclar datos y diagnóstico en la misma salida.** Rompe a quien consume la salida estándar.
- **Chequeos sin criterio de éxito claro.** «Parece bien» no sirve; cada uno debe ser pasa o falla.
- **Tratarlo como sustituto de reproducir.** Dice cómo es el entorno, no demuestra el defecto.

## Límites y cuándo no aplica

El entorno reduce variabilidad conocida, no congela hardware, red ni servicios externos ([SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md)): el diagnóstico solo puede informar de lo que el proyecto sabe mirar. Un comando que intenta comprobarlo todo se vuelve lento y frágil. Para un script personal que nadie más ejecuta, un `--version` basta. Y no reemplaza la observabilidad en producción, que mira sistemas en vivo, no un entorno de desarrollo.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Comando](../c/comando.md), [Plataforma](../p/plataforma.md), [Secreto](../s/secreto.md), [Versión](../v/version.md), [Configuración versionada mínima](../c/configuracion-versionada-minima.md), [Contrato de bootstrap](../c/contrato-de-bootstrap.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-108 — Proyecto: entorno de desarrollo autocontenido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) — Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft.
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) — Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Pdb, cprofile, timeit, tracemalloc y límites instrumentales; autoridad: Python Software Foundation.
- [Python venv](https://docs.python.org/3/library/venv.html) — Aislamiento de intérprete, scripts y entorno virtual; autoridad: Python Software Foundation.
- [Development Container Specification](https://containers.dev/implementors/spec/) — Configuración reproducible de herramientas y ciclo de vida del contenedor; autoridad: Dev Container Specification maintainers.

---

[↑ Glosario](../../README.md) · [← Diagnóstico](./diagnostico.md) · [Diagrama →](./diagrama.md)
