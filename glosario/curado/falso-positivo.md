# Falso positivo

## Definición

Un **falso positivo** es un aviso que una herramienta emite sobre código (o sistema) que no tiene el defecto que dice detectar (`SE-452`). En `SE-420` el sentido es el de pruebas: una prueba que falla sin que haya un defecto. En ambos casos, la señal dice «hay un problema» cuando no lo hay.

## Por qué importa

Una herramienta con muchos falsos positivos deja de ser creíble: la gente ignora sus avisos o la desactiva, y con ellos se pierde el aviso verdadero. `SE-420` lo dice así: una batería que falla con defectos y también con el producto limpio no sirve. La decisión que cambia es cómo se evalúa una herramienta o una prueba: no solo si detecta defectos, sino si guarda silencio cuando no los hay.

## Cómo funciona

Una batería de pruebas se valida con dos ejecuciones opuestas. Con **defectos sembrados**, debe fallar (si no, no detecta). Con el producto **limpio**, debe dar cero fallos de forma estable, repetida y en entornos distintos. Si falla sin defecto, es un falso positivo.

`SE-420` da el procedimiento: en el taller se repitió la ejecución completa tres veces con salida idéntica; si una prueba depende del orden, del reloj o de la velocidad de la máquina, se convierte en una prueba inestable y se corrige antes de confiar en ella. La clase enumera las causas habituales: el reloj, el orden de ejecución, datos compartidos entre pruebas y la velocidad de la máquina. El tratamiento es investigar antes de continuar, aislar, corregir y repetir la ejecución limpia varias veces.

En el análisis estático (`SE-452`, sistemas críticos), el falso positivo es el aviso que la herramienta emite sobre código correcto. Cada uno cuesta tiempo de revisión y, si se acumulan, entrena a quien revisa a descartar avisos sin leerlos. El mecanismo de fondo es el compromiso entre sensibilidad y especificidad: una herramienta más sensible encuentra más defectos y emite más avisos falsos.

## Ejemplo

Una prueba de plazos falla de vez en cuando porque usa el reloj real: cerca de medianoche el resultado cambia. Con el producto limpio, la batería da rojo algunas veces; es un falso positivo. Se aísla fijando un reloj controlado y se repite la ejecución limpia varias veces hasta que sale estable. Es el tratamiento de `SE-420`.

## Errores y confusiones comunes

- **Desactivar la prueba o ignorar el aviso sin investigar**: se pierde la señal verdadera.
- **Confundirlo con un defecto menor**: un falso positivo no es un defecto.
- **Medir solo detección**: sin ejecutar con el producto limpio no se ve.
- **Culpar a la herramienta sin comprobar**: algunos avisos «falsos» son defectos reales poco evidentes.

## Límites y cuándo no aplica

Un número cero de falsos positivos no es alcanzable en general: reducirlos suele costar detecciones. Lo que se exige es que sean pocos, conocidos y tratables. La definición cambia con el contexto: en pruebas es un fallo sin defecto, en análisis estático un aviso sobre código correcto, y en un sistema crítico el costo de un falso negativo puede justificar tolerar más falsos positivos.
