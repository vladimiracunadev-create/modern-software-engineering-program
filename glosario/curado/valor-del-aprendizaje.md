# Valor del aprendizaje

## Definición

El **valor del aprendizaje** es la mejora esperada de una decisión gracias a información obtenida antes de decidir, menos el costo de obtenerla (SE-128). Es la versión de producto del «valor de la información»: cuánto vale hacer una prueba antes de comprometerse.

## Por qué importa

Una prueba barata puede evitar construir lo que no funciona; una cara o poco fiable no compensa. Cambia la decisión de investigar: no se prueba «por si acaso», se calcula si la información mejora lo bastante la decisión como para pagarla.

## Cómo funciona

SE-128 da un ejemplo con números. Construir un ítem con **35 % de probabilidad de éxito**, ganancia de **100** y coste de **40** tiene un valor esperado de 0,35 × 100 − 40 = **−5**: no conviene.

Ahora una prueba previa que cuesta 5 y acierta el 90 % de las veces (detecta el éxito real con 90 % y da falso positivo con 10 %). La probabilidad de que salga positiva es 0,35 × 0,9 + 0,65 × 0,1 = 0,38. Si sale positiva, la probabilidad de éxito sube a 0,315 / 0,38 ≈ 0,83, y construir vale 0,83 × 100 − 40 ≈ 43. Se construye **solo si la prueba sale positiva**: valor esperado = 0,38 × 43 − 5 ≈ **+11,3**. La prueba convierte una apuesta perdedora en una decisión informada: el valor esperado neto sube de −5 a +11,3, de modo que el aprendizaje, descontado su costo, aporta valor.

Con una prueba que cuesta **15** y acierta solo el **70 %**, el valor esperado neto es **−8,1** y **conviene no hacerla**: la información es poco fiable y cara. El mecanismo general: la prueba vale lo que mejora la decisión menos lo que cuesta, y depende de tres cosas: la probabilidad previa (si ya es casi seguro, no hay qué aprender), la fiabilidad de la prueba y el costo de equivocarse.

La idea se conecta con las preguntas críticas, los experimentos de demanda y las reglas de parada: todas son formas de comprar información barata antes de gastar mucho.

## Ejemplo

Con los datos de SE-128: sin prueba, −5 (no construir, o construir perdiendo); con una prueba de 5 y 90 % de acierto, +11,3; con una de 15 y 70 %, −8,1. La conclusión práctica es hacer la primera y descartar la segunda. (Cifras de la clase; el cálculo detallado es propio y reproduce sus resultados.)

## Errores y confusiones comunes

- **Hacer pruebas por costumbre** sin calcular su valor.
- **Creer que toda información vale**: una prueba cara y poco fiable destruye valor.
- **Ignorar la probabilidad previa.**
- **Confundir valor de aprender con valor esperado del proyecto.**

## Límites y cuándo no aplica

Los cálculos suponen probabilidades y costos estimables; con estimaciones muy inciertas, el resultado también lo es. Para decisiones baratas y reversibles, aprender antes no compensa. El modelo simple supone una prueba con una sola tasa de acierto, que en la práctica varía.
