# Registro de auditoría

## Definición

Un **registro de auditoría** es un historial de acciones que responde quién hizo qué, sobre qué, cuándo y con qué resultado, protegido frente a la alteración (SE-152). SE-574 lo exige también en sistemas con agentes de IA: sin él no se reconstruye lo ocurrido ni se puede responder por ello. No es un registro técnico de depuración (logs de errores), aunque pueda convivir con ellos.

## Por qué importa

Es lo que permite reconstruir los hechos y detectar manipulaciones. Una auditoría, una investigación de incidente o una disputa necesitan evidencia de lo que ocurrió y de quién lo hizo. Si el registro puede alterarse sin dejar rastro, no sirve como evidencia. Cambia el diseño: no basta escribir líneas; hay que decidir su contenido, su integridad y su retención.

## Cómo funciona

SE-152 distingue dos requisitos. El **contenido**: quién (identidad), qué (acción), sobre qué (objeto), cuándo (hora) y con qué resultado. Y la **integridad**: que no se pueda alterar o borrar sin que alguien lo note. Un mecanismo básico es la **cadena de hashes**: cada entrada incluye el hash de la anterior, de modo que modificar o eliminar una entrada intermedia rompe la cadena y se detecta.

La clase precisa sus límites: la cadena de hashes **no detecta el truncado del final** (borrar las últimas entradas deja una cadena válida) ni la **reconstrucción completa** por alguien con acceso de escritura que recalcule todos los hashes. Esas amenazas se cubren con un **ancla externa**: publicar periódicamente el hash más reciente en un lugar que el atacante no controle, o enviarlo a un sistema de solo anexar. NIST SP 800-53 incluye controles de generación y protección de registros de auditoría, como marco de referencia.

Hay una tensión con la privacidad: el registro debe permitir demostrar lo ocurrido sin guardar el contenido sensible. SE-152 la ilustra con el borrado de datos: si una auditoría pide evidencia de que se borró algo y no hay, es porque no se diseñó cómo generarla; se define la evidencia junto con el requisito, sin guardar el contenido borrado. Y bajo retención legal el borrado no procede: la regla debe incluir las excepciones.

## Ejemplo

Cada entrada de un registro de la plataforma incluye: `{actor: "docente-17", acción: "conceder_prórroga", objeto: "entrega-342", hora: "…", resultado: "ok", hash_anterior: "…"}`. Si alguien edita la entrada 40, el `hash_anterior` de la 41 deja de coincidir; si borra las entradas 90–100 y reescribe el final, solo el ancla publicada ayer lo delata. (Estructura ilustrativa; SE-152 desarrolla la técnica.)

## Errores y confusiones comunes

- **Registrar sin integridad**: se puede editar sin que nadie lo note.
- **Pensar que la cadena de hashes lo resuelve todo**: no ve el truncado ni la reconstrucción completa.
- **Guardar contenido sensible en el registro** para «tener evidencia».
- **No diseñar la evidencia del borrado** y fallar la auditoría.

## Límites y cuándo no aplica

El registro prueba que algo se registró, no que sea verdad: si el sistema que escribe está comprometido, escribirá lo que el atacante quiera. Necesita retención acotada y control de acceso, porque también es un blanco. Para sistemas de bajo riesgo, un registro estructurado sin cadena de hashes puede bastar; el nivel de protección se calibra con el costo de una disputa.
