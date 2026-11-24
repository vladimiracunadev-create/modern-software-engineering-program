# Contenedor de desarrollo

## Definición

Un **contenedor de desarrollo** (*dev container*) es, en `SE-104`, la descripción de un entorno de trabajo aislado: la imagen base, las *features* (componentes que se añaden), los *mounts* (carpetas del equipo que se montan), el usuario, los puertos y el *lifecycle* (comandos que se ejecutan al crear o al iniciar). Se escribe en un archivo del repositorio, de modo que quien lo abre obtiene el mismo entorno. Reutiliza la tecnología de los contenedores, pero con otro objetivo: la **experiencia de desarrollo**, no demostrar paridad con producción.

## Por qué importa

Cada persona del equipo con un entorno ligeramente distinto produce fallos que solo ocurren en una máquina. Un contenedor de desarrollo convierte la preparación del entorno en código revisable y repetible, y lo hace **desechable**: si se corrompe, se destruye y se reconstruye. La decisión que cambia es cuánto vale el tiempo de incorporación y de diagnóstico: en lugar de seguir una lista de pasos manuales, se abre el proyecto y se trabaja. También permite reproducir el entorno de un defecto, requisito del diagnóstico de `SE-104`.

## Cómo funciona

El contenedor se define de forma declarativa y el editor (o una herramienta de línea de comandos) lo construye y se conecta a él. Cada elemento resuelve un problema:

- **Imagen:** fija el sistema y las herramientas base. Si se identifica por una etiqueta mutable, la imagen puede cambiar sin que el repositorio cambie; la corrección de `SE-104` es **fijar el digest**.
- **Features:** instalan herramientas adicionales sin escribir un Dockerfile propio.
- **Mounts:** el código vive en el equipo anfitrión y se ve dentro del contenedor, de modo que las ediciones persisten.
- **Usuario y puertos:** evitan trabajar como superusuario y exponen lo necesario para ver la aplicación.
- **Lifecycle:** comandos de preparación (instalar dependencias) que se ejecutan una vez o en cada arranque.

Como el contenedor es una capa sobre el motor de contenedores, depende de que este esté en marcha: un síntoma frecuente es que el cliente `docker` responda pero no se pueda ejecutar nada, porque el servidor no está activo; se verifica con `docker info`.

## Ejemplo

En el entorno reproducible de diagnóstico de `SE-104`, el archivo `devcontainer.json` fija una imagen por digest, instala la versión del lenguaje con una *feature*, monta el repositorio y ejecuta al crear la instalación de dependencias. Un esquema mínimo (ilustración, los nombres de campos siguen la especificación de dev containers):

```json
{
  "image": "mcr.microsoft.com/devcontainers/python@sha256:<digest>",
  "postCreateCommand": "pip install -e .[dev]",
  "forwardPorts": [8000]
}
```

Quien clona el repositorio y abre el contenedor obtiene el mismo entorno que quien reportó el fallo, que es el punto de partida del delta debugging manual de la clase siguiente.

## Errores y confusiones comunes

- **Creer que es un reemplazo del despliegue.** No demuestra paridad productiva; su meta es trabajar cómodo y reproducir.
- **Etiquetas mutables.** `latest` o una etiqueta de versión que se republica cambia el entorno sin tocar el repositorio.
- **Asumir que el motor está activo.** Que el cliente responda no implica que el servidor lo esté.
- **Meter secretos en la imagen o en el archivo.** Se inyectan por otro mecanismo, no se versionan.

## Límites y cuándo no aplica

Un contenedor estable no reduce automáticamente un fallo (`SE-104`): reproducir el entorno es solo el primer paso del diagnóstico. No congela hardware ni servicios externos, y las diferencias de sistema de archivos o de rendimiento entre anfitrión y contenedor pueden alterar un resultado. En equipos donde nadie puede ejecutar contenedores, o en proyectos triviales con un solo requisito, el costo de mantener la definición supera el beneficio.
