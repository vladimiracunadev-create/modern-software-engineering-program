# Seudonimización

## Definición

La **seudonimización** sustituye un identificador (un nombre, un correo, un número) por un seudónimo, de modo que la persona solo pueda reidentificarse con información adicional que se guarda aparte. Es el sentido de `SE-129`, `SE-358`, `SE-369` y `SE-463`; `SE-295` la presenta, en el dominio de salud y datos sensibles, como sustitución de un identificador por un código reversible para quien posea la tabla de equivalencias. Lo decisivo es la **reversibilidad controlada**: el vínculo existe, pero vive en otro lugar y bajo otro control de acceso.

## Por qué importa

Permite trabajar con datos sin mostrar a quién pertenecen: analizar, depurar o probar sin exponer identidades. Pero tiene una consecuencia legal que `SE-129` y `SE-463` repiten: para la normativa de protección de datos (el RGPD, citado por las clases), el dato seudonimizado **sigue siendo dato personal**, porque la reidentificación es posible con la información adicional. Es una medida de reducción de riesgo, no una salida del ámbito de la norma.

## Cómo funciona

El mecanismo importa porque hay formas de seudonimizar que no protegen:

- **Hash sin clave.** `SE-129` muestra por qué falla: un hash de un identificador de siete dígitos no protege, porque quien conozca el formato puede calcular el hash de los diez millones de valores posibles y comparar. `SE-463` lo repite para correos: con una lista de candidatos, se calculan los hashes y se comparan.
- **HMAC con clave secreta.** Un código de autenticación con clave obliga a conocer la clave; esta se guarda aparte, con acceso restringido, y se destruye cuando la finalidad termina (`SE-129`).
- **Clave por conjunto.** `SE-463` advierte que una clave única para todos los conjuntos hace que los seudónimos coincidan entre conjuntos y se puedan **enlazar**; con una clave por conjunto, cada uno tiene seudónimos distintos y solo quien tiene las claves puede cruzarlos.

La causa común es la información adicional: la protección es exactamente tan fuerte como la separación y el control de esa clave o tabla de equivalencias.

## Ejemplo

En `SE-129`, un identificador de siete dígitos tiene diez millones de valores posibles. Con un hash sin clave, calcular los diez millones de hashes y compararlos es trivial; con HMAC y una clave guardada aparte, quien tiene los hashes pero no la clave no puede reconstruir los identificadores. `SE-463` añade que los entornos de prueba merecen la misma disciplina: datos sintéticos o enmascarados, nunca una copia de producción.

## Errores y confusiones comunes

- **Creer que un hash simple basta.** Sin clave, el espacio de valores posibles se enumera (`SE-129`, `SE-463`).
- **Creer que seudonimizar es anonimizar.** El dato sigue siendo personal para la norma porque se puede reidentificar con la información adicional (`SE-129`, `SE-463`).
- **Usar la misma clave en todos los conjuntos.** Los seudónimos coinciden y permiten enlazar registros entre conjuntos (`SE-463`).
- **Guardar la clave junto a los datos.** Anula la separación que define la técnica.

## Límites y cuándo no aplica

La seudonimización no impide la reidentificación por otros atributos: para ese riesgo, `SE-369` y `SE-463` tratan el k-anonimato sobre los cuasi-identificadores, que es una técnica distinta. Tampoco elimina las obligaciones legales sobre el dato. Y su fuerza depende de gestionar la clave: si se pierde el control de la clave o de la tabla, el seudónimo deja de proteger. Las clases citan el RGPD y normas nacionales como fuente; la aplicación legal concreta debe consultarse con la norma vigente y con asesoría competente, no con este glosario.
