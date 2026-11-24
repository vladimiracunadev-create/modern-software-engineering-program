# Análisis de alcance

## Definición

El **análisis de alcance** determina los elementos que un cambio obliga a revisar, a partir de las dependencias y los enlaces entre artefactos (SE-153). No debe confundirse con definir el «alcance del proyecto» (qué entra y qué no): aquí el alcance es el conjunto de lo afectado por un cambio concreto. Es muy cercano al análisis de impacto, que SE-151 y SE-168 formulan con el mismo mecanismo.

## Por qué importa

Estima el costo y el riesgo de un cambio antes de aprobarlo. Un cambio aparentemente pequeño en una especificación puede obligar a tocar media especificación; saberlo antes permite decidir con información. Sin análisis, el síntoma que SE-153 describe es un cambio «pequeño» que rompe media especificación porque nadie calculó el alcance.

## Cómo funciona

El alcance de un cambio es el conjunto de elementos que habría que revisar: los **requisitos que dependen del modificado**, los **criterios y pruebas enlazados**, los módulos, la documentación y las obligaciones. Con el grafo de enlaces de SE-151 se obtiene **recorriendo las dependencias hacia quienes dependen del cambiado**: se parte del elemento que cambia y se sigue cada arista hacia sus consumidores, de forma transitiva.

El tamaño del resultado informa la decisión. Un cambio con alcance cero es un ajuste local. Uno con muchos dependientes transitivos es una decisión de arquitectura de los requisitos y merece más cuidado: revisión específica, aviso a los dueños de lo afectado y, a menudo, una solicitud de cambio formal contra la línea base. SE-153 pide registrar el resultado en la solicitud de cambio, de modo que quien decide vea el alcance y quien revisa sepa qué mirar.

El análisis es tan bueno como el grafo: si faltan enlaces, el alcance se subestima; si se enlazó todo con todo, se sobrestima. Por eso va de la mano de una granularidad de enlaces que responda a las preguntas reales.

## Ejemplo

Cambiar el tope de penalización por entrega tardía. Recorriendo las dependencias: las pruebas de frontera de esa regla, el módulo de cálculo de la nota, las vistas que muestran el descuento al estudiante, al docente y a secretaría, y el texto de la política publicada. Esa lista es el alcance; con ella se estima el trabajo y se avisa a quienes mantienen cada pieza. Si el cambio solo toca un texto de ayuda sin dependientes, el alcance es cero. (Ilustración sobre el escenario de la plataforma.)

## Errores y confusiones comunes

- **Un cambio «pequeño» rompe media especificación**: no se calculó el alcance; corrección: recorrer las dependencias antes de aprobar y registrar el resultado.
- **Nadie sabe cuál era la versión acordada**: sin línea base no hay contra qué calcular el cambio.
- **Confundirlo con «alcance del proyecto».**
- **Tratar la lista como lo que hay que modificar**: es lo que hay que revisar.

## Límites y cuándo no aplica

Solo ve dependencias enlazadas; las implícitas (datos compartidos, configuración) quedan fuera. El resultado es una cota superior, no una predicción. En un sistema pequeño con pocos artefactos, la revisión directa suele bastar.
