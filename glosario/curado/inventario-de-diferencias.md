# Inventario de diferencias

## Definición

Un **inventario de diferencias** es una tabla de los comportamientos del producto que pueden variar entre plataformas, cada uno ejecutado y registrado en cada plataforma. Es el sentido de `SE-263` (taller: adaptar un producto a dos plataformas). Lo distintivo es el verbo: no se enumera lo que se recuerda, se *ejecuta* y se registra el resultado.

## Por qué importa

Las diferencias se miden, no se recuerdan. Lo que se recuerda («Linux distingue mayúsculas») suele ser cierto pero incompleto; lo que se mide encuentra lo que nadie recordó. Para adaptar un producto a dos plataformas, el inventario decide qué se comparte, qué se adapta y qué se excluye.

## Cómo funciona

Según `SE-263`:

1. **Enumerar** cada comportamiento que pueda variar (rutas, mayúsculas en nombres, finales de línea, hora, notificaciones, selección de archivos).
2. **Ejecutarlo** en cada plataforma, con el mismo programa de prueba.
3. **Registrar** la salida de cada una en la tabla.
4. **Mantenerlo vivo:** cada diferencia nueva descubierta en uso se añade con su prueba.

Con el inventario se clasifica cada función como *igual*, *a adaptar* o *ausente*, y se estima el costo con un intervalo. Después se aíslan las diferencias detrás de **puertos** (almacenamiento, hora, notificaciones, selección de archivos) con un contrato ejecutable por puerto, que se corre contra el adaptador real de cada plataforma y contra uno falso.

## Ejemplo

El equipo del cliente de entregas hace el taller en cuatro pasos (`SE-263`): ejecuta el inventario en los dos sistemas y guarda la tabla con la salida de cada uno; clasifica cada función y estima el costo con un intervalo; define puertos y escribe un contrato ejecutable por puerto; y escribe qué se comparte (reglas del borrador, sincronización), qué se adapta (rutas, notificaciones) y qué se excluye en una plataforma, con el aviso a la persona.

## Errores y confusiones comunes

- **Un adjunto no se guarda en una plataforma** por una diferencia que nadie había registrado (por ejemplo, nombres de archivo); el remedio es añadirla al inventario con su prueba.
- **Llenar el inventario de memoria** sin ejecutar.
- **Hacerlo una vez y abandonarlo,** cuando es una tabla viva.
- **Confundirlo con una matriz de compatibilidad de versiones,** que trata de versiones de un mismo sistema.

## Límites y cuándo no aplica

Solo cubre las diferencias que alguien pensó en probar; no demuestra ausencia de otras. Mide el comportamiento en las plataformas y versiones concretas ejecutadas. Para un producto de una sola plataforma no hace falta.
