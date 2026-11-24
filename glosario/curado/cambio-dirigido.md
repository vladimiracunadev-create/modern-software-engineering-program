# Cambio dirigido

## Definición

Un **cambio dirigido** es, en el taller de `SE-083`, una modificación pequeña y fija que se introduce **después** de que varias soluciones ya son equivalentes en resultado: se añade una regla de negocio nueva a cada implementación y se observa el **diff** que cada una necesita. La palabra «dirigido» indica que el cambio lo elige quien compara, no cada autor, para que todas las soluciones se enfrenten exactamente al mismo cambio. Es un instrumento de comparación propio del programa, no un término estándar.

## Por qué importa

Comparar paradigmas (imperativo, orientado a objetos, funcional, entre otros) por su gusto o por su elegancia no decide nada. Lo que se vive después, al mantener el código, es cuánto cuesta cambiarlo. El cambio dirigido convierte esa pregunta en un dato: cuántos archivos, funciones y pruebas se tocan. La decisión que cambia es el criterio de elección: no «la solución más corta», sino la que localiza mejor el cambio. `SE-083` aclara el objetivo: medir **superficie de cambio**, no velocidad de tecleo.

## Cómo funciona

El procedimiento tiene un orden que importa:

1. **Lograr equivalencia.** Todas las soluciones producen el mismo resultado ante los mismos casos; sin esto, comparar diffs es comparar cosas distintas.
2. **Fijar el cambio.** Una sola regla nueva, escrita antes de implementarla en ninguna solución.
3. **Aplicarlo en cada solución** y medir el diff: archivos tocados, funciones modificadas, pruebas que cambian.
4. **Interpretar.** Una solución que exige tocar cinco lugares revela **dispersión** de la decisión aunque conserve el resultado: la regla vivía repartida.

La razón por la que funciona es la misma que sostiene la cohesión: si una decisión de negocio está concentrada, cambiarla es local; si está repartida, cada cambio dispara ediciones en varios sitios y cada una puede olvidarse.

## Ejemplo

En el motor de reglas comparado de `SE-083`, una recomendación contiene acción, evidencia usada, versión de política y explicación. Tras igualar las cinco versiones, se agrega una regla (por ejemplo, una condición nueva sobre la prioridad). En una versión la regla vive en una tabla de datos y el cambio es una fila; en otra está dispersa en tres métodos de tres clases. Registro de ilustración, con números inventados:

```text
solucion    archivos  funciones  pruebas_nuevas
tabla            1         0          1
clases           3         3          2
```

Los números no dicen cuál es «mejor» en general: dicen qué tan local fue este cambio en este problema.

## Errores y confusiones comunes

- **Medir antes de igualar.** Sin equivalencia, el diff más pequeño puede ser el de la solución incorrecta.
- **Elegir un cambio que favorece a una solución.** El cambio debe fijarse antes de ver los diffs.
- **Medir líneas tecleadas.** Importa la dispersión, no la longitud.
- **Pruebas que no ejercitan la regla.** `SE-083` advierte que un defecto plantado puede sobrevivir si falta el caso mínimo; hay que comprobar que el mutante falla. Y si dos versiones divergen solo con ciertos tipos, el contrato no definía los tipos inválidos.

## Límites y cuándo no aplica

El taller compara **un** cambio y una carga pequeña; no demuestra mantenibilidad a largo plazo (`SE-083`). Un solo cambio puede favorecer una forma y penalizar otra por azar; con otro cambio el orden podría invertirse. Por eso el proyecto siguiente amplía pruebas, criterios y reporte para una comparación defendible. No sustituye observar el costo de mantenimiento real en un sistema vivo ni sirve cuando el equipo no puede dedicar tiempo a implementar la misma solución varias veces.
