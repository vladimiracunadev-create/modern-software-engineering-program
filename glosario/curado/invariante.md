# Invariante

## Definición

Un **invariante** es una propiedad que permanece verdadera en puntos definidos de un proceso, de la vida de un objeto o de un modelo. El programa lo usa en cuatro escalas que comparten una misma idea, la de escribir de forma comprobable qué significa «estado válido»: en un procedimiento, `SE-052` lo define como propiedad preservada en puntos definidos; en una clase, `SE-159` como condición que se cumple antes y después de cada operación pública; en un modelo de estados, `SE-161` como propiedad que debe cumplirse en todos los estados alcanzables; y en un agregado de dominio, `SE-329` como regla que debe cumplirse siempre dentro de esa unidad. En datos, `SE-352` lo formula como afirmación verdadera siempre que no haya una operación en curso. El sentido que usa el programa es el de la frase «lo que es verdad entre operaciones», no el de una lista de comprobaciones sueltas.

## Por qué importa

Sin un invariante escrito, «estado válido» vive en la cabeza de quien programó y cada persona lo reconstruye distinto. Escribirlo concentra la definición en un solo lugar y cambia dos decisiones profesionales: dónde comprobar y a quién culpar cuando algo falla. `SE-159` lo plantea así: un invariante bien elegido permite localizar un defecto por el primer invariante que falla, en vez de descubrir la corrupción lejos de donde ocurrió. En el producto SaaS mínimo de `SE-420` los invariantes son lo que el producto promete mantener siempre, y por eso se pide al menos un caso de prueba por invariante más uno que no esperes.

## Cómo funciona

Un invariante se sostiene con tres argumentos que `SE-052` pide demostrar: que se cumple al **inicializar**, que cada **paso preserva** la propiedad (si era verdadera antes del paso, lo es después) y que, al **terminar**, la propiedad junto con la condición de parada da el resultado buscado. Es el mismo razonamiento de la inducción: base, paso y conclusión.

En una clase, el mecanismo es comprobarlo en las **fronteras** de las operaciones públicas, no en medio de ellas. Dentro de una operación el estado puede estar transitoriamente roto (se actualizó un campo y falta el otro); lo que importa es que, al devolver el control, la clase vuelva a un estado válido. En la plataforma de `SE-159` un método `inv()` se llama al terminar cada operación, y las pruebas con un conductor aleatorio ejecutan secuencias válidas hasta que algún invariante salta.

En un modelo de estados, `SE-161` explora todos los estados alcanzables con una búsqueda y comprueba el invariante en cada uno; si se rompe, entrega la traza más corta que lo produce. En un agregado de dominio (`SE-329`), el invariante es la razón de existir del agregado: dos comandos que leen el mismo estado y escriben después pueden violarlo si no hay control, por lo que el tamaño del agregado es una decisión de concurrencia. En datos (`SE-352`), la pregunta es quién vigila el invariante: el motor mediante restricciones o la aplicación, y cuántos datos inválidos deja pasar cada capa.

## Ejemplo

En `SE-159`, una calificación tiene tres invariantes: la nota está entre 0 y el máximo, una calificación publicada tiene nota y la prórroga no supera 72 horas. Cada operación pública de `Calificacion` termina llamando a `inv()`. Si `publicar()` se ejecuta sobre una calificación sin nota, el invariante «publicada implica nota» falla en esa misma operación y la traza apunta a `publicar()`, no a un informe semanas después.

En `SE-329`, un invariante de agregado: «una entrega admite como máximo tres reenvíos». Si dos comandos de reenvío leen que hay dos reenvíos y ambos escriben, el invariante se rompe aunque cada comando, por separado, fuera correcto. El invariante explica por qué hace falta un control de concurrencia en el agregado.

## Errores y confusiones comunes

- **Comprobar al final o cada muchas operaciones.** El invariante falla lejos de donde se corrompió el estado y no se sabe qué operación lo rompió. Corrección según `SE-159`: comprobar en la frontera de cada operación pública, al menos en pruebas.
- **Contrato implícito.** La función falla sin decir quién se equivocó. Corrección según `SE-052`: escribir precondición, invariante y poscondición; la precondición obliga al llamador, la poscondición a quien implementa y el invariante a ambos entre operaciones.
- **Confiar en el diagrama.** Un diagrama de estados que parece correcto no recorre combinaciones de transiciones y deja pasar un estado ilegal. Según `SE-161`, se explora el modelo con una búsqueda y se comprueba el invariante en integración continua.
- **Confundir invariante con validación de entrada.** Validar una entrada decide si se acepta un dato; el invariante describe qué debe seguir siendo verdad sobre el estado que ya existe.

## Límites y cuándo no aplica

Un invariante solo es tan fuerte como las operaciones que lo comprueban: si una ruta de código modifica el estado sin pasar por la frontera, el invariante no la protege. Comprobar un invariante en producción cuesta tiempo, por eso `SE-159` distingue qué contratos se mantienen en producción (nota en rango, publicada con nota) y cuáles se retiran después de las pruebas. En un modelo, la exploración exhaustiva deja de ser viable cuando el número de estados crece demasiado (`SE-161` lo mide con una tabla de crecimiento). Y un invariante expresa lo que la persona que lo escribió supo ver: no sustituye a las pruebas con casos que no esperaba.
