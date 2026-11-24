# Contenedor

## Definición

Un **contenedor** es un proceso, o un grupo de procesos, al que el núcleo muestra una vista restringida y cuyos recursos limita, sin un núcleo propio (`SE-398`). `SE-034` lo describe como un conjunto de procesos con vistas y límites que suele compartir el kernel. No es un objeto del núcleo ni una máquina virtual ligera: es una combinación de funciones del sistema operativo.

## Por qué importa

Permite empaquetar y repetir un entorno (dependencias, configuración, binarios) y arrancarlo en cualquier anfitrión compatible. Pero el error costoso es tomarlo por una frontera de seguridad fuerte: `SE-398` lo califica como una frontera más débil que una máquina virtual. La decisión que cambia es dónde ejecutar código propio y dónde código ajeno.

## Cómo funciona

Dos mecanismos del núcleo (`SE-398`):

- **Espacios de nombres:** dan al proceso una vista propia de procesos, red, montajes o usuarios.
- **Grupos de control (cgroups):** limitan recursos como memoria, procesos y CPU.

Las especificaciones de OCI fijan cómo se describe su configuración, su sistema de archivos y su ciclo de vida, de modo que distintos entornos de ejecución cumplen el mismo contrato. Como el contenedor comparte núcleo con el anfitrión y los demás contenedores, una vulnerabilidad del núcleo o una configuración con demasiados privilegios puede permitir que un proceso salga de su vista. De ahí que el aislamiento sea una propiedad de la configuración efectiva (montajes, capacidades, usuario), no de la palabra «contenedor» (`SE-034`).

## Ejemplo

Un contenedor sin límite de memoria que sufre una fuga consume el anfitrión: se aisló la vista, no el consumo. Ilustración:

```bash
docker run --memory=256m --pids-limit=100 imagen
```

Para ejecutar código ajeno, `SE-398` recomienda una máquina virtual o microVM.

## Errores y confusiones comunes

- **Un contenedor agota la memoria del anfitrión.** Causa: se aisló la vista y no el consumo; corrección: límites de memoria y procesos (`SE-398`).
- **Suponer que contiene código hostil.** Causa: confundir vista restringida con frontera de hardware; corrección: VM o microVM (`SE-398`).
- **«Está aislado porque está en un contenedor».** Causa: se ignoraron kernel, montajes y privilegios compartidos; corrección: enumerar fronteras y capacidades efectivas (`SE-034`).

## Límites y cuándo no aplica

No sustituye a una VM cuando la amenaza es el propio código. No es portable entre núcleos distintos: un contenedor Linux necesita un núcleo Linux. Y una imagen empaqueta un entorno, no garantiza por sí sola reproducibilidad ni seguridad: ambas dependen de cómo se construya y se configure.
