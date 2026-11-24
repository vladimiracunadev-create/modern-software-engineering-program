# Actividad

## Definición

En el programa, **actividad** es lo que ocurre dentro del producto: inicios de sesión, vistas, clics, mensajes. Es la definición de `SE-135`: mide movimiento, no logro. Una persona puede generar mucha actividad sin conseguir nada de lo que vino a hacer, y puede conseguir su objetivo con muy poca. Por eso la clase la sitúa entre la producción del equipo (lo que se entrega) y el resultado (lo que cambia para quien usa el producto).

## Por qué importa

Cambia la decisión de qué número se convierte en meta. Según `SE-135`, la actividad es el primer indicio de que algo se usa, pero puede crecer por razones ajenas al valor: una notificación, o un cambio de diseño que obliga a más clics. Un equipo que persigue actividad puede «mejorar» el panel empeorando el producto. En el experimento de los equipos de `SE-135`, la actividad correlaciona apenas 0,20 con el resultado: informa algo, pero no lo bastante para ser meta.

## Cómo funciona

La actividad se cuenta fácil porque el producto ya la registra. Esa facilidad es su trampa: lo que se mide sin esfuerzo tiende a sustituir a lo que importa. `SE-135` propone clasificar cada métrica de una auditoría en cuatro tipos (producción, actividad, resultado, vanidad) y exigir para cada una la decisión que informa y una métrica contraria. La actividad no se descarta: sirve como señal temprana y para diagnosticar. Lo que no sirve es premiarla.

La diferencia útil está dentro de la propia actividad. Enviar una entrega aceptada es actividad cercana al valor; abrir la aplicación no lo es. `SE-136` desarrolla esa distinción con la «tarea útil»: el evento que prueba que la persona logró algo. Además, una cifra acumulada («sesiones totales») solo crece y esconde el estancamiento; por eso `SE-135` recomienda métricas por periodo (activos del mes, retenidos).

## Ejemplo

En la plataforma de entregas de `SE-135`, `metric-audit.md` tiene una fila por métrica: definición calculable (numerador, denominador, ventana, filtros), tipo, decisión que informa, métrica contraria y fecha de revisión. «Sesiones por semana» queda tipificada como actividad. Si el equipo quisiera elevarla como meta, la regla del contrato exige emparejarla con una métrica de resultado y responder «qué haría distinto si bajara». Sin ese contrapeso, la meta no se acepta.

## Errores y confusiones comunes

- **La meta se cumple y nadie mejora.** Se premió la producción o la actividad; corrección de `SE-135`: sustituirla o acompañarla con un resultado y su métrica contraria.
- **El panel solo muestra crecimiento.** La métrica es acumulada; usar cifras por periodo.
- **Confundir actividad con uso valioso.** Que alguien abra la aplicación no prueba que consiga lo que necesita (`SE-136`).
- **Tratarla como vanidad sin matiz.** Una métrica de vanidad no informa ninguna decisión; la actividad sí puede informar, si se declara para qué.

## Límites y cuándo no aplica

La actividad es valiosa cuando todavía no hay un resultado medible: informa de adopción inicial. Deja de valer como meta en cuanto puede subir sin que suba el resultado. Y no es un defecto del concepto sino de la evidencia: la correlación de 0,20 de `SE-135` proviene de un experimento con datos sintéticos, no de un hallazgo general sobre productos reales. El criterio sigue siendo comprobar, en cada producto, qué tan cerca del valor está el evento que se cuenta.
