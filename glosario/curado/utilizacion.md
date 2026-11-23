# Utilización

## Definición

La **utilización** es la fracción de la capacidad de un recurso que está ocupada. El programa la usa en nueve clases con el mismo núcleo y una fórmula distinta según el recurso, por lo que conviene identificar cuál es en cada caso:

- **De un servidor o una cola** (`SE-184`, `SE-247`, `SE-436`): la fracción del tiempo en que el recurso está ocupado; en una cola, la tasa de llegadas dividida por la tasa de servicio. Se escribe ρ.
- **De un procesador y sus tareas** (`SE-268`, `SE-451`): la fracción de CPU que consume una tarea, igual a su cómputo dividido por su periodo.
- **De la capacidad comprada** (`SE-281`, `SE-343`, `SE-404`): la fracción de la capacidad de servicio (o de una unidad de aceleración) que ocupa la demanda.
- **De un equipo** (`SE-533`): la fracción del tiempo disponible que el equipo, o una persona, dedica a trabajo asignado.

Sentido común: cuánto del tiempo o de la capacidad disponible está en uso. No es lo mismo que eficiencia: `SE-184` lo señala como la confusión de pedir «llegar al 100 % de ocupación».

## Por qué importa

Según `SE-184`, la espera crece de forma explosiva con la utilización, no lineal: un sistema que «da abasto» en promedio puede acumular cola cuando se acerca a la saturación. Por eso la utilización objetivo es una decisión de diseño y no un valor a maximizar: decide cuánta holgura se deja para absorber la variación. En costos (`SE-281`) y en capacidad (`SE-404`, `SE-436`) es además la medida de cuánta de la capacidad pagada se aprovecha.

## Cómo funciona

En una cola de un servidor con llegadas aleatorias, `SE-184` presenta la relación que explica la no linealidad: la espera media en cola es ρ/(1 − ρ) veces el tiempo medio de servicio. A 50 % de utilización la espera equivale a un servicio; a 80 %, cuatro; a 90 %, nueve; a 95 %, diecinueve. La razón es que el servidor pierde capacidad cada vez que está libre y no puede recuperarla, mientras que las llegadas siguen acumulándose cuando está ocupado. La consecuencia de gestión que la clase destaca es incómoda: la última fracción de utilización es la más cara, y un equipo sin holgura no puede absorber ninguna variación.

En tiempo real (`SE-268`, `SE-451`) la utilización de un conjunto de tareas se compara con cotas de planificabilidad. `SE-268` muestra que la cota es suficiente y no necesaria: en su simulación, todos los conjuntos con U ≤ 0,8 son planificables aunque 0,8 supere la cota, y entre 0,9 y 0,95 la fracción de conjuntos planificables cae del 92,5 % al 49,7 % según el número de tareas.

En costos (`SE-281`), la utilización se mezcla con las unidades enteras que se compran: con los supuestos del autor, el acelerador gana a partir de unos 1 000 a 2 000 peticiones por segundo; por debajo de eso, se paga capacidad que no se usa.

## Ejemplo

En `SE-184`, una cola de un servidor con llegadas y servicios exponenciales de media 1 se simula con 300 000 elementos por nivel de utilización (descartando los primeros 20 000). La simulación coincide con la fórmula hasta el 90 %; al 95 % queda un 6 % por debajo, porque cerca de la saturación la convergencia es lenta y 280 000 elementos aún no bastan. La clase usa la curva para fijar una utilización objetivo del equipo en lugar de buscar el 100 %.

## Errores y confusiones comunes

- **Pedir llegar al 100 % de ocupación.** Se confunde ocupación con eficiencia; corrección (`SE-184`): mostrar la curva de espera y fijar una utilización objetivo.
- **Un plazo que se incumple con baja utilización media.** El tiempo de ejecución varía y se analiza con la media; hay que usar el peor caso o un percentil alto y medir la cola (`SE-268`).
- **Confiar en la cota como condición necesaria.** Se confunde suficiente con necesaria; hay que aplicar el análisis exacto de tiempo de respuesta (`SE-268`).
- **Mezclar los sentidos.** Una utilización del 80 % de CPU, de un servidor de cola y de un equipo no se interpretan igual: hay que confirmar a qué recurso se refiere.

## Límites y cuándo no aplica

La fórmula ρ/(1 − ρ) vale para una cola de un servidor con llegadas y servicios exponenciales; con otra variabilidad o con lotes la espera cambia, y `SE-184` mide cuánto añaden la variabilidad y los lotes. Las cifras de costo de `SE-281` dependen de los precios y capacidades supuestos por el autor, y los resultados de planificabilidad de `SE-268` son de conjuntos generados con un algoritmo y periodos concretos. Una utilización media baja no garantiza cumplir plazos si el tiempo de ejecución varía mucho.
