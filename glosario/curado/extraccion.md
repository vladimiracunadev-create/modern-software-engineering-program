# Extracción

## Definición

En el sentido principal del programa (`SE-609`), la **extracción** es la copia del comportamiento de un modelo mediante consultas: un atacante hace muchas preguntas y usa las respuestas para entrenar su propia réplica. El término tiene otros sentidos en el programa, que conviene no confundir:

- En `SE-361` (ingeniería de datos): el paso de un proceso de datos en que se decide qué filas entran y cuáles se omiten.
- En `SE-487` (CI/CD): un modelo de despliegue en que el agente que despliega lee el repositorio desde dentro del entorno, en lugar de recibir órdenes desde fuera.

Esta entrada desarrolla el primero y resume los otros dos.

## Por qué importa

Un modelo expuesto por una interfaz es un activo que se puede copiar sin acceso a su código ni a sus datos: basta con consultarlo. La decisión que cambia es qué se expone y a qué ritmo: la interfaz del modelo es parte de su superficie de ataque, y limitarla es una defensa de seguridad, no solo de capacidad.

## Cómo funciona

`SE-609` incluye la extracción en el modelo de amenazas del equipo de *Avisos-ML*. Activos: el modelo, los datos de comportamiento de estudiantes, las etiquetas, el registro y la interfaz; para cada uno, un atacante y una prueba. Frente a la extracción, la defensa elegida es doble: limitar a 1 000 consultas por cuenta y por día, y devolver una clasificación en lugar de la probabilidad. La razón es de información: cada respuesta es una pista sobre la frontera de decisión del modelo; cuantas menos respuestas y menos informativas, más cuesta reconstruirlo. Una probabilidad revela más que una etiqueta.

En `SE-361`, la extracción de datos es uno de tres puntos donde una columna cambia de sentido sin cambiar de nombre (junto con la transformación y el consumo): qué filas entran y cuáles se omiten define lo que el dato significa aguas abajo. La defensa es escribir la definición junto con la columna y comprobarla.

En `SE-487`, la extracción en CI/CD tiene una ventaja de seguridad concreta: la canalización de integración no necesita credenciales del clúster (basta con que publique un artefacto y actualice un manifiesto), de modo que comprometer la integración no entrega el control de producción.

## Ejemplo

El modelo de marcados de *Avisos-ML* se expone con una interfaz que devuelve una probabilidad. Un atacante la consulta decenas de miles de veces y entrena una copia. La mitigación del equipo: tope de 1 000 consultas por cuenta y por día, y respuesta en forma de clasificación. No impide del todo la copia, pero la encarece.

## Errores y confusiones comunes

- **Confundirla con la evasión o el envenenamiento**: la evasión engaña a un modelo existente; el envenenamiento corrompe sus datos; la extracción lo copia.
- **Devolver siempre la probabilidad por comodidad**: entrega más información de la necesaria.
- **Mezclar sentidos**: la extracción de un proceso de datos no tiene relación con el robo de un modelo.
- **Tratar el límite de consultas como defensa completa**: las cuentas múltiples pueden eludirlo.

## Límites y cuándo no aplica

Las medidas de `SE-609` forman parte de un modelo de amenazas del ejemplo, con aceptación documentada de ciertos riesgos; no son una garantía contra la copia. Si el modelo no está expuesto fuera de la organización, o su valor no justifica el costo de protegerlo, la extracción puede no ser un riesgo prioritario.
