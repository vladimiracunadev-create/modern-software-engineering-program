# Revocación

## Definición

La **revocación** es la retirada de algo concedido. El sentido principal de `SE-257` (permisos, sensores y capacidades del dispositivo) es la retirada de un permiso concedido, normalmente desde los ajustes del sistema y sin que la aplicación participe. En seguridad de claves (`SE-473`, `SE-272`) es la declaración de que una clave o certificado ya no debe aceptarse. Ambos sentidos comparten la estructura: concedido en el pasado, retirado después, y el que verifica debe enterarse.

## Por qué importa

Un permiso comprobado una vez al iniciar la sesión puede dejar de valer a los diez minutos (`SE-257`). Y una clave filtrada sigue funcionando hasta que alguien la declara inválida. La decisión de diseño es cuándo y cómo se comprueba.

## Cómo funciona

**Permisos de dispositivo (`SE-257`).** La revocación ocurre fuera de la aplicación y puede llegar en cualquier momento. Comprobar el permiso al iniciar la sesión y asumirlo después produce usos tras la revocación. Comprobar en cada uso lo evita y cuesta una consulta; comprobar periódicamente reduce el costo y deja una ventana. La tolerancia de esa ventana es una decisión de privacidad.

**Claves (`SE-473`).** Las claves se pierden, se filtran o caducan. La *rotación* es el cambio planificado; la *revocación*, la declaración de que una clave ya no debe usarse. Una rotación sólida se **declara antes de necesitarla**, firmada con la clave vigente, de modo que los clientes aprendan la clave nueva por la cadena de confianza anterior. Una revocación necesita llegar a los clientes, y entre el robo de la clave y la llegada de la revocación hay una ventana en la que el atacante puede firmar. `SE-272` la aplica a dispositivos: retirar una clave o certificado para que el servidor deje de aceptarlo.

## Ejemplo

Ilustración propia de permisos: una aplicación de entregas guarda la ubicación solo mientras la usa. La persona revoca el permiso desde los ajustes; en el siguiente uso, la comprobación devuelve «denegado» y la función ofrece alternativa en vez de fallar. De claves: un dispositivo robado se revoca en el servidor; mientras la lista de revocación no llega a los clientes, hay una ventana.

## Errores y confusiones comunes

- **Comprobar el permiso una vez y asumirlo.**
- **No definir qué hace la función al revocarse.**
- **Confundir revocación con caducidad:** la caducidad ocurre sola; la revocación es una acción.
- **Creer que revocar equivale a borrar los datos ya obtenidos.**

## Límites y cuándo no aplica

La revocación no deshace lo ya hecho: las firmas anteriores y los datos ya recogidos siguen existiendo. La ventana entre el compromiso y la revocación no se elimina, solo se acota. Para clientes sin conexión, la revocación no llega hasta que se reconectan.
