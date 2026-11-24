# Revisión por muestreo

## Definición

La **revisión por muestreo** es la comprobación de un subconjunto de las afirmaciones de un documento, elegido al azar o por criterio, en lugar de revisarlas todas. Es la definición de trabajo de `SE-540`, donde se analiza cómo se revisa un *dossier* de evidencias (portafolio, informe técnico) con tiempo limitado.

## Por qué importa

Quien revisa no lee todo. Eso cambia cómo debe comportarse quien escribe: no puede apostar a que «nadie lo mirará», ni a que «seguro lo encontrarán». Cambia también cómo se diseña la revisión: el tamaño de la muestra determina qué defectos se pueden detectar con una probabilidad dada, y esa probabilidad se puede calcular.

## Cómo funciona

Si un dossier tiene `n` afirmaciones, `m` de ellas sin respaldo, y la revisora inspecciona `k` elegidas al azar, la probabilidad de ver al menos una sin respaldo es

```text
1 − C(n−m, k) / C(n, k)
```

una distribución hipergeométrica que se calcula con `math.comb`. En `SE-540`: con `n = 30` y `m = 3`, inspeccionar 5 da el 43,3 % y inspeccionar 12 el 79,9 %.

Hay dos consecuencias de diseño. **Primera:** pocas afirmaciones sin respaldo se esconden muy bien en una muestra; el autor no debe contar con que nadie las verá ni con que seguro las encontrarán. El **verificador** automático es la forma de no depender del azar. **Segunda:** la velocidad de comprobación cambia la muestra: si comprobar una afirmación cuesta segundos y no minutos, la revisora puede inspeccionar más. De ahí el valor de una tabla afirmación-evidencia con ruta y huella.

## Ejemplo

Un dossier de 30 afirmaciones, de las cuales 3 no tienen respaldo. Una revisora que mira 5 al azar solo encuentra algún hueco en el 43,3 % de los casos; la mayoría de las veces el dossier pasa con defectos. Con un verificador que comprueba las 30 contra el archivo `claims.csv` (ruta y huella de cada evidencia), los 3 huecos aparecen siempre. `SE-540` usa seis dossiers sintéticos construidos por el autor en un directorio temporal para probar el verificador.

## Errores y confusiones comunes

- **La revisora no encuentra la evidencia.** Falta una tabla afirmación-evidencia; corrección de `SE-540`: construir `claims.csv` con ruta y huella.
- **La evidencia no coincide con la huella.** Se modificó después de calcularla; hay que recalcular y registrar el cambio, o restaurar el original.
- **Creer que una muestra pequeña sin hallazgos prueba que no hay defectos.** Con pocos defectos, la muestra pequeña los pasa por alto la mayor parte del tiempo.
- **Muestrear siempre lo mismo.** Si el criterio es predecible, el defecto se esconde fuera de él.

## Límites y cuándo no aplica

La fórmula supone una elección uniforme y sin reposición, y un número `m` de defectos fijo; `SE-540` declara que la elección uniforme de la muestra, los tiempos de revisión y los dossiers de prueba son construcciones del autor y que no se revisó ningún dossier ni persona reales. Una muestra elegida «por criterio» (las afirmaciones más llamativas) no sigue esa fórmula y detecta mejor los defectos visibles y peor los discretos. Donde un solo defecto es inaceptable (seguridad crítica), el muestreo no basta: se revisa todo o se automatiza la comprobación total.
