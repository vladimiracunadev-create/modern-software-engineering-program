# Reconstrucción de la solución

## Definición

La **reconstrucción de la solución** es el paso de **recuperar qué decisiones produjeron un valor óptimo**, no solo cuánto vale ese óptimo. En `SE-091`, al resolver un problema con programación dinámica o con una estrategia voraz, el **valor óptimo no basta si se necesita explicar qué casos se eligieron**: un costo mínimo de 17 dice poco sin saber qué combinación lo logra. Para reconstruir, se guardan **predecesores o decisiones** durante el cálculo y se recorren al final en sentido inverso.

## Por qué importa

Muchas veces se pide el valor (el costo mínimo, el máximo de actividades) y después se descubre que se necesita el plan: qué actividades, qué monedas, qué casos. Calcular de nuevo para obtenerlo es caro o imposible si no se previó. Además, en un sistema que decide por personas o dinero, la explicación es un requisito: auditar una decisión exige saber qué se eligió y por qué. La decisión que cambia es qué se guarda durante el cálculo: solo el valor, o también el rastro de decisiones. `SE-091` añade que los **empates deben seguir una política estable** para que los resultados y la auditoría sean reproducibles.

## Cómo funciona

En programación dinámica se llena una tabla de subproblemas: `mejor[i]` es el valor óptimo para el subproblema `i`. Para reconstruir:

1. **Registrar la decisión** que dio cada celda (de cuál subproblema o con qué elección se llegó: un puntero al **predecesor**).
2. **Partir del estado final** y seguir los predecesores hacia atrás hasta el inicio.
3. **Invertir** la secuencia obtenida para presentarla en orden.

El costo adicional es memoria (una entrada por celda) y un recorrido lineal. Los empates son el punto delicado: si dos decisiones dan el mismo valor, cuál se registra cambia la solución reconstruida, aunque el valor sea igual. Si la política de desempate es implícita (depende del orden de iteración o de una estructura sin orden definido), dos ejecuciones pueden producir soluciones distintas con el mismo óptimo, y la auditoría no es reproducible. Por eso la regla de empate se declara (por ejemplo, «a igualdad, el de menor identificador») y se prueba.

## Ejemplo

Cambio mínimo de monedas con reconstrucción (ilustración):

```python
def cambio(monedas, total):
    INF = float("inf")
    mejor = [0] + [INF] * total
    eleg = [None] * (total + 1)
    for t in range(1, total + 1):
        for m in sorted(monedas):               # orden fijo: desempate estable
            if m <= t and mejor[t - m] + 1 < mejor[t]:
                mejor[t], eleg[t] = mejor[t - m] + 1, m
    usadas, t = [], total
    while t > 0 and eleg[t] is not None:
        usadas.append(eleg[t]); t -= eleg[t]
    return mejor[total], usadas

cambio([1, 3, 4], 6)       # (2, [3, 3])
```

`mejor[total]` da el valor; `eleg` permite reconstruir el plan. Con monedas no canónicas, la regla voraz habría entregado un plan peor, que es el error que `SE-091` documenta (más monedas de las necesarias).

## Errores y confusiones comunes

- **Guardar solo el valor.** Después no se puede explicar el plan.
- **Desempate implícito.** Resultados distintos entre ejecuciones con el mismo óptimo.
- **Reconstruir sin validar.** Conviene comprobar que el plan reconstruido suma el valor reportado.
- **Confundir reconstruir con recalcular.** El rastro se guarda al calcular; no se vuelve a resolver.

## Límites y cuándo no aplica

La programación dinámica exige un estado finito y manejable (`SE-091`): si la tabla no cabe en memoria, tampoco caben los predecesores. Reconstruir solo tiene sentido cuando alguien necesita el plan; si solo se pide el valor, guardar decisiones es costo sin uso. Y cuando hay muchas soluciones óptimas distintas, reconstruir una no dice nada sobre las demás; si se necesitan todas, es otro problema.
