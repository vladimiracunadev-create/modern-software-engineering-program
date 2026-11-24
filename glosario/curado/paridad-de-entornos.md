# Paridad de entornos

## Definición

La **paridad de entornos** es el grado en que los entornos (desarrollo, preproducción, producción) coinciden en forma, versiones y configuración que afecta al comportamiento (`SE-403`). La idea viene de la metodología de las doce factores. No es identidad: el tamaño, los datos y los secretos son distintos y deben serlo.

## Por qué importa

Un entorno de preproducción que ya no se parece a producción da una falsa seguridad: pasa pruebas que producción no pasaría. La decisión que cambia es qué se mantiene igual a propósito y qué se deja diferir: se invierte en que lo que afecta al comportamiento coincida, para que lo que se prueba sea lo que se despliega.

## Cómo funciona

La metodología de las doce factores identifica tres brechas que la paridad intenta cerrar, y `SE-403` las recoge:

- **De tiempo**: el código tarda semanas en llegar a producción.
- **De personal**: quien escribe el código no lo despliega.
- **De herramientas**: se usa una base distinta en desarrollo que en producción.

El criterio práctico es distinguir qué debe coincidir y qué no. Debe coincidir **la forma, las versiones y la configuración que afecta al comportamiento**. No debe coincidir el tamaño (preproducción puede ser más pequeña), los datos (no se copian datos reales de personas sin motivo) ni los secretos (cada entorno tiene los suyos).

Los síntomas que da la clase muestran por qué importa y cómo se pierde. «Preproducción pasa y producción falla» ocurre cuando las configuraciones divergieron; la corrección es promoción periódica (llevar los cambios de configuración por la misma ruta a todos los entornos) y comparación semanal. «Un script de desarrollo afecta producción» ocurre cuando la frontera entre entornos es una convención (misma cuenta, prefijos en los nombres); se corrige con una cuenta por entorno con políticas heredadas. Ambas ideas se conectan con el radio de explosión y la separación de funciones.

## Ejemplo

Preproducción usa una versión menor de la base y una configuración de caché distinta de producción. Una consulta que pasa las pruebas allí falla en producción porque la versión de producción optimiza distinto. La comparación semanal de configuración habría mostrado la divergencia. Ejemplo ilustrativo del patrón de `SE-403`.

## Errores y confusiones comunes

- **Un script de desarrollo afecta producción**: misma cuenta y prefijos como frontera; se corrige con una cuenta por entorno.
- **Preproducción pasa y producción falla**: configuraciones que divergieron; se corrige con promoción periódica y comparación semanal.
- **Confundir paridad con copia exacta**: los datos y los secretos deben ser distintos.
- **Mantenerla solo la primera vez**: la divergencia se acumula sin comprobación.

## Límites y cuándo no aplica

`SE-403` precisa que sus experimentos son sintéticos: los 24 recursos, el 5 % de acciones comodín, la frecuencia de edición manual, los 12 permisos y los 6 pares son supuestos del autor, y no se evaluó ninguna organización real. La paridad completa puede ser demasiado cara (replicar la capacidad de producción); se elige qué diferencias se aceptan y se documentan. Y no sustituye observar producción: algunas fallas solo ocurren con carga y datos reales.
