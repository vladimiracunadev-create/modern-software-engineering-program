# Deriva

## Definición

La **deriva** es la diferencia entre lo que un registro afirma y lo que realmente existe, nacida de cambios hechos fuera del flujo previsto. El programa la usa en varios dominios con el mismo núcleo. En infraestructura como código (`SE-402`, `SE-486`): diferencia entre el estado deseado o el que cree el archivo de estado y la realidad, causada por cambios hechos fuera del código. En especificaciones (`SE-165`, `SE-548`): diferencia entre lo que la especificación afirma y lo que el sistema hace. En `SE-442`: cambio acumulado lento de una magnitud a lo largo de muchos cambios pequeños.

## Por qué importa

Cambia cuándo se descubre que el registro ya no es la verdad. En infraestructura, `SE-402` lo resume así: un cambio manual no desaparece; el siguiente `apply` lo revierte o lo ignora. En especificaciones, una spec que ya no describe el sistema engaña a quien la lee. Ver la deriva a tiempo permite decidir en lugar de descubrirla en un incidente.

## Cómo funciona

El mecanismo es una comparación entre dos fuentes. Un arreglo de emergencia en la consola o con otra herramienta modifica la realidad sin pasar por el código. Un plan que solo compara código con estado no lo ve; uno que primero **refresca** el estado contra la realidad lo detecta y propone revertirlo. Ninguna conducta es incorrecta: la primera es rápida y ciega; la segunda es exacta y puede deshacer un arreglo necesario. Lo esencial es la decisión explícita: incorporar el cambio al código o revertirlo.

Para no descubrirla semanas después, `SE-486` propone un plan solo de lectura periódico (cada pocas horas, con responsable) que abre una incidencia por cada diferencia. En el caso de contratos (`SE-160`), la comparación debe incluir tipos y restricciones, no solo nombres, o un cambio de tipo pasa inadvertido.

## Ejemplo

El equipo de la plataforma guarda el estado en un almacén remoto con bloqueo y cifrado y exige que todo cambio pase por un plan revisado por otra persona. Cada noche corre un plan de solo lectura y abre una incidencia por diferencia. Si la deriva era un arreglo de emergencia, se incorpora al código o se revierte de forma deliberada, no al pasar. En el experimento de `SE-402`, sin refresco el plan ve siempre los mismos 10 cambios y detecta la deriva solo cuando coincide con una edición del código.

## Errores y confusiones comunes

- **Un `apply` revierte un arreglo de emergencia.** Deriva no incorporada; revisar las acciones que el código no editó y decidir cada una.
- **La deriva se descubre semanas después.** Sin comprobación periódica con responsable.
- **Tratar toda deriva como error.** Puede ser un arreglo válido que falta incorporar.
- **Comparar solo nombres.** Un cambio de tipo pasa inadvertido.

## Límites y cuándo no aplica

El refresco solo ve lo que el proveedor expone y lo que el código modela; recursos creados por completo fuera de él pueden quedar invisibles. La deriva lenta de `SE-442` exige series de tiempo y presupuestos, no una comparación puntual. Los experimentos de `SE-402` usan datos sintéticos.
