# Migración

## Definición

Una **migración** es un cambio versionado del esquema o de los datos que se aplica en orden y deja registro de que se aplicó. Es el sentido principal de la clase `SE-558` (generación de pruebas, documentación y migraciones). `SE-254` lo usa en aplicaciones: la transformación explícita de un estado guardado por una versión anterior a la forma que espera la versión actual. El común es que algo guardado con una forma antigua debe pasar a una nueva sin perderse.

## Por qué importa

Una conversión sin error no es una conversión correcta. El riesgo está en los valores que no encajan, y esos pasan las comprobaciones habituales. Cambia la decisión de qué se verifica después de migrar: no basta que el script termine.

## Cómo funciona

`SE-558` describe el mecanismo del fallo silencioso: SQLite convierte con `CAST` el prefijo numérico de un texto y devuelve cero si no hay ninguno, sin error ni aviso; otros motores lanzan error o devuelven nulos, y cada uno tiene sus reglas. Un script generado sin conocer los valores reales convierte «NP», cadenas vacías o «5,5,0» en ceros o en números parciales plausibles, y el recuento de filas coincide: las comprobaciones habituales no lo ven.

De ahí un procedimiento defendible:

1. **Perfilar** los valores reales antes de escribir la conversión.
2. **Definir** qué hacer con cada clase de valor que no encaja (rechazar, marcar, mapear).
3. **Aplicar en orden**, con registro de versión aplicada.
4. **Verificar** contra reglas del dominio, no solo recuentos.

En `SE-254`, al reanudar una aplicación, el estado guardado por una versión anterior pasa por una migración explícita antes de usarse.

## Ejemplo

Ilustración propia basada en el riesgo de la clase: una columna de notas en texto, con valores «NP» (no presentó) y «5,5». Una conversión directa a número las transforma en 0 o en 5, y el número de filas sigue igual. Una migración cuidada trata «NP» como ausencia, normaliza la coma y falla con un informe de las filas no convertibles.

## Errores y confusiones comunes

- **Confiar en que el recuento de filas valida la migración.**
- **Aplicar un script generado sin revisar los valores reales** (`SE-558`).
- **Migrar sin versión registrada,** de modo que no se sabe qué se aplicó.
- **Confundirla con una reescritura o con el cambio de plataforma.**

## Límites y cuándo no aplica

Una migración que modifica datos no siempre es reversible; conviene copia previa y plan de vuelta atrás. Las reglas de conversión dependen del motor concreto. Y para esquemas que cambian de forma compatible (añadir una columna opcional), el costo es menor, pero sigue necesitando orden y registro.
