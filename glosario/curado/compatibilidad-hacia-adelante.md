# Compatibilidad hacia adelante

## Definición

Un cambio de contrato es **compatible hacia adelante** si un lector viejo entiende los datos escritos con el contrato nuevo. Es el sentido de `SE-164`, repetido en `SE-380` (un lector con el esquema viejo lee datos escritos con el nuevo) y `SE-366`. Es la dirección opuesta a la compatibilidad hacia atrás, en la que el lector nuevo entiende datos viejos.

## Por qué importa

Cambia el orden en que se puede desplegar. Según `SE-164`, una API que se actualiza primero en el servidor necesita compatibilidad hacia adelante para los clientes que aún no se actualizaron: el servidor ya habla el contrato nuevo y los clientes viejos siguen leyendo. Sin ella, cada cambio exige actualizar a todos a la vez, algo imposible cuando hay aplicaciones móviles instaladas o consumidores de otros equipos.

## Cómo funciona

La compatibilidad se evalúa por dirección y por tipo de cambio. `SE-164` ofrece el criterio: muchos cambios son compatibles en una sola dirección. Agregar un campo requerido rompe a quien lee datos viejos con el esquema nuevo (falla hacia atrás); quitarlo rompe a quien espera encontrarlo.

Hacia adelante, el lector viejo debe sobrevivir a lo que no conoce: campos nuevos, valores nuevos de una enumeración. Eso solo ocurre si el contrato exige a los consumidores **tolerar lo desconocido**. Un cliente estricto, que falla ante un campo o valor inesperado, convierte un cambio «que solo agrega» en una ruptura. Por eso `SE-164` pide documentar la tolerancia y probar con un valor nuevo. Para gobernarlo, la política de la plataforma distingue cambios que agregan campos opcionales o valores de enumeración (se anuncian, sin versión mayor) de renombrados, campos requeridos nuevos y eliminaciones (versión mayor, aviso con `Deprecation` y `Sunset` y ventana mínima de 180 días), y un comprobador en integración continua compara esquemas.

## Ejemplo

En la API de entregas de `SE-164`, agregar un campo opcional `comentario` a la respuesta es compatible hacia adelante: un cliente viejo lo ignora. Agregar un valor nuevo `en_revision` a la enumeración de estados solo lo es si los clientes tratan un estado desconocido de forma segura. Si un cliente viejo lanza una excepción ante el valor, el cambio «solo agrega» y aun así rompe.

## Errores y confusiones comunes

- **«Solo agrega, no puede romper».** Rompe a clientes estrictos con lo desconocido; corrección de `SE-164`: exigir tolerancia y probar con un valor nuevo.
- **Confundir las dos direcciones.** Hacia atrás: el lector nuevo, datos viejos; hacia adelante: el lector viejo, datos nuevos.
- **Subir el número de versión y creer que basta.** Se versionó por intención sin comprobar compatibilidad; corrección: comparar esquemas en integración continua.
- **Suponer que un esquema es compatible en ambas direcciones.** Muchos cambios lo son en una sola.

## Límites y cuándo no aplica

Exige que los lectores viejos se escriban con tolerancia desde el principio: no se puede obtener retroactivamente de un cliente ya desplegado y estricto. Donde el almacén se lee con código nuevo y datos antiguos, la dirección que importa es hacia atrás. Y para rupturas inevitables la solución es versionar, avisar y retirar con ventana, no forzar la compatibilidad.
