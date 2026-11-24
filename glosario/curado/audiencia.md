# Audiencia

## Definición

En el programa, **audiencia** es un grupo de personas descrito por lo que sabe, lo que quiere conseguir y el tiempo del que dispone al leer; no es un cargo ni una etiqueta de rol. Es el sentido de `SE-205`, de documentación. En seguridad, el mismo término tiene otro sentido, el del campo *audience* de una credencial: el destinatario para el que un token es válido (`SE-245`, `SE-286`, `SE-484`). Esta entrada desarrolla el primero y señala el segundo para no confundirlos.

## Por qué importa

Una audiencia mal definida produce documentación que nadie termina. Define el vocabulario, el nivel de detalle y lo que se puede dar por sabido: un mismo hecho se escribe distinto para cada grupo. En el sentido de seguridad, comprobar la audiencia decide si una API acepta un token emitido para otro servicio.

## Cómo funciona

Según `SE-205`, «docente» es un cargo; «docente que debe mover un plazo antes de que termine el día, sin haber leído nunca el manual» es una audiencia. La diferencia fija decisiones concretas: si se puede usar «prórroga» sin definirla, si el primer párrafo da la respuesta o el contexto, si hay capturas o comandos. La audiencia se descubre preguntando a personas reales; cuando no es posible, se escribe como hipótesis y se marca como tal.

En el sentido de seguridad, el mecanismo es una comprobación. `SE-245` indica que verificar un token exige varias cosas: algoritmo esperado, firma contra la clave del emisor, emisor y audiencia propios de esta API, y hora entre `nbf` y `exp`. Si la audiencia no se comprueba, un token legítimo emitido para otra API funciona aquí.

## Ejemplo

El portal documental de la plataforma de entregas (`SE-205`) mantiene un inventario de tareas por audiencia en `audiencias.md`: estudiante (entender el descuento, pedir prórroga), docente (cambiar plazo, conceder prórroga), secretaría (exportar el acta) y mantenimiento (depurar el cálculo). La regla vive una sola vez en `politica/penalizacion.md`; las cuatro vistas la enlazan con una frase de contexto. Cuando el tope cambia al 30 %, es un solo commit en la fuente y una lista señala las cuatro vistas por revisar.

## Errores y confusiones comunes

- **Una página explica todo y nadie la termina.** Mezcla audiencias y tareas; corrección: separar por audiencia o tarea y enlazar lo común (`SE-205`).
- **Definir la audiencia por cargo.** El cargo no dice qué sabe ni cuánto tiempo tiene.
- **Copiar la regla en cada vista.** Genera versiones divergentes; mejor una fuente y vistas que la enlazan.
- **Un token para otro receptor funciona.** No se comprueba la audiencia (`SE-484`, `SE-245`); corrección: exigir la audiencia propia y el emisor.

## Límites y cuándo no aplica

La audiencia documental, cuando no se pudo preguntar a personas reales, es una hipótesis y debe marcarse así; nada garantiza que describa a quien realmente lee. Y no toda documentación necesita varias audiencias: un README mínimo de una herramienta personal puede tener una sola. En seguridad, la audiencia es una comprobación necesaria pero no suficiente: no sustituye verificar firma, emisor y vigencia.
