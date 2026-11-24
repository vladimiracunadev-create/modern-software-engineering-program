# Máquina de estados

## Definición

Una **máquina de estados** es un modelo con un conjunto finito de estados, un estado inicial y transiciones etiquetadas con eventos o acciones, que describe cómo reacciona un sistema a su entorno. SE-161 la presenta como técnica de especificación; SE-239 la usa para el comportamiento de la interfaz; SE-412 la aplica al ciclo de vida de una suscripción (vigente, vencida, cancelada, etc.).

## Por qué importa

Hace explícito qué puede ocurrir y qué decide el acceso. Las reglas de negocio con tiempo suelen describirse con frases sueltas que dejan huecos («si el pago falla, se reintenta»), y los huecos aparecen como defectos. Dibujar estados y transiciones obliga a responder para cada estado qué evento puede ocurrir y a dónde lleva, y a declarar lo que no está permitido.

## Cómo funciona

El modelo tiene cuatro elementos: **estados** (situaciones estables), **eventos** (lo que ocurre), **transiciones** (de qué estado, con qué evento, a qué estado, con qué acción) y un **estado inicial**. La propiedad útil es que el comportamiento queda enumerable: se puede comprobar que cada par (estado, evento) tiene una respuesta definida, que no hay estados inalcanzables y que no hay estados sin salida salvo los finales intencionales. Una matriz estado × evento es una forma de revisar la completitud; las celdas vacías son preguntas pendientes.

SE-412 sigue el ciclo de una suscripción con transiciones explícitas y el ciclo de facturación anclado, y propone un ejercicio de ingeniería inversa: tomar una suscripción real (streaming, nube) y reconstruir su máquina de estados respondiendo qué ocurre si se cancela hoy, si el pago falla o si se cambia de plan a mitad de ciclo; lo que no se pudo responder sin probar es lo que el producto debería haber puesto por escrito.

## Ejemplo

Una suscripción con estados `prueba`, `activa`, `en_mora`, `cancelada`. Transiciones: `prueba → activa` al pagar; `activa → en_mora` si el cobro falla; `en_mora → activa` si el reintento tiene éxito; `en_mora → cancelada` tras agotar reintentos; `activa → cancelada` si la persona cancela. La pregunta «¿qué ocurre si cancelo estando en mora?» expone una celda no definida: hay que decidir si cancela de inmediato o se debe lo adeudado. (Modelo ilustrativo; SE-412 desarrolla uno más completo.)

## Errores y confusiones comunes

- **Estados que son en realidad datos**: si el número de estados crece con cada valor posible de un campo, el modelo es inadecuado.
- **Transiciones implícitas**: el código permite cambios que el modelo no declara.
- **Confundir estado con evento**: «pago fallido» es un evento; «en mora», el estado resultante.
- **Creer que el modelo cubre todo el dominio**: solo cubre el comportamiento que se modeló.

## Límites y cuándo no aplica

SE-412 es explícita en lo que la máquina de estados no decide: los impuestos aplicables (dependen de la jurisdicción del cliente y del producto), la regulación sobre cobros recurrentes y avisos previos, el reconocimiento contable del ingreso en planes anuales y la facturación electrónica que algunos países exigen. Son restricciones reales que se incorporan con asesoría especializada; un procesador de pagos o un servicio de facturación puede absorber parte, con su propio costo y dependencia. Además, con muchos estados concurrentes el modelo se vuelve inmanejable y se descompone en máquinas jerárquicas o en varias máquinas coordinadas.
