# Espacio de estados

## Definición

El **espacio de estados** es el conjunto de todas las situaciones parciales por las que puede pasar la resolución de un problema, organizado como un grafo: en `SE-092`, **cada nodo representa una decisión parcial y cada arista una elección**. Antes de programar una búsqueda se define el **estado**, las **acciones** posibles, el **objetivo** y qué hace a un estado **inválido**. El backtracking y otras exploraciones recorren este espacio sin construirlo entero en memoria; existe como una forma de pensar el problema.

## Por qué importa

Un problema de búsqueda parece un montón de combinaciones sin estructura hasta que se modela. Definir el espacio de estados dice qué se está contando, dónde se puede podar y cuándo dos caminos son el mismo. La decisión que cambia es qué se escribe antes del código: una definición explícita de estado, acciones, objetivo e invalidez. Un modelo mal definido produce errores que ninguna optimización arregla; uno bien definido muestra el costo (cuántos nodos) y las oportunidades (qué se repite).

## Cómo funciona

Cuatro piezas definen el modelo:

- **Estado:** la información mínima necesaria para continuar. Si se omite algo relevante, el algoritmo pierde la capacidad de decidir bien; si se incluye de más, se multiplican estados sin necesidad.
- **Acciones:** las elecciones disponibles desde un estado, que producen sucesores.
- **Objetivo:** cómo se reconoce un estado final válido.
- **Invalidez:** cómo se reconoce que un estado parcial ya no puede completarse, base de la **poda**.

El tamaño del espacio suele ser exponencial en el número de decisiones. Lo que lo hace abordable es la estructura: si **dos rutas distintas llegan al mismo estado relevante**, se pueden **memoizar** y resolver una vez; si no, fusionarlas **pierde historia necesaria** (por ejemplo, el camino recorrido importa para el resultado). Esa pregunta, «¿el estado incluye lo suficiente para que el futuro no dependa del pasado?», decide entre la programación dinámica (estados repetidos y finitos) y la exploración con retroceso (el camino importa).

## Ejemplo

En `SE-092`, el orden de resolución de casos con dependencias se modela así (ilustración):

```text
estado:      (casos ya resueltos, caso pendiente actual)
acciones:    elegir un caso pendiente cuyas dependencias estén resueltas
objetivo:    todos los casos resueltos
invalidez:   no quedan casos elegibles pero faltan casos por resolver
```

Si el resultado depende solo de **qué** casos están resueltos y no del orden en que se resolvieron, dos caminos con el mismo conjunto son el mismo estado: se memoiza por conjunto. Si el orden altera el costo, hay que conservar el camino. Para validar la poda, la clase pide contrastar el conteo con una enumeración completa en un `n` pequeño.

## Errores y confusiones comunes

- **Programar sin definir el estado.** Cada elección parece lógica, pero el algoritmo no sabe cuándo repite trabajo.
- **Fusionar estados que difieren en algo relevante.** Pierde historia y da respuestas incorrectas sin error.
- **Podar con una condición demasiado agresiva.** Elimina soluciones válidas; el síntoma es encontrar menos soluciones que la fuerza bruta.
- **Culpar al algoritmo por la lentitud.** A menudo es el orden de decisiones: probar primero las variables más restringidas reduce nodos.

## Límites y cuándo no aplica

La exploración exacta puede seguir siendo intratable (`SE-092`): modelar bien el espacio no reduce su tamaño si no hay estados repetidos ni poda eficaz. Cuando el espacio es continuo o no se puede enumerar, otros métodos (optimización, aproximación) son más apropiados. Modelar un problema trivial como un grafo de estados puede ser más formal de lo necesario; la técnica se justifica cuando hay decisiones encadenadas.
