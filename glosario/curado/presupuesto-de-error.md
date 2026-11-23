# Presupuesto de error

## Definición

El **presupuesto de error** es la cantidad de fallo que un SLO permite en su ventana: uno menos el objetivo. `SE-497` lo formula así, `SE-252` como la fracción de solicitudes que pueden fallar sin incumplir el objetivo y `SE-419` como el complemento del objetivo expresado como cantidad de fallo tolerable. Con un SLO de 99,9 % en 30 días, el presupuesto es 0,1 % de las peticiones o 43,2 minutos de caída total.

## Por qué importa

Convierte la fiabilidad en una moneda que se gasta. Según `SE-497`, mientras queda presupuesto, el equipo puede desplegar con ritmo y asumir riesgo; cuando se agota, una política acordada de antemano decide qué cambia. Así la discusión entre «entregar más» y «estabilizar» deja de ser una opinión y pasa a ser una cantidad: `SE-252` lo resume como un número que obliga a elegir entre cambiar y estabilizar.

## Cómo funciona

El presupuesto se **gasta** con incidentes, con despliegues arriesgados y con mantenimientos (`SE-419`). Lo que da sentido al número es la **política de presupuesto**, que las clases describen con un ejemplo de tres tramos (`SE-419`): por debajo del 50 % de consumo, el equipo despliega con normalidad; entre 50 % y 100 %, se exige revisión adicional de los cambios riesgosos; al agotarse, se detienen los lanzamientos de funcionalidad hasta restablecer el margen y se prioriza la fiabilidad. `SE-497` añade que la política necesita un responsable que la aplique y una excepción explícita para lo que el presupuesto no puede frenar, como una corrección de seguridad. Sin política, el presupuesto es un número en un panel.

Para alertar, `SE-252` usa la **tasa de consumo**: cuántas veces más rápido que lo permitido se gasta el presupuesto. La alerta rápida salta si la tasa supera 14,4 en una hora y en cinco minutos; la lenta, si supera 6 en seis horas y en 30 minutos.

## Ejemplo

En `SE-252`, con SLO de 99,5 % en 30 días (presupuesto de 0,5 %), tres incidentes sintéticos comienzan el día 20. Una caída total de 10 minutos consume el 14,6 % del presupuesto y la alerta rápida salta a los 4 minutos. Un 5 % de errores durante 6 horas consume el 18,3 %; la alerta rápida no salta y la lenta lo hace a los 215 minutos. Una degradación lenta del 0,8 % consume el 63,3 % y ninguna de las dos alertas salta, porque su tasa de consumo (unas 1,7 veces) queda por debajo de ambos umbrales: es un incidente que gasta mucho presupuesto sin que nadie sea avisado.

En `SE-419`, un mes tranquilo termina en 12 minutos (28 %), uno con un incidente grande de 40 minutos cierra en 44 (102 %). Las series son inventadas para mostrar la lectura.

## Errores y confusiones comunes

- **Un presupuesto sin política.** Es un número en un panel que no cambia ninguna decisión (`SE-497`).
- **Alertar solo por picos.** Una degradación lenta puede consumir la mayor parte del presupuesto sin cruzar ningún umbral rápido (`SE-252`).

## Límites y cuándo no aplica

Las cifras de las clases suponen un mes de 30 días y que toda caída cuenta; en un sistema real el presupuesto se calcula con SLI por solicitud y se consume también por degradaciones parciales (`SE-419`). El presupuesto no decide solo: necesita una excepción explícita para lo que no puede frenarse (`SE-497`), y las alertas por tasa de consumo de `SE-252` se calibraron con tráfico constante y un error de base del 0,05 %, supuestos que no siempre se cumplen.
