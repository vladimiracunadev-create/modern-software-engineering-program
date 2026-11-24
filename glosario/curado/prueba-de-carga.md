# Prueba de carga

## Definición

Una **prueba de carga** aplica la carga esperada (o la prevista para un evento) durante el tiempo suficiente para que el sistema alcance su régimen estable, y comprueba que el escenario de calidad se cumple (`SE-435`).

## Por qué importa

Responde «¿cumple en el uso esperado?», pero no responde «¿qué pasa en un pico?» ni «¿qué pasa tras horas de uso?». Confundir los tipos de prueba lleva a declarar «aguanta» y caer en el cierre.

## Cómo funciona

En el simulador de `SE-435`, cuatro servidores con 50 ms de servicio medio tienen una capacidad nominal de 80 solicitudes por segundo. A 60 solicitudes por segundo la utilización es del 75 %, y con llegadas aleatorias eso ya produce colas pasajeras: mediana de 57 ms, p95 de 202 ms y p99 de 285 ms. Por eso se miden percentiles y no solo la media. Otras pruebas responden otras preguntas: la de **pico** el comportamiento ante una ráfaga; la de **resistencia** (*soak*) el desgaste en el tiempo.

## Ejemplo

En la misma clase, a 60 solicitudes por segundo se pierden unas tres conexiones en cinco minutos (6 % del pool); una prueba de carga de esa duración no lo vería, y el pool se agota a los 67 minutos tras 241 135 solicitudes. Solo una prueba de resistencia larga lo detecta.

## Errores y confusiones comunes

**La prueba «aguanta» y el sistema cae en el cierre.** Solo se hizo prueba de carga; añadir prueba de pico y de resistencia.

## Límites y cuándo no aplica

Las cifras son de un simulador. Una prueba de carga con datos o patrones de uso poco realistas da confianza falsa; el generador de carga también puede ser el cuello de botella.
