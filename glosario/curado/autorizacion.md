# Autorización

## Definición

La **autorización** es la decisión sobre si una identidad ya autenticada puede realizar una acción sobre un recurso. `SE-027` la define como decisión sobre una acción solicitada por una identidad; `SE-245` y `SE-459` la precisan: si un sujeto puede hacer una acción sobre un recurso, y `SE-459` añade «en un momento dado». No es identificar a la persona (eso es la autenticación), sino evaluar acción sobre objeto bajo reglas.

## Por qué importa

Decide qué datos ve y qué cambios hace cada persona. Su fallo no produce errores visibles: produce una respuesta correcta para la persona equivocada. `SE-459` recuerda que OWASP sitúa la autorización rota a nivel de objeto como el riesgo número uno de las API. La decisión profesional que cambia es dónde se comprueba (en el servidor, en cada petición) y qué se comprueba (la relación del sujeto con ese recurso concreto, no solo su rol).

## Cómo funciona

La sesión responde «quién es»; la autorización, «qué puede hacer sobre qué». Son decisiones separadas y la segunda se repite en cada petición, en el servidor, porque el cliente puede enviar cualquier identificador, rol o campo oculto. Saltzer y Schroeder lo llamaron **mediación completa**: cada acceso a cada objeto se comprueba, sin atajos por caché ni por «ya se comprobó en la pantalla anterior» (`SE-459`). Ocultar un botón mejora la experiencia, no la seguridad.

La regla práctica es un único punto de decisión, invocado en cada acceso, que deniega salvo que una regla permita. Cuando un endpoint recibe un identificador (`/entregas/4521`), el servidor busca el recurso y verifica que el sujeto tiene la relación requerida con *ese* recurso. En un sistema operativo (`SE-027`) la decisión depende de más que el nombre: grupos, credenciales, propietario del objeto y política aplicable.

## Ejemplo

Ilustración mínima, no código de una clase:

```python
entrega = repo.obtener(id)
if entrega is None or entrega.autor_id != sujeto.id:
    raise Denegado()
```

En `SE-459`, un estudiante lee la entrega de otro porque el endpoint comprobaba el rol («estudiante») y no el dueño. Cambiar el número en la dirección es la prueba más simple del atacante y la que menos recursos exige.

## Errores y confusiones comunes

- **Acceso universal.** Se confunde disponibilidad con autorización; corrección: definir quién necesita qué acción y limitar el alcance (`SE-027`).
- **Comprobar el rol y no el dueño.** Un estudiante lee la entrega de otro; corrección: autorización por objeto en cada endpoint con identificador (`SE-459`).
- **Confiar en el cliente.** Ocultar la opción no impide enviar la petición.

## Límites y cuándo no aplica

Una autorización correcta presupone una autenticación válida: si la identidad es falsa, la decisión se aplica a quien no corresponde. Las reglas deben revisarse con el tiempo, porque permisos concedidos se acumulan; `SE-459` lo vincula al mínimo privilegio. Y una decisión bien tomada no impide el abuso por quien sí tiene permiso.
