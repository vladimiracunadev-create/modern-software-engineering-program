# Compuerta

## Definición

Una **compuerta** (*gate*) es una comprobación con veredicto de paso o fallo que un cambio debe superar para avanzar. Es una de las palabras más usadas del programa y no siempre con el mismo alcance, así que conviene precisar qué sentido usa cada clase:

- **El sentido central** (`SE-483`, `SE-564`, `SE-578`, `SE-583`): una comprobación automática cuyo resultado decide si un cambio puede integrarse o pasar de etapa. `SE-583` pide que su criterio no dependa de opinión y que su veredicto sea reproducible: con el mismo cambio, el mismo resultado.
- **En integración continua** (`SE-432`): el punto del flujo que bloquea o avisa según un umbral.
- **En una plataforma de datos** (`SE-372`): el conjunto de reglas que decide si un conjunto de datos se publica.
- **Un uso más amplio** (`SE-299`): una medida que reduce la probabilidad o el impacto de un riesgo, es decir, un control.

El glosario recoge el sentido central y señala los otros como matices del mismo núcleo: una condición que se comprueba antes de dejar pasar algo.

## Por qué importa

Una compuerta convierte una expectativa («esto debería compilar y pasar las pruebas») en un freno que no depende de la memoria ni de la buena voluntad de nadie. Es la pieza que hace posible delegar trabajo, a otras personas o a un agente, sin revisar cada paso: si el cambio pasa las compuertas, está dentro de lo que se verificó. `SE-583` la presenta en el contexto de un agente que escribe código, donde la compuerta es lo que da confianza en un «pasa».

## Cómo funciona

`SE-583` describe el diseño de un conjunto de compuertas con cuatro decisiones:

1. **Criterio ejecutable.** «El código compila», «el linter no reporta problemas», «no hay cadenas con forma de secreto», «las pruebas pasan». Böckeler llama controles computacionales a los deterministas y baratos, y los distingue de los inferenciales (un modelo que revisa), más ricos y menos fiables.
2. **Menú único.** La persona, el agente y la integración continua ejecutan las mismas compuertas con el mismo comando. Si cada cual ejecuta un subconjunto, un cambio pasa en un lugar y falla en otro y se erosiona la confianza en «pasa». El menú es un script con un solo punto de entrada que lista las compuertas en orden, se detiene en la primera que falla, imprime su nombre y el motivo y devuelve un código de salida.
3. **Orden por costo.** Las compuertas baratas detectan muchos defectos con poco costo: en el experimento, la de estilo (de microsegundos a un milisegundo) atrapa 5 de los 11 defectos, y las pruebas, que tardan cientos de milisegundos, atrapan 2. Se ordena de barato a caro y se detiene en el primer fallo. `SE-483` lo expresa como ordenar por razón de detección sobre costo: si el primer rojo tarda más de diez minutos, las etapas caras están primero.
4. **Meta-verificación.** Una compuerta que compara con la versión anterior detecta que las aserciones no bajen y que no aparezcan marcas de omisión sin justificación: no prueba el código, prueba que la prueba no se debilitó.

## Ejemplo

En el experimento de `SE-583`, once defectos se evalúan contra un menú de compuertas. Solo dos (un error de sintaxis que rompe la importación y un error de lógica que una prueba ve) son atrapados por las pruebas; los demás (una importación sin usar, un `except` sin tipo, un argumento mutable, una impresión de depuración, un secreto literal) pasan las pruebas y los atrapa alguna compuerta barata. Dos defectos más consisten en debilitar la prueba, y los atrapa la compuerta de meta-verificación. Dos escapan: un error de lógica en una rama que ninguna prueba ejerce y una prueba que replica el error. La conclusión de la clase: «las pruebas pasan» es una compuerta, no la compuerta.

## Errores y confusiones comunes

- **El primer rojo tarda más de diez minutos.** Las etapas caras van primero; corrección (`SE-483`): ordenar por razón de detección sobre costo.
- **El análisis de seguridad se ignora.** Bloquea por hallazgos sin corrección; hay que separar el bloqueo (críticos con corrección) del informe.
- **Las reglas se desactivan.** Muchas falsas alarmas; corrección: medir precisión y afinar con casos negativos.
- **Que cada cual ejecute un subconjunto.** Rompe la confianza en «pasa» (`SE-583`).
- **Confundir la compuerta con la garantía.** Una compuerta verde dice que se verificó lo que se verificó, y no más.

## Límites y cuándo no aplica

`SE-583` declara que ningún menú lo ve todo y que declarar ese límite es parte del menú: una rama que ninguna prueba ejerce se mitiga con cobertura y pruebas basadas en propiedades; una prueba que replica el error exige una fuente independiente del oráculo (una especificación, una revisión humana, una evaluación de otro tipo). Un control inferencial (un modelo que revisa) es más rico y menos fiable que uno computacional, y su veredicto no es reproducible. Y los resultados cuantitativos (5 de 11, 2 de 11) son de un experimento de la clase con un módulo de siete líneas, no una proporción transferible.
