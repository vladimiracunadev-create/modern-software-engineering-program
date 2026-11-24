# Deriva de covariables

## Definición

La **deriva de covariables** (*covariate shift*) es el cambio de la distribución de las entradas de un modelo sin que cambie su relación con la etiqueta. `SE-601` la define así y `SE-608` la reduce a «cambio de la distribución de las entradas». Es la hermana de la deriva de concepto, donde lo que cambia es la relación entradas-etiqueta.

## Por qué importa

Es la deriva que se *puede* ver sin etiquetas, y por eso suele ser la única vigilada. Pero verla no basta: cambia la decisión de qué hacer cuando una alerta salta. Una distribución distinta puede dañar al modelo o no; si la reacción automática es reentrenar, se gasta y se arriesga en vano. `SE-608` concluye que una alerta de PSI debe abrir un diagnóstico, no un reentrenamiento automático.

## Cómo funciona

Se compara la distribución actual de cada característica contra una de referencia (la de entrenamiento o una ventana sana). `SE-608` presenta dos señales:

- **PSI** (índice de estabilidad de población), calculado por característica: suma, por intervalo, la diferencia de proporciones ponderada por el logaritmo de su cociente. Cuanto mayor, más se aparta la distribución.
- **Kolmogorov-Smirnov**, que mide la mayor distancia entre las funciones de distribución acumuladas de ambas muestras.

Ambas **localizan** qué característica cambió, y ninguna dice **si importa**. Eso lo determina el peso de la característica en el modelo y la métrica con etiquetas (por ejemplo AUC). La causa es que son medidas de la entrada, ciegas a la relación con el resultado: un cambio en una región donde el modelo es insensible o ya extrapola bien no degrada nada.

## Ejemplo

En `SE-608`, con una deriva de +1,0 en la carga y una ventana de 5 000 registros, el PSI por característica fue 0,259 para la carga y entre 0,000 y 0,004 para las otras cinco: el índice señala la característica que se movió. Kolmogorov-Smirnov dio 0,217 para la carga. En una deriva de covariables con +2,5 de carga (`SE-601`), el AUC no se movió. El mismo mecanismo, entonces, produce una alarma legítima que no se tradujo en daño. Los datos son sintéticos, inyectados a propósito.

## Errores y confusiones comunes

- **«PSI alto = modelo roto».** Mide cambio de distribución, no pérdida de calidad.
- **Reentrenar automáticamente ante cada alerta.** Puede degradar o gastar sin necesidad; hay que diagnosticar primero.
- **Confundirla con la deriva de concepto.** Esa no mueve las entradas y, por eso, el PSI no la ve.
- **Vigilar solo el promedio.** Una distribución puede cambiar de forma conservando la media; por eso se comparan distribuciones completas.

## Límites y cuándo no aplica

Los umbrales numéricos (qué PSI se considera «grande») son convenciones de la práctica y no una ley; `SE-608` no los presenta como universales y trabaja con series sintéticas. Las pruebas por característica no capturan cambios en la *relación entre* características (una combinación nueva con marginales iguales). Y con datos de muy pocas observaciones, ambas señales son ruidosas: la ventana de 5 000 de la clase importa para la estabilidad de las cifras.
