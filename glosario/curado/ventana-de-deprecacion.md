# Ventana de deprecación

## Definición

La **ventana de deprecación** es el periodo entre el aviso de retirada de una versión (o característica) y su eliminación efectiva (SE-312, SE-164). Es el plazo que se da a quienes consumen una interfaz para migrar.

## Por qué importa

Equilibra el costo de mantener dos versiones con el de romper a quien no migró. Una ventana demasiado corta rompe a consumidores que no tuvieron tiempo; una demasiado larga obliga a mantener lo viejo indefinidamente. Cambia la planificación de la evolución de un contrato: retirar es una decisión con plazo, aviso y responsable.

## Cómo funciona

SE-312 dice que retirar una versión antigua exige **un aviso, un plazo y una forma de saber quién sigue usándola**. El plazo equilibra dos costos: **mantener dos versiones** (crece con la ventana) y **romper a quien no migró** (decrece con ella, pero **no llega a cero**, porque algunos consumidores nunca migrarán por sí solos). Hay, por tanto, una ventana razonable más allá de la cual alargar poco aporta.

Para comunicar el plazo, los protocolos de red ofrecen cabeceras de deprecación y retirada (`Deprecation` y `Sunset` en HTTP), que anuncian a los clientes la fecha. En la plataforma de entregas, la política es que los renombrados, los campos requeridos nuevos y las eliminaciones exigen versión mayor, aviso con esas cabeceras y una ventana mínima de 180 días (SE-164).

El mecanismo para saber quién usa lo viejo es **medir el uso**: registrar qué versión llama cada cliente. SE-164 describe el síntoma que ocurre sin ello: la ventana termina y quedan clientes activos porque parte de los consumidores no migra sola. La corrección es **medir quién usa lo viejo, contactar directamente y decidir el corte con un responsable**. En SE-312, el componente `tarifas` cierra la parte con un plan de evolución que incluye una ventana de deprecación estimada, contratos de ocho consumidores y las tres fases de cada cambio (añadir lo nuevo, migrar, retirar lo viejo).

## Ejemplo

Se anuncia que `GET /v1/entregas` se retira el 1 de diciembre. La respuesta incluye `Deprecation: true` y `Sunset: <fecha>`. Un panel muestra cuántas llamadas a `/v1` reciben cada semana y de qué clientes: de 12 clientes iniciales quedan 3 a un mes del corte. El equipo los contacta uno a uno y decide, con el responsable del producto, si aplaza o corta. (Ilustración del mecanismo de SE-164 y SE-312.)

## Errores y confusiones comunes

- **La ventana termina y quedan clientes activos**: no migran solos; corrección: medir, contactar y decidir con un responsable.
- **Avisar sin fecha ni cabeceras.**
- **No medir el uso de lo viejo.**
- **Fijar la ventana por calendario interno** sin considerar los ciclos de los consumidores (aplicaciones móviles instaladas).

## Límites y cuándo no aplica

Para interfaces internas con consumidores conocidos y coordinables, una ventana formal puede sobrar. Cuando la retirada es urgente por seguridad, se acorta o se omite a cambio de un costo de ruptura explícito. Los 180 días de la plataforma son una política de ese caso, no un estándar universal.
