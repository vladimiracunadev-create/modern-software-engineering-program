# Guarda

## Definición

Una **guarda** es, en producto (`SE-139`), un límite de una métrica que no debe empeorar al perseguir la métrica norte, con umbral, responsable y acción. El programa usa la palabra con sentidos emparentados:

- **Guarda de métrica** (`SE-139`, `SE-607`): métrica con umbral cuyo incumplimiento detiene o revierte un cambio o despliegue.
- **Guarda de código** (`SE-062`): comprobación temprana que protege el camino principal.
- **Guarda de transición** (`SE-057`): condición para habilitar una transición en un modelo de estados.

## Por qué importa

Optimizar una sola métrica daña lo que no se mide: si la métrica norte sube y el producto empeora, faltan guardas (`SE-139`). Las guardas convierten «tener cuidado» en una regla ejecutable. El presupuesto de error del enfoque de fiabilidad es una guarda: fija cuánto riesgo se acepta para ir más rápido.

## Cómo funciona

Una guarda de métrica tiene tres piezas (`SE-139`): **umbral** (fijado antes de optimizar, sin él es una opinión), **responsable** (quién decide) y **acción** (detener el despliegue, revertir o convocar revisión). Ejemplos: tasa de quejas, tiempo de carga, tasa de errores, baja del servicio. En `SE-607`, la métrica con umbral detiene o revierte el despliegue de un modelo. Hay que cuidar la cantidad: con demasiadas, el equipo ignora las alarmas y aparecen comparaciones múltiples (falsas alarmas por azar). En código (`SE-062`), una cláusula de guarda sale temprano del camino principal ante una entrada inválida, de modo que el resto de la función asume lo ya comprobado. En modelos de estados (`SE-057`), una transición solo se habilita si su condición se cumple.

## Ejemplo

`SE-139` hace un experimento con un optimizador de recordatorios: sin guarda de bajas de notificación, el optimizador sube el envío hasta cruzar el umbral de quejas. Con guarda, el experimento se detiene. Ilustración:

```python
def desplegar(m):
    if m["bajas"] > 0.02: return revertir()    # guarda: umbral, acción y dueño documentados
    return publicar()
```

## Errores y confusiones comunes

- **La métrica norte sube y el producto empeora.** Causa: no hay guardas; corrección: definirlas con umbral antes de optimizar (`SE-139`).
- **El equipo ignora las alarmas.** Causa: hay demasiadas y sin corrección por comparaciones múltiples; corrección: reducirlas (`SE-139`).
- **Una guarda se cruza y nadie actúa.** Causa: sin responsable ni acción; corrección: escribir quién decide y qué ocurre (`SE-139`).

## Límites y cuándo no aplica

Una guarda protege lo que se midió: no detecta daños no medidos. Un umbral mal elegido bloquea cambios buenos o deja pasar malos. Y los tres sentidos no son intercambiables: una guarda de métrica opera sobre agregados y con retraso; una guarda de código, sobre una entrada concreta y de inmediato.
