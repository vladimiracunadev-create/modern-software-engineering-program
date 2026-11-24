# Subida reanudable

## Definición

Una **subida reanudable** (*resumable upload*) es un protocolo que permite continuar una subida interrumpida desde el último desplazamiento confirmado. Es el sentido de `SE-248` (archivos, streaming y cargas extensas). No es una subida «más rápida»: es una subida que sobrevive a cortes sin repetir lo ya recibido.

## Por qué importa

Con caídas frecuentes (redes móviles, archivos grandes), reiniciar multiplica los datos enviados; reanudar los repite solo hasta el último trozo confirmado. Para quien sube un archivo de cientos de megabytes por una red inestable, es la diferencia entre completar o abandonar.

## Cómo funciona

`SE-248`: si la conexión cae al 80 %, reiniciar descarta 80 MiB ya enviados. En una subida reanudable:

1. El cliente **divide el archivo en trozos.**
2. El servidor **recuerda cuántos bytes recibió** (el desplazamiento confirmado).
3. Tras un corte, el cliente **pregunta el desplazamiento** y continúa desde ahí.

Lo que se repite es, como máximo, el trozo en curso. El tamaño del trozo es un intercambio: un trozo grande repite más al fallar; uno pequeño exige más confirmaciones y más sobrecarga. La clase cita como ejemplo publicado de este diseño el protocolo **tus**, un protocolo abierto para subidas reanudables sobre HTTP.

Dos requisitos de diseño que se derivan: el servidor debe **persistir** el desplazamiento (si lo pierde, no hay reanudación) y debe **verificar la integridad** al final (una suma o huella del archivo completo), porque un trozo mal ensamblado no se vería en el desplazamiento.

## Ejemplo

Ilustración numérica propia con la cifra de la clase: un archivo de 100 MiB, con corte al 80 %. Sin reanudación, el reintento envía otros 100 MiB y el total llega a 180 MiB. Con trozos de 5 MiB, el cliente consulta el desplazamiento (80 MiB) y envía los 20 MiB restantes; en el peor caso repite 5 MiB.

## Errores y confusiones comunes

- **El servidor se queda sin memoria con pocas subidas:** lee el cuerpo completo. Corrección: procesar por trozos y limitar subidas simultáneas (`SE-248`).
- **Una caída obliga a empezar de cero:** falta el protocolo de reanudación.
- **No verificar la integridad del archivo ensamblado.**
- **Dejar sesiones de subida abiertas indefinidamente,** que consumen almacenamiento.

## Límites y cuándo no aplica

Para archivos pequeños la sobrecarga de confirmaciones no compensa. Requiere estado en el servidor (sesiones de subida) y una política de caducidad de las incompletas. No resuelve la autorización ni la validación del contenido subido.
