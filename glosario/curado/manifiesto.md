# Manifiesto

## Definición

En el programa, un **manifiesto** es una lista de elementos con su identificador y su huella, que permite verificar un conjunto. Tiene varios usos según la clase: en SE-456, la lista de resúmenes de los archivos de evidencia en el momento de una revisión; en SE-168 y SE-300, la lista de artefactos o ficheros de un paquete con la huella de cada uno; en SE-368, la lista de archivos de una versión de una tabla de lakehouse; en SE-612, el archivo con las huellas, la semilla, las versiones y las métricas de un modelo; en SE-444, el archivo estructurado que describe la pregunta, el plan, el entorno, los datos, los resultados, el veredicto y los límites de un informe. No es el manifiesto de una aplicación web ni el manifiesto ágil.

## Por qué importa

Hace detectable un cambio que las demás comprobaciones no ven. Un manifiesto fija qué había en el conjunto en un momento dado; comparándolo después se descubre qué cambió. Cambia la confianza en un paquete o una versión: se verifica en lugar de suponer.

## Cómo funciona

El mecanismo es una lista de pares (elemento, huella), donde la huella es un resumen criptográfico (por ejemplo SHA-256) del contenido. Si el contenido cambia, la huella cambia. Dos usos ilustran su valor.

**Evidencia (SE-456).** Las comprobaciones de contenido no ven un cambio que mantenga todas las referencias válidas. Si se edita el texto de un requisito (REQ-02 pasa de «la puerta abierta» a «abierta o entreabierta»), todas las pruebas siguen enlazadas y pasan, y el paquete sigue «en verde», pero la prueba verificó un requisito anterior. La defensa mínima es un manifiesto con el SHA-256 de cada archivo de evidencia en el momento de la revisión: al comparar, el archivo editado aparece con otra huella y la revisión debe repetirse.

**Datos (SE-368).** Una tabla de un lakehouse no es una carpeta de archivos sino la lista de archivos de una versión, guardada en un manifiesto. Una escritura añade archivos nuevos y publica una **nueva versión del manifiesto** con un único renombrado atómico. Un lector que abrió la versión 1 sigue viendo sus archivos mientras una compactación prepara la versión 2; un lector nuevo ve la 2. Así se logran lecturas consistentes durante los cambios.

En los paquetes de SE-168 y SE-300, el manifiesto permite verificar la integridad de lo recibido antes de usarlo.

## Ejemplo

Un paquete de evidencia tiene tres archivos. Su manifiesto registra `requisitos.md: 9f2c…`, `pruebas.md: 41ab…` y `resultados.json: c07d…`. Tras la revisión, alguien edita `requisitos.md`. Al verificar, la huella de ese archivo difiere y la revisión se declara obsoleta, aunque todos los enlaces sigan válidos. (Ilustración del mecanismo de SE-456; las huellas son ficticias.)

## Errores y confusiones comunes

- **Creer que «en verde» implica que lo revisado es lo vigente.**
- **Manifiesto sin verificar** nunca.
- **Almacenar el manifiesto junto al contenido sin protegerlo**: quien altera el contenido altera también la lista.
- **Confundir manifiesto con índice**: el índice dice dónde está; el manifiesto, qué contenido tiene.

## Límites y cuándo no aplica

Un manifiesto prueba integridad, no corrección. Protege contra cambios si la propia lista está protegida (firmada o guardada aparte). Para conjuntos que cambian constantemente, mantenerlo a mano es impracticable y se genera automáticamente.
