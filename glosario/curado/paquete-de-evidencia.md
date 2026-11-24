# Paquete de evidencia

## Definición

Un **paquete de evidencia** es un conjunto de datos que prueban cómo se construyó, verificó, aprobó y ensayó una versión. El programa usa el término en varias clases con matices: en `SE-431`, un archivo que asocia cada prueba con el defecto que detecta y el resultado de ejecutarla con y sin él; en `SE-240`, artefactos y comprobaciones con enlaces y huellas que permiten repetir una verificación; en `SE-576`, el conjunto que permite a otra persona revisar y operar el producto; en `SE-468`, un conjunto versionado de requisitos, controles, pruebas y evidencias con fecha, alcance y huella.

## Por qué importa

Una afirmación («está probado», «es seguro», «está listo») sin evidencia es opinión. El paquete convierte la afirmación en algo que otra persona puede repetir y revisar. `SE-492` advierte el reverso: un paquete válido en forma puede ser falso en contenido, así que hace falta mirar qué prueban realmente los artefactos.

## Cómo funciona

El hilo común de los usos del programa:

1. **Cada afirmación enlaza con un artefacto** (una prueba, un resultado, un registro).
2. **Los artefactos llevan huella** (hash) y fecha, para detectar cambios.
3. **El alcance está declarado:** qué cubre la evidencia y qué no.
4. **Es repetible:** otra persona puede volver a ejecutar la verificación.

En `SE-431`, la evidencia clave para una prueba es que *detecta* el defecto: se asocia cada prueba con el defecto que atrapa y se registra el resultado con y sin él. En `SE-492`, el camino a producción reúne integración con ramas cortas, un grafo de trabajos con camino crítico de 14 minutos, compuertas, escaneo de secretos, política sobre el plan de infraestructura, preproducción con datos sintéticos, un canario del 5 % con retroceso automático y ensayo mensual del retroceso.

## Ejemplo

Ilustración propia con el sentido de `SE-468`: una fila «el servicio exige autenticación en todas las rutas» enlaza con la prueba que lo comprueba, su resultado de la última ejecución con fecha y la huella del commit evaluado. Si el commit cambia, la huella ya no coincide y la evidencia queda caduca.

## Errores y confusiones comunes

- **Un paquete completo en forma y falso en contenido** (`SE-492`): se valida la estructura, no el sentido.
- **Evidencia sin fecha ni alcance.**
- **Confundirlo con documentación:** el paquete son pruebas y registros, no explicaciones.
- **Reutilizar evidencia de una versión anterior** sin volver a ejecutarla.

## Límites y cuándo no aplica

La evidencia prueba lo que se midió, no que no existan otros defectos. Los proyectos de la clase son escenarios didácticos y no constituyen una certificación. Y reunir evidencia tiene costo: debe ser proporcional al riesgo.
