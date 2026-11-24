# Harness

## Definición

El **harness** (arnés) es todo lo que rodea al modelo en un agente: instrucciones, contexto, herramientas, permisos, bucle, parada, verificación y registro. Es la definición de `SE-577`, que cita la formulación de Böckeler: un agente es el modelo más todo lo que lo rodea.

## Por qué importa

El comportamiento observado depende del arnés tanto como del modelo. Cuando un asistente deja de ejecutar las pruebas, la causa puede estar en el modelo, en el prompt o en el entorno; sin separarlas por trazas, se culpa al modelo y el defecto queda.

## Cómo funciona

`SE-577` acota la definición amplia al caso de los agentes de código: parte del arnés viene incorporada en el producto (el mensaje de sistema, la recuperación de código) y la persona construye un arnés *exterior* con lo que el producto ofrece: instrucciones del repositorio, ganchos, permisos y compuertas de verificación. El arnés decide qué acciones se traducen en efectos, cuándo se detiene el agente y qué se verifica.

## Ejemplo

En `SE-577`, un asistente de código da por terminados tres cambios con pruebas en rojo. Las trazas muestran que no ejecutó pruebas porque una reorganización había movido la línea de verificación a un archivo que el producto ya no cargaba. Se corrige en el arnés y se añade una compuerta, sin tocar el modelo.

## Errores y confusiones comunes

Confundirlo con un *framework*: un framework es una biblioteca para construir agentes; el arnés es el entorno configurado alrededor de un agente concreto, y puede construirse con un framework, un producto o un script. Lo que lo define es qué decide (permisos, parada, verificación), no qué biblioteca usa.

## Límites y cuándo no aplica

Quitar una herramienta cambia el comportamiento sin avisar al agente; un arnés que no registra las herramientas ofrecidas deja trazas ambiguas. La definición es deliberadamente amplia y por eso conviene fijar qué parte se considera exterior.
