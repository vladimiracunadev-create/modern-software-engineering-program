# Configuración versionada mínima

## Definición

La **configuración versionada mínima** es, en el proyecto de `SE-108`, el conjunto más pequeño de archivos de entorno que se guardan en el control de versiones para que otra persona reconstruya el entorno de trabajo: el **manifest** (qué dependencias y qué versión del lenguaje), el **lock** cuando aplica (las versiones exactas resueltas), la definición del **contenedor** y la **configuración compartible del editor**. «Mínima» es parte de la definición: lo que no es necesario para reconstruir no se versiona.

## Por qué importa

Un entorno que solo existe en la máquina de quien lo montó no se puede reproducir: el siguiente que investigue un fallo pierde tiempo averiguando qué versión, qué extensión o qué variable se usó. Versionar demasiado produce el problema contrario: tokens, rutas locales y preferencias personales terminan en el repositorio. La decisión que cambia es dónde pasa la frontera: lo que define el entorno entra; lo que describe a la persona o a la máquina, no. Con eso el diagnóstico de `SE-108` (síntoma, entorno, reproducción, hipótesis, causa, corrección, regresión) puede repetirse.

## Cómo funciona

Cada archivo versionado cubre una causa distinta de irreproducibilidad:

- **Manifest:** declara lo que el proyecto necesita (dependencias y rangos, versión del lenguaje).
- **Lock** (si el ecosistema lo ofrece): fija las versiones exactas resueltas, de modo que dos instalaciones obtengan lo mismo.
- **Contenedor:** fija el sistema base y las herramientas, para que no dependan del equipo.
- **Configuración del editor** compartible (formateo, extensiones recomendadas): reduce diferencias triviales entre personas.

Se **excluyen** tokens, rutas locales y preferencias que no son necesarias. Hay además una regla de independencia: un default del editor ayuda, pero debe existir una **ruta de línea de comandos independiente del IDE**; quien use otro editor, o el servidor de integración, debe poder levantar el mismo entorno con un comando. `SE-108` añade dos comprobaciones concretas: el entorno debe reconstruirse en otra máquina con un comando probado **desde cero**, y los hashes no deben cambiar entre construcciones por detalles como marcas de tiempo (se fija el archivo instalado en lugar de reconstruirlo).

## Ejemplo

En el entorno reproducible de diagnóstico de `SE-108`, el repositorio contiene un manifest, un lock, la definición del contenedor y un archivo con ajustes comunes del editor, y un script que lo levanta todo:

```bash
./bootstrap.sh      # crea el entorno desde cero y ejecuta la prueba de humo
```

Se descubre que «el entorno no se reconstruye en otra máquina» por pasos manuales no documentados; la corrección es un único comando probado desde cero. Un archivo `.env` con un token queda fuera del repositorio y se reemplaza por un `.env.example` sin valores.

## Errores y confusiones comunes

- **Versionar secretos.** Un token en el repositorio es una filtración; se guarda un ejemplo sin valores.
- **Versionar todo el directorio del editor.** Mezcla preferencias personales con configuración necesaria.
- **Depender del IDE.** Si el entorno solo se levanta desde un editor concreto, el servidor de integración y otras personas no lo reproducen.
- **Manifest sin lock.** Dos instalaciones en fechas distintas pueden resolver versiones diferentes.

## Límites y cuándo no aplica

El entorno reduce la variabilidad conocida, no congela hardware, red ni servicios externos (`SE-108`). Un lock no es aplicable en todos los ecosistemas ni en todas las bibliotecas (una biblioteca publicada suele declarar rangos, no versiones exactas). Para un script de una sola vez, la sobrecarga de versionar entorno no se justifica. Y esta práctica no sustituye la reproducción del propio defecto.
