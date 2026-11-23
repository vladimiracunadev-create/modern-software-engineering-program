# Idempotencia

## Definición

Una operación es **idempotente** cuando ejecutarla una vez o varias veces con la misma intención deja el sistema en el mismo estado. La idea no pide que la operación «no haga nada» la segunda vez ni que tarde lo mismo: `SE-114` precisa que idempotente es respecto del *efecto observable*, y `SE-246` lo ilustra con operaciones HTTP: `PUT /entregas/42` con el cuerpo completo es idempotente, `POST /entregas` no lo es porque cada llamada crea otra entrega, «sumar 1 a un contador» no lo es y «fijar el contador a 5» sí. Las demás clases usan el mismo sentido con matices de contexto: en automatización (`SE-114`, `SE-224`) es poder reejecutar un script sin acumular cambios, en mensajería (`SE-270`) es que un consumidor trate igual un mensaje repetido y en datos (`SE-364`) que una transformación pueda reejecutarse sin duplicar filas.

## Por qué importa

Toda red y todo proceso fallan en el peor momento: tras confirmar una escritura y antes de que la respuesta llegue. Quien llama no puede distinguir «no se ejecutó» de «se ejecutó y no me enteré», y la única reacción segura es reintentar. Si la operación no es idempotente, cada reintento puede cobrar dos veces, crear dos entregas o enviar dos mensajes. La idempotencia es lo que convierte el reintento, que es una necesidad, en una decisión sin riesgo. Además abarata el diseño: `SE-270` muestra que un consumidor que tolera duplicados hace aceptable una garantía de entrega más barata («al menos una vez») en vez de exigir «exactamente una vez».

## Cómo funciona

Hay dos caminos. El primero es elegir operaciones **naturalmente idempotentes**: «fijar a 5» en vez de «sumar 1», reemplazar un contenido canónico en vez de añadirle algo, crear-si-falta en vez de crear. El segundo es **volver idempotente** una operación que no lo es, asociándole una **clave de idempotencia**, según `SE-246`:

1. El cliente genera la clave por *intención* (una por cada «quiero crear esta entrega») y la reutiliza en todos los intentos de esa intención.
2. El servidor guarda la clave junto con el efecto y la respuesta **en la misma transacción**, y una restricción única de la base de datos impide dos filas con la misma clave.
3. Si llega la misma clave con la misma carga, el servidor devuelve la respuesta guardada sin repetir el efecto; si llega con otra carga, es un error del cliente (422), cosa que se distingue con una huella (hash) del contenido.
4. La unicidad se garantiza donde está el estado: comprobar «¿existe la clave?» y luego insertar deja una ventana de carrera; la restricción única la cierra, porque el segundo `insert` falla.

La clave no puede vivir para siempre: debe cubrir el reintento más tardío de un cliente legítimo (una aplicación móvil sin conexión puede reintentar horas o días después), y alargarla cuesta almacenamiento (`SE-246`, sobre la ventana de retención). `SE-392` extiende el mismo razonamiento al procesamiento distribuido, donde el reintento lo hace el propio sistema.

## Ejemplo

En la simulación de `SE-246` (datos sintéticos, base de datos real, semilla fija) se crean 5 000 entregas y, tras confirmar cada escritura, la respuesta se pierde con probabilidad *p*; el cliente reintenta hasta tres veces. Sin clave de idempotencia, una pérdida de respuesta del 1 % duplica el 0,82 % de las entregas, la del 5 % el 5,30 % y la del 20 % el 23,84 %. Con clave y un índice único parcial, el segundo `insert` falla con `IntegrityError`, se devuelve la respuesta guardada y los duplicados son el 0 % en los tres casos. En el mismo experimento, de 6 000 reintentos con retardos que llegan hasta 7 días, el 66,9 % llega con la clave ya caducada si su tiempo de vida es de 10 minutos y el 16,9 % si es de 48 horas: la ventana es una decisión medible.

## Errores y confusiones comunes

- **Reintentar sin clave una operación que cobra.** Entregas duplicadas tras un error de red: el `POST` no llevaba clave de idempotencia. Corrección de `SE-246`: clave por intención y restricción única.
- **Una clave nueva en cada intento.** El servidor no puede reconocer el reintento y crea un duplicado; la protección supone que el cliente reutiliza la clave.
- **Confundir idempotente con atómico.** Una operación puede ser idempotente y quedar a medias, o atómica y no idempotente. `SE-224` pide separar qué parte del diseño dependía de cada una.
- **Pensar que la garantía de entrega sustituye al consumidor.** Un comando («abre la puerta») duplicado puede ser peligroso aunque el transporte prometa «una vez»; la idempotencia debe diseñarse (`SE-270`).
- **Confundir con determinismo.** Idempotente habla del estado final tras repetir, no de que cada ejecución haga el mismo trabajo ni devuelva la misma latencia (`SE-114`).

## Límites y cuándo no aplica

La clave protege el efecto que está en la base de datos; un efecto externo que ocurre fuera de la transacción (un correo, un cobro) puede repetirse igualmente (`SE-246`). La idempotencia de un script sobre archivos locales no se hereda a un servicio remoto: crear un recurso o enviar un mensaje necesita además identidad de operación, y su idempotencia depende del servicio (`SE-114`). Una operación cuyo efecto no tolera repetición y no admite clave exige otra defensa, como deduplicación o exclusión (`SE-028`). Y los porcentajes citados salen de una simulación con distribuciones supuestas, no de una medición de clientes reales: lo transferible es el método.
