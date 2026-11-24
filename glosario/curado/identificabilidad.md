# Identificabilidad

## Definición

La **identificabilidad** es la posibilidad de distinguir a una persona de otras en un conjunto de datos, directamente o combinando atributos (cuasi-identificadores) (SE-129, SE-226). Un dato es identificable no solo si contiene un nombre o un número de documento, sino también si la combinación de sus atributos es lo bastante rara como para señalar a alguien.

## Por qué importa

Varios atributos inocuos, combinados, pueden identificar a una persona; **quitar el nombre no basta**. Cambia cómo se comparten, publican y analizan los datos: una tabla sin nombres puede seguir permitiendo reconocer a una persona a quien la conoce.

## Cómo funciona

SE-129 define el **cuasi-identificador**: un atributo que no identifica por sí mismo pero sí junto con otros, como región, rango de edad, rol, dispositivo e idioma. El mecanismo es combinatorio: cada atributo parte el conjunto en grupos más pequeños, y con cuatro o cinco atributos muchos grupos quedan reducidos a una persona.

El **k-anonimato** mide esa propiedad: exige que cada combinación de cuasi-identificadores aparezca en al menos k personas. Si una combinación es única (k = 1), esa persona es reconocible por quien conozca esos atributos. La unicidad **crece rápidamente con el número de atributos** y depende del tamaño del grupo: en una población pequeña (un curso de 30 personas) se identifica con muy pocos atributos.

La defensa es medir y actuar: calcular el **k mínimo** del conjunto, **generalizar** (rangos de edad en lugar de edad exacta, región amplia en lugar de ciudad) o **suprimir** valores raros, y no publicar combinaciones con k menor que el umbral. SE-129 añade una trampa frecuente: los identificadores con hash se recuperan con un script corto cuando el hash no tiene clave y el espacio de posibles valores es pequeño (se prueban todos los valores y se comparan los hashes). La corrección es usar HMAC con una clave guardada aparte, o identificadores aleatorios sin relación con el original.

SE-226 recuerda el mismo principio en contexto de privacidad en el producto: atributos inocuos por separado identifican en conjunto.

## Ejemplo

Una tabla de uso de la plataforma sin nombres con columnas `curso`, `rol`, `rango de edad` e `idioma`. Una fila es la única «docente, 50–59, inglés» del curso de Física. Cualquiera que sepa que hay una única docente de ese perfil la reconoce y ve todo lo demás de su fila. Medido k = 1, se generaliza el curso a «área» o se suprime la fila antes de compartir. (Ilustración del mecanismo de SE-129.)

## Errores y confusiones comunes

- **Un revisor identifica a una persona en una tabla sin nombres**: se combinaron cuasi-identificadores; corrección: medir k mínimo, generalizar o suprimir.
- **Hash sin clave de un identificador** de espacio pequeño.
- **Creer que anonimizar es quitar el nombre.**
- **Medir k solo con los atributos publicados**: el atacante puede tener otras fuentes.

## Límites y cuándo no aplica

El k-anonimato no protege contra quien conoce atributos sensibles homogéneos dentro de un grupo ni contra el cruce con fuentes externas ricas. No sustituye una evaluación jurídica de qué es dato personal. Con grupos muy grandes y pocos atributos, el riesgo es menor, pero debe medirse.
