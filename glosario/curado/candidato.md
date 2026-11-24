# Candidato

## Definición

En la evaluación de sistemas con modelos, un **candidato** es una configuración del sistema que se somete a la puerta (`SE-600`).

## Por qué importa

Elegir entre configuraciones (un workflow, un agente, un híbrido) exige medir cada una con los mismos criterios y decidir con una puerta fijada antes de medir.

## Cómo funciona

Cada candidato se mide en varias columnas con su método: la **calidad** con el conjunto de casos de `SE-597` (pareada, con repeticiones y puerta estadística); los **tokens** y la **latencia p95** con los modelos de costo y de cadena de llamadas de `SE-589` y `SE-598`; y una prueba de seguridad. En el experimento, los candidatos van de 85,0 % de calidad (workflow solo) a 99,0 % (híbrido), con 774 tokens el workflow, 1 862 el agente y 1 421 el híbrido.

## Ejemplo

`SE-600`: el equipo de *Avisos* entrega un dossier a una comisión; la primera página es la puerta con umbrales, firmada antes de medir; luego cuatro candidatos medidos con 400 casos y tres repeticiones; el híbrido gobernado pasa las cinco columnas con calidad 98,1 % (intervalo 96,9 % a 99,0 %).

## Errores y confusiones comunes

Fijar umbrales después de ver los resultados; comparar candidatos en conjuntos distintos.

## Límites y cuándo no aplica

Los números son de un experimento sintético; el dossier debe declarar lo que no se midió y la condición de revisión.
