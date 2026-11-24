# Entrega continua

## Definición

La **entrega continua** (*continuous delivery*) es la capacidad de que todo cambio verificado pueda desplegarse a producción en cualquier momento, por decisión humana (`SE-485`).

## Por qué importa

Se confunde con dos cosas cercanas, y la confusión lleva a prometer lo que el proceso no hace. `SE-485` separa tres decisiones: **entregar** (dejar cada cambio listo para producción), **desplegar** y **exponer** (quién usa la versión nueva y cuándo).

## Cómo funciona

Cada cambio que pasa la canalización queda en un estado desplegable; la decisión de hacerlo es humana. El **despliegue continuo** (*continuous deployment*) elimina esa decisión: todo cambio que pasa se despliega automáticamente. La **exposición** (liberación, *release*) puede separarse del despliegue con una bandera o con un porcentaje de tráfico. Las tres se confunden porque en muchos equipos ocurren juntas. Para comprobar un despliegue gradual, un **canario** compara la versión nueva con la anterior; su veredicto solo vale con tráfico suficiente.

## Ejemplo

Un equipo despliega cada cambio verificado a producción detrás de una bandera apagada (despliegue continuo), y una persona de producto decide cuándo activarla para el 5 % del tráfico (exposición). Si además la canalización exige una aprobación humana antes de producción, es entrega continua sin despliegue continuo.

## Errores y confusiones comunes

- **El canario dice «sin errores» y producción falla.** Tráfico insuficiente para ver el cambio; calcular la potencia y exigir un tráfico mínimo (`SE-485`).
- **Se retiran versiones buenas.** Umbral laxo o tasa base inestable; calcular la tasa de falsas alarmas y usar ventanas comparables.

## Límites y cuándo no aplica

La entrega continua exige pruebas automáticas confiables y desplegar sin dolor; sin eso, «siempre desplegable» es una promesa vacía. En entornos regulados puede haber aprobaciones que deban permanecer.
