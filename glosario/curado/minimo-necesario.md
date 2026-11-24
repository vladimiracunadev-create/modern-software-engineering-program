# Mínimo necesario

## Definición

El **mínimo necesario** es el criterio de pedir solo la capacidad, con la precisión y el alcance más pequeños, sin los cuales una función falla. Es el sentido de `SE-257` (permisos, sensores y capacidades del dispositivo); `SE-226` lo aplica a la telemetría de herramientas: cada dato recogido es un riesgo que hay que justificar. Es el mismo espíritu del mínimo privilegio y de la minimización de datos, aplicado a lo que una aplicación solicita.

## Por qué importa

Cada capacidad que se pide es una superficie de ataque y una carga de confianza. Pedir menos reduce lo que puede filtrarse, abusarse o exigirse en una revisión de tienda, y aumenta la probabilidad de que la persona acepte.

## Cómo funciona

`SE-257` propone una pregunta de control: **qué función falla sin la capacidad**, no qué dato podría ser útil. Dos formas de reducir:

- **Precisión:** si la función solo necesita saber que se entregó en la ciudad, la ubicación aproximada alcanza.
- **Alcance:** si solo adjunta una imagen, el selector del sistema puede evitar pedir acceso a toda la galería.

En `SE-226`, el principio se ve en la telemetría *opt-in*: se recoge solo lo que se puede justificar, con consentimiento y plazo de retención. Los pasos prácticos son enumerar las funciones, asignar a cada una la capacidad más estrecha, definir qué ocurre si se deniega o revoca, y decidir cuánto tiempo se guarda el dato.

## Ejemplo

El equipo del cliente escribe una tabla de capacidades con una fila por función (`SE-257`): qué capacidad necesita, con qué precisión, cuándo la pide, qué hace si se deniega o revoca y cuánto tiempo guarda el dato. «Adjuntar foto» usa el selector del sistema o la cámara, y si se deniega, ofrece la galería. «Notificar vencimiento» usa notificaciones y, si se deniega, muestra un aviso dentro de la aplicación. «Registrar lugar de entrega» no existe: el equipo decidió que no lo necesitaba y no pidió ubicación.

## Errores y confusiones comunes

- **Pedir todos los permisos al inicio,** antes de que la función los necesite.
- **Pedir ubicación precisa cuando basta la aproximada.**
- **No definir qué ocurre al denegar:** la función se rompe en vez de degradarse.
- **Confundirlo con «pedir poco» sin criterio:** el criterio es lo que la función necesita para funcionar.

## Límites y cuándo no aplica

Una capacidad realmente necesaria no se evita: si la función es navegación, la ubicación precisa es parte del mínimo. Las reglas de permisos de cada plataforma cambian; la tabla de la clase refleja las de su fecha. Minimizar no reemplaza proteger bien los datos que sí se recogen.
