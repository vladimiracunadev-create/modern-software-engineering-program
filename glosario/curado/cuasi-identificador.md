# Cuasi-identificador

## Definición

Un **cuasi-identificador** es un dato que no identifica a una persona por sí solo pero sí en combinación con otros. Es la definición de `SE-488` (entornos preview y datos seguros), con el mismo núcleo en `SE-295` (edad, sexo, código postal), `SE-463` (combinado con otros o con una fuente auxiliar) y `SE-369`. Se contrapone al **identificador directo** (nombre, correo), que señala a la persona por sí solo.

## Por qué importa

Quitar el nombre no anonimiza. Es la idea central de `SE-488`: en un entorno de revisión con datos «enmascarados», los cuasi-identificadores siguen presentes y pueden devolver la identidad. Cambia la decisión de qué se copia a un entorno no productivo y qué se considera dato personal.

## Cómo funciona

`SE-488` lo explica con la investigación de Sweeney: una gran parte de la población estadounidense era única por fecha de nacimiento, código postal y género. El mecanismo es el **ataque de vinculación**:

1. El conjunto «anonimizado» conserva cuasi-identificadores (fecha de nacimiento, código postal, género, curso).
2. Otra fuente accesible contiene nombres y esos mismos atributos.
3. Se cruzan; donde la combinación es única en ambas, la identidad se recupera.

La defensa técnica más sencilla es **generalizar** (el año en lugar de la fecha completa; tres dígitos del código postal) y **suprimir** los grupos pequeños, hasta que cada combinación corresponda a al menos *k* personas, que es el k-anonimato. Para saber si hay riesgo, se cuenta cuántos registros comparten cada combinación de cuasi-identificadores.

## Ejemplo

En el caso de `SE-488`, una persona ajena identifica a un estudiante en un entorno de revisión. Hipótesis rivales: (a) falló el enmascarado de un campo; (b) alguien filtró el nombre; (c) la combinación de datos corrientes es única y permite la vinculación. Al contar registros por combinación, el 97,6 % es único; con una lista externa que tiene los mismos datos, la causa es (c), y la corrección es generalizar y suprimir, no enmascarar el nombre otra vez. El porcentaje es de los datos sintéticos de la clase.

## Errores y confusiones comunes

- **Creer que quitar nombre y correo anonimiza.**
- **Tratar cada columna por separado:** el riesgo está en la combinación, no en un campo.
- **Confundirlo con seudonimización:** esta reemplaza el identificador por otro valor, pero los cuasi-identificadores siguen vinculando.
- **Suponer que k-anonimato basta siempre:** `SE-463` lo trata como una medida entre otras.

## Límites y cuándo no aplica

El riesgo depende de la fuente auxiliar que tenga el atacante, que no se conoce de antemano. Generalizar pierde precisión y puede inutilizar datos para análisis fino. El 97,6 % no es una cifra extrapolable a otra población. En conjuntos sin atributos combinables (agregados ya generalizados) el concepto pierde peso.
