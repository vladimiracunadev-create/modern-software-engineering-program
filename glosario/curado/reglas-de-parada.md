# Reglas de parada

## Definición

Una **regla de parada** es un procedimiento que, tras cada observación o lote, decide continuar, detener por futilidad o detener por éxito, con tasas de error conocidas (SE-130). Se fija antes de empezar el experimento, junto con los criterios de éxito y de no éxito.

## Por qué importa

Una regla fijada de antemano ahorra recursos cuando la idea es mala y limita cuántas ideas buenas se pierden. Sin regla, la decisión de seguir o parar se toma mirando los datos y bajo presión, con tendencia a seguir con ideas que no funcionan o a parar con las que podrían. Cambia la gestión de experimentos: parar es una decisión prevista, no una improvisación.

## Cómo funciona

SE-130 describe la **regla de futilidad**: se abandona si, dado lo observado, la probabilidad de que la tasa real supere el umbral cae por debajo de un valor declarado (por ejemplo, 5 %). Por ejemplo, si el éxito exige una tasa de al menos 10 % y tras 60 personas se han observado 2 conversiones, la probabilidad posterior de que la tasa real supere 10 % es pequeña y la regla ordena parar.

El **costo** está declarado: ahorra personas cuando la idea es mala, **a costa de un pequeño porcentaje de ideas buenas abandonadas por mala suerte**. Ese porcentaje es una elección y se calcula por **simulación**: se simula una idea buena y se cuenta con qué frecuencia la regla la abandonaría. El umbral se elige con el costo en la mano: cuánto cuesta perder una idea buena frente a cuánto cuesta seguir con una mala. Lo que no vale es decidir sobre la marcha, mirando los resultados repetidamente y parando cuando conviene, lo que infla los errores.

El documento de abandono de la plataforma conserva por cada hipótesis: criterio de éxito, criterio de no éxito, **zona gris** con su acción, regla de parada y su error simulado, ventana, responsable (externo al equipo que construye, para evitar sesgos), fecha de fijación y el cierre: qué se aprendió, qué se desmonta y qué reabriría la idea. El criterio se fecha antes de empezar y no se reescribe tras mirar.

## Ejemplo

Hipótesis: tasa de interés ≥ 10 %. Regla: parar por futilidad si, tras al menos 50 personas, la probabilidad posterior de que la tasa real sea ≥ 10 % es menor que 5 %; parar por éxito si es mayor que 95 %. Simulación: con una tasa real del 12 %, la regla abandona por error el 4 % de las veces. Se acepta ese 4 % o se ajusta el umbral. (Ilustración del método de SE-130; las cifras son de ejemplo.)

## Errores y confusiones comunes

- **La regla abandona demasiadas ideas buenas**: umbral de futilidad demasiado alto para el costo de perder una; corrección: simular con tasas realistas y elegir el umbral con el costo en la mano.
- **Parar cuando el resultado «parece bueno».**
- **Responsable que construye y decide parar.**
- **No declarar la zona gris.**

## Límites y cuándo no aplica

Las tasas de error dependen de los supuestos de la simulación. Con muestras pequeñas el comportamiento es muy variable. Una regla estadística no tiene en cuenta consideraciones éticas o de seguridad que podrían exigir parar antes.
