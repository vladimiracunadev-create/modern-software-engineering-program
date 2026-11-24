# Archivo de bloqueo

## Definición

Un **archivo de bloqueo** (*lockfile*) es el documento que fija la versión exacta y la huella de cada pieza de la clausura de dependencias (`SE-471`); en `SE-520` es el archivo que fija las versiones exactas de todas las dependencias para repetir una instalación.

## Por qué importa

El manifiesto suele declarar **rangos** («cualquier versión compatible con 2.3»). Un resolvedor elige en el momento de instalar las versiones concretas que satisfacen todos los rangos; mientras los paquetes publican versiones nuevas, el resultado cambia. Ese no es un defecto del resolvedor, es el significado de un rango. Para un servicio que se despliega, es una entrada no declarada del build.

## Cómo funciona

El bloqueo registra la **clausura** completa (directas y transitivas) con versión exacta y huella. Instalar desde él exige las huellas y rechaza cualquier archivo distinto. Las actualizaciones llegan como cambios revisables del bloqueo, que muestran la diferencia de versiones y de huellas. Además es la base para el inventario (SBOM) y para saber si un aviso de vulnerabilidad afecta.

## Ejemplo

`SE-471`: el equipo de la API de entregas mantiene un manifiesto con seis dependencias directas y rangos amplios, y un bloqueo con 31 piezas, versiones exactas y huellas. El CI instala exigiendo las huellas; las actualizaciones llegan como solicitudes semanales automáticas que modifican el bloqueo y pasan las pruebas antes de fusionarse. La clase observa que sin archivo de bloqueo el conjunto cambia casi todos los días con novedad, y con él casi nunca.

## Errores y confusiones comunes

**El CI falla sin cambios en el repositorio.** Resolución sin bloqueo: el árbol cambió al publicarse una versión; archivo de bloqueo con versiones y huellas.

## Límites y cuándo no aplica

En una biblioteca que otros consumen, el bloqueo no se distribuye con ella: manda el rango del manifiesto. El bloqueo fija lo publicado, pero no lo audita.
