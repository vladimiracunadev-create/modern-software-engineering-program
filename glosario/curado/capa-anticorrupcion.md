# Capa anticorrupción

## Definición

La **capa anticorrupción** es un traductor entre dos modelos que impide que el modelo de un sistema se imponga al del otro. Es un concepto del diseño orientado al dominio. `SE-521` la usa en la modernización de un sistema antiguo; `SE-546` la define como la traducción entre contextos que protege al modelo propio; `SE-381` la describe como el componente que traduce entre el modelo de otro sistema y el propio, y es el único que conoce ambos.

## Por qué importa

Un sistema antiguo tiene convenciones propias: textos con coma decimal, estados de una letra con significado implícito, fechas de dos dígitos, nulos y espacios que significan cosas distintas. Si el sistema nuevo habla ese lenguaje directamente, lo hereda, y la modernización reproduce las rarezas del pasado. La decisión que cambia es dónde vive la traducción: en un lugar único y explícito, no repartida por todo el código nuevo.

## Cómo funciona

El mecanismo tiene dos partes. Primero, **aislamiento**: solo la capa conoce los dos vocabularios; el resto del sistema nuevo ve únicamente el modelo limpio. `SE-546` lo muestra con una función de seis líneas que convierte `entrega_id` en `id`, `estudiante` en `student`, `vence_en` en `due` y, lo más importante, el estado textual en un booleano («recibida» verdadero, «pendiente» falso). Si mañana aparece un estado «en revisión», se decide en un solo sitio si cuenta como entregada.

Segundo, **decisiones semánticas ante lo raro**. `SE-521` pide que una buena capa no lance excepciones ante datos extraños: los clasifica (traducido, traducido con advertencia, no traducible) y envía lo no traducible a una cuarentena para revisión. Qué hacer con una nota vacía, un estado desconocido o una fecha imposible es una decisión de negocio que la capa vuelve explícita.

## Ejemplo

Un sistema legado entrega una calificación como el texto `"8,5"` y un estado `"R"`. La capa produce `grade = 8.5` y `received = true`. Si llega `"R "` con espacio o una fecha `31/02`, no se detiene el flujo: el registro se marca con advertencia o va a cuarentena, y el equipo lo revisa sin que el sistema nuevo tenga que conocer el formato antiguo. Ilustración basada en los casos de `SE-521` y `SE-546`.

## Errores y confusiones comunes

- **El sistema nuevo adopta las rarezas del antiguo** (`SE-521`): no hay capa de traducción; se corrige introduciéndola con cuarentena.
- **Dejar que la capa lance excepciones** ante datos raros: detiene el flujo en vez de clasificar.
- **Dispersar la traducción** en varios módulos: se pierde la propiedad esencial de que un solo componente conoce ambos modelos.
- **Confundirla con una simple conversión de formato**: traduce también significados.

## Límites y cuándo no aplica

Añade un componente que mantener y un salto más en el camino de los datos. Si ambos sistemas comparten ya el mismo modelo, o el externo es tan estable y limpio que adoptarlo no daña al propio, la capa sobra; en la relación entre contextos, aceptar el modelo ajeno tal cual es la opción llamada conformista. Tampoco corrige problemas de calidad del origen: los hace visibles y los aísla.
