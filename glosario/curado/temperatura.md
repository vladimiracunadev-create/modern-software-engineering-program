# Temperatura

## Definición

La **temperatura** es el parámetro de muestreo de un modelo de lenguaje que concentra o reparte la probabilidad entre las continuaciones posibles (`SE-553`).

## Por qué importa

Un modelo recibe un contexto y calcula una distribución de probabilidad sobre el siguiente símbolo; se elige uno, se añade y se repite. De ahí `SE-553` deduce: la salida no es una consulta a una base de hechos, es la continuación *probable* de un texto, y una continuación probable puede ser falsa. La temperatura decide cuánto se arriesga al elegir.

## Cómo funciona

Con temperatura baja, la distribución se concentra y se elige casi siempre lo más probable; con temperatura alta, se reparte y aparecen alternativas. Bajarla reduce la variación entre ejecuciones; con semilla fija, cuando la herramienta la admite, se reduce más. Aun así, en servicios cuya infraestructura introduce otras fuentes de variación, no desaparece del todo.

## Ejemplo

Para extraer un campo estructurado se usa temperatura baja; para generar variantes de un texto, mayor. La respuesta de temperatura cero es la más probable según el modelo.

## Errores y confusiones comunes

- **Creer que temperatura cero da la respuesta correcta.** `SE-553`: es la más probable, no la correcta; da repetibilidad, no corrección.
- **Se acepta una respuesta porque «suena segura».** Tono no es calibración; medir acierto por tramos con tareas del equipo.
- **Votar entre varias respuestas y confirmar un error.** Los errores están correlacionados; añadir un comprobador externo.

## Límites y cuándo no aplica

La temperatura no existe como control en todos los modelos o servicios. No sustituye a una verificación externa de lo que el modelo afirma.
