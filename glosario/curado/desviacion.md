# Desviación

## Definición

En un estándar de codificación, una **desviación** es una excepción justificada, revisada y registrada de una regla (`SE-452`). (En estadística, «desviación» designa la dispersión de una medida; aquí es la excepción formal.)

## Por qué importa

Una regla mecánica también se equivoca. Si un aviso no se puede descartar con una justificación revisada, el equipo aprende a ignorar los avisos y la política deja de proteger.

## Cómo funciona

`SE-452`: la regla de recursión marca una función `altura` que recorre un árbol llamándose a sí misma, aunque su profundidad esté acotada y sea analizable. La respuesta no es abandonar la regla sino ajustarla (permitir recursión con una cota declarada y comprobada) o permitir una desviación: una excepción por escrito, con su motivo, su alcance y quién la aprobó. Para bases existentes, la clase propone congelar los avisos conocidos en un archivo, exigir cero avisos nuevos y atacar el archivo por riesgo.

## Ejemplo

`SE-452`: un equipo adopta un estándar y aparecen 4 000 avisos el primer día; en lugar de silenciar la regla más ruidosa, congela la base existente, exige cero avisos nuevos y reduce el archivo empezando por las funciones del limitador.

## Errores y confusiones comunes

Silenciar una regla ruidosa en lugar de desviarse con justificación; desviaciones sin dueño ni alcance.

## Límites y cuándo no aplica

Cuantas más desviaciones, menos vale el estándar; deben revisarse periódicamente.
