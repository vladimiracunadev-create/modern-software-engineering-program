# Marca de agua

## Definición

La **marca de agua** (*watermark*) es el instante hasta el que se decide esperar a los rezagados de una ventana de un flujo de datos. `SE-362` (ingesta batch y streaming) la presenta como «la ventana de las 10:00 se cierra cuando el reloj de llegada pasa de las 11:10»; `SE-290` la define como la estimación del tiempo del evento hasta el cual se espera que hayan llegado todos los datos. No es la marca de agua de imágenes ni de documentos.

## Por qué importa

Un flujo no sabe si ya llegó todo lo de una ventana. La marca de agua fija cuánto se espera y qué se declara tardío. Es una decisión de compromiso entre resultados completos y resultados a tiempo, no un detalle técnico.

## Cómo funciona

Cada evento tiene dos tiempos: cuándo *ocurrió* y cuándo *llegó* (`SE-290`). Contar «entregas por minuto» con el tiempo de llegada mezcla minutos; contarlas con el tiempo del evento exige decidir cuándo una ventana está completa. Los eventos que llegan después de la marca son **tardíos** y se descartan, se aplican como corrección o se envían a un canal aparte. La **tolerancia de retraso** fija el compromiso: esperar más da resultados más completos y más tardíos.

El laboratorio de `SE-362` muestra la forma de la curva: un flujo sin tolerancia dejó fuera de su ventana 315 de 10 000 eventos (3,15 %); con 1 minuto de tolerancia, 262; con 10 minutos, 257; con 1 hora, 229; con 6 horas, 0. La curva es plana mientras la tolerancia sea menor que el retraso típico de los rezagados y cae de golpe cuando lo supera, porque los tardíos están concentrados entre 1 y 6 horas.

## Ejemplo

Con los datos de la clase, una tolerancia de 10 minutos casi no mejora lo que logra la de 1 minuto (257 frente a 262 tardíos), y cuesta diez veces más latencia; subir a 6 horas elimina los tardíos pero retrasa cada resultado seis horas. La decisión depende de quién consume el número y cuánto vale la exactitud frente a la frescura.

## Errores y confusiones comunes

- **Usar el tiempo de llegada como tiempo del evento.**
- **Elegir una tolerancia sin mirar la distribución de retrasos reales.**
- **Descartar los tardíos sin registrarlos,** perdiendo la evidencia de que ocurrieron.
- **Esperar que exista una tolerancia universal correcta:** `SE-290` dice que no existe.

## Límites y cuándo no aplica

La marca de agua es una *estimación*; un evento puede llegar después de cualquier tolerancia. Los datos de `SE-362` son sintéticos, con retrasos concentrados entre 1 y 6 horas por construcción. En procesamiento por lotes, donde la ventana se cierra por calendario y se reprocesa, el problema se aborda con reprocesos.
