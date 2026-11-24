# Explosión de estados

## Definición

La **explosión de estados** es el crecimiento del número de estados globales de un sistema con el número de componentes concurrentes (SE-161). SE-453 la precisa como el crecimiento exponencial del espacio de estados con el tamaño del modelo. Es el principal obstáculo práctico de la verificación de modelos.

## Por qué importa

El costo de verificar crece con el espacio de estados, y este crece de forma exponencial. Con unos pocos componentes la verificación puede tardar horas o no terminar. Cambia cómo se modela: hay que decidir qué se abstrae, qué se acota y qué se reduce, o la herramienta no llega a ningún resultado.

## Cómo funciona

Cada componente concurrente añade su propio estado, y los estados globales son el **producto** de los locales. SE-161 ejemplifica con N estudiantes que envían a la vez, con tres estados locales cada uno: el espacio tiene 3ᴺ combinaciones. SE-453 lo mide en un laboratorio: n procesos independientes de cuatro pasos tienen 4ⁿ estados: **16 con 2, 1.024 con 5 y 16.384 con 7**. Cada proceso añadido multiplica por cuatro.

Tres defensas, según SE-161:

- **Abstraer**: modelar solo lo que importa para la propiedad, descartando detalles irrelevantes.
- **Acotar**: probar con N pequeño (dos o tres procesos), con la hipótesis de que un defecto de coordinación suele manifestarse con pocos participantes.
- **Reducir por simetría**: tratar como idénticos los componentes intercambiables (los estudiantes son equivalentes entre sí), de modo que estados que difieren solo en el orden de los nombres se cuentan una vez. La reducción por simetría solo es válida si la intercambiabilidad es real; si los componentes se distinguen (uno es administrador), la reducción puede ocultar defectos.

La razón de que funcione es que la propiedad suele depender de una estructura pequeña del sistema; el resto del espacio es redundante respecto de ella. El riesgo es que la abstracción elimine justo lo que causaba el defecto.

## Ejemplo

Tres estudiantes que envían entregas en paralelo, cada uno con estados «sin enviar», «enviando» y «enviado»: 3³ = 27 estados globales. Con diez estudiantes, 3¹⁰ = 59.049. Con simetría (los estudiantes son intercambiables), basta contar cuántos hay en cada estado: la combinación (2 sin enviar, 1 enviando, 0 enviado) representa a todas las asignaciones equivalentes, y el espacio se reduce a unas decenas de configuraciones. (Cálculo propio para ilustrar la defensa de SE-161.)

## Errores y confusiones comunes

- **La verificación tarda horas con pocos componentes**: explosión sin reducción; corrección: abstraer detalles, acotar N y aplicar simetría solo a componentes intercambiables.
- **Reducir por simetría componentes que no lo son.**
- **Abstraer lo que causa el defecto.**
- **Confundirla con la complejidad de un algoritmo**: aquí crece el número de configuraciones del sistema.

## Límites y cuándo no aplica

Las defensas aceptan perder garantía: lo verificado con N pequeño no prueba N grande. En modelos muy secuenciales con pocos componentes, el problema no aparece. Algunas técnicas (verificación simbólica, ejecución parcial del espacio) amplían lo verificable, pero no eliminan el crecimiento exponencial en general.
