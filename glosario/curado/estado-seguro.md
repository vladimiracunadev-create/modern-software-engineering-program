# Estado seguro

## Definición

Un **estado seguro** (*safe state*) es aquel en que un sistema con un fallo causa el menor daño posible, y que se define de antemano. Es el sentido de `SE-274` (safety, seguridad y vida útil prolongada). El adjetivo no significa «seguro» en el sentido de ciberseguridad: se refiere a seguridad funcional (*safety*), es decir, a no causar daño a personas o al entorno cuando algo falla.

## Por qué importa

Un fallo detectado debe llevar a un lugar conocido, no a un comportamiento improvisado. `SE-274` advierte la razón: quien programa bajo presión elige el estado que facilita probar, no el que minimiza el daño. Definirlo de antemano, por peligro, lo convierte en una decisión de diseño revisable.

## Cómo funciona

El mecanismo, según `SE-274`:

1. **Identificar el peligro** (qué daño puede ocurrir).
2. **Definir el estado de menor daño** para ese peligro: el extractor encendido si no se sabe el nivel de CO₂, la puerta desbloqueada o bloqueada según el riesgo, el actuador parado. El estado seguro **no siempre es «apagado»**: depende del peligro.
3. **Documentarlo.**
4. **Probarlo:** forzar el fallo (`SE-275`, inyección de fallos) y comprobar que se alcanza.

Se combina con detección de fallos (sensores diversos con comparación, temporizador de vigilancia) y con un análisis de peligros por escrito.

## Ejemplo

El análisis de peligros del nodo de `SE-274` tiene cuatro filas. Primera: el extractor no arranca con CO₂ alto; defensa: dos sensores de principios distintos con comparación, estado seguro «extractor encendido» si discrepan, y prueba por inyección de fallos. Segunda: el firmware se cuelga; defensa: temporizador de vigilancia con plazo de 5 s, alimentado solo tras una comprobación de salud. Tercera: un contador de tiempo da la vuelta; defensa: restas sin signo y una prueba que simula el arranque a 49 días. Cuarta: un atacante apaga el extractor.

## Errores y confusiones comunes

- **Equiparar estado seguro con «apagado».** Apagar un extractor con CO₂ alto es el peligro.
- **Elegir el estado que facilita probar** en vez del que reduce el daño.
- **No probar el camino al estado seguro:** un estado seguro nunca alcanzado en pruebas es una suposición.
- **Confundirlo con seguridad informática,** que protege contra atacantes (aunque el cuarto peligro de la clase une ambas).

## Límites y cuándo no aplica

No existe un estado seguro único válido siempre: algunos sistemas (un avión en vuelo) no pueden «parar». El análisis se limita a los peligros identificados. Los números de `SE-274` son un caso didáctico del nodo ambiental, no una certificación de seguridad funcional.
