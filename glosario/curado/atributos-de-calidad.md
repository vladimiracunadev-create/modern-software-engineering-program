# Atributos de calidad

## Definición

Los **atributos de calidad** son propiedades del sistema, distintas de su función, como rendimiento, fiabilidad, seguridad, usabilidad o mantenibilidad (SE-147). Describen cuán rápido, cuán seguro o cuán fácil de cambiar es el sistema, más allá de lo que hace. También se llaman requisitos no funcionales, aunque ese nombre hace pensar que son secundarios.

## Por qué importa

El cliente suele pedirlos con una palabra («rápido», «seguro») y esa palabra no es un requisito: no se puede construir ni probar. Cambia lo que se pregunta en la elicitación: no solo qué debe hacer el sistema sino cuánto, con qué fiabilidad y a qué costo. Y cambia la arquitectura, porque la mayoría de las decisiones estructurales responden a atributos de calidad.

## Cómo funciona

SE-147 usa ISO/IEC 25010 como vocabulario común (rendimiento, fiabilidad, seguridad, usabilidad, mantenibilidad, portabilidad y otros). Su utilidad es de **lista de preguntas**: ayuda a no olvidar dimensiones. No decide por sí misma cuáles importan: una plataforma de entregas de tareas que se usa dos veces al día no necesita el mismo nivel de disponibilidad que un servicio de emergencias.

El paso de la palabra al requisito es convertirla en un **escenario de calidad verificable**: un estímulo, un contexto y una medida. «La recuperación es rápida» se vuelve «tras un fallo del servidor, el 95 % de las entradas se recupera en menos de 30 segundos». Dos precauciones de la clase: la media oculta la cola donde se concentra el daño (se fija un percentil y una fracción de peticiones), y una ventana anual diluye una caída larga (se declara la ventana mensual o un tope de caída continua).

Además los atributos **compiten** entre sí (compromisos entre atributos): mejorar uno suele costar otro, y la especificación debe mostrar con cuál compite y quién decide cuál cede.

## Ejemplo

El cliente pide «que sea seguro y rápido». Con el vocabulario de calidad, el equipo pregunta: ¿seguro frente a qué amenazas?, ¿rápido para qué operación y con qué percentil? Resultado: dos escenarios, «el 95 % de las subidas de menos de 10 MB termina en menos de 3 segundos» y «tras cinco intentos de acceso fallidos se bloquea la cuenta durante un tiempo». Ahora hay algo que probar y, además, se ve el roce entre ellos. (Ilustración del método de SE-147.)

## Errores y confusiones comunes

- **Tablero verde y gente quejándose**: el objetivo usa la media y la cola concentra el daño.
- **99,9 % anual con un mes catastrófico**: la ventana anual diluye una caída larga.
- **Tratar la lista de ISO 25010 como obligatoria**: es una guía de preguntas.
- **Especificar un atributo sin medida.**

## Límites y cuándo no aplica

La clase usa datos sintéticos y no midió un sistema real. Algunos atributos son difíciles de medir antes de construir (mantenibilidad), y se aproximan con indicadores indirectos. La taxonomía puede variar entre normas; lo que importa es que cada atributo relevante tenga una medida y un decisor.
