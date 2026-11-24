# Lector tolerante

## Definición

Un **lector tolerante** es un consumidor que usa los campos que conoce e ignora los demás (SE-380). SE-164, SE-441 y SE-312 lo formulan igual; SE-524 añade que aplica valores por defecto a lo ausente. Se opone al lector estricto, que rechaza cualquier campo que no esté en su esquema.

## Por qué importa

La compatibilidad no es una propiedad solo del esquema: depende de **cómo** lee el consumidor. La misma evolución (añadir un campo) es compatible o no según el lector. Cambia cómo se escriben los consumidores y cómo se prueba la evolución de un contrato.

## Cómo funciona

SE-380 explica que, con un lector tolerante, **añadir un campo es compatible hacia adelante**: el lector viejo ignora el campo nuevo y sigue funcionando. Con un lector estricto, no lo es: falla ante lo desconocido. La recomendación de Fowler (la «ley de Postel» aplicada a datos: sé liberal en lo que aceptas) es leer lo que se necesita y no más.

La clase incluye un fragmento que prueba si añadir un campo opcional rompe a un lector estricto viejo, y pide predecir el resultado para el tolerante y para el estricto. El resultado esperado: el tolerante sigue funcionando; el estricto falla.

SE-380 precisa que el lector tolerante **no es una excusa para no validar**: tolerar campos desconocidos no significa aceptar datos incorrectos en los campos que sí se usan. Y se complementa con valores por defecto para campos ausentes, de modo que los datos viejos (sin el campo nuevo) se lean bien (compatibilidad hacia atrás).

El equipo de la plataforma fija las reglas de evolución del evento `EntregaRecibida`: modo de compatibilidad completa, porque el log se retiene 14 días y hay consumidores que se despliegan con semanas de desfase; se permite añadir campos opcionales con valor por defecto y quitar campos opcionales; se prohíbe renombrar, cambiar tipos y volver obligatorio un campo. Los lectores deben ser tolerantes por contrato, y se verifica con una prueba que añade un campo y comprueba que los consumidores siguen funcionando.

## Ejemplo

Evento versión 1: `{id, estudiante, archivo}`. Versión 2 añade `comentario`. Un consumidor tolerante extrae `id`, `estudiante` y `archivo` e ignora `comentario`. Uno estricto, que valida contra el esquema cerrado de la versión 1, lanza un error con la versión 2 y deja de procesar eventos. (Ilustración del mecanismo de SE-380 y SE-164.)

## Errores y confusiones comunes

- **«Solo agrega, no puede romper»**: rompe a lectores estrictos.
- **Tolerar datos inválidos en campos usados**: tolerancia no es falta de validación.
- **No probar con un campo nuevo.**
- **Esquemas cerrados por defecto** en bibliotecas de deserialización.

## Límites y cuándo no aplica

La tolerancia solo cubre campos añadidos; renombrar o cambiar tipos rompe igual. Si el sistema debe rechazar mensajes sospechosos (por seguridad), cierta rigidez es deseable. Y para ignorar un campo hay que saber que no es crítico: ignorar silenciosamente una restricción nueva puede ser un defecto.
