# Evidencia trazable

## Definición

La **evidencia trazable** es la relación verificable entre una afirmación del brief y uno o más registros (citas, datos, observaciones) que existen y la respaldan. Es el sentido de `SE-132` (product brief respaldado por evidencia). La palabra «trazable» importa: no basta decir «los usuarios piden X»; debe poder seguirse el hilo hasta el registro.

## Por qué importa

Cambia qué se acepta como base de una decisión de producto. Según `SE-132`, cada afirmación debe poder rastrearse a una evidencia que exista, de más de una persona o fuente. Sin eso, una opinión del equipo se presenta como hallazgo y la decisión se apoya en aire.

## Cómo funciona

`SE-132` gradúa las afirmaciones por su respaldo: sin evidencia es una **hipótesis**; con una sola persona, una **pista**; con dos o más personas o con un registro, un **hallazgo con límites**. La trazabilidad se comprueba en dos planos. El mecánico: que el identificador de evidencia exista, que haya al menos dos participantes distintos o un registro, que no sea solo lo declarado. Un validador lo hace. El de lectura: que la evidencia diga lo que la afirmación dice. Eso lo hace una persona.

La separación importa porque un validador puede pasar un brief cuya cifra no coincide con la evidencia: solo comprueba estructura. La corrección de la clase es añadir una comparación de cifras con la fuente y una lectura humana antes de decidir. Y la decisión debe tener responsable y fecha, para que alguien responda por ella y pueda revisarse cuando llegue evidencia nueva.

## Ejemplo

En la plataforma de entregas, el brief se acompaña de un expediente: tickets y su agrupación, mapa de actores, transcripciones y códigos, mapa de hipótesis, propuesta, mapa de mercado, plan de experimento, registro de prioridad, protocolo ético, reglas de parada y petición descompuesta. El contrato es que `brief.md` remite a ellos por identificador, que cada afirmación declare sus evidencias y que la decisión indique responsable y fecha.

## Errores y confusiones comunes

- **El brief pasa el validador pero una cifra no coincide.** El validador solo comprueba estructura; añadir comparación con la fuente y lectura humana.
- **La decisión sin responsable ni fecha.** Se redactó como recomendación general; exigirlos en el formato.
- **Contar una persona como hallazgo.** Una sola persona es una pista.
- **Citar la evidencia sin que respalde la frase.** El enlace existe, el contenido no coincide.

## Límites y cuándo no aplica

Que haya evidencia trazable no hace verdadera la conclusión: dos personas pueden coincidir y estar equivocadas. Los experimentos de `SE-132` usan evidencias y participantes sintéticos. Para decisiones reversibles y baratas, el costo de trazar todo puede superar el beneficio; la clase pide el rigor proporcional al costo de equivocarse.
