# Borde de la red

## Definición

El **borde de la red** (*edge*) es el conjunto de puntos de ejecución cercanos al usuario que ejecutan cómputo o sirven datos sin pasar por el origen. Es el sentido de `SE-331`. `SE-273` lo usa con un matiz del mundo embebido: dispositivos y pasarelas cercanos a la fuente de los datos, donde se procesa antes de enviar a la nube. En ambos, la idea es la misma: acercar el trabajo a quien lo origina o lo consume.

## Por qué importa

La decisión es qué piezas viven lejos y cuáles cerca. Acercar reduce la latencia de ida y vuelta y descarga el origen; a cambio cuesta consistencia, operación y limitaciones del entorno. `SE-331` lo trata como un trade-off, no como mejora gratuita.

## Cómo funciona

`SE-331` describe tres beneficios y tres costos:

- **Beneficios:** menor latencia, menos carga en el origen, y funcionamiento con datos locales cuando el origen está lejos o inaccesible.
- **Costos:** *consistencia* (las copias pueden estar desactualizadas); *operación* (muchos puntos que desplegar y observar); *limitaciones del entorno de ejecución* (lo que puede correr en el borde es menos que en el origen).

Por eso una pieza se lleva al borde si su escenario es de latencia o de disponibilidad local y si tolera datos algo viejos. Es natural para contenido que cambia poco o para decisiones con datos locales. El **estado autoritativo sigue en el origen**.

En `SE-273` (IoT), el borde son dispositivos y pasarelas que filtran, agregan o deciden localmente antes de subir datos, lo que ahorra ancho de banda y permite seguir operando sin conexión.

## Ejemplo

`SE-331` asigna cada pieza de la plataforma de entregas a un estilo según su escenario: unas funciones bajo demanda, otras en servidor, y las que sirven contenido estable cerca del usuario. Un ejemplo ilustrativo (no de la clase): una página de ayuda que cambia una vez al mes se sirve desde el borde; el saldo de una cuenta, no, porque una copia vieja daría una respuesta incorrecta.

## Errores y confusiones comunes

- **Llevar al borde estado que exige consistencia fuerte:** copias viejas dan respuestas erróneas.
- **Subestimar la operación:** desplegar y observar muchos puntos es trabajo propio.
- **Confundir el borde de `SE-331` (puntos de presencia de una red) con el de `SE-273` (pasarelas y dispositivos):** comparten el principio, no la infraestructura.

## Límites y cuándo no aplica

No conviene cuando el dato cambia constantemente y debe leerse al instante, cuando el entorno limitado no soporta la lógica, o cuando el volumen de tráfico no justifica operar muchos puntos. Las simulaciones de `SE-331` no midieron ningún proveedor real; sus tiempos y precios son construcciones del autor.
