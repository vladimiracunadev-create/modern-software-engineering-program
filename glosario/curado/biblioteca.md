# Biblioteca

## Definición

Una **biblioteca** (*library*) es un conjunto de funciones o tipos que el programa consumidor **llama y compone**. En la clase `SE-109` se contrasta con framework, runtime, plataforma y SDK, y el criterio que las separa es quién ocupa el fondo de la pila: con una biblioteca el consumidor conserva el flujo principal de su programa y decide cuándo invocar. No es un sinónimo de «paquete» (la unidad de distribución) ni de «módulo» (una unidad de organización del código); una biblioteca se distribuye normalmente como paquete y contiene módulos.

## Por qué importa

Elegir entre biblioteca y framework decide quién manda sobre la estructura del programa. Con una biblioteca el costo de salir es bajo, porque se reemplaza una llamada por otra; con un framework, el programa se organiza alrededor de él y migrar es reescribir. `SE-109` también cuida un error de comunicación: llamar «plataforma» a un conjunto de bibliotecas promete propiedad, soporte, cuotas y política de cambios que nadie ofrece. Nombrar bien el producto fija qué promete el equipo.

## Cómo funciona

El mecanismo es la **dirección de la llamada**. Con una biblioteca, el código del consumidor llama al de la biblioteca y recupera el control al retornar. Con un framework ocurre lo contrario: el framework llama al código del consumidor en puntos que él define (inversión de control, tema que `SE-109` toma de Martin Fowler). Que una biblioteca sea pequeña o grande no cambia la categoría.

Una biblioteca, sin embargo, puede traer efectos o su propio runtime (hilos, conexiones, estado global). Por eso debe declarar en su API la **inicialización**, la **seguridad ante hilos** y el **ciclo de vida**: cuándo se crea, cuándo se cierra y qué pasa si se usa desde dos hilos. Si no lo declara, el consumidor tiene que descubrirlo en producción. La frontera entre lo que la biblioteca promete y lo que no es su API pública, con su versionado.

## Ejemplo

El producto reutilizable de `SE-109` empaqueta el motor de la biblioteca de estructuras y algoritmos como `engineering_sdk`, expone la función `choose_next`, una CLI y un punto de extensión. El consumidor escribe su propio flujo y llama a la función cuando lo decide:

```python
from engineering_sdk import choose_next

for caso in cola:
    elegido = choose_next(caso, politica)   # el consumidor manda el flujo
```

El caso verifica instalación limpia, entrada válida, configuración ausente, plugin incompatible y actualización entre dos versiones, y cambia después una regla para revisar qué archivos, pruebas y trazas debieron modificarse. Esa superficie de cambio es la que mide si la biblioteca está bien acotada.

## Errores y confusiones comunes

- **Llamar plataforma a un conjunto de bibliotecas.** Una plataforma exige responsable, SLO, cuotas y política de cambios; sin eso, es una biblioteca (`SE-109`).
- **Distinguir por tamaño o por nombre.** La diferencia con un framework es quién invoca a quién.
- **Ignorar el ciclo de vida.** Una biblioteca con estado global y sin inicialización documentada rompe cuando se usa desde dos hilos o dos veces.
- **Confundir biblioteca con SDK.** Un SDK agrupa bibliotecas con herramientas, documentación y ejemplos para una plataforma o servicio; hay una entrada propia.

## Límites y cuándo no aplica

La categoría es un espectro: una biblioteca que exige registrar *callbacks* y orquesta el flujo se parece ya a un framework. `SE-109` ofrece criterio, no una frontera rígida. Tampoco toda reutilización requiere publicar una biblioteca: copiar veinte líneas puede costar menos que mantener un paquete versionado. Y una biblioteca con pocos consumidores internos no necesita la formalidad de un producto público; el esfuerzo debe corresponder a cuántos dependerán de ella.
