# Runbook

## Definición

Un **runbook** es un procedimiento paso a paso para una situación operacional conocida, ejecutable sin conocer el sistema (SE-211). SE-499 lo precisa como el documento operativo que acompaña a una alerta y describe diagnóstico, mitigación, verificación, reversión y escalamiento. Se distingue del *playbook*, que da preguntas y criterios para situaciones no previstas.

## Por qué importa

Reduce el tiempo de decisión. Quien está de guardia a las tres de la mañana no debe razonar desde cero ni conocer el sistema a fondo: sigue pasos comprobados. Cambia el diseño de una alerta: toda alerta que despierta a alguien debe tener un runbook enlazado.

## Cómo funciona

El runbook es una receta operativa. Cada **paso** es una acción única con un **comando** y un **resultado esperado** («ejecuta `kubectl get pods`; deben aparecer 3 pods en estado Running»). La estructura de SE-499 tiene cinco partes: **diagnóstico** (cómo confirmar qué pasa), **mitigación** (cómo limitar el daño), **verificación** (cómo saber que funcionó), **reversión** (cómo deshacer si empeora) y **escalamiento** (a quién avisar y cuándo).

SE-611 lo aplica a la operación de modelos de ML. El runbook **pregunta primero qué clase de falla es**: dos clases son fallas de datos (de ingeniería, como un cambio de unidad en la entrada) y otras dos son cambios del mundo (deriva real). El diagnóstico y la mitigación correctos son distintos para cada una, y esa es la razón por la que el runbook pregunta primero la clase. En el ensayo de la clase, la persona de guardia, sin aviso previo, recibe a los dos minutos el aviso de la validación de entrada, abre el runbook, sigue la rama «falla de calidad de entrada», confirma que la tasa de lectura llega en porcentaje y a los veinte minutos despliega una corrección de la conversión.

Dos fallos con corrección conocida: el runbook que dice «revisa los servicios» tiene pasos sin comando ni salida esperada (un paso por acción, con comando y resultado esperado); y el runbook que falla al ejecutarse se desactualizó (se ensaya y se versiona junto al sistema). Un incidente nuevo deja a la guardia sin guía cuando solo hay runbooks y no playbook: se complementa con preguntas y criterios de escalada.

## Ejemplo

Runbook «Cola de entregas creciendo». 1) Diagnóstico: `consultar-cola` debe devolver menos de 500 elementos; si devuelve más, continuar. 2) Mitigación: escalar consumidores a 6 con `escalar --consumidores 6`; resultado esperado: la cola baja en 10 minutos. 3) Verificación: la latencia p95 vuelve por debajo de 2 s. 4) Reversión: volver a 3 consumidores si hay errores de base de datos. 5) Escalamiento: si no baja en 30 minutos, avisar al equipo de datos. (Runbook ilustrativo en la estructura de SE-499.)

## Errores y confusiones comunes

- **«Revisa los servicios»**: pasos vagos sin comando ni resultado.
- **Runbook desactualizado** que falla al ejecutarse.
- **Solo runbooks, sin playbook** para lo imprevisto.
- **No ensayarlo.**

## Límites y cuándo no aplica

Un runbook solo cubre situaciones conocidas; ante un incidente nuevo no basta. Para incidentes raros, el costo de mantenerlo puede superar su uso. Los runbooks excesivamente detallados se vuelven frágiles; los mejores se automatizan cuando el paso es mecánico.
