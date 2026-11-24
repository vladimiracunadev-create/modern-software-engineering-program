# Registro de cambios

## Definición

El **registro de cambios** (*changelog*) es el documento para humanos que describe qué cambió en cada versión y qué debe hacer el cliente (`SE-474`). `SE-366` lo usa en el contexto de datos como el historial anunciado de cambios de significado y de esquema. No es un volcado del historial de commits.

## Por qué importa

Quien consume una biblioteca, una API o un conjunto de datos decide si actualizar según lo que este documento le diga. Si es vago u omite una ruptura, el cliente se entera cuando algo falla en producción. La decisión que cambia es quién es el lector: se escribe pensando en quien debe decidir y actuar, no en quien hizo el cambio.

## Cómo funciona

`SE-474` fija el formato. El registro agrupa los cambios **por versión** y **por tipo**: añadido, cambiado, obsoleto, eliminado, corregido, seguridad. Cada versión lleva fecha y, para lo incompatible, una **guía de migración**. Una entrada útil responde tres preguntas: **qué cambió desde el punto de vista del cliente, a quién afecta y qué debe hacer**.

Un registro que dice «mejoras de rendimiento y correcciones» incumple su función: no dice a quién afecta ni qué hacer. Generarlo a partir de mensajes de commit con una convención ayuda a no olvidar cambios, pero la redacción, la clasificación y la advertencia siguen necesitando criterio humano: un commit describe lo que hizo el autor, no lo que el cliente nota.

Va de la mano del versionado semántico: el número de versión indica el tipo de cambio y el registro explica su contenido. La obsolescencia anunciada («este campo se eliminará en la versión X») permite que el cliente se prepare, y el error típico (clientes que no se enteran de una ruptura) se corrige con formato fijo, guía de migración y obsolescencia anunciada. En datos (`SE-366`), el equivalente es el aviso de cambios de significado y esquema para los consumidores.

## Ejemplo

Una entrada: «**Cambiado**: el campo `nota` pasa de entero a decimal (afecta a quienes lo leen como entero; usar `round()` o actualizar el tipo antes de la 2.0). **Obsoleto**: `calificacion_vieja`, se eliminará en 3.0». Responde qué cambió, a quién afecta y qué debe hacerse. Formato de `SE-474`.

## Errores y confusiones comunes

- **Los clientes no se enteran de una ruptura**: registro genérico o sin aviso previo; se corrige con formato fijo, guía de migración y obsolescencia anunciada.
- **Pegar la lista de commits**: no es un registro de cambios.
- **Entradas escritas desde el punto de vista del autor** («refactor del módulo X»).
- **Omitir los cambios de seguridad** o los cambios de significado sin cambio de firma.

## Límites y cuándo no aplica

Según `SE-474`, para una aplicación sin consumidores externos el número de versión puede ser una fecha o un contador; lo importante es que sea monótono y que el registro sea veraz. Un registro solo es útil si es veraz y se mantiene al día: uno desactualizado es peor que ninguno. No sustituye la documentación del uso ni la comunicación directa con consumidores críticos.
