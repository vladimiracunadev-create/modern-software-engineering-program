# Temporizador de vigilancia

## Definición

Un **temporizador de vigilancia** (*watchdog*) es un temporizador que reinicia el sistema si el firmware no lo reinicia periódicamente. Es el sentido de `SE-274` (safety, seguridad y vida útil prolongada). El firmware «lo alimenta» (reinicia su cuenta) mientras funciona; si deja de hacerlo, el temporizador vence y fuerza un reinicio.

## Por qué importa

Recupera de cuelgues y de bucles infinitos sin intervención humana, algo esencial en dispositivos desplegados sin acceso. A cambio, su plazo es un intercambio de riesgos: corto, recupera rápido pero reinicia sin motivo durante operaciones largas legítimas; largo, casi no se equivoca y deja al dispositivo colgado mucho tiempo.

## Cómo funciona

`SE-274` da dos reglas de diseño:

1. **El plazo se fija con la distribución del tiempo de las operaciones más largas,** no con la intuición.
2. **La alimentación se hace solo cuando varias comprobaciones de salud pasan,** no desde una interrupción que sigue viva aunque el programa principal esté colgado.

La segunda regla es la que más se incumple: si una interrupción de temporizador alimenta el watchdog automáticamente, el sistema puede estar colgado y el watchdog nunca vencer. La alimentación debe depender de pruebas de que las tareas importantes avanzaron.

Se combina con el **estado seguro**: qué hace el dispositivo mientras reinicia y al arrancar.

## Ejemplo

El análisis de peligros del nodo en `SE-274` incluye: peligro, el firmware se cuelga; defensa, temporizador de vigilancia con plazo de 5 s, alimentado solo tras una comprobación de salud, y operaciones largas partidas en pasos de 200 ms. Así, una operación legítima nunca excede el plazo, y un bucle infinito lo vence en 5 segundos. Los otros peligros de la misma tabla (un contador que da la vuelta, un atacante que apaga el extractor) se tratan con otras defensas.

## Errores y confusiones comunes

- **Alimentarlo desde una interrupción,** que hace que nunca venza ante un cuelgue del bucle principal.
- **Plazo corto que reinicia durante operaciones largas legítimas.**
- **Usarlo como sustituto de corregir el defecto:** reiniciar oculta el síntoma.
- **No registrar los reinicios:** pierde la señal de que algo falla.

## Límites y cuándo no aplica

No arregla fallos que sobreviven al reinicio (datos corruptos, hardware dañado). Un reinicio puede ser peligroso en el estado físico del sistema (un actuador a mitad de movimiento), por eso el estado seguro debe estar definido. Los plazos de la clase son los de un nodo ambiental simulado.
