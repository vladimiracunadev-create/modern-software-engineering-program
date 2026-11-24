# Comparación pareada

## Definición

Una **comparación pareada** compara dos versiones de un sistema sobre *los mismos casos*, de modo que cada caso aporta un par de resultados. `SE-597` la usa para decidir si una versión nueva de un sistema con modelos es mejor que la anterior; `SE-603` la aplica a dos configuraciones sobre los mismos datos y las mismas particiones. Lo que importa en ella no son los casos donde ambas aciertan o ambas fallan, sino los casos donde **discrepan**.

## Por qué importa

Cambia la forma de aprobar un cambio. Comparar dos tasas de acierto globales (82 % contra 84 %) mezcla la diferencia real con la variación entre conjuntos de casos. Al fijar los casos, la dificultad de cada uno se cancela y solo queda el efecto de la versión. Además obliga a dos preguntas distintas que suelen confundirse: ¿qué tan seguido declaro mejor algo que no lo es?, y ¿qué tan seguido detecto una mejora que sí existe?

## Cómo funciona

`SE-597` usa el esquema de McNemar. Sea `b` el número de casos que la versión 2 acierta y la 1 falla, y `c` el de los que la 1 acierta y la 2 falla. El estadístico

```text
z = (b − c) / √(b + c)
```

mide cuánto se aparta de cero la diferencia entre discrepancias. Si se exige `z > 1,645` (una cola, 5 %), la tasa de **falsos positivos**, es decir, declarar mejor una versión idéntica, queda cerca del 5 %. La causa de que funcione es que bajo «no hay diferencia» las discrepancias deberían repartirse parejo entre `b` y `c`.

La **potencia** es otra magnitud: la probabilidad de detectar una mejora real. Depende sobre todo del número de casos, no del umbral.

## Ejemplo

En el experimento de `SE-597` (sistemas sintéticos), con 50, 100, 400 y 1 600 casos los falsos positivos fueron 5,6 %, 5,1 %, 4,8 % y 6,8 %: la prueba protege igual con pocos o muchos casos. La potencia para una mejora real de unos 4 puntos fue 10,1 %, 15,2 %, 37,2 % y 81,8 %. Con 100 casos, entonces, una mejora real de 4 puntos casi nunca se detecta: la prueba no se equivoca al aprobar, pero tampoco aprueba. La conclusión práctica es dimensionar el conjunto de evaluación según la mejora que se quiere poder ver.

## Errores y confusiones comunes

- **Creer que «sin diferencia significativa» significa «iguales».** Con pocos casos la potencia es baja: la ausencia de señal no es ausencia de efecto.
- **Comparar sobre casos distintos o particiones distintas.** Rompe el emparejamiento y reintroduce la variación que se quería cancelar.
- **Confundir falsos positivos con potencia.** Quedar cerca del 5 % de falsos positivos no dice nada de cuántas mejoras reales se pierden.
- **Repetir la prueba hasta que sale.** Cada repetición sobre los mismos casos agrega oportunidades de falso positivo; fija el criterio antes.

## Límites y cuándo no aplica

`SE-597` declara que los sistemas, la dificultad por caso, el sesgo del juez y la traza son sintéticos, que usa una prueba z de McNemar de una cola con 800 evaluaciones por celda, y que no se evaluó ningún modelo real ni herramienta de evaluación. McNemar sirve para resultados binarios (acierta/falla); para puntuaciones continuas o para varias métricas se necesita otra prueba. Asume casos independientes y representativos de lo que ocurrirá en producción: si el conjunto no refleja el uso real, la comparación es rigurosa sobre lo equivocado.
