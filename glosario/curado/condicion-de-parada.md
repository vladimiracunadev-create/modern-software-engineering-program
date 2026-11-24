# Condición de parada

## Definición

Una **condición de parada** es una regla explícita que detiene un bucle de agente y define qué se hace después. Es la definición de `SE-567` y `SE-575`. Un sentido emparentado aparece en `SE-509`, en ingeniería del caos: la alarma que detiene un experimento si el sistema alcanza un estado inaceptable. En ambos, la idea es la misma: el fin del proceso no se deja al azar ni al agotamiento de recursos.

## Por qué importa

Un bucle sin condición de parada, dice `SE-567`, se detiene cuando se acaba el dinero o la paciencia. Es una decisión de diseño que cambia el riesgo: con parada explícita, el peor caso está acotado y es predecible; sin ella, un agente puede trabajar toda la noche sin avanzar (`SE-575`) y la factura o el daño llegan antes que cualquier revisión.

## Cómo funciona

`SE-567` enumera cinco condiciones útiles, y cada una vigila una causa distinta de no terminar:

1. **Convergencia:** el verificador no encuentra nada y el trabajo acaba bien. Es la única salida «feliz».
2. **Máximo de pasadas:** tras N pasadas se detiene aunque haya criterios abiertos; es la condición que la guía de Anthropic cita como habitual para mantener el control.
3. **Sin progreso:** el número de criterios abiertos no baja en dos pasadas seguidas.
4. **Presupuesto:** tope de tokens, tiempo o dinero.
5. **Regresión:** una pasada reabre criterios ya cumplidos; indica que el agente deshace su propio trabajo.

Salvo la convergencia, la acción es la misma: **detener, guardar el estado y llamar a una persona** con la lista de lo abierto. Por eso la parada incluye el «qué se hace después»: una parada que solo mata el proceso pierde el contexto.

En ingeniería del caos (`SE-509`), la condición es una alarma sobre el sistema: si una señal cruza un umbral definido de antemano, el experimento se aborta y el estado se restaura.

## Ejemplo

Un agente corrige fallos de un conjunto de criterios de aceptación. Pasada 1: abiertos 7. Pasada 2: abiertos 4. Pasada 3: abiertos 4. Pasada 4: abiertos 4 → *sin progreso* (dos pasadas seguidas sin bajar). El bucle se detiene, guarda el estado y entrega a una persona la lista de los 4 criterios abiertos y lo intentado. Si en la pasada 5 un criterio ya cumplido se reabriera, saltaría *regresión* aun antes. (Los números son ilustración, no datos de la clase.)

## Errores y confusiones comunes

- **El bucle no acaba nunca.** No hay condiciones de parada; corrección de `SE-567`: máximo de pasadas, sin progreso, presupuesto y regresión.
- **Poner solo un máximo enorme.** `SE-575` señala que un agente puede trabajar toda la noche sin avanzar; hay que añadir estado repetido y falta de avance, con presupuesto por tarea.
- **Parar sin guardar el estado.** Se pierde lo hecho y la persona no sabe qué falta.
- **Confundirla con el criterio de aceptación.** Este define cuándo el trabajo está bien; la condición de parada define cuándo dejar de intentarlo aunque no lo esté.

## Límites y cuándo no aplica

Las condiciones de no convergencia dependen de poder medir el progreso: si el verificador es débil, «sin progreso» o «convergencia» pueden ser engañosos (un verificador que no ve un defecto declara convergencia). Un máximo demasiado bajo corta trabajo legítimo; uno demasiado alto no protege. En un único paso de modelo sin bucle no hay nada que detener. Y en experimentos de caos, una alarma sobre una señal mal elegida puede no saltar a tiempo.
