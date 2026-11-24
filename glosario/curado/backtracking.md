# Backtracking

## Definición

El **backtracking** (vuelta atrás) es una estrategia de búsqueda exhaustiva en la que se **elige** una opción, se **avanza** con ella, se **detecta** si el estado parcial ya no puede completarse y, en ese caso, se **revierte** la última elección para probar otra. En `SE-092` se enseña junto con divide y vencerás como dos formas de organizar un problema grande: una explora un espacio de decisiones en profundidad; la otra lo parte en subproblemas independientes. No es un algoritmo concreto sino un esquema que se instancia para cada problema.

## Por qué importa

Muchos problemas (asignar tareas respetando dependencias, colocar piezas, elegir subconjuntos) no tienen una fórmula directa y obligan a explorar combinaciones. La decisión profesional es **cómo explorar sin enumerar todo**: el backtracking descarta ramas completas en cuanto una decisión parcial es imposible, y eso separa un programa que termina en segundos de uno que no termina. También importa por su riesgo: una poda equivocada elimina soluciones válidas sin dar error, así que el algoritmo puede ser rápido y estar mal.

## Cómo funciona

Se recorre un **árbol de decisiones** implícito: cada nivel es una variable por decidir y cada rama, uno de sus valores. En cada nodo:

1. Si el estado parcial viola una restricción, se abandona la rama (poda).
2. Si está completo y es válido, se registra la solución.
3. Si no, para cada candidato se aplica, se llama recursivamente y se **deshace**.

El corazón del mecanismo es la **restauración simétrica**: lo que la elección cambió debe quedar exactamente como estaba al volver, incluso si la llamada recursiva falla con una excepción (`SE-092`). Hay dos maneras de lograrlo. Copiar el estado en cada paso simplifica el razonamiento (cada rama trabaja sobre su copia) pero cuesta tiempo y memoria. Mutar y deshacer es más barato pero exige un invariante claro y pruebas de que no queda contaminación entre ramas. La eficiencia depende de dos palancas: qué tan temprano se detecta la imposibilidad y el **orden** en que se eligen las variables; probar primero la más restringida suele reducir mucho los nodos visitados.

## Ejemplo

En la biblioteca de estructuras y algoritmos de `SE-092`, un caso lleva identidad, prioridad, dependencias, instante de llegada y estado. Elegir un orden de resolución que respete las dependencias es un problema de este tipo. Un esqueleto (ilustración) muestra la simetría exigida:

```python
def resolver(estado, pendientes, solucion, salida):
    if not pendientes:
        salida.append(list(solucion)); return
    for c in list(pendientes):
        if estado.puede(c):
            estado.aplicar(c); pendientes.remove(c); solucion.append(c)
            try:
                resolver(estado, pendientes, solucion, salida)
            finally:
                solucion.pop(); pendientes.add(c); estado.deshacer(c)
```

El `finally` garantiza la restauración aunque haya error. Para validar la poda, `SE-092` pide contrastar el conteo de soluciones con enumeración completa en un `n` pequeño.

## Errores y confusiones comunes

- **Podar una rama válida.** El algoritmo encuentra menos soluciones que la fuerza bruta; se detecta comparando conteos en `n` pequeño.
- **Restaurar solo en el camino feliz.** Una excepción deja el estado sucio y las ramas siguientes parten de datos contaminados.
- **Culpar al algoritmo cuando la búsqueda es lenta.** A menudo el orden de las decisiones es desfavorable; probar primero las variables más restringidas y medir nodos.
- **Confundirlo con recursión.** La recursión es el mecanismo; el backtracking es la política de elegir, deshacer y podar.

## Límites y cuándo no aplica

La exploración exacta puede seguir siendo intratable: en el peor caso el árbol es exponencial y ninguna poda lo evita (`SE-092`). Si el problema tiene subproblemas superpuestos, la programación dinámica evita recomputar lo que el backtracking repite. Si basta una solución aproximada, una estrategia voraz o una heurística puede ser mejor. El backtracking conviene cuando se necesita una solución exacta o todas las soluciones y el espacio, tras la poda, es abarcable.
