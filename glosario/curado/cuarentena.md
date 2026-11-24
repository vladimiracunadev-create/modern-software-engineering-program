# Cuarentena

## Definición

La **cuarentena** es, en el sentido principal del programa (`SE-381`), el destino de los registros que no se pueden traducir sin ambigüedad, conservados con el motivo del rechazo. El término tiene otros sentidos en el programa, que esta entrada distingue:

- En `SE-430` (pruebas): estado en el que una prueba se ejecuta sin bloquear la integración, con responsable y fecha de salida.
- En `SE-558` (desarrollo asistido por IA): conjunto de filas apartadas durante una migración por no cumplir la validación, conservadas sin cambios.

Los tres comparten la idea de apartar algo sin descartarlo ni dejarlo pasar, con registro de por qué.

## Por qué importa

Ante un dato ambiguo hay tres respuestas malas: aceptarlo adivinando, rechazarlo en silencio o romper el flujo entero. `SE-381` lo dice así: adivinar es fabricar datos. La cuarentena es la cuarta respuesta, y la que permite decidir con información. La decisión que cambia es tratar lo no traducible como un resultado esperado del proceso, con un destino y un responsable.

## Cómo funciona

En `SE-381`, una nota vacía no es una nota cero; `"N/P"` puede significar «no presentó» o «no procede»; una fecha `03/04/2026` es el 3 de abril o el 4 de marzo según una convención que el proveedor puede no haber declarado. La política correcta es **apartar** el registro a una cuarentena con su motivo, **contar** cuántos hay por motivo y **decidir** con el dueño del dato si se añade una regla, se pide una aclaración o se descarta. La cuarentena hace visible lo que no se pudo traducir, y por eso la capa que rechaza en silencio es tan peligrosa como la que acepta todo.

En pruebas (`SE-430`), una prueba inestable se pone en cuarentena para que no bloquee a todos, pero con responsable, fecha de revisión y criterio de salida; sin eso se olvida. En migraciones (`SE-558`), las filas que no cumplen la validación se apartan sin modificarse para revisarlas después.

## Ejemplo

Una capa recibe filas de un sistema antiguo. Una fila trae `"N/P"` en la nota. La capa no la traduce: la envía a la cuarentena con el motivo «nota ambigua». Al final del día se cuenta: 14 por «nota ambigua», 3 por «fecha imposible». Con el dueño del dato se añade la regla correspondiente y se reprocesan. Ejemplo ilustrativo del flujo de `SE-381`.

## Errores y confusiones comunes

- **Registros que desaparecen sin rastro**: la capa rechaza en silencio; se corrige con cuarentena con motivo, conteo y alarma (`SE-381`).
- **La capa crece sin control**: hace más que traducir; debe limitarse a traducción, validación y cuarentena.
- **Las pruebas en cuarentena se olvidan**: sin responsable ni fecha; se corrige con responsable, fecha de revisión y criterio de salida (`SE-430`).
- **Tratar la cuarentena como basurero**: si nadie la revisa, equivale a descartar.

## Límites y cuándo no aplica

La cuarentena solo vale si alguien la revisa; sin conteo, alarma y dueño, es una pérdida disfrazada. No resuelve la ambigüedad, solo la aplaza con evidencia. Para datos cuyo significado es inequívoco, o cuyo volumen ambiguo sea cero, no hace falta. Y en pruebas, mantener demasiadas en cuarentena oculta una regresión real.
