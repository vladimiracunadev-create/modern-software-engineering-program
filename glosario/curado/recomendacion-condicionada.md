# Recomendación condicionada

## Definición

Una **recomendación condicionada** es una conclusión de ingeniería formulada con la forma que `SE-095` indica: **«si [carga y garantía], entonces [opción]; si cambia [umbral], revisar»**. En lugar de decir «use X», dice bajo qué condiciones X es la mejor opción y qué medición haría cambiar la recomendación. Es la conclusión con la que cierra el taller de elección de estructuras: acompaña al perfil de operaciones y a la matriz de compromisos, y se entrega con los datos y los *scripts* que la respaldan.

## Por qué importa

Un benchmark corre en una máquina, con una carga y unos datos concretos. Convertir su resultado en un estándar universal («siempre use `set`») es la forma más común de transformar una medición en un dogma. La decisión que cambia es cómo se comunica un resultado: con sus condiciones de validez explícitas. `SE-095` lo dice así: declarar las condiciones **evita convertir un benchmark del taller en estándar universal**. Además, quien lee la recomendación puede comprobar si su situación cumple las condiciones, y sabe cuándo volver a medir.

## Cómo funciona

La recomendación tiene tres partes, y cada una aporta algo:

- **Condiciones (el «si»):** la carga (mezcla de operaciones y tamaños), las garantías necesarias (orden, estabilidad, memoria máxima) y el objetivo (el SLO). Son las que definen el dominio de validez.
- **Opción (el «entonces»):** la estructura o el algoritmo recomendado.
- **Disparador de revisión:** la medición o el cambio que invalidaría la recomendación, por ejemplo un umbral de tamaño o de proporción de operaciones.

Se acompaña de los **datos y *scripts*** que la sustentan, de modo que otra persona pueda reproducir la medición. Así la recomendación es una **hipótesis falsable**, no una autoridad: puede ser refutada por una medición posterior, y eso es una propiedad deseable.

## Ejemplo

Siguiendo el taller de `SE-095` (ilustración, números inventados):

```text
Si el perfil es >= 90 % consultas de pertenencia, con más de 1 000 consultas
por cada construcción, y se acepta ~2x la memoria de la lista,
entonces usar `set`.
Si el número de consultas por construcción baja de 50, o la memoria supera
el presupuesto, usar lista ordenada con búsqueda binaria.
Revisar si cambia la mezcla de operaciones o el tamaño pasa de 10^6.
Datos y scripts: bench/pertenencia/ (commit abc1234).
```

Un error documentado en la clase es que la recomendación no convence a otro equipo porque no declara carga ni tamaño; la corrección es escribir el perfil antes de medir. Otro: elegir `set` para todo; se corrige calculando el umbral de reutilización y la memoria.

## Errores y confusiones comunes

- **Recomendación absoluta.** «Siempre X» sin condiciones.
- **Condiciones implícitas.** El lector no sabe para qué carga vale.
- **Sin disparador de revisión.** La recomendación sobrevive al contexto que la justificaba.
- **Datos que no se pueden reproducir.** Nadie puede comprobar ni refutar.

## Límites y cuándo no aplica

El taller cubre cargas sintéticas y una plataforma (`SE-095`): las condiciones de la recomendación son tan buenas como la representatividad de esas cargas. En decisiones pequeñas y reversibles, escribir una recomendación condicionada formal es desproporcionado. Y una recomendación condicionada con demasiadas condiciones deja de ser útil: si cada caso exige medir de nuevo, se ha perdido el valor de decidir.
