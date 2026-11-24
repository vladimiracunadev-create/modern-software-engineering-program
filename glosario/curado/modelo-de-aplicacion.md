# Modelo de aplicación

## Definición

Un **modelo de aplicación** es el conjunto de reglas con que una plataforma crea, mantiene y termina el código en ejecución, y que reparte entre el sistema y el equipo las decisiones sobre proceso, ventanas e instancias. Es el sentido de `SE-253` (modelos de aplicación móvil y de escritorio). No es un patrón de diseño ni un diagrama de dominio: es lo que la plataforma impone sobre cuándo y cómo existe tu código.

## Por qué importa

Fija qué entidades existen (proceso, ventana, instancia) y cuáles controla el sistema y cuáles el equipo. `SE-253` distingue una restricción de diseño de un error de implementación: lo que decide el sistema (cuándo terminar un proceso, cuántas copias abrir) no se «arregla» con código; se diseña con ello.

## Cómo funciona

`SE-253` ofrece dos ejemplos:

- **Android.** La documentación describe que cada aplicación corre en su propio proceso con su propio usuario de sistema, que el sistema arranca el proceso cuando un componente lo necesita y que puede terminarlo cuando necesita memoria. El equipo no controla cuándo muere el proceso.
- **Escritorio con un marco como Electron.** Hay un proceso principal que gestiona ventanas y procesos de interfaz que las dibujan. Aquí el equipo controla más: puede permitir varias ventanas o varias instancias.

De ahí el método de la clase: una **tabla de supuestos** con una fila por modelo (teléfono, escritorio, ventana dividida) y una columna por supuesto (proceso permanente, copia única, ancho mínimo, estado en memoria). Cada celda es «se cumple», «no se cumple» o «depende», con su fuente (documentación de la plataforma o medición propia). Lo importante no es memorizar cada modelo, sino distinguir qué decide el equipo y qué decide el sistema.

## Ejemplo

El cliente de la plataforma de entregas es el caso conductor de la Parte 21. En `SE-253` deja la tabla de supuestos que cada modelo rompe; `SE-254` mide qué guardar en cada transición del ciclo de vida, `SE-255` compara formas de construir, `SE-256` decide dónde vive el estado y `SE-260` qué ocurre al editar sin conexión. Cambiar una sola decisión, permitir o prohibir la segunda instancia, obliga a revisar qué más se mueve.

## Errores y confusiones comunes

- **Suponer un proceso permanente** en un teléfono: el sistema puede terminarlo.
- **Tratar la terminación del proceso como un error del programa.**
- **Aplicar el modelo de escritorio al móvil** (estado solo en memoria, una segunda ventana inesperada).
- **Confundirlo con el enfoque de construcción:** el modelo es lo que la plataforma impone; el enfoque es cómo el equipo produce el cliente.

## Límites y cuándo no aplica

Las reglas son las de cada plataforma y versión, y cambian; la tabla de supuestos fecha su fuente. Para servicios de servidor el concepto se sustituye por el de ciclo de vida del proceso de despliegue. No sustituye medir el comportamiento real en el dispositivo.
