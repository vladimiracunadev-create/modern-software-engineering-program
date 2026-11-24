# Traza

## Definición

Una **traza** es el registro ordenado del recorrido de algo por un sistema. El programa la usa con matices según el contexto:

- **De una petición distribuida** (`SE-382`, `SE-496`, `SE-326`): el recorrido de una petición o de un flujo por varios componentes, formado por tramos (*spans*) relacionados.
- **De un agente** (`SE-577`): el registro ordenado de cada acción, su resultado y el estado del *harness* en ese paso.
- **De ejecución** (`SE-033`, `SE-047`): la secuencia de eventos de un caso, que se compara con otra.

## Por qué importa

La traza responde a «¿qué pasó, en qué orden y dónde se fue el tiempo o el error?». Sin ella, un fallo en un sistema distribuido o en un agente es una caja negra. En agentes, es lo que permite distinguir dos grupos de fallas con tratamientos opuestos (`SE-577`): una falla del modelo (razona mal, inventa una función) se trata cambiando de modelo, dividiendo la tarea o dándole más información; una falla del entorno (no ve el resultado, no puede escribir, nadie verifica) se trata cambiando el entorno, y cambiar de modelo no la arregla.

## Cómo funciona

Para unir tramos de procesos distintos, cada uno debe recibir y reenviar un **identificador de correlación** o un contexto de traza (`SE-382`). Una traza es un conjunto de *spans* que describen el recorrido (`SE-496`); calcular la **ruta crítica** (la cadena de tramos que determina la duración total) indica dónde optimizar. Si el contexto se pierde en un grupo de hilos o en una cola, aparecen trazas huérfanas. En arquitectura (`SE-326`), las trazas permiten verificar dependencias reales contra la vista lógica, que solo declara lo permitido.

En el harness de un agente (`SE-577`), la traza guarda cada acción y su resultado; revisarla permite saber, por ejemplo, que tres cambios con pruebas en rojo no ejecutaron las pruebas porque la línea de verificación había quedado en un archivo que el producto ya no cargaba.

## Ejemplo

```text
span A  gateway    0–480 ms
 └ span B  api       10–470
    ├ span C  cola     20–60
    └ span D  almacenamiento 70–460   <- ruta crítica
```

Optimizar el tramo C no cambia la duración total; D sí.

## Errores y confusiones comunes

- **Trazas huérfanas de 3 segundos.** Causa: contexto perdido en un grupo de hilos o una cola; corrección: copiar el contexto explícitamente y probar la frontera (`SE-496`).
- **Traza completa pero la mejora no llega.** Causa: se optimizó un span fuera de la ruta crítica; corrección: calcular la ruta crítica antes de elegir (`SE-496`).
- **Dependencias que nadie dibujó.** Causa: la vista lógica no se verifica; corrección: comparar con trazas o con el código en cada cambio (`SE-326`).

## Límites y cuándo no aplica

Una traza completa cuesta almacenamiento y puede contener datos sensibles; se muestrea y se limpia. Sin una acción registrada, la traza no distingue contexto perdido de herramienta ausente: `SE-577` advierte que un harness que no registra deja una traza idéntica en ambos casos. Y una traza muestra lo que ocurrió, no por qué: hay que contrastar hipótesis.
