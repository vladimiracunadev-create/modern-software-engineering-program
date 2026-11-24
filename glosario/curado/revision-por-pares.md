# Revisión por pares

## Definición

La **revisión por pares** es una lectura estructurada por personas con criterios distintos, que busca los defectos que una máquina no ve (SE-156). En requisitos, complementa al validador de estructura: este comprueba la forma; la revisión busca contradicciones semánticas, umbrales absurdos y criterios que no prueban el requisito.

## Por qué importa

Encuentra lo que el validador no ve, con límites que hay que conocer. Un validador puede dar verde sobre una especificación con errores graves; una lectura atenta los encuentra. Cambia cómo se organiza una revisión: con lectoras que usan criterios distintos, no la misma lista repetida, y con una estimación de cuántos defectos quedan.

## Cómo funciona

Una revisión estructurada tiene lectoras que miran con **criterios distintos** (una el contenido, otra la consistencia, por ejemplo), de modo que no dependen de los mismos puntos ciegos. Es el mismo argumento de las comprobaciones correlacionadas: dos revisiones iguales encuentran lo mismo.

Para saber **cuánto falta**, SE-156 toma prestada de la ecología la técnica de **captura–recaptura**: si dos revisoras encuentran n₁ y n₂ defectos y coinciden en m, el total estimado es n₁·n₂/m. Por ejemplo, si una encuentra 10, otra 8 y coinciden en 5, el total estimado es 10 × 8 / 5 = 16, de modo que quedan 16 − (10 + 8 − 5) = 3 por encontrar. La estimación **funciona si** las revisoras trabajan de forma independiente y los defectos son igualmente fáciles de encontrar; falla cuando hay defectos difíciles que ninguna ve (la correlación sesga el total hacia abajo).

La revisión es parte de la **decisión de entrega** de una especificación: el expediente registra las dos revisiones, los criterios de cada una y el defecto estimado restante con su incertidumbre. Y se combina con el validador y con las mutaciones, que miden qué detecta el validador. Un riesgo: confiar en la revisión porque «alguien la leyó»; sin criterios explícitos, cada lectora mira lo que le llama la atención.

## Ejemplo

Dos revisoras leen la misma especificación con criterios distintos. Ana encuentra 12 defectos y Luis 9; coinciden en 6. El total estimado es 12 × 9 / 6 = 18. Hay 12 + 9 − 6 = 15 encontrados y quedan unos 3 sin encontrar. Si el equipo exigía como criterio de salida menos de 2, hace una tercera revisión. (Aritmética de captura–recaptura de SE-156, con cifras ilustrativas.)

## Errores y confusiones comunes

- **El validador pasa y la especificación tiene errores graves**: solo comprueba estructura.
- **La lectora tarda un día en entender qué falta**: el expediente no responde sin su autor.
- **Revisoras con los mismos criterios.**
- **Tomar la estimación de captura–recaptura como exacta.**

## Límites y cuándo no aplica

La estimación supone independencia y homogeneidad que rara vez se cumplen. Las cifras de SE-156 son supuestos del autor. Para documentos muy pequeños, una revisión informal basta. Una revisión no sustituye la validación con quienes usarán el sistema.
