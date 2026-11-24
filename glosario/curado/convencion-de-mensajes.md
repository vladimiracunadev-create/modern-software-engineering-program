# Convención de mensajes

## Definición

Una **convención de mensajes** es una forma común, legible por máquinas, para los mensajes de commit. Es el sentido de `SE-199`. El ejemplo que cita es Conventional Commits: un tipo (`feat`, `fix`, `docs`…), un alcance opcional y una descripción. Es una convención de **forma**; no dice si el contenido del mensaje es verdadero ni si el tipo elegido es el correcto.

## Por qué importa

Cambia lo que se puede automatizar sobre el historial. Con una forma común, se generan registros de cambios, se decide el número de versión y se filtra el historial sin leerlo todo. `SE-199` añade la condición que la vuelve útil: su valor depende de que se cumpla, y por eso se comprueba en un gancho local o en integración continua.

## Cómo funciona

El mensaje se descompone en campos con significado: el tipo indica la naturaleza del cambio, el alcance opcional su zona, y la descripción el resumen. Una herramienta puede leer los tipos para decidir, por ejemplo, que un `fix` sube el parche y un `feat` la versión menor, según la política del proyecto. Un comprobador valida la forma: si el mensaje no sigue el patrón, el commit o el PR se rechaza.

La limitación es que la comprobación es sintáctica. Un mensaje `feat: ajustes` es válido en forma y pobre en contenido; un `fix` que en realidad rompe compatibilidad pasa el comprobador. Por eso la convención se complementa con revisión humana y, dentro de las doce comprobaciones de forma de `SE-204`, con la regla de que los commits sean atómicos.

## Ejemplo

El repositorio de la plataforma de entregas es el caso conductor de la Parte 16. `SE-199` deja allí el archivo de propietarios (`CODEOWNERS`), la convención de mensajes y la lista de revisiones a ignorar. `SE-200` abre el proyecto a contribuciones externas y necesita estas reglas para recibirlas, y `SE-202` protege la rama con ellas. Un commit del proyecto tendría la forma `fix(entregas): corrige el tope de penalización`, que una herramienta clasifica como corrección.

## Errores y confusiones comunes

- **Creer que la convención garantiza buenos mensajes.** Solo garantiza la forma.
- **Elegir el tipo por costumbre.** Un tipo equivocado produce un registro de cambios y una versión equivocados.
- **No comprobarla.** Sin gancho ni integración continua se erosiona commit a commit.
- **Confundirla con `CODEOWNERS`.** Aquella regula la forma del mensaje; esta, quién revisa qué rutas. En `CODEOWNERS`, una regla posterior cubre a una anterior: lo específico va después de lo general.

## Límites y cuándo no aplica

En un proyecto personal pequeño, el costo de imponerla puede superar su beneficio. Con una herramienta de versionado que no lee los tipos, la convención es solo una costumbre de estilo. Los experimentos de `SE-199` usan repositorios temporales y un modelo de coincidencia simplificado respecto al de una plataforma real, con rutas, equipos y mensajes del autor.
