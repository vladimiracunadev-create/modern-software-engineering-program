# Herramientas

## Definición

En el trabajo con agentes y modelos, las **herramientas** (*tools*) son las funciones que un servidor expone y que el modelo puede invocar; las controla el modelo, no la persona ni la aplicación. `SE-571` lo define así en el contexto del protocolo de contexto de modelos (MCP). `SE-577` lo amplía al arnés de un agente: las herramientas son las acciones que el *harness* acepta traducir en efectos (leer un archivo, aplicar un cambio, ejecutar pruebas). El programa usa también «herramienta» en otros sentidos (las de ingeniería en general); aquí se trata el de agentes.

## Por qué importa

Las herramientas son el límite entre lo que el agente *dice* y lo que *hace*. Cada una amplía lo que el agente puede lograr y lo que puede romper. Decidir qué herramientas se exponen, con qué permisos y con qué verificación es diseñar la superficie de riesgo del agente, no un detalle de integración.

## Cómo funciona

El modelo recibe una descripción de cada herramienta (nombre, parámetros, propósito) y decide cuándo invocarla; el servidor o el arnés ejecuta la acción y devuelve el resultado. Dos consecuencias de que las controle el modelo:

- **Lo que el agente puede hacer es exactamente lo que el arnés acepta traducir**; quitar una herramienta cambia su comportamiento. `SE-577` lo muestra: quitar la herramienta de escritura deja al agente leyendo en bucle, porque la política no tiene otra salida. El agente no «sabe» que no puede escribir hasta que lo intenta, y un arnés que no lo registra deja una traza idéntica a la del contexto perdido.
- **La decisión de usarlas es probabilística**, por lo que el servidor no debe confiar en la entrada: la autorización y la validación se hacen en el servidor, no en el prompt.

`SE-571` aporta dos puntos de control: verificar en el servidor la coherencia entre cabecera y cuerpo (para que no se ejecute una herramienta no autorizada), y fijar el tiempo de vida de cualquier caché de la lista de herramientas según el riesgo de la herramienta.

## Ejemplo

`SE-577`: el equipo adopta un asistente de código para el mantenimiento de *Avisos*. A la tercera semana, tres cambios llegan a revisión con las pruebas en rojo: el asistente los dio por terminados. Compiten tres hipótesis (el modelo empeoró, cambió el prompt, cambió el entorno). Las trazas muestran que ninguno ejecutó las pruebas; el archivo de instrucciones había perdido la línea de verificación en una reorganización. La corrección no toca el modelo: restaura la línea y añade una compuerta (`SE-583`) que rechaza la terminación sin pruebas en verde. La lección es que el comportamiento depende de las herramientas, las instrucciones y las compuertas, no solo del modelo.

## Errores y confusiones comunes

- **Se ejecuta una herramienta no autorizada.** Causa (`SE-571`): cabecera y cuerpo no coinciden y nadie lo comprueba; corrección: verificar la coherencia en el servidor y rechazar.
- **Una herramienta retirada sigue funcionando.** Caché demasiado larga; fijar el tiempo de vida por el riesgo de la herramienta.
- **Confiar en el prompt para limitar el alcance.** Un límite que solo está en el texto de instrucciones no es un control.
- **Confundirlas con recursos o prompts del protocolo.** En MCP, las herramientas son las controladas por el modelo; otros elementos los controla la aplicación o la persona.

## Límites y cuándo no aplica

Una herramienta bien definida no hace seguro a un agente: hay que acotar lo que puede tocar (confinamiento, mínimo privilegio) y poder deshacer lo que hizo. `SE-577` es un caso de estudio sobre un asistente, no una medición de agentes reales. Y la lista de herramientas debe ser pequeña y con nombres claros: más herramientas amplían la superficie y la confusión del modelo.
