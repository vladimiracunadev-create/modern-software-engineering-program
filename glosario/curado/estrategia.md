# Estrategia

## Definición

**Estrategia** es, en las clases de razonamiento (`SE-049` a `SE-056`), la forma de descomponer una afirmación o un problema en partes que se puedan resolver o demostrar; `SE-450` la usa en casos de seguridad como **estrategia de argumento**: el modo en que una meta se divide en submetas que se demuestran con evidencia. No es «plan de negocio»: es un método de resolver o argumentar.

## Por qué importa

Elegir mal la estrategia produce resultados plausibles y erróneos. `SE-056` lo muestra con un caso claro: una estrategia codiciosa para dar cambio puede parecer óptima y no serlo. En un caso de seguridad (`SE-450`), la estrategia es lo que hace visible y desafiable el argumento: quien lee puede preguntar «¿y si falla el sensor?» y hallar qué rama responde.

## Cómo funciona

- **Algoritmos** (`SE-056`): se compara una estrategia (codiciosa, programación dinámica) contra criterios. Para devolver 6 con ciertas monedas, la codiciosa usa 3 y la óptima solo 2: un contraejemplo basta para refutar la optimalidad. La programación dinámica es óptima pero cuesta tiempo y memoria proporcionales al monto.
- **Casos de seguridad** (`SE-450`): el caso responde tres preguntas: qué se afirma, por qué se cree (la estrategia: argumentar por cada peligro identificado, que tiene un control verificado) y con qué evidencia (resultados de pruebas, análisis, revisiones). La notación GSN (estructuración de metas) tiene nodos de meta, estrategia, solución, contexto, supuesto y justificación.
- **Descomposición de problemas** (`SE-049`): la estrategia declara el criterio de corte.

## Ejemplo

`SE-056`: con monedas {1, 3, 4} y objetivo 6, la estrategia codiciosa elige 4+1+1 (3 monedas); la óptima, 3+3 (2). Ilustración:

```python
def codiciosa(monto, monedas):
    out = []
    for m in sorted(monedas, reverse=True):
        while monto >= m: out.append(m); monto -= m
    return out        # codiciosa(6, [1,3,4]) -> [4,1,1]
```

## Errores y confusiones comunes

- **«Es óptimo» tras probar tres casos.** Causa: muestra pequeña; corrección: buscar contraejemplos en un dominio acotado (`SE-056`).
- **Reportar solo la media.** Causa: se oculta el peor caso; corrección: reportar media, peor y mejor observados (`SE-056`).
- **Confundir estrategia con evidencia.** En un caso de seguridad, la estrategia estructura el argumento; no lo prueba (`SE-450`).

## Límites y cuándo no aplica

La ventaja de una heurística es real en problemas grandes, y hay que decidir si el exceso sobre el óptimo es tolerable (`SE-056`). En casos de seguridad, un argumento bien estructurado con evidencia débil no es confiable. La palabra, además, se usa en otros ámbitos (de producto, de pruebas) con sentidos distintos que esta entrada no cubre.
