# Bandera de funcionalidad

## Definición

Una **bandera de funcionalidad** (*feature flag*) es una condición en el código que activa o desactiva un comportamiento sin desplegar código nuevo. `SE-485` la define así, `SE-475` como una condición de ejecución que activa o desactiva una función sin desplegar y `SE-414` como un interruptor que decide qué código se ejecuta. `SE-414` insiste en no mezclarla con otras dos cosas que los productos SaaS suelen confundir: el **plan** (un paquete comercial que se vende) y el **derecho** (lo que una cuenta concreta puede hacer hoy, con límites y vencimientos).

## Por qué importa

Permite separar la **exposición** del **despliegue** (`SE-485`): se despliega apagada, se enciende para unas personas y se apaga ante un problema sin volver a la versión anterior. Eso reduce el costo de revertir y habilita lanzamientos graduales.

## Cómo funciona

El código contiene la condición y el valor se lee de configuración, de modo que cambiarlo no requiere un nuevo despliegue. `SE-485` toma de Fowler una tipología: banderas de **lanzamiento** (de corta vida), de **experimento**, **operativas** (para apagar una dependencia) y de **permisos**. Cada tipo tiene ciclo de vida distinto. `SE-414` separa su rol del de los derechos de uso: la bandera es un interruptor técnico, el derecho es una regla de negocio por cuenta.

## Ejemplo

`SE-485`: una función nueva se despliega con la bandera apagada, se activa para un grupo de personas y, si aparece un problema, se apaga sin desplegar de nuevo. `SE-414` muestra el error contrario: usar la misma tabla o el mismo `if` para plan, derecho y bandera.

## Errores y confusiones comunes

- **Mezclar plan, derecho y bandera** en una misma condición (`SE-414`).
- **Banderas olvidadas.** Se convierten en código que nadie se atreve a borrar (`SE-485`).
- **Ignorar las combinaciones.** Cada bandera duplica las configuraciones posibles del sistema y las combinaciones dejan de probarse (`SE-485`).

## Límites y cuándo no aplica

`SE-485` nombra el costo: duplicación de configuraciones, combinaciones sin probar y banderas olvidadas; la disciplina consiste en darle a cada bandera un dueño y un plazo de retiro. Una bandera cambia la ruta de ejecución en producción, de modo que apagarla no equivale a deshacer cambios de datos ya realizados con ella encendida.
