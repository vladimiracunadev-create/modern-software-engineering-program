# Entorno virtual

[↑ Glosario](../../README.md) · [← Entorno de vista previa](./entorno-de-vista-previa.md) · [Entrada de directorio →](./entrada-de-directorio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Un **entorno virtual** (en Python, el creado por `venv`) es un **prefijo**: un directorio con scripts y un archivo de configuración (`pyvenv.cfg`) que usa una **instalación base** de Python y mantiene su propio conjunto de paquetes ([SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md)). No es una máquina virtual ni un contenedor: es, según la clase, un archivo de configuración y una forma de calcular rutas. Aísla los **paquetes**; no aísla el núcleo del sistema, las variables de entorno, las herramientas del sistema ni la red.

## Por qué importa

Dos proyectos pueden necesitar versiones incompatibles de la misma dependencia. Instalar todo en un único espacio global hace que actualizar uno rompa al otro y que «funcione en mi máquina» dependa de lo que se haya instalado alguna vez. La decisión que cambia es dónde viven las dependencias de un proyecto: en un entorno propio, **recreable desde su definición**, y no en el sistema. Además, la regla de probar en un entorno vacío es lo que detecta una dependencia declarada a medias.

## Cómo funciona

Al crear el entorno, `venv` genera un directorio con tres piezas:

- **`pyvenv.cfg`:** indica qué instalación base se usa.
- **Un intérprete de entorno:** en Linux es un enlace simbólico al intérprete base; en Windows se copia un lanzador ([SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md)).
- **Un directorio de paquetes propio** (`site-packages`), donde se instala lo que se pida.

Al arrancar, el intérprete lee `pyvenv.cfg`, detecta que está en un entorno y ajusta sus rutas de búsqueda para que los paquetes instalados allí tengan prioridad y la biblioteca estándar venga de la base. «Activar» el entorno solo cambia la variable de rutas de la terminal para encontrar los scripts del entorno.

Como el entorno contiene **rutas absolutas** a la base y a sí mismo, no es portable: moverlo o copiarlo a otro sitio lo deja roto. Por eso la regla es **recrearlo**, no copiarlo.

## Ejemplo

[SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md) midió el costo de crearlo. En Windows, `python -m venv` tomó 11 344 ms y dejó 860 archivos y 11 550 KiB; con `--without-pip` tomó 180 ms, 7 archivos y 557 KiB; con `uv venv`, 278 ms, 16 archivos y 555 KiB. En Linux (WSL2), `--without-pip` tomó 118 ms con 8 archivos, y con pip 6 376 ms. Casi todo el costo es instalar pip: 860 archivos frente a 7. Estos números son de la medición de la clase, en esas máquinas. Un uso típico:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest
```

Para comprobar que el proyecto no depende de nada del sistema, se repite desde un entorno recién creado.

## Errores y confusiones comunes

- **«Funciona aquí y no en otra máquina».** Una dependencia usada pero no declarada estaba instalada en el sistema; se prueba siempre en un entorno vacío.
- **Mover o copiar el entorno.** Por las rutas absolutas, deja de funcionar; se recrea desde su definición.
- **Creer que aísla el sistema.** No aísla variables de entorno, herramientas ni red.
- **Versionar el directorio del entorno.** Es un artefacto local; se versiona la definición (manifest, lock), no el resultado.

## Límites y cuándo no aplica

Un entorno virtual no es un contenedor ([SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md)): no fija el sistema operativo, las bibliotecas nativas ni la versión del intérprete base, y no impide que un paquete lea el sistema de archivos o la red. Cuando el problema es la variabilidad del sistema, se necesita un contenedor de desarrollo. Para un script de un solo archivo sin dependencias externas, el entorno no aporta nada, aunque sigue siendo buena práctica en cuanto aparece la primera dependencia.

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
