# Espacio de nombres

## Definición

Un **espacio de nombres** (*namespace*) del núcleo es el mecanismo que da a un conjunto de procesos una vista propia de un recurso global (`SE-398`): otros procesos, la red, los montajes o los usuarios (`SE-282`). Es una pieza del sistema operativo, no una carpeta ni un paquete de lenguaje. Otras disciplinas usan «espacio de nombres» para evitar colisiones de identificadores; aquí el sentido es de aislamiento de vista.

## Por qué importa

Es lo que permite que un contenedor «crea» que es el único proceso de su máquina, que tiene su propia red y su propio sistema de archivos. Entender qué aísla y qué no cambia una decisión de seguridad: la vista restringida no es una frontera de hardware (`SE-398`).

## Cómo funciona

Según `SE-398`, un contenedor es un proceso, o un grupo de procesos, al que el núcleo muestra una vista restringida mediante espacios de nombres y al que limita los recursos mediante **grupos de control** (otro mecanismo, que decide cuánto se consume). `SE-282` ordena las fronteras por lo que comparten con el anfitrión:

- un **hilo** comparte todo el proceso;
- un **proceso** comparte el núcleo pero tiene memoria virtual propia;
- un **contenedor** es un proceso con espacios de nombres (lo que ve), grupos de control (cuánto consume) y filtros de llamadas de sistema; sigue compartiendo el núcleo;
- un **núcleo de aplicación** como gVisor interpone un núcleo propio en espacio de usuario que reduce las llamadas que llegan al núcleo real.

La causa de la debilidad es que los espacios de nombres cambian lo que el proceso *ve*, no lo que el núcleo *ejecuta*.

## Ejemplo

En Linux, `unshare` crea un proceso con un espacio de nombres de procesos propio:

```bash
sudo unshare --pid --fork --mount-proc ps aux
```

El `ps` dentro solo lista sus propios procesos, aunque el anfitrión ejecute miles. Es la vista, no un núcleo nuevo.

## Errores y confusiones comunes

- **Creer que equivale a una máquina virtual.** Comparte núcleo; una vulnerabilidad del núcleo atraviesa la vista (`SE-398`).
- **Confundir vista con límite de consumo.** Sin grupos de control, un proceso aislado agota la memoria del anfitrión.
- **Confundirlo con el directorio de trabajo o los alcances de nombres de un lenguaje.** Son conceptos de capas distintas (`SE-026` trata el directorio de trabajo).

## Límites y cuándo no aplica

No protege contra código hostil: para eso `SE-398` recomienda una máquina virtual o microVM. Su eficacia depende de la configuración (montajes, privilegios, capacidades concedidas). Y existen espacios de nombres solo en núcleos que los implementan (Linux); en otros sistemas el aislamiento se logra con mecanismos distintos.
