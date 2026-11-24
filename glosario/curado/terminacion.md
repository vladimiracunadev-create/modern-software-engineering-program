# Terminación

## Definición

La **terminación** es la propiedad de finalizar para toda entrada del dominio (`SE-054`). Un algoritmo cuya ejecución puede no acabar para alguna entrada no termina, aunque casi siempre lo haga. En operación (`SE-222`), la palabra tiene un segundo sentido: cómo se detiene un proceso o un servicio, ordenada o forzosamente.

## Por qué importa

Un programa que no termina consume recursos indefinidamente o bloquea a quien lo espera. Un timeout detiene una ejecución, pero no demuestra que el algoritmo termine para cualquier entrada (`SE-054`). Importa distinguir ambas cosas: parar un proceso es una decisión operativa; demostrar que termina es una propiedad del algoritmo. Y en producción, la forma de terminar decide si se pierden datos.

## Cómo funciona

**Del algoritmo** (`SE-054`): se demuestra con una **variante**, una cantidad que toma valores en un orden bien fundado (por ejemplo, enteros no negativos) y disminuye estrictamente en cada iteración. Si `b` decrece en cada paso y no baja de 0, el bucle termina; su **corrección** viene de un invariante (una igualdad que se conserva) junto con esa terminación. `pendientes` puede servir como variante si ningún paso vuelve a insertar indefinidamente. En recorridos de grafos con ciclos, el conjunto de visitados garantiza que los nodos pendientes decrecen (`SE-051`).

**Operativa** (`SE-222`): terminar un servicio puede ser ordenado (el proceso recibe una señal, vacía lo pendiente, escribe en un archivo temporal y renombra) o forzado (se corta sin limpieza). La terminación forzada puede dejar un archivo truncado; en Windows, `terminate()` equivale a una terminación forzada, por lo que se usa `CTRL_BREAK_EVENT` o un canal de cierre propio.

## Ejemplo

```python
def mcd(a, b):
    while b:                    # variante: b decrece estrictamente y es >= 0
        a, b = b, a % b         # invariante: mcd(a, b) no cambia
    return a
```

Como `a % b < b`, el valor de `b` baja en cada paso: termina para cualquier par de enteros no negativos.

## Errores y confusiones comunes

- **Un archivo queda truncado al detener el servicio.** Causa: terminación forzada o manejador que no vació; corrección: cierre ordenado y escritura en archivo temporal (`SE-222`).
- **`terminate()` no limpia en Windows.** Causa: equivale a terminación forzada; corrección: `CTRL_BREAK_EVENT` o un canal de cierre propio (`SE-222`).
- **Creer que un timeout prueba terminación.** Solo corta una ejecución concreta (`SE-054`).

## Límites y cuándo no aplica

La terminación no es decidible en general para programas arbitrarios (problema de la parada); se demuestra caso a caso con una variante. Para servicios que por diseño no terminan, la propiedad relevante es la de cada petición, no la del proceso. Y una demostración de terminación no acota el tiempo: un programa puede terminar tras un tiempo inaceptable.
