# Ventana de exposición

## Definición

La **ventana de exposición** es el tiempo transcurrido entre la publicación de un aviso de seguridad y el momento en que el sistema deja de usar la versión afectada (`SE-520`). `SE-397` la formula en un sentido más amplio: el tiempo que transcurre entre que existe una vulnerabilidad y que se corrige o se mitiga.

## Por qué importa

Mientras la ventana está abierta, el sistema es vulnerable a una falla ya conocida y, a menudo, explotable. Reducirla es una de las pocas defensas que dependen enteramente de la organización. La decisión que cambia es la política de actualización de dependencias: no «cuando se pueda», sino con una cadencia que acote cuánto tiempo se permanece expuesto.

## Cómo funciona

`SE-520` descompone la ventana en tres tramos:

1. Hasta que el **proveedor publica** una versión corregida.
2. Hasta que **tu política decide** aplicarla.
3. Hasta que **el cambio llega a producción**.

El primer tramo no depende de ti; los otros dos, sí. Una política **continua** (actualizar en cuanto hay corrección, tras una breve verificación) reduce el segundo tramo a días. Una política por **lotes** (mensual, trimestral, anual) lo ata al calendario: en promedio, un aviso espera a la mitad del periodo y, en el peor caso, al periodo completo. La política puede combinarse con prioridad: un carril rápido para avisos con explotación activa conocida, y el lote regular para el resto.

La clase explica por qué las actualizaciones espaciadas son más difíciles: se acumulan cambios incompatibles, y la actualización «de una hora» dura semanas; actualizar en pasos pequeños con una cadencia mantiene bajo el costo y la ventana. La política se escribe, se revisa con datos (ventana de exposición real, rezago medio) y admite excepciones documentadas, como una dependencia que se mantiene en una versión por razones de compatibilidad con un sistema externo.

## Ejemplo

Se publica un aviso crítico sobre una biblioteca. El proveedor libera la corrección al día siguiente. Con política mensual, el equipo la aplica en la próxima ventana (hasta 30 días después); con política continua y carril rápido para explotación conocida, la aplica en un par de días. La diferencia es el tamaño del segundo tramo. Aplicación del razonamiento de `SE-520`.

## Errores y confusiones comunes

- **La actualización «de una hora» dura semanas**: se acumularon cambios incompatibles; se corrige actualizando en pasos pequeños con una cadencia.
- **Un aviso queda abierto meses**: política por lotes sin prioridad; se añade un carril rápido para avisos con explotación conocida.
- **Medir solo la fecha de publicación del aviso**: la ventana incluye el despliegue.
- **No medir la ventana real**.

## Límites y cuándo no aplica

El primer tramo (que el proveedor publique una corrección) escapa al control del equipo, y para dependencias sin soporte puede no cerrarse nunca; ahí corresponde mitigar o reemplazar. Una política continua exige pruebas fiables: sin ellas, actualizar rápido es arriesgado. `SE-520` presenta la cadencia como decisión con compromisos, no como una cifra única.
