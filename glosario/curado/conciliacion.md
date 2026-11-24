# Conciliación

## Definición

La **conciliación** es la comparación de dos fuentes del mismo hecho y la explicación de sus diferencias (`SE-417`). En `SE-371` se usa en un sentido más acotado: comparar totales (número de filas, importes) entre dos capas o fuentes de datos, para saber si lo que llegó coincide con lo que salió.

## Por qué importa

Dos sistemas que registran el mismo hecho (un cobro en el libro propio y en el informe del procesador de pagos) terminan por discrepar: por fallos, duplicados, retrasos o errores de configuración. La conciliación convierte esas discrepancias en algo medible y asignado, en vez de descubrirlas en el cierre contable. La decisión que cambia es tratar la consistencia entre fuentes como una verificación periódica con responsable, no como una suposición.

## Cómo funciona

`SE-417` describe una conciliación diaria en tres pasos:

1. **Descargar** el informe de liquidación del procesador.
2. **Comparar** con el libro por referencia y **clasificar** las diferencias: faltantes en cada lado, montos distintos, duplicados.
3. **Informar** con la antigüedad de cada diferencia.

Dos reglas hacen que sea operable. Las diferencias de menos de un centavo por redondeo se aceptan con un límite de diez al día; todas las demás generan una tarea con responsable. Y lo que no se puede resolver sin el procesador (una disputa pendiente) queda registrado con fecha y estado.

Las decisiones de modelado que la hacen posible vienen de la misma clase: los importes se guardan en la unidad mínima de la moneda (centavos) como enteros, porque la coma flotante binaria no representa exactamente 0,10 y acumula diferencias que, a escala, aparecen en la conciliación; y los asientos son inmutables, de modo que un error se corrige con un asiento nuevo que lo revierte, conservando el historial para auditar. `SE-371` aplica la misma idea de contrastar totales entre capas de un flujo de datos.

## Ejemplo

En el caso de `SE-417`, la primera semana la conciliación encuentra tres cobros de un entorno de ensayo configurado contra producción. El equipo corrige la configuración y añade una comprobación al despliegue. Al mes, el cierre pasa de dos días de investigación a unas horas, y la brecha media sin explicar baja a cero. Son resultados del escenario construido en la clase, no una medición general.

## Errores y confusiones comunes

- **Guardar importes como decimales binarios**: acumulan diferencias; se usan enteros en la unidad mínima.
- **Corregir editando el asiento**: se pierde la auditoría; se corrige con un asiento nuevo.
- **Aceptar cualquier diferencia pequeña sin límite**: debe haber un tope diario.
- **Confundir conciliar con igualar**: lo esencial es explicar, no forzar que coincidan.

## Límites y cuándo no aplica

Solo detecta diferencias entre las dos fuentes que se comparan: si ambas se equivocan igual, no lo ve. Exige una clave común (la referencia) y fuentes disponibles; donde falta una clave, un libro o una conciliación, no hay respuesta posible, como señala `SE-417`. Y lo que depende de un tercero (una disputa) no se resuelve comparando, solo se registra con estado.
