# Enfoque de construcción

## Definición

Un **enfoque de construcción** es la forma de producir el cliente de una aplicación: determina dónde corre la interfaz, quién la dibuja y qué capa de código se comparte entre plataformas. Es el término con que `SE-255` (nativo, híbrido, web wrapper y cross-platform) organiza las opciones. Son categorías de enfoque, no veredictos sobre marcas: dentro de cada una hay mucha variedad.

## Por qué importa

De esa elección derivan el acceso a las capacidades del dispositivo, el rendimiento y el costo de mantener varios clientes. `SE-255` pide documentarla y no tomarla por moda: cada enfoque decide dónde corre la interfaz y quién la dibuja.

## Cómo funciona

`SE-255` distingue cinco enfoques:

1. **Nativo:** cada cliente con las herramientas de su plataforma. Máximo acceso y adaptación, a costa de mantener un código por plataforma.
2. **Multiplataforma con interfaz propia:** un motor propio dibuja la interfaz, como describe la arquitectura de Flutter. Mismo aspecto en todas partes; la interfaz no usa los elementos nativos.
3. **Multiplataforma con elementos nativos gobernados desde código compartido:** como describe React Native; delega el dibujo a la plataforma.
4. **Híbrido en contenedor:** una web dentro de una aplicación; accede a capacidades vía un puente.
5. **Web instalable:** corre en el navegador con capacidades limitadas.

La pregunta técnica útil es dónde están las **fronteras** entre el código compartido y el de la plataforma, y cuántas veces por segundo se cruzan: la frontera más sensible es la que cruza más veces.

## Ejemplo

El equipo del cliente documenta la elección en cuatro artefactos enlazados (`SE-255`): la tabla de criterios con puntuaciones y su fuente; el análisis de sensibilidad, que cuenta con qué frecuencia gana cada opción al sortear pesos; un prototipo de la frontera más sensible con su medición; y la lista de capacidades que el cliente necesita, marcadas como disponibles, opcionales o ausentes en cada opción.

## Errores y confusiones comunes

- **Elegir por marca o por tendencia** en lugar de por criterios con fuente.
- **Tomar una sola puntuación sin analizar su sensibilidad** a los pesos.
- **Suponer que «multiplataforma» significa una sola base sin trabajo nativo:** casi siempre hay capacidades que exigen código de plataforma.
- **Confundir enfoque con modelo de aplicación,** que trata del ciclo de vida del proceso (`SE-253`).

## Límites y cuándo no aplica

La tabla de criterios codifica supuestos del equipo y de la fecha: los enfoques evolucionan. Un prototipo mide una frontera concreta, no el producto completo. Y cuando el producto es solo contenido web, la discusión de enfoques de cliente pierde sentido.
