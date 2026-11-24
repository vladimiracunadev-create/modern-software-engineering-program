# Caducidad

## Definición

La **caducidad** es el momento a partir del cual un registro deja de valer o se borra. En `SE-593` se aplica a la memoria de un agente; en `SE-432`, a las exclusiones de una estrategia de pruebas.

## Por qué importa

Lo que se guarda para siempre se vuelve obsoleto y, si son datos personales, un riesgo. Una memoria con datos personales necesita caducidad, borrado a petición y control de quién escribe (`SE-593`). Es una decisión que ninguna otra estrategia de memoria ofrece: **olvidar a propósito**.

## Cómo funciona

Cada tipo de hecho persistente tiene clave, esquema, caducidad y quién puede escribirlo. El agente no escribe directamente: propone un registro con la cita del turno de donde lo sacó, y una validación de código comprueba el esquema y que quien solicita tenga permiso. La caducidad hace que lo almacenado deje de ser consultado cuando pierde vigencia.

## Ejemplo

`SE-593`: el equipo de *Avisos* define cuatro tipos de hecho persistente (silencios por curso, preferencias de canal, excepciones de plazo y contactos alternativos); un silencio caduca el día indicado.

## Errores y confusiones comunes

Guardar sin fecha de vencimiento; borrar al caducar sin comprobar que algo no depende del registro.

## Límites y cuándo no aplica

La caducidad reduce el volumen y el riesgo, pero no sustituye al borrado a petición ni a la validación del esquema.
