# Política como código

## Definición

La **política como código** es una regla de configuración escrita de forma que una herramienta pueda comprobarla de manera automática (`SE-406`). `SE-483` la define con más precisión: una regla escrita en un lenguaje ejecutable que se evalúa sobre datos de entrada (la configuración de infraestructura, un archivo de flujo de trabajo, una lista de dependencias) y produce una decisión auditable.

## Por qué importa

Las normas escritas en un documento dependen de que alguien las recuerde y las revise a mano. Una política como código se aplica siempre, igual y sin depender de la memoria de nadie. La decisión que cambia es dónde vive una regla de seguridad o de operación: en una puerta automática por la que pasa todo, no en una guía que se lee una vez.

## Cómo funciona

`SE-406` describe un verificador de políticas que lee un descriptor de servicio (qué imagen, con qué usuario, qué límites) y comprueba reglas escritas como código: el servicio debe tener dueño, límites, una imagen con versión fija y un usuario sin privilegios. Dos propiedades hacen valiosa la puerta:

- **Independencia del origen**: un servicio de la plantilla (camino dorado) y uno hecho a mano pasan por la misma puerta. La plataforma no depende de que todos usen el camino fácil.
- **Decisión auditable**: la regla es texto versionado y la decisión se puede reproducir con los mismos datos de entrada.

Herramientas como Open Policy Agent ofrecen un lenguaje para escribir esas reglas. `SE-483` las inserta en la canalización de CI/CD como compuerta: una violación bloquea el cambio antes de llegar a producción.

El límite está en la propia clase: estas políticas comprueban **forma, no sentido**. Un límite de CPU de mil núcleos cumple la regla «tiene límite» y es absurdo. Por eso se acompañan de rangos razonables y de revisión.

## Ejemplo

Una regla exige que todo descriptor declare un usuario distinto de root. El verificador revisa los descriptores en cada cambio. Un servicio nuevo sin usuario declarado falla la compuerta antes de desplegarse y el equipo recibe el motivo. El resultado es igual para el servicio generado por plantilla y para el escrito a mano. Mecanismo descrito en `SE-406`.

## Errores y confusiones comunes

- **Los equipos no usan el camino**: es más difícil que lo manual o no cubre su caso; se corrige midiendo pasos y excepciones y mejorándolo. La política complementa el camino, no lo reemplaza.
- **El equipo de plataforma está saturado de solicitudes**: baja adopción y servicios hechos a mano.
- **Escribir reglas que solo miran la forma** y creer que garantizan sentido.
- **Políticas sin excepciones registradas**: obligan a puentear la puerta.

## Límites y cuándo no aplica

Solo comprueba lo que se le pidió y lo que puede evaluar sobre sus datos de entrada: no ve intención, contexto ni comportamiento en ejecución. Una política mal escrita bloquea trabajo legítimo o deja pasar lo inseguro con apariencia de control. Para reglas que dependen de juicio humano (aprobaciones, riesgo de negocio), el código solo puede exigir que la aprobación exista, no evaluarla.
