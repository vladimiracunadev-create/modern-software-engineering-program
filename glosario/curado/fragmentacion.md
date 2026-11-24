# Fragmentación

## Definición

En sistemas de recuperación para modelos, la **fragmentación** (*chunking*) es la división de documentos en unidades indexables, con un tamaño y una solapación. Es el sentido común a `SE-555` (contexto, archivos, memoria y recuperación), `SE-214` (documentación para humanos, máquinas y LLM) y `SE-594` (embeddings, recuperación y agentic RAG). Aquí no se trata de la fragmentación de memoria ni de disco.

## Por qué importa

Cambia qué encuentra el sistema y cuánto cuesta. El tamaño del fragmento condiciona qué se recupera. Según `SE-214`, separar una regla de su excepción produce respuestas falsas con apariencia de fuente: el sistema cita un fragmento real que, sin su excepción, lleva a una conclusión equivocada. Y según `SE-594`, decide qué unidad se recupera y con qué contexto.

## Cómo funciona

El documento se parte en fragmentos que se indexan (por palabras clave como BM25 o por vectores) y se recuperan por consulta. Dos parámetros dominan: el **tamaño** y la **solapación** entre fragmentos consecutivos. `SE-594` describe el compromiso: un fragmento demasiado corto pierde el contexto que lo hace entendible («el plazo es de 72 horas», ¿de qué?); uno demasiado largo diluye la señal y llena el contexto del modelo.

Dos prácticas reducen el daño. Primera, fragmentar **por estructura** (secciones, funciones) y con solapamiento, no por número fijo de caracteres, para no empezar a mitad de frase (`SE-555`). Segunda, conservar la cita al fragmento exacto con enlace a la fuente, de modo que se pueda verificar. Pero la cita no basta si el fragmento está truncado en una excepción: la respuesta puede ser errónea con una cita real. Por eso `SE-594` añade que una base vectorial aporta escalabilidad, filtros y actualización, no calidad por sí misma: la calidad la determinan el modelo de embeddings y la fragmentación.

## Ejemplo

En el escenario hipotético de `SE-555`, el equipo diseña el contexto para tres tareas. Para «explicar la regla de redondeo» no recupera nada: aporta la función entera y la sección de decisiones fechada y exige citar líneas. Para «¿qué decidimos sobre las notas ausentes?» recupera por BM25 con fragmentos de 200 palabras y filtro de versión vigente; la respuesta debe incluir la fecha de la decisión.

## Errores y confusiones comunes

- **El fragmento empieza a mitad de frase.** Fragmentación por número fijo de caracteres; fragmentar por estructura y con solapamiento.
- **Separar la regla de su excepción.** Produce respuestas falsas con apariencia de fuente.
- **Atribuir la calidad a la base vectorial.** Depende de los embeddings y de la fragmentación.
- **Usar el mismo tamaño para todo documento.** Un código y un acta no se parten igual.

## Límites y cuándo no aplica

Si la fuente cabe entera en el contexto y la tarea la necesita, fragmentar es innecesario y arriesga perder relaciones. Ningún tamaño es universalmente correcto: se ajusta evaluando con consultas reales. Los escenarios de `SE-555` son hipotéticos, sin datos reales.
