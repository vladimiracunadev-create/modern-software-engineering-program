# Generación determinista

## Definición

La **generación determinista** es la propiedad de un generador que produce salida idéntica para la misma entrada (SE-165). Un generador (de clientes, de documentación, de diagramas, de índices) es determinista si ejecutarlo dos veces sobre la misma fuente da exactamente los mismos bytes.

## Por qué importa

Un generador que no es reproducible hace imposible comparar y revisar lo generado. Si cada regeneración produce un resultado distinto aunque la fuente no cambió, el diff está lleno de ruido, no se puede comprobar si lo comprometido coincide con lo que genera la fuente, y los cambios reales se pierden entre los falsos. Cambia el diseño de un generador y de su integración continua.

## Cómo funciona

SE-165 señala las **fuentes habituales de no determinación**:

- **Iterar estructuras sin orden garantizado**: en Python, el orden de iteración de un conjunto de cadenas puede cambiar entre procesos porque el valor de hash de las cadenas se aleatoriza por proceso; recorrerlo y emitir en ese orden da salidas distintas.
- **Marcas de tiempo** o **rutas absolutas** incrustadas en la salida.
- **Configuración regional**: formatos de fecha, número y orden alfabético que dependen del entorno.

La regla de diseño es **ordenar todo lo que se emite** (claves, nodos, aristas, archivos) con un criterio explícito y estable, eliminar o normalizar lo dependiente del entorno (fechas, rutas) y fijar la semilla de hash cuando se comprueba.

La comprobación de que funciona es mecánica: regenerar y comparar huellas con lo comprometido; si hay diferencias, la integración continua falla. En la plataforma de entregas, los clientes se generan desde el documento OpenAPI (spec-as-source) con un generador que ordena toda su salida y **marca la región generada**; una comprobación regenera y compara huellas.

El segundo fallo que la clase enlaza es la **regeneración que borra trabajo manual**: se editó dentro de lo generado. La corrección es delimitar la región generada y mover lo manual fuera. La generación determinista es también la base de la construcción reproducible: sin ella, comparar artefactos no dice nada.

## Ejemplo

Un generador emite un diagrama con las dependencias de un conjunto de servicios iterando un `set` de Python. En cada ejecución las aristas salen en distinto orden y el archivo cambia, así que cada regeneración produce un diff de decenas de líneas aunque nada cambió. Al ordenar nodos y aristas alfabéticamente antes de emitir, la salida es idéntica y el diff vacío. (Ilustración del mecanismo de SE-165 y SE-209.)

## Errores y confusiones comunes

- **Cada regeneración produce un diff enorme**: el generador no ordena su salida.
- **Incluir la fecha de generación** en el archivo.
- **Rutas absolutas** del equipo que genera.
- **Editar a mano dentro de lo generado.**

## Límites y cuándo no aplica

El determinismo se pierde si cambian la versión del generador o sus dependencias; hay que fijarlas. Para salidas que deben incluir una marca de tiempo por razones de negocio, se separa del contenido comparado. Un generador determinista puede generar algo incorrecto; solo garantiza reproducibilidad.
