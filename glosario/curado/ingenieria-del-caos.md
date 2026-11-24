# Ingeniería del caos

## Definición

La **ingeniería del caos** es la disciplina de experimentar sobre un sistema para ganar confianza en su capacidad de resistir condiciones turbulentas (`SE-507`, que toma la definición oficial del campo y subraya la palabra «confianza»).

## Por qué importa

Un sistema declarado resiliente en un documento no es un sistema probado resiliente. Los experimentos sacan a la luz debilidades antes de que lo haga una caída real.

## Cómo funciona

`SE-507` fija el vocabulario: una **falla** es un evento o condición que se aparta del funcionamiento normal (un proceso que cae, un disco que se detiene, una dependencia lenta); una **debilidad sistémica** es una propiedad que convierte esa falla en daño visible para las personas usuarias; un **experimento** es una intervención controlada que busca *refutar* una afirmación sobre esa propiedad. Esa afirmación es la hipótesis de estado estable, y el experimento se detiene con una condición de parada si el daño crece. Se inyectan fallas de red, latencia, dependencias y datos.

## Ejemplo

`SE-507` ejecuta tres experimentos con tiempo virtual y semillas fijas sobre el cliente de la API de entregas, mostrando que los reintentos sin protección amplifican la carga y que el cortacircuitos la contiene.

## Errores y confusiones comunes

- **Todo parece resiliente en el documento.** Se revisó la presencia de mecanismos, no su comportamiento; inyectar la falla que cada mecanismo dice cubrir.
- **El servicio no se recupera tras la falla.** Reintentos y cola mantienen la sobrecarga; cortacircuitos, descarte de carga o pausa con azar.
- **Confundirlo con romper cosas al azar.** Es un experimento con hipótesis, radio acotado y parada.

## Límites y cuándo no aplica

Los experimentos de la clase no se inyectaron en un sistema real. Ejecutarlos en producción exige observabilidad, radio de impacto acotado y capacidad de abortar.
