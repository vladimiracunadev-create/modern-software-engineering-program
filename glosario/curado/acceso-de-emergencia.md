# Acceso de emergencia

## Definición

El **acceso de emergencia** es una concesión excepcional de permisos mayores a los habituales, limitada en el tiempo, justificada y registrada (`SE-403`). Es la válvula de un sistema de mínimo privilegio: reconoce que a veces hay que actuar en producción con más poder del cotidiano, y define bajo qué condiciones se puede hacer sin abrir un hueco permanente.

## Por qué importa

Cuando algo falla en producción la presión empuja a dar permisos amplios «por ahora» y a no volver a quitarlos. La decisión profesional que cambia este concepto es dejar de elegir entre dos malos extremos: bloquear al equipo de guardia cuando más lo necesita, o repartir administración permanente. Con un acceso de emergencia bien diseñado, la rapidez se compra con trazabilidad y con una fecha de caducidad, no con confianza ciega.

## Cómo funciona

`SE-403` describe cuatro propiedades que lo definen y que se pueden comprobar:

1. **Excepcional**: no es el camino normal. Si se usa a diario, el problema son los permisos de base, que se quedaron cortos.
2. **Limitado en el tiempo**: el permiso expira solo; no depende de que alguien se acuerde de revocarlo.
3. **Justificado**: quien lo pide declara por qué, de modo que la revisión posterior tenga contra qué comparar.
4. **Registrado y revisado por otra persona**: el registro lo revisa alguien distinto de quien actuó.

La causa de fondo de la cuarta propiedad es la **separación de funciones**: quien usa el acceso no debería poder borrar su propio rastro. Por eso `SE-403` corrige el error típico («el acceso de emergencia no deja rastro») ubicando el registro en una cuenta de auditoría separada, que quien actúa no puede escribir ni borrar. Sin esa separación, el acceso de emergencia es, en palabras de la clase, un administrador permanente con otro nombre.

## Ejemplo

Un servicio cae a las tres de la madrugada y la persona de guardia necesita leer y modificar un recurso para el que su rol diario no tiene permiso. Solicita el acceso indicando el incidente; recibe permisos ampliados por un plazo corto; cada acción queda en el registro de una cuenta de auditoría separada; al expirar el plazo vuelve sola a sus permisos habituales; al día siguiente otra persona revisa el registro frente a la justificación. Ilustración construida a partir del mecanismo de `SE-403`, no un caso medido.

## Errores y confusiones comunes

- **Registro escribible por quien lo usa**: es el error que nombra `SE-403`. Se corrige con el registro en una cuenta de auditoría aparte.
- **Convertirlo en rutina**: si cada semana hace falta, no es una emergencia sino un rol mal definido.
- **Confundirlo con un permiso de administrador «por si acaso»**: la diferencia es el plazo, la justificación y la revisión; sin ellas es solo un permiso amplio.
- **Pensar que reemplaza el mínimo privilegio**: lo complementa; lo habitual sigue siendo mínimo.

## Límites y cuándo no aplica

`SE-403` fija el límite explícitamente: no debe volverse el camino normal ni deshacer la separación de funciones. No sustituye el diseño de permisos del día a día ni sirve para trabajo planificado, que debe pasar por el flujo ordinario de cambios. Tampoco da por sí solo seguridad: depende de que alguien revise realmente el registro; un registro que nadie lee solo documenta el abuso a posteriori.
