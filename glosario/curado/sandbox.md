# Sandbox

## Definición

Un **sandbox** (caja de arena) es un aislamiento que el sistema impone entre aplicaciones. En el sentido de `SE-262` (firma, sandbox y seguridad del cliente), es el aislamiento que la plataforma impone *entre* aplicaciones y que **no protege contra errores de la propia aplicación**. `SE-582` (sandboxes, reversibilidad y control de daño) usa el término de forma más amplia: un entorno que restringe lo que un proceso puede hacer en el sistema, por ejemplo para ejecutar un agente.

## Por qué importa

Es fácil sobrestimarlo. El sandbox impide que una aplicación lea los datos de otra sin permiso, pero no impide que la propia aplicación lea archivos suyos que no debía ni que sirva un archivo cuya ruta eligió un tercero. Los errores de confinamiento ocurren *dentro* del sandbox.

## Cómo funciona

`SE-262`: en Android, cada aplicación corre con un usuario de sistema propio y el kernel impone el aislamiento; otras plataformas aíslan de otras formas. Ese límite se impone desde fuera, con permisos del sistema operativo sobre archivos, procesos y recursos.

Para el sentido ampliado de `SE-582`, el mecanismo es el mismo en espíritu: restringir qué archivos, red y llamadas al sistema puede usar un proceso, de modo que un fallo o un abuso quede acotado. La reversibilidad (poder deshacer lo que el proceso cambió) y el control de daño completan la protección.

La consecuencia de diseño es una **división de responsabilidades**: el sandbox protege una aplicación de otra; la aplicación debe protegerse a sí misma de sus entradas, con validación del lado del servidor, confinamiento de rutas y verificación de las actualizaciones.

## Ejemplo

El equipo del cliente en `SE-262` escribe su modelo de amenazas con una fila por activo (borrador local, token de sesión, paquete de actualización, adjuntos) y una columna por capacidad del atacante (lee el paquete, modifica archivos, observa el tráfico, controla el dispositivo). De la tabla salen reglas: el servidor valida todo, el cliente solo guarda tokens de corta duración emitidos por el servidor, los adjuntos se confinan a una carpeta con normalización, y la actualización se verifica con una firma asimétrica cuya clave privada solo existe en el sistema de compilación.

## Errores y confusiones comunes

- **Creer que el sandbox protege de los errores propios:** no lo hace.
- **Dejar la ruta de un archivo en manos de una entrada externa** dentro del sandbox.
- **Confundirlo con una máquina virtual o un contenedor:** son otros mecanismos de aislamiento, con otras garantías.
- **Considerar el sandbox como control único.**

## Límites y cuándo no aplica

Un sandbox protege hasta donde llegue la implementación del sistema; sus fallos permiten escapes. No cubre lo que la propia aplicación tiene permitido (por ejemplo, un permiso que la persona concedió). Para código de terceros no confiable, el aislamiento debe elegirse con un modelo de amenazas explícito.
