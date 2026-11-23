# Mínimo privilegio

## Definición

El **mínimo privilegio** es el principio de conceder a cada sujeto (persona, programa, cuenta de servicio, flujo o agente) solo los permisos que necesita para su función y solo mientras los necesita. Las clases lo formulan en cuatro contextos con el mismo núcleo: `SE-027` lo define como autoridad mínima acotada en acción, alcance y duración; `SE-459` como concesión estricta a la función y al tiempo; `SE-478` y `SE-491` lo aplican a cada flujo y trabajo de una canalización de integración continua; y `SE-569` lo traslada a los agentes de IA. La formulación clásica es de Saltzer y Schroeder (1975): cada programa y cada usuario deben operar con el menor conjunto de privilegios necesario para su trabajo.

## Por qué importa

Un permiso que nadie usa sigue siendo un permiso que alguien puede abusar. Según `SE-569`, limitar los privilegios acota el daño que puede resultar de un accidente o de un error y reduce el número de programas con privilegios que hay que revisar. No evita el fallo: reduce su radio. Por eso es la defensa que más rinde cuando el control de entrada ya falló, sea por una credencial filtrada, un trabajo de compilación comprometido o un agente que interpreta mal una instrucción.

## Cómo funciona

El principio se aplica en tres dimensiones que `SE-027` nombra juntas: **acción** (qué operaciones), **alcance** (sobre qué recursos) y **duración** (por cuánto tiempo). En la práctica, las clases lo concretan así:

- **Quitar** lo que la tarea no necesita: un agente que corrige un error no necesita enviar correos (`SE-569`).
- **Confinar** lo que queda: escribir solo dentro del espacio de trabajo, leer solo el repositorio del trabajo (`SE-569`, `SE-478`).
- **Exigir aprobación humana** para lo que no se puede acotar (`SE-569`).
- **Conceder con caducidad** y renovar solo lo necesario, para que el permiso no sobreviva a la tarea (`SE-459`).

La causa de que no basta configurarlo una vez la explica `SE-459`: el mínimo privilegio **se pierde con el tiempo**. Cada cambio de función añade permisos y rara vez retira los anteriores; tras unos meses, la persona tiene todo lo que alguna vez necesitó. Las tres respuestas son revisar periódicamente y retirar (cuesta trabajo humano y deja residuo), conceder con caducidad (cuesta solicitudes y fricción) o reasignar el conjunto completo al cambiar de función (exige un registro de qué se concedió y por qué). Cuanto más sensible el permiso, más corta debe ser la concesión. Las cuentas de servicio siguen la misma regla.

## Ejemplo

En la canalización de `SE-478` y `SE-491`, cada flujo y cada trabajo recibe solo los permisos que necesita. Como ilustración (no es un caso de las clases): un trabajo que solo ejecuta pruebas no necesita permiso para publicar, de modo que si una dependencia comprometida corre en él, el daño queda limitado a lo que ese trabajo podía tocar. En `SE-569` el mismo razonamiento se aplica a un agente: se le retiran las herramientas que no necesita, se confina el espacio donde escribe y se pide aprobación para lo irreversible.

## Errores y confusiones comunes

- **Configurarlo una vez y olvidarlo.** Los permisos se acumulan con los cambios de función (`SE-459`); sin revisión o caducidad, el mínimo se convierte en el máximo histórico.
- **Confundir mínimo privilegio con denegar todo.** El principio pide los permisos que la función necesita, no ninguno; una función sin los permisos que requiere no se puede ejecutar y acaba compartiendo credenciales.
- **Dar permisos amplios «por si acaso» a cuentas de servicio y flujos.** Las cuentas de servicio y los trabajos automáticos también son sujetos y se rigen por la misma regla.
- **Tratar la aprobación humana como sustituto del confinamiento.** `SE-569` los trata como capas distintas: aprobar cada acción no reemplaza limitar lo que el agente puede tocar.

## Límites y cuándo no aplica

El mínimo privilegio reduce el daño, no lo elimina: un permiso legítimo mal usado sigue causando daño dentro de su alcance. Tiene costos operativos que las clases reconocen: revisar cuesta trabajo humano, caducar cuesta solicitudes y fricción, y cuanto más fino el control, más permisos que administrar. Exige conocer qué necesita realmente cada función, y esa información suele estar incompleta; por eso se afina con el uso observado. Y no sustituye a la autenticación, a la separación de funciones ni a la detección: es una capa más de defensa en profundidad.
