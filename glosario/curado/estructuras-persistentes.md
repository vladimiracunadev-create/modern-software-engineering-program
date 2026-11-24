# Estructuras persistentes

## Definición

Una **estructura persistente** es una estructura de datos en la que **una actualización produce una nueva versión que comparte partes inmutables con la anterior**, de modo que las versiones previas siguen disponibles sin haber sido modificadas (`SE-093`). La palabra «persistente» designa aquí **conservar versiones**, no necesariamente guardar en disco: una estructura persistente puede vivir solo en memoria. Es un uso técnico distinto del coloquial «persistencia» de datos en una base de datos.

## Por qué importa

Cuando se necesita conservar el estado anterior (para deshacer, para auditar, para razonar sobre versiones o para compartir datos entre hilos sin bloquear), copiar la estructura completa en cada cambio es caro. Una estructura persistente ofrece versiones baratas porque **comparte** lo que no cambió. La decisión que cambia es cómo se maneja el historial: en lugar de mutar y perder el pasado, se produce un valor nuevo y se conservan ambos. Al ser inmutables, las versiones antiguas pueden leerse concurrentemente sin riesgo.

## Cómo funciona

El mecanismo más sencillo es la **copia del camino** (*path copying*) en un árbol: para «cambiar» una hoja se crean copias solo de los nodos desde la raíz hasta esa hoja; el resto de los nodos se comparte entre la versión vieja y la nueva. La nueva raíz es la nueva versión; la raíz antigua sigue válida. Como ningún nodo compartido se modifica, la versión anterior permanece intacta.

Esto tiene un costo y un beneficio medibles. El costo de una actualización es proporcional a la altura del árbol (`O(log n)` si está equilibrado). El beneficio es memoria: se almacenan los nodos copiados, no la estructura completa. El costo oculto, que `SE-093` advierte, es que **compartir retiene memoria mientras haya referencias a raíces antiguas**: una versión vieja que sigue referenciada mantiene vivos todos sus nodos, incluidos los que la versión nueva ya no usa.

## Ejemplo

`SE-093` mide esto con un árbol binario equilibrado de 4 095 nodos. Al insertar una clave copiando solo el camino desde la raíz, se crearon **13 nodos nuevos** y **4 083 quedaron compartidos** entre las dos versiones; en memoria existen 4 108 nodos distintos, no 8 190 (el doble). Copiar la lista completa de 4 095 referencias tardó entre 13,6 y 19,0 µs y copiar el camino entre 6,6 y 16,0 µs: el **tiempo fue parecido**; la ganancia es de memoria y de poder conservar ambas versiones.

```python
class Nodo:
    __slots__ = ("clave", "izq", "der")
    def __init__(self, clave, izq=None, der=None):
        self.clave, self.izq, self.der = clave, izq, der

def insertar(n, k):           # devuelve una raíz nueva; no muta n
    if n is None: return Nodo(k)
    if k < n.clave: return Nodo(n.clave, insertar(n.izq, k), n.der)
    return Nodo(n.clave, n.izq, insertar(n.der, k))
```

Solo se copian los nodos del camino; los subárboles no visitados se comparten.

## Errores y confusiones comunes

- **Confundir persistente con guardado en disco.** El término habla de versiones, no de almacenamiento.
- **Esperar que sea más rápida.** En la medición, el tiempo fue parecido; lo que se gana es memoria y versiones.
- **Olvidar que las raíces antiguas retienen memoria.** Una referencia olvidada a una versión vieja evita liberar sus nodos.
- **Mutar un nodo compartido.** Rompe la garantía para todas las versiones que lo comparten.

## Límites y cuándo no aplica

Si no hace falta conservar versiones, una estructura mutable es más simple y suele ser más rápida en constantes. Las estructuras persistentes añaden asignaciones y punteros y empeoran la localidad frente a un arreglo. Y el ahorro de memoria depende de que los cambios sean pequeños respecto del total: si cada actualización toca casi todo, no hay nada que compartir. La clase advierte que una garantía teórica no predice constantes ni la distribución real; se mide.
