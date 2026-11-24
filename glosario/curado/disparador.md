# Disparador

## Definición

Un **disparador** es una condición medible sobre una señal, con umbral, ventana y responsable, que obliga a revisar el plan (SE-192). SE-352 usa la palabra en otro sentido, de bases de datos: código que el motor ejecuta antes o después de un cambio y que puede rechazarlo (*trigger*). Esta entrada desarrolla el primero y señala el segundo.

## Por qué importa

Convierte una señal en una acción con responsable. Un plan sin disparadores se revisa por costumbre o por pánico; con ellos, se revisa cuando una regla acordada de antemano lo exige. Cambia la gestión del plan: se pasa de reaccionar a cada oscilación a replanificar solo cuando hay una razón escrita.

## Cómo funciona

SE-192 da un ejemplo: «el percentil 85 del pronóstico supera la fecha comprometida dos semanas seguidas». Un disparador tiene **cuatro partes**:

- la **señal** (qué se mide, aquí el percentil 85 del pronóstico);
- el **umbral** (cuándo es preocupante, aquí superar la fecha comprometida);
- la **ventana** (cuántas observaciones o cuánto tiempo, aquí dos semanas seguidas);
- la **acción con su responsable** (revisar el plan, y quién).

La clase explica por qué cada parte es necesaria: sin ventana, cualquier oscilación lo activa; sin responsable, nadie lo atiende; sin acción, es una alarma sin protocolo. La ventana es lo que controla las **falsas alarmas**: si cada semana hay una probabilidad independiente de 5 % de activarse sin motivo, en 20 semanas la probabilidad de al menos una falsa alarma es 1 − 0,95²⁰ ≈ 64 %, más de la mitad. Una regla sin ventana que alarma casi siempre acaba ignorada.

En el plan de la plataforma de entregas, el objetivo es «lanzar la recuperación de borradores con la regla de penalización verificada en 22 semanas», los supuestos son cuatro con responsable y fecha, el rango comunicado es «entre 18 y 23 semanas con 85 % de confianza», y el disparador es el anterior. En SE-352, el sentido de base de datos comparte la idea de condición que ejecuta una acción, pero la ejecuta el motor automáticamente.

## Ejemplo

Disparador: «si el rendimiento de las últimas cuatro semanas baja por debajo de cierto valor, el responsable del plan convoca una revisión en 48 horas». Señal: rendimiento semanal; umbral: valor fijado; ventana: cuatro semanas; acción: convocar revisión; responsable: quien lleva el plan. Si baja una semana, no hace nada; si baja cuatro seguidas, se revisa. (Estructura ilustrativa derivada de SE-192.)

## Errores y confusiones comunes

- **Nadie reacciona a la alarma de replanificación**: la regla no tiene ventana y alarma casi siempre; corrección: exigir avisos seguidos, ampliar la ventana y medir falsas alarmas.
- **El plan se rehace cada semana**: se replanifica por cada oscilación.
- **Disparador sin responsable.**
- **Confundirlo con un trigger de base de datos.**

## Límites y cuándo no aplica

Un disparador solo detecta lo que se midió; una causa no medida no lo activa. Las ventanas largas retrasan la reacción: equilibrar falsas alarmas y detección tardía es una decisión de riesgo. Y los umbrales deben revisarse con la experiencia del proyecto.
