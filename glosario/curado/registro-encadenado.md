# Registro encadenado

## Definición

Un **registro encadenado** es una secuencia de entradas donde cada una incluye el resumen (huella, *hash*) de la anterior. `SE-288` (proyecto: plataforma de ejecución aislada con evidencia) lo usa como mecanismo de evidencia, y `SE-610` (gobierno de IA y regulación) lo define como el registro en que cada entrada incluye la huella de la anterior. Es la misma idea de una cadena de bloques, sin consenso distribuido ni minería.

## Por qué importa

Hace detectable la alteración y el borrado. Cambiar o eliminar una entrada del pasado rompe la huella de todas las siguientes, de modo que quien revisa el registro lo nota. Es una forma barata de dar credibilidad a un registro de auditoría.

## Cómo funciona

Cada entrada contiene los datos del evento y el hash de la entrada anterior. La huella de la entrada *n* se calcula sobre sus datos más la huella de la *n−1*. Para verificar:

1. Se recorre el registro desde el principio.
2. Se recalcula la huella de cada entrada con los datos y la huella anterior.
3. Si alguna no coincide con la almacenada o con la que cita la siguiente, hubo alteración.

Qué detecta y qué no: **detecta** modificación y borrado intermedios, e inserciones. **No detecta** el borrado de las últimas entradas ni la reescritura completa de todo el registro por quien controla el almacenamiento, a menos que la última huella se publique o se guarde fuera de su alcance. Por eso el patrón se acompaña de anclar la cabeza de la cadena en otro lugar.

En `SE-288`, el expediente de la plataforma de ejecución aislada incluye un registro encadenado y una sección «no cubierta» que otra persona pueda discutir.

## Ejemplo

El proyecto de `SE-288` pide implementar la mínima plataforma que haga cumplir el contrato de ejecución de código de terceros, con registro encadenado y un expediente con lo que no cubre. En `SE-610`, el equipo de *Avisos-ML* construye una tabla de evidencia de gobierno; un registro encadenado respalda que las decisiones de aprobación no se modificaron después. Ilustración propia: tres entradas A, B, C; si se cambia B, la huella de C ya no corresponde.

## Errores y confusiones comunes

- **Pensar que impide la alteración:** solo la hace detectable.
- **No anclar la última huella,** de modo que quien controla el registro lo reescribe entero.
- **Confundirlo con firma:** el encadenado prueba integridad de secuencia, no procedencia.
- **Confundirlo con una cadena de bloques con consenso.**

## Límites y cuándo no aplica

No garantiza que lo registrado sea verdadero, solo que no se alteró después. Verificar exige recorrer el registro. Si el volumen es muy alto, se agrupan entradas en lotes. Y no sustituye controles de acceso al almacenamiento.
