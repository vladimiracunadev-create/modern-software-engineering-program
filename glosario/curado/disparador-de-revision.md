# Disparador de revisión

## Definición

Un **disparador de revisión** es una condición medible (métrica, umbral y duración) que reabre una decisión (`SE-348`). `SE-456` lo usa en un sentido vecino: la condición (un cambio, un incidente) que obliga a revisar el paquete de evidencia de un sistema crítico. En ambos casos responde a la pregunta «¿qué tendría que pasar para que esta decisión deje de valer?».

## Por qué importa

Una decisión de arquitectura se toma con la información de un momento. Sin disparador, solo se revisa cuando alguien se acuerda o cuando ya hay un problema. La decisión que cambia es tratar una decisión como válida hasta que una señal concreta diga lo contrario, y dejar esa señal escrita junto con la decisión, no en la memoria de alguien.

## Cómo funciona

En `SE-348`, el disparador es una de las siete secciones que debe tener un registro de decisión (contexto, decisión, alternativas consideradas, consecuencias, reversibilidad, disparador de revisión y evidencia). La clase define once criterios que un analizador puede comprobar; cuatro son propiedades de contenido, y una de ellas exige un disparador con un número. Aplicados a tres registros de ejemplo: el ADR-A (monolito modular con extracción del módulo de avisos si el p99 supera 200 ms) cumple 11 de 11; el ADR-B («Usar microservicios… porque son la mejor práctica») cumple 3 de 11 y no tiene ninguna alternativa, consecuencia negativa, número, reversibilidad, disparador ni evidencia.

El mecanismo que lo hace útil es que **vuelve comprobable** la revisión: una métrica con umbral y duración se puede vigilar con una alerta, de modo que reabrir la decisión es un evento, no una iniciativa.

`SE-456` lo extiende a sistemas críticos: el paquete se actualiza con cada cambio de requisitos, diseño, entorno o uso, y con cada incidente; la integración continua ejecuta el comprobador y falla si hay huecos nuevos o evidencia obsoleta sin una decisión registrada. Los disparadores están escritos (un cambio de proveedor del sensor, una actualización de una biblioteca, un incidente).

## Ejemplo

Una decisión elige un monolito modular, y su disparador dice: «si el p99 del módulo de avisos supera 200 ms durante siete días, se estudia su extracción». Cuando la métrica cruza el umbral por ese tiempo, se reabre la decisión con los datos a la vista. Es el caso del ADR-A de `SE-348`.

## Errores y confusiones comunes

- **Disparador sin número**: «si crece mucho» no es comprobable.
- **Registro de decisión sin disparador**: la decisión se vuelve permanente por inercia.
- **Escribirlo y no vigilarlo**: sin alerta ni revisión, la condición no dispara nada.
- **Un paquete de evidencia hecho una vez para una auditoría**: equivale al archivo de riesgos que nunca se actualizó (`SE-449`).

## Límites y cuándo no aplica

El disparador reabre la decisión, no la cambia: alguien debe evaluar si la condición realmente invalida lo decidido. Un umbral mal elegido genera falsas revisiones o revisiones tardías. Los once criterios y los tres registros de `SE-348` son un ejercicio didáctico, no una norma. Para decisiones triviales y baratas de revertir, escribir un disparador es más costoso que la decisión.
