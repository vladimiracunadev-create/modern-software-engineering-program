# Evento privilegiado

## Definición

Un **evento privilegiado** es un evento de activación de un flujo de integración continua cuyo flujo se ejecuta con secretos y permisos de escritura aunque lo origine un tercero. Es la definición de trabajo de `SE-491`, que lo ejemplifica con `pull_request_target` de GitHub Actions. Es un concepto de seguridad de la cadena de entrega: lo peligroso no es el evento por sí mismo, sino el privilegio con el que corre.

## Por qué importa

Cambia una decisión de configuración de CI aparentemente inocente: «¿qué evento dispara este flujo?». Un flujo disparado por una solicitud de cambio de una bifurcación externa puede ejecutarse con los secretos del repositorio. Si además ejecuta el código del cambio, un tercero cualquiera consigue ejecutar código propio con esos secretos y permisos de escritura. `SE-491` llama a ese patrón «solicitud pwn».

## Cómo funciona

`SE-491` contrasta dos eventos:

- **`pull_request`**: ejecuta el flujo *del cambio*, con permisos reducidos y sin secretos cuando viene de una bifurcación. Es seguro por diseño porque el código no revisado corre sin credenciales.
- **`pull_request_target`**: ejecuta el flujo de la **rama base**, con acceso a secretos y permisos de escritura. Está pensado para tareas como etiquetar o comentar, que necesitan escribir.

El peligro aparece al **combinar** el evento privilegiado con una descarga del código del cambio (por ejemplo, `ref` apuntando al SHA de la cabeza de la solicitud) y ejecutarlo: código no revisado se ejecuta con privilegios completos. La causa es la confusión de dos propiedades que normalmente van juntas: «qué flujo corre» (el de la base, de confianza) y «qué código procesa» (el de un tercero, no confiable).

Defensas de la clase: no descargar ni ejecutar código del cambio en un evento privilegiado, o **dividir el trabajo en dos flujos**: uno sin privilegios que construye y prueba, y otro privilegiado que solo consume el resultado como datos, nunca como código.

## Ejemplo

Un flujo se dispara con `pull_request_target` para comentar el resultado de las pruebas. Para ello descarga el código de la solicitud y ejecuta las pruebas. Una persona externa abre una solicitud cuyo script de pruebas lee las credenciales del entorno y las envía fuera. Como el flujo corre con secretos, la fuga funciona. Corregido: un primer flujo con `pull_request` construye y prueba sin secretos y guarda el resultado como artefacto; un segundo flujo privilegiado lee ese resultado *como datos* y publica el comentario. (Ilustración construida a partir del patrón de `SE-491`.)

## Errores y confusiones comunes

- **Una solicitud externa accede a secretos.** Causa: evento privilegiado más código del cambio; corrección (`SE-491`): `pull_request` o dos flujos separados.
- **Creer que «corre el flujo de la base, luego es seguro».** Lo es solo mientras no procese código del tercero.
- **Tratar el resultado del flujo no privilegiado como confiable.** Se consume como datos: se valida, no se ejecuta ni se interpola en comandos.
- **Dar permisos amplios por defecto.** Reducir los permisos del flujo al mínimo necesario limita el daño si algo falla.

## Límites y cuándo no aplica

Es un término de la clase de CI/CD y del modelo de GitHub Actions; otras plataformas tienen eventos equivalentes con otros nombres, y el principio (separar el privilegio del código no confiable) se traslada, pero el detalle no. Dentro de un repositorio privado con colaboradores de confianza el riesgo baja, pero no desaparece: una dependencia o una rama comprometidas tienen el mismo efecto. Dividir en dos flujos reduce el riesgo, no lo elimina si el segundo flujo trata los datos como comandos.
