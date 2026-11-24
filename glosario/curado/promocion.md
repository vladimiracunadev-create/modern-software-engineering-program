# Promoción

## Definición

**Promover** es avanzar un mismo artefacto de una etapa a la siguiente sin reconstruirlo (`SE-470`). `SE-403` lo usa en el contexto de entornos: el movimiento de un cambio ya probado de un entorno al siguiente por un proceso definido. La clave es «el mismo»: lo que se probó es lo que se despliega.

## Por qué importa

Una prueba es evidencia sobre un objeto concreto: si el objeto cambia, la evidencia no se traslada. Cuando cada entorno reconstruye el artefacto, aparece un hueco entre lo probado y lo desplegado. La decisión que cambia es dónde se construye: una sola vez, y de ahí en adelante se mueve ese resultado y se cambia solo la configuración.

## Cómo funciona

`SE-470` explica la razón lógica. El tamaño del hueco entre lo probado y lo desplegado es la probabilidad de que el *build* produzca un resultado distinto. Con una construcción reproducible, ese hueco se acerca a cero y la reconstrucción solo cuesta tiempo; con una que no lo es, es un riesgo que crece con cada etapa.

Lo que sí cambia entre entornos es la **configuración** (direcciones, credenciales, parámetros). Se inyecta en el despliegue y no se incrusta en el artefacto, porque un artefacto con la configuración dentro no se puede promover. Para asegurar que es el mismo objeto se usa su huella (digest), no una etiqueta que pueda moverse.

`SE-403` añade el efecto sobre la divergencia entre entornos: sin promoción, con una edición cada diez semanas, hay divergencia durante 38 de 52 semanas, y las diferencias se acumulan; promover periódicamente la configuración por la misma ruta a todos los entornos mantiene la paridad. El síntoma «preproducción pasa y producción falla» suele indicar configuraciones que divergieron; la corrección es promoción periódica y comparación semanal.

## Ejemplo

El artefacto se construye una vez, queda identificado por su huella y se despliega en preproducción con su configuración de ese entorno. Pasan las pruebas. Ese mismo artefacto (misma huella) se despliega en producción con la configuración de producción. Si en cambio se reconstruyera desde el código, la prueba de preproducción no probaría el artefacto de producción. Es el principio de `SE-470`.

## Errores y confusiones comunes

- **Preproducción pasa y producción falla**: configuraciones que divergieron; se corrige con promoción periódica y comparación semanal.
- **Reconstruir en cada entorno** confiando en que «es el mismo código».
- **Incrustar la configuración en el artefacto**: lo vuelve no promovible.
- **Usar etiquetas mutables** en lugar de huellas para identificar el artefacto.

## Límites y cuándo no aplica

La promoción exige construir de forma reproducible y separar configuración de código; sin eso, no es aplicable de forma segura. Tiene sentido cuando hay varias etapas; en un flujo de una sola etapa no hay nada que promover. Y no sustituye la observación en producción: un artefacto bien promovido puede comportarse distinto con datos y carga reales.
