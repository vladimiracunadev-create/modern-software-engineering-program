# Separación de funciones

## Definición

La **separación de funciones** es el principio de que ninguna persona complete sola una actividad crítica (`SE-403`). Es un control de NIST: quien propone un cambio no es quien lo aprueba, quien despliega no puede alterar el registro de auditoría, quien crea usuarios no puede asignarles administración.

## Por qué importa

Si una sola persona puede iniciar, aprobar y ocultar una acción, un error o un abuso pasa sin que nadie lo detecte. La decisión que cambia es cómo se reparten los permisos: se diseñan pares de funciones que no deben coincidir en una misma persona, y esa regla se comprueba, no solo se declara.

## Cómo funciona

`SE-403` propone expresar cada **par prohibido** como una regla comprobable sobre los **permisos efectivos**. Ejemplos de pares: proponer y aprobar un cambio; desplegar y alterar el registro de auditoría; crear usuarios y asignarles administración. La regla se evalúa automáticamente contra la configuración de permisos real.

La dificultad que señala la clase es la **combinación**: un rol puede ser inocuo y la suma de dos, no. Por eso se revisa la **unión** de los roles de cada persona y no cada rol por separado. Una persona con el rol A y el rol B puede tener, en conjunto, los dos permisos que el par prohíbe aunque ninguno de sus roles lo haga individualmente.

Conecta con otros mecanismos del mismo tema. El **acceso de emergencia** es la excepción controlada: concede permisos mayores por tiempo limitado, pero sin deshacer la separación (quien lo usa no debería poder borrar su registro). El **radio de explosión** acota el daño de un error o de una credencial comprometida. Y la **promoción** de cambios entre entornos por un proceso definido permite que quien aprueba sea distinto de quien escribe.

## Ejemplo

Una regla dice: ninguna identidad puede tener a la vez «desplegar a producción» y «modificar el registro de auditoría». El verificador calcula los permisos efectivos de cada persona (suma de todos sus roles) y detecta que una persona, por pertenecer a dos grupos, tiene ambos. Se corrige antes de que ocurra un incidente. Mecanismo descrito en `SE-403`.

## Errores y confusiones comunes

- **Un script de desarrollo afecta producción**: misma cuenta y prefijos como frontera; se corrige con una cuenta por entorno con políticas heredadas.
- **Revisar cada rol por separado**: la suma de dos inocuos puede violar la regla.
- **Confundirla con el mínimo privilegio**: este limita cuánto puede una persona; la separación impide que una sola complete una actividad crítica.
- **Dejar que quien actúa escriba su propio registro**.

## Límites y cuándo no aplica

En equipos muy pequeños puede no haber dos personas para cada función; entonces se compensa con registros inmutables y revisión posterior, y se declara el límite. La separación añade fricción y tiempo de espera: se aplica a las actividades críticas, no a todas. `SE-403` aclara que sus experimentos son sintéticos (12 permisos y 6 pares de ejemplo) y no evalúan ninguna organización real.
