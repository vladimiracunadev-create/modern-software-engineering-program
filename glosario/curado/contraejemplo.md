# Contraejemplo

## Definición

En verificación formal, un **contraejemplo** es la traza de pasos desde el estado inicial hasta una violación de una propiedad (SE-453). SE-161 lo precisa: traza finita de transiciones que lleva del estado inicial a un estado que viola una propiedad. Es la salida de un verificador de modelos cuando la propiedad no se cumple.

## Por qué importa

Es la salida más útil de un verificador: un escenario concreto. Un resultado «la propiedad falla» no dice cómo reproducirlo; un contraejemplo da la secuencia exacta de pasos, que se puede leer, discutir y convertir en una prueba. Cambia cómo se encuentran los defectos de concurrencia y protocolo: no se esperan a observarlos en producción.

## Cómo funciona

SE-453 describe el método. Un modelo describe el sistema como un conjunto de estados posibles (valores de las variables y posición de cada proceso) y las transiciones que pueden ocurrir. Una **propiedad de seguridad** es un invariante: una condición que debe cumplirse en todos los estados alcanzables («no hay dos procesos en la sección crítica»). El verificador parte del estado inicial, explora los sucesores con una **búsqueda en anchura** y comprueba el invariante en cada estado. Si encuentra uno que lo viola, reconstruye el camino que llevó hasta él: ese camino es el contraejemplo.

La búsqueda en anchura tiene una propiedad útil: el primer contraejemplo encontrado es de **longitud mínima**, lo que lo hace más fácil de leer (existe también el contraejemplo mínimo como concepto aparte). Si el verificador agota el espacio sin hallar violación, la propiedad se cumple en el modelo (no necesariamente en el sistema real, porque el modelo es una abstracción).

SE-453 da un caso de laboratorio: un equipo modela en TLA+ el protocolo de reserva de un tramo entre dos controladores ferroviarios, con tres estados por controlador y un canal que puede perder mensajes. El verificador halla en la primera ejecución un contraejemplo de **once pasos**: un mensaje perdido y un reintento hacen que ambos controladores crean tener el tramo. En el sistema real nunca se había observado, y una prueba tradicional difícilmente lo habría producido.

## Ejemplo

Contraejemplo de cuatro pasos (ilustrativo): 1) el controlador A envía «reservar tramo»; 2) el canal pierde el mensaje; 3) A reintenta tras el tiempo de espera y B responde «concedido» al primer envío retrasado; 4) A y B creen tener el tramo. La traza es una receta para escribir una prueba que reproduzca el defecto y para corregir el protocolo. (Reducción didáctica del caso de SE-453.)

## Errores y confusiones comunes

- **Confundir contraejemplo con prueba fallida**: el contraejemplo viene de explorar el modelo, no de ejecutar el sistema.
- **Corregir el modelo y no el sistema** (o al revés).
- **Ignorar un contraejemplo por «improbable».**
- **Creer que la ausencia de contraejemplo prueba el sistema**: solo prueba el modelo.

## Límites y cuándo no aplica

El modelo debe ser fiel a lo que importa; si abstrae mal, el contraejemplo puede ser espurio o faltar uno real. El número de estados crece muy rápido (explosión de estados) y limita lo que se verifica. En lógica y matemáticas, «contraejemplo» tiene también el sentido general de caso que refuta una afirmación universal.
