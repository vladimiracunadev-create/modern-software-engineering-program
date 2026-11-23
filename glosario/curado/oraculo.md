# Oráculo

## Definición

Un **oráculo** es el mecanismo que decide si el resultado de una prueba o de una operación es el esperado. Las clases lo definen con ese núcleo: `SE-060` como el mecanismo para determinar el resultado esperado, `SE-069` como el criterio que decide el resultado esperado, `SE-541` como el mecanismo que decide si un resultado es correcto, y `SE-294` y `SE-300` como un modelo de referencia independiente (y, en `SE-300`, más simple que lo probado) con el que se compara el resultado. Una aserción, un ejemplo acordado, un esquema, un contrato, una especificación ejecutable o una evaluación con umbral son oráculos.

## Por qué importa

Una prueba solo es tan buena como su oráculo: sin una fuente de «lo correcto» independiente de lo que se prueba, la prueba confirma lo que el código ya hace. `SE-541` lleva la idea al plano de las metodologías: casi toda disputa metodológica es una disputa de oráculo disfrazada de disputa de proceso: quién decide que algo está bien, cuándo y con qué evidencia.

## Cómo funciona

La causa de que el oráculo importe es la independencia. `SE-300` distingue dos cosas que se complementan: las **invariantes** dicen lo que nunca debe suceder; el **oráculo** es un modelo de referencia independiente que dice qué debe suceder. `SE-294` mostró que las primeras no bastan: un importe equivocado puede conservar el total, de modo que una invariante de suma no lo detecta y un oráculo que calcula el importe esperado sí. En cada dominio el oráculo toma una forma distinta (`SE-300`): una suma exacta en ciencia, una tabla ya idempotente en datos, un umbral con línea base en aprendizaje automático, una simulación de paso fino en juegos, una implementación lenta y simple en dinero. Lo que importa es que sea más simple que lo probado, porque un oráculo tan complejo como el sistema reproduce sus mismos errores.

## Ejemplo

En `SE-294`, una operación monetaria que reparte mal un importe puede dejar el total correcto. Una invariante («el total se conserva») pasa; un oráculo, una implementación lenta y simple del cálculo de dinero, calcula el reparto esperado y detecta la diferencia. En `SE-583`, el límite de un menú de compuertas es justamente que una prueba que replica el error escapa: se mitiga con una fuente independiente del oráculo (una especificación, una revisión humana o una evaluación de otro tipo).

## Errores y confusiones comunes

- **Una prueba que replica el error.** El valor esperado se cambió para coincidir con el código incorrecto; corrección (`SE-583`): una fuente independiente del oráculo.
- **Tomar las invariantes por oráculo.** Dicen lo que nunca debe pasar, no qué debe suceder (`SE-300`).
- **Un oráculo tan complejo como lo probado.** Reproduce los mismos errores; debe ser más simple (`SE-300`).

## Límites y cuándo no aplica

Un oráculo decide solo lo que su fuente permite decidir: una evaluación con umbral depende de su línea base (`SE-300`). `SE-583` declara que ningún menú lo ve todo y que declarar ese límite es parte del diseño.
