# Estados e invariantes

## Definición

Los **estados** son las situaciones por las que pasa una entidad (por ejemplo, una entrega: borrador, enviada, en revisión, calificada), y los **invariantes** son las propiedades que deben cumplirse en todas ellas (SE-146). La pareja es una herramienta de requisitos: el ciclo de vida de la entidad se modela con estados y lo que nunca debe romperse se escribe como invariante.

## Por qué importa

Lo que siempre debe ser cierto se verifica en cada transición. Sin invariantes explícitos, las reglas viven repartidas en el código y cada ruta de cambio las respeta o no. Cambia el modo de especificar: en lugar de repetir la misma regla en cada operación, se escribe una vez como invariante y se comprueba siempre.

## Cómo funciona

SE-146 ilustra con una entrega que pasa por borrador, enviada, en revisión y calificada. Ciertas propiedades deben cumplirse **siempre**: una entrega calificada no se modifica sin reabrirse; una entrega enviada tiene fecha de envío. Un **invariante** es una regla que **no depende de la transición que ocurra**: se escribe una vez y se comprueba en cada una (en la frontera de cada operación que cambia el estado).

La utilidad analítica es doble. Primero, los estados delimitan qué operaciones son válidas en cada situación: «editar» no está permitido en «calificada». Segundo, **descubrir que algo debería ser un invariante** es parte del análisis de requisitos: aparece cuando alguien pregunta «¿puede pasar que…?» y la respuesta es «nunca». Escribirlo evita que cada operación tenga que recordarlo.

Los estados se representan con una máquina de estados (transiciones entre ellos) y, para verificar, los invariantes se comprueban sobre todos los estados alcanzables. Un invariante que falla lejos de donde se corrompió el estado indica que se comprueba tarde: la corrección es comprobarlo en la frontera de cada operación pública, al menos en pruebas.

La política de entregas tardías de la plataforma se registra como regla con identificador, texto, responsable y fecha, separada del requisito que la aplica, de modo que la regla vive en un solo punto.

## Ejemplo

Estados de una entrega: borrador → enviada → en revisión → calificada. Invariantes: (1) toda entrega enviada tiene fecha de envío; (2) una entrega calificada tiene nota entre 0 y 100; (3) una entrega calificada no se modifica sin reabrirse. La operación «editar texto» se rechaza si el estado es «calificada»; la operación «calificar» comprueba que el resultado respete (2) antes de confirmar. (Ejemplo derivado de SE-146.)

## Errores y confusiones comunes

- **Dos módulos calculan notas distintas**: la regla vive duplicada; corrección: único punto con identificador y responsable.
- **El comité pregunta «¿qué pasa si…?» y nadie lo sabe**: solo se redactaron casos felices; corrección: enumerar combinaciones y asignar acción o decisión pendiente.
- **Confundir estado con dato**: no todo valor de un campo es un estado.
- **Invariantes comprobados solo al final.**

## Límites y cuándo no aplica

El modelo de estados cubre el comportamiento modelado; si falta un estado, falta una regla. Con muchos estados y componentes concurrentes, el espacio se multiplica (explosión de estados). Algunos invariantes dependen de más de una entidad o de tiempo, y son más difíciles de comprobar localmente.
