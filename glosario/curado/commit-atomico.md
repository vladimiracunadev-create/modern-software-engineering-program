# Commit atómico

## Definición

Un **commit atómico** hace una sola cosa, deja el repositorio en un estado comprobable (compila y pasa las pruebas) y puede revertirse sin arrastrar otra cosa (SE-194). No se mide en líneas: un renombre de cuarenta archivos puede ser atómico y una corrección de tres líneas que además cambia un formato no lo es.

## Por qué importa

Un commit que mezcla cambios obliga a leer todo para entender uno. Con commits atómicos, cada paso de la historia cuenta una cosa, se revisa sin ruido, se revierte sin daño colateral y se localiza con una bisección. Cambia cómo se organiza el trabajo antes de publicarlo: se ordena y divide la historia para que sea legible.

## Cómo funciona

SE-194 da tres criterios prácticos de uso: el commit debe poder **revertirse sin arrastrar otra cosa**, **revisarse sin leer lo ajeno** y **localizarse con una bisección**. Para eso se cumplen dos condiciones: una intención única (describible en una frase de resumen) y un estado consistente (compila y pasa las pruebas), de modo que cada punto de la historia sea comprobable.

En la práctica se consigue dividiendo antes de publicar: `git add -p` permite elegir trozos de un archivo para cada commit, de manera que una refactorización, una corrección y un cambio de formato terminen en commits distintos. En la plataforma, cada cambio a `penal.py` va en un commit con una frase de resumen, un cuerpo que explica la regla de negocio afectada y un pie con el issue.

La atomicidad es lo que hace funcionar la bisección: si el commit culpable mezcla varias intenciones, aunque se localice hay que leer cientos de líneas; y si un commit intermedio no compila, la bisección no puede señalar un solo cambio. De ahí la exigencia de que cada commit de una rama compile. La atomicidad también es la base de las comprobaciones de forma de un paquete (SE-204), que acotan archivos y líneas por commit como heurística de que hace una sola cosa.

## Ejemplo

Un cambio mezcla (a) corregir el redondeo de la nota, (b) renombrar una variable y (c) reformatear el archivo. En un solo commit, revertir la corrección arrastra el renombre y el formato. En tres commits atómicos («fix: redondear al alza en el empate», «refactor: renombrar nota_base», «style: formatear penal.py»), cada uno se revisa, se revierte y se bisecta de forma independiente. (Ejemplo ilustrativo construido con el criterio de SE-194.)

## Errores y confusiones comunes

- **La bisección no señala un solo commit**: hay un commit que no compila; corrección: reordenar la rama para que cada paso compile.
- **Hay que leer cientos de líneas tras bisecar**: el culpable mezcla intenciones; corrección: dividir con `git add -p`.
- **Confundir atómico con pequeño**: lo que cuenta es la intención única.
- **Commit «WIP»** que se publica tal cual.

## Límites y cuándo no aplica

Reordenar la historia tiene un costo y solo es seguro sobre ramas propias no publicadas. En un prototipo desechable la atomicidad rinde poco. El criterio último es el uso: si el commit se puede revertir, revisar y localizar sin ayuda, es suficientemente atómico.
