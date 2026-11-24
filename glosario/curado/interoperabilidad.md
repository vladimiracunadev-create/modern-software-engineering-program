# Interoperabilidad

## Definición

La **interoperabilidad** es la capacidad de que dos sistemas intercambien datos con el mismo significado (`SE-441`).

## Por qué importa

Un formato estándar fija la sintaxis pero deja libres cosas que importan. Compartir un formato no basta para compartir significado.

## Cómo funciona

`SE-441` da ejemplos: JSON dice que un número es una secuencia de dígitos, y cada implementación decide su rango y precisión; un identificador de 64 bits que un lector convierte a decimal de doble precisión pierde los dígitos bajos si supera 2⁵³. El texto tiene el mismo problema con las formas de normalización (la «é» puede ser un solo carácter o una «e» más un acento combinante), la codificación por defecto y el fin de línea. La defensa es hacer explícito lo que el estándar deja implícito: codificación, normalización, rango numérico.

## Ejemplo

Un identificador de 64 bits enviado como número JSON y leído por un cliente JavaScript pierde precisión; se envía como cadena.

## Errores y confusiones comunes

- **Acentos rotos en un sistema y no en otro.** Codificación por defecto distinta; especificar `encoding="utf-8"` siempre.
- **Un archivo difiere de bytes y tiene el mismo tamaño.** Fin de línea o codificación distintos; fijar `newline` y `encoding` y comparar hashes.

## Límites y cuándo no aplica

No se logra por declaración: se verifica con pruebas de contrato entre las implementaciones reales. Y no equivale a reproducibilidad entre sistemas, aunque comparten las mismas causas.
