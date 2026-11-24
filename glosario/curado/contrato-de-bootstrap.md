# Contrato de bootstrap

## Definición

El **contrato de bootstrap** es, en `SE-108`, una guía que **parte de un host soportado y termina en una prueba verde**: describe cómo pasar de una máquina con lo mínimo declarado a un entorno de desarrollo que ejecuta las pruebas con éxito. Se llama contrato porque promete algo comprobable: quien siga los pasos, en el tipo de máquina indicado, obtiene ese resultado. No es un tutorial informal ni un README orientativo; cada paso tiene una condición de éxito observable. Es un término propio del programa.

## Por qué importa

Un entorno que solo funciona para quien lo montó es una deuda que se paga en cada incorporación y en cada diagnóstico. El bootstrap define cuándo un proyecto está «listo para trabajar». La decisión que cambia es cómo se documenta la preparación: no como memoria de quien la hizo, sino como procedimiento que alguien ajeno ejecuta y que otra persona puede corregir cuando falla. También separa lo que el proyecto promete (un host soportado) de lo que no (cualquier máquina del mundo).

## Cómo funciona

El contrato se compone de cinco elementos:

- **Host soportado:** sistema y arquitectura sobre los que se afirma que funciona.
- **Prerrequisitos y versiones:** lo que debe existir antes de empezar, con versión, sin asumir configuración personal (alias, variables, rutas propias).
- **Comandos exactos:** los que se copian y ejecutan, con **tiempo esperado**, para distinguir «tarda» de «se colgó».
- **Señal de éxito por paso:** una salida o comprobación que dice que ese paso salió bien.
- **Corrección para el fallo común:** qué hacer si falla, para los problemas que ya se vieron.

Termina en una **prueba verde**: ejecutar la suite o una prueba de humo demuestra que el entorno funciona, no solo que los comandos no dieron error. El contrato se valida igual que cualquier otro: ejecutándolo **desde cero** en una máquina limpia, por alguien que no lo escribió, y corrigiéndolo cuando falla.

## Ejemplo

En el proyecto de entorno autocontenido de `SE-108`, el contrato sería un archivo corto del repositorio, con una estructura como esta (ilustración):

```text
Host soportado: Linux x86-64, Windows 11 con WSL2.
1. Instalar Docker (>= 24). Éxito: `docker info` muestra Server.
   Si falla: arrancar el servicio del motor.
2. ./bootstrap.sh   (≈ 4 min). Éxito: imprime "entorno listo".
3. ./scripts/check.sh. Éxito: "N pruebas, 0 fallos".
```

Los errores que la clase documenta tienen su paso: «el entorno no se reconstruye en otra máquina» (pasos manuales no documentados) se corrige con un solo comando probado desde cero; «los hashes de la rueda cambian entre construcciones» (marcas de tiempo) se corrige fijando el archivo instalado y no reconstruyéndolo.

## Errores y confusiones comunes

- **Asumir configuración personal.** Alias, variables y herramientas ya instaladas hacen que el contrato solo valga para su autor.
- **Pasos sin señal de éxito.** Quien sigue no sabe si avanzó bien o arrastra un fallo.
- **No probarlo desde cero.** Un bootstrap que nunca se ejecutó en una máquina limpia está sin verificar.
- **Escribir un README en lugar de un contrato.** Un texto sin comandos, versiones ni condiciones de éxito no se puede verificar.

## Límites y cuándo no aplica

El entorno reduce variabilidad conocida, no congela hardware, red ni servicios externos (`SE-108`): un bootstrap que depende de un servicio caído fallará aunque esté bien escrito. Se mantiene vivo solo si se ejecuta con frecuencia (por ejemplo, en integración continua); si no, envejece. Para proyectos de un solo autor y de vida corta, el esfuerzo de escribir y mantener el contrato puede no compensar.
