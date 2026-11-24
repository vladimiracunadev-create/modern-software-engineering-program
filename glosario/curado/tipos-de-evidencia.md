# Tipos de evidencia

## Definición

Los **tipos de evidencia** son una clasificación de la evidencia según su origen (dijo, hizo, comprometió, registro), con una ponderación explícita y revisable (SE-132). Se usan al escribir un brief de producto para declarar cuánto pesa cada tipo de respaldo.

## Por qué importa

Lo que alguien hizo o comprometió pesa distinto de lo que dijo, y el brief debe declarar el peso. Sin esa clasificación, diez frases entusiastas pueden parecer más sólidas que dos personas que entregaron un borrador real. Cambia cómo se leen las entrevistas y los datos: no todo respaldo vale lo mismo.

## Cómo funciona

SE-132 ordena los tipos por fiabilidad:

- **Dijo**: lo que una persona afirma. Es el tipo **más barato y el menos fiable**.
- **Hizo**: lo que la persona hace (por ejemplo, copia su texto a un documento aparte para no perderlo). Es más fiable, porque es comportamiento observado.
- **Comprometió**: lo que la persona se compromete a hacer o entrega (reserva tiempo, entrega un borrador real). Es **el más fiable** de los tres, porque implica un costo.
- **Registro**: datos de uso o de tickets (42 tickets). Cuenta **frecuencia pero no motivos**.

Al **ponderar**, el orden de las opciones puede cambiar: si una opción acumula muchas frases y otra pocos compromisos, el peso decide cuál sube. Por eso el peso es **una decisión del brief, no un detalle interno**, y se muestra la comparación con distintos pesos, de modo que quien decide vea si la conclusión resiste al cambio.

El mecanismo se conecta con la evidencia trazable: cada afirmación del brief declara sus evidencias y su tipo, y el validador comprueba que el identificador exista y que haya al menos dos personas o un registro; que la evidencia diga lo que la afirmación dice lo comprueba una persona. Y con el experimento de demanda, que busca evidencia de tipo «hizo» y «comprometió» a bajo costo.

## Ejemplo

Afirmación: «los docentes necesitan ver quién no entregó». Evidencia: cinco docentes lo dijeron (dijo); dos copian a mano la lista de entregas a una hoja (hizo); una docente pidió acceso anticipado y reservó una hora para probarlo (comprometió); 42 tickets mensuales piden la lista (registro). La opinión de cinco pesa menos que el compromiso de una; el brief declara los pesos y muestra qué pasa si cambian. (Ilustración de la clasificación de SE-132.)

## Errores y confusiones comunes

- **Contar frases como si fueran compromisos.**
- **El brief pasa el validador pero una cifra no coincide con la evidencia**: el validador solo comprueba estructura.
- **Decisión sin responsable ni fecha.**
- **Pesos fijados después de ver el resultado.**

## Límites y cuándo no aplica

La ordenación es una guía, no una ley: un registro bien medido puede ser más fiable que un compromiso aislado. Los pesos son una decisión y deben revisarse. Con muy poca evidencia, ponderar da una falsa precisión.
