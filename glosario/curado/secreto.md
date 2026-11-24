# Secreto

## Definición

Un **secreto** es un dato cuya divulgación permite o facilita una acción no autorizada (`SE-031`). `SE-219` lo concreta como un valor cuya divulgación da acceso o daña a alguien: contraseñas, tokens, claves; `SE-462`, como un valor cuyo conocimiento concede una capacidad. No es lo mismo que un dato personal ni que un dato privado: lo define lo que permite hacer a quien lo posee.

## Por qué importa

Un secreto se usa para demostrar identidad y se vuelve una vulnerabilidad cuando se copia al lugar equivocado: el repositorio, un registro, una imagen, un mensaje de chat (`SE-401`). La mayoría de los incidentes con secretos no son criptográficos: son de manejo. Cambia dónde se guardan, quién los ve y cuánto tiempo valen.

## Cómo funciona

`SE-401`, con la guía de OWASP, propone:

- **centralizarlos** en un almacén con control de acceso y auditoría;
- **rotarlos** (cambiarlos periódicamente y tras sospecha);
- **no incluirlos en el código**;
- **preferir credenciales de vida corta** emitidas a cada servicio.

La razón es la contención: un secreto en un solo lugar y con caducidad corta limita cuánto tiempo y a quién sirve si se filtra. `SE-462` añade una regla útil: un secreto sin dueño y sin fecha de caducidad es un incidente esperando. En configuración (`SE-219`), los secretos no deben pasar por argumentos de línea de comandos (visibles en la lista de procesos) ni por registros.

Una causa frecuente de persistencia: el historial de Git conserva lo que se borró del último *commit*, de modo que quitar el secreto del archivo no lo elimina.

## Ejemplo

```bash
# mal: el secreto queda en el historial del shell y en la lista de procesos
herramienta --token abc123
# mejor: leer de un almacén o de una variable de entorno inyectada y de vida corta
herramienta --token-desde-env APP_TOKEN
```

Una vez filtrado, el procedimiento de `SE-031` y `SE-462`: revocar y rotar primero, evaluar la exposición después y recién entonces limpiar.

## Errores y confusiones comunes

- **Una clave aparece en el repositorio.** Causa: secreto copiado a un script; corrección: mover al almacén, rotar la clave y activar el análisis en cada confirmación (`SE-401`).
- **Se borró del último *commit* y se da por resuelto.** Causa: se ignoraron copias e historial; corrección: revocar o rotar primero y evaluar exposición (`SE-031`).
- **Secreto vivo tras borrarlo del archivo.** Causa: el historial lo conserva; corrección: rotarlo y buscar en el historial (`SE-462`).

## Límites y cuándo no aplica

Un almacén de secretos reduce el riesgo, no lo elimina: quien tiene acceso al almacén es otro punto de confianza. Las credenciales de vida corta dependen de que la plataforma las soporte. Y un valor público (un identificador, una clave pública) no es un secreto: tratarlo como tal añade fricción sin protección.
