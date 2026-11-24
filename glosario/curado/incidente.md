# Incidente

## Definición

Un **incidente** es un evento que degrada o amenaza el servicio de un modo que requiere una respuesta coordinada y no rutinaria. Es la definición de `SE-500`.

## Por qué importa

Distinguir un incidente de un fallo cotidiano decide cuándo se activa la maquinaria de respuesta (canal propio, roles, comunicación). `SE-500` señala una asimetría: **declararlo** pronto tiene un costo bajo (una persona avisa, se abre un canal) y es mucho más barato que declararlo tarde, cuando ya hay confusión.

## Cómo funciona

La **severidad** clasifica el impacto en niveles (por ejemplo, 1 a 4) y decide quién se involucra, con qué rapidez y con qué comunicación. Un criterio útil usa magnitudes observables: fracción de personas afectadas, funciones no disponibles, pérdida de datos, duración prevista. «Grave» o «moderado» dependen de quien lo lee; «más del 10 % de las entregas falla o hay pérdida de datos» se aplica igual por dos personas. Los incidentes graves abren un canal con roles definidos y comunicación periódica.

## Ejemplo

`SE-500` (caso hipotético, no medición): severidad 1 si más del 10 % de las entregas falla o hay pérdida de datos; 2 entre 1 % y 10 %; 3 degradación sin pérdida visible; 4 sin impacto externo. Las severidades 1 y 2 abren un canal con cuatro roles (comando, operaciones, comunicaciones, escriba) con suplentes por rotación; la página de estado publica una actualización a los 10 minutos y luego cada 30, aunque no haya novedades.

## Errores y confusiones comunes

- **Veinte personas opinan y nadie decide.** Sin comandante ni roles; asignarlos al declarar.
- **La media mejora y no se sabe si es real.** Pocos incidentes y variación por azar; usar medianas, percentiles y rango esperado.

## Límites y cuándo no aplica

Los umbrales de severidad son decisiones de cada organización; los de la clase son ilustrativos. No todo fallo merece un incidente: declararlos de más agota a las personas y desvaloriza el proceso. Tras el incidente sigue el postmortem sin culpa.
