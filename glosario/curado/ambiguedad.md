# Ambigüedad

## Definición

La **ambigüedad** es la propiedad de un texto que admite más de una lectura razonable con consecuencias distintas (`SE-154`). `SE-157` la vuelve verificable: un enunciado es ambiguo si admite al menos dos implementaciones compatibles con el texto que dan resultados distintos para la misma entrada. `SE-565` la mira como decisión no resuelta: un comportamiento que el documento no fija y que, por tanto, decide quien implementa. En `SE-059` es, más simplemente, la pluralidad de interpretaciones de un problema.

## Por qué importa

Una frase con dos lecturas se implementa de dos maneras, y nadie lo nota porque cada persona lee una sola versión. El coste aparece tarde, en integración o producción. Y se multiplica: `SE-157` observa que cuatro puntos abiertos binarios dan dieciséis comportamientos posibles. Con agentes de código (`SE-565`) el efecto es mayor: el agente entrega algo que funciona y no es lo que se quería, porque resolvió por su cuenta las ambigüedades.

## Cómo funciona

`SE-154`, siguiendo a Berry y colegas, distingue fuentes:

- **léxica**: una palabra con varios sentidos;
- **sintáctica**: cómo se agrupa la frase;
- **de alcance**: qué abarca «todos» o «no»;
- **referencial**: a qué se refiere «lo» o «esto»;
- **de elipsis**: lo que se omite.

La estructural con «y» y «o» es la más fácil de contar y de pasar por alto. `SE-157` la distingue del **silencio** (omitir un caso). Su causa no es descuido individual sino que el texto se lee frente a lectores con supuestos distintos. Por eso se detecta ejecutando: se escriben las lecturas, se calculan los resultados y se compara. Se corrige añadiendo ejemplos, una forma semiformal o formal, o resolviendo la decisión por escrito (`SE-565`).

## Ejemplo

«Máximo tres reintentos por día»: ¿día natural o ventana de 24 horas? Dos implementaciones compatibles dan resultados distintos con una misma secuencia de intentos; eso demuestra la ambigüedad sin discutir opiniones (ejemplo de `SE-157` en esencia: «por día»). En `SE-154` el inventario de defectos sirve cuando cada uno tiene tipo, técnica y responsable.

## Errores y confusiones comunes

- **Entrega que funciona pero no es lo pedido.** Causa: ambigüedades sin resolver que el agente resolvió; corrección: resolver las de mayor costo y declarar las que se delegan (`SE-565`).
- **Confundirla con contradicción o incompletitud** (`SE-154`): la ambigüedad admite dos lecturas; la contradicción, dos reglas incompatibles; la incompletitud, un caso no cubierto.
- **Creer que es un fallo de redacción personal.** Es propiedad del texto frente a sus lectores.

## Límites y cuándo no aplica

No toda indeterminación es un defecto: algunos puntos se delegan a propósito. No se elimina escribiendo más; se reduce con ejemplos y comprobaciones. La medición por implementaciones alternativas solo cubre las lecturas que alguien imaginó.
