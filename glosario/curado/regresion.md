# Regresión

## Definición

Una **regresión** es la pérdida de algo que antes funcionaba. Las clases la definen con el mismo núcleo y distintos objetos: `SE-035` como la pérdida de una propiedad previamente satisfecha, `SE-069` como un defecto corregido que reaparece, `SE-179` como la reaparición de un defecto ya reparado y `SE-567` como un criterio que estaba cumplido y deja de estarlo tras un cambio. No hay que confundirla con el defecto original: la regresión es el retroceso tras un cambio.

## Por qué importa

Cada cambio, incluso una reparación, puede romper algo que no se estaba mirando. `SE-035` formula la regla: la regresión busca que la corrección no haya roto otro contrato. Una reparación que se comprueba solo en el caso que falló no demuestra que el sistema siga bien.

## Cómo funciona

La defensa es conservar y repetir la comprobación. En `SE-035`, el kit de diagnóstico multiplataforma conserva versiones y una matriz de plataformas para que otra persona pueda repetir la reparación y verificar contratos vecinos. `SE-587` añade el paso final del procedimiento de diagnóstico de un agente: tras reproducir, leer la traza, formular una hipótesis sobre una sola pieza y cambiarla, se añade el caso a la regresión. En los bucles automáticos de `SE-567`, cada pasada debe ejecutar todos los criterios y detenerse ante una regresión; si no, cada pasada arregla algo y rompe otra cosa. `SE-179` pide un auditor que se ejecute en cada cambio y una lista manual periódica.

## Ejemplo

En `SE-567`, un bucle de mejora que en cada pasada ejecuta solo el criterio que acaba de arreglar puede romper otro criterio sin notarlo; con una batería completa en cada pasada, la regresión aparece en la pasada en que ocurre y el bucle se detiene. En `SE-035`, reparar solo el caso feliz de un entorno deja sin verificar los contratos vecinos; la matriz de regresión adversa los recorre.

## Errores y confusiones comunes

- **Se repara solo el caso feliz.** No se verificaron contratos vecinos; corrección (`SE-035`): ejecutar una matriz de regresión adversa.
- **Cada pasada arregla algo y rompe otra cosa.** Regresiones sin batería de criterios completa; corrección (`SE-567`): ejecutar todos los criterios en cada pasada y detener ante regresión.
- **Un cambio rompe lo reparado.** No hay regresión comprobada; corrección (`SE-179`): auditor en cada cambio y lista manual periódica.
- **El bucle no acaba nunca.** Faltan condiciones de parada; corrección: máximo de pasadas, sin progreso, presupuesto y regresión (`SE-567`).

## Límites y cuándo no aplica

Una prueba de regresión solo vigila lo que se escribió: un contrato que nadie convirtió en comprobación puede romperse sin aviso. Las clases sitúan la regresión dentro de contextos concretos (entornos, auditoría de un flujo, bucles de un agente), por lo que lo que cuenta como «lo que antes funcionaba» depende de cada contexto y de qué criterios se conservaron.
