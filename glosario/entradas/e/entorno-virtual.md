# Entorno virtual

[↑ Glosario](../../README.md) · [← Entorno de vista previa](./entorno-de-vista-previa.md) · [Entrada de directorio →](./entrada-de-directorio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

`venv` crea un prefijo con scripts y configuración que usa una instalación base.

Definición de trabajo de [SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md).

## Por qué importa

En [SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), el tema «Entorno virtual» importa porque `venv` crea un prefijo con scripts y configuración que usa una instalación base.

## Cómo funciona

Según [SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), en la sección «Entorno virtual»:

`venv` crea un prefijo con scripts y configuración que usa una instalación base. Aísla paquetes por defecto, no kernel, variables, herramientas del sistema ni red. El entorno se recrea; no se copia entre rutas como artefacto portable.

## Ejemplo

Caso medido en la sección «Cuánto cuesta un entorno virtual y por qué» de [SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md):

Crear un entorno con `python -m venv` tomó 11 344 ms en Windows y dejó 860 archivos y 11 550 KiB. Con `--without-pip` tomó 180 ms, 7 archivos y 557 KiB. Con `uv venv`, 278 ms, 16 archivos y 555 KiB. En Linux (WSL2), `venv --without-pip` tomó 118 ms con 8 archivos y con pip 6 376 ms. Casi todo el costo es instalar pip: 860 archivos frente a 7. En Linux, además, el intérprete del entorno es un enlace simbólico al base; en Windows se copia un lanzador.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md)) son:

- **Funciona aquí y no en otra máquina** — causa: dependencia no declarada presente en el sistema. Corrección: probar siempre en un entorno vacío.
- **El entorno deja de funcionar al moverlo** — causa: rutas absolutas. Corrección: recrearlo desde su definición.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un entorno virtual no es un contenedor: es un archivo `pyvenv.cfg` y una forma de calcular rutas. ([SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Base](../b/base.md), [Prefijo](../p/prefijo.md), [Activación y ejecutable explícito](../a/activacion-y-ejecutable-explicito.md), [Dependencias de proyecto y herramientas](../d/dependencias-de-proyecto-y-herramientas.md), [Recreación y comprobación](../r/recreacion-y-comprobacion.md), [Secretos y configuración](../s/secretos-y-configuracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), [SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), [SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md), [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python venv](https://docs.python.org/3/library/venv.html) — Aislamiento de intérprete, scripts y entorno virtual; autoridad: Python Software Foundation.
- [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) — Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft.
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) — Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Pdb, cprofile, timeit, tracemalloc y límites instrumentales; autoridad: Python Software Foundation.
- [Development Container Specification](https://containers.dev/implementors/spec/) — Configuración reproducible de herramientas y ciclo de vida del contenedor; autoridad: Dev Container Specification maintainers.

---

[↑ Glosario](../../README.md) · [← Entorno de vista previa](./entorno-de-vista-previa.md) · [Entrada de directorio →](./entrada-de-directorio.md)
