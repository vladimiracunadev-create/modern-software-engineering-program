# Entorno virtual

## Definición

Un **entorno virtual** (en Python, el creado por `venv`) es un **prefijo**: un directorio con scripts y un archivo de configuración (`pyvenv.cfg`) que usa una **instalación base** de Python y mantiene su propio conjunto de paquetes (`SE-103`). No es una máquina virtual ni un contenedor: es, según la clase, un archivo de configuración y una forma de calcular rutas. Aísla los **paquetes**; no aísla el núcleo del sistema, las variables de entorno, las herramientas del sistema ni la red.

## Por qué importa

Dos proyectos pueden necesitar versiones incompatibles de la misma dependencia. Instalar todo en un único espacio global hace que actualizar uno rompa al otro y que «funcione en mi máquina» dependa de lo que se haya instalado alguna vez. La decisión que cambia es dónde viven las dependencias de un proyecto: en un entorno propio, **recreable desde su definición**, y no en el sistema. Además, la regla de probar en un entorno vacío es lo que detecta una dependencia declarada a medias.

## Cómo funciona

Al crear el entorno, `venv` genera un directorio con tres piezas:

- **`pyvenv.cfg`:** indica qué instalación base se usa.
- **Un intérprete de entorno:** en Linux es un enlace simbólico al intérprete base; en Windows se copia un lanzador (`SE-103`).
- **Un directorio de paquetes propio** (`site-packages`), donde se instala lo que se pida.

Al arrancar, el intérprete lee `pyvenv.cfg`, detecta que está en un entorno y ajusta sus rutas de búsqueda para que los paquetes instalados allí tengan prioridad y la biblioteca estándar venga de la base. «Activar» el entorno solo cambia la variable de rutas de la terminal para encontrar los scripts del entorno.

Como el entorno contiene **rutas absolutas** a la base y a sí mismo, no es portable: moverlo o copiarlo a otro sitio lo deja roto. Por eso la regla es **recrearlo**, no copiarlo.

## Ejemplo

`SE-103` midió el costo de crearlo. En Windows, `python -m venv` tomó 11 344 ms y dejó 860 archivos y 11 550 KiB; con `--without-pip` tomó 180 ms, 7 archivos y 557 KiB; con `uv venv`, 278 ms, 16 archivos y 555 KiB. En Linux (WSL2), `--without-pip` tomó 118 ms con 8 archivos, y con pip 6 376 ms. Casi todo el costo es instalar pip: 860 archivos frente a 7. Estos números son de la medición de la clase, en esas máquinas. Un uso típico:

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

Un entorno virtual no es un contenedor (`SE-103`): no fija el sistema operativo, las bibliotecas nativas ni la versión del intérprete base, y no impide que un paquete lea el sistema de archivos o la red. Cuando el problema es la variabilidad del sistema, se necesita un contenedor de desarrollo. Para un script de un solo archivo sin dependencias externas, el entorno no aporta nada, aunque sigue siendo buena práctica en cuanto aparece la primera dependencia.
