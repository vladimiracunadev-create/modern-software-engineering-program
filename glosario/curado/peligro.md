# Peligro

## Definición

Un **peligro** (*hazard*) es una condición o estado del sistema que, con ciertas circunstancias, puede llevar a daño (`SE-445`). Ejemplo de la clase: «calentador conectado con la puerta abierta».

## Por qué importa

Separar peligro, riesgo y control evita documentos donde el control aparece como si fuera el peligro («falta un limitador») o donde el riesgo se declara aceptable sin decir quién lo acepta ni con qué supuestos.

## Cómo funciona

`SE-445` fija tres piezas: el **peligro** es una condición; el **riesgo** añade cuánto daño y con qué frecuencia («una quemadura grave, una vez cada cien mil usos, si el operador no reacciona»); el **control** es lo que cambia uno de esos dos factores y se puede verificar («el contacto de la puerta corta la potencia por hardware»). La disciplina mínima es escribir cada peligro con su contexto operativo (fase de uso, usuario, entorno) y cada control con la forma de verificarlo.

## Ejemplo

`SE-445`: el equipo del *Horno de curado* analiza peligros antes de un piloto de tres meses. El árbol de fallos muestra una probabilidad de sobretemperatura aceptable. Al repasarlo con el técnico aparece algo no escrito: el mismo técnico calibra, el mismo día y con el mismo patrón, el sensor del lazo y el del limitador. Se añade el evento «calibración compartida» y la probabilidad sube de golpe. La decisión es cambiar el proceso (patrones distintos, registrar quién y cuándo).

## Errores y confusiones comunes

Describir el control como peligro; analizar fallos como independientes cuando comparten causa.

## Límites y cuándo no aplica

El caso es un ejercicio de la clase, no una medición de un equipo real. Un análisis de peligros cubre los que se imaginaron; la búsqueda de causas comunes es lo que reduce el riesgo de no verlos.
