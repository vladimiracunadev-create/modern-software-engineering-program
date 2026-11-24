# Runtime

## Definición

El **runtime** (entorno de ejecución) es el conjunto de servicios que ejecutan o sostienen un programa durante su ejecución: memoria, carga de código, recolección de basura (*garbage collection*), bucle de eventos o biblioteca estándar (`SE-109`). `SE-021` lo define como los servicios que implementan la ejecución de un lenguaje y `SE-013` como los servicios que sostienen un programa durante la ejecución. No es el programa ni el sistema operativo: es la capa entre ambos.

## Por qué importa

Es una dependencia operacional distinta del paquete: dos máquinas con el mismo código pueden comportarse distinto por tener runtimes distintos. Muchas explicaciones erróneas del tipo «una línea equivale a una instrucción» o «`del` libera memoria» ignoran esta capa. Cambia qué se declara al publicar o desplegar: la versión del runtime y, si afecta, la implementación y la plataforma.

## Cómo funciona

El runtime media entre el código y la máquina. Entre otras funciones:

- **memoria y referencias:** `del` elimina una referencia; el efecto depende de las referencias restantes, del runtime y del asignador, no de una liberación física inmediata (`SE-021`);
- **carga:** resuelve e importa módulos; un SDK que importa un runtime pesado para una sola función penaliza el arranque de todos sus usuarios (`SE-109`);
- **ejecución:** entre la línea de código y la instrucción de máquina hay compilador y runtime, con representaciones intermedias (`SE-013`).

`SE-109` pide que las versiones compatibles incluyan implementación y plataforma cuando afectan a la interfaz binaria o al comportamiento. En la práctica, un paquete declara qué versiones del runtime soporta y se prueba en cada una.

## Ejemplo

`SE-109`: `import mi_sdk` tarda 300 ms y carga más de 100 módulos porque el `__init__` importa un runtime completo aunque se use una función. Corrección: importar de forma perezosa dentro de la función o dividir en extras. Ilustración:

```python
def convertir(x):
    import pesado          # se carga solo si se usa esta función
    return pesado.convierte(x)
```

## Errores y confusiones comunes

- **`del` equivale a liberación física.** Causa: niveles confundidos; corrección: hablar de referencias y política del runtime (`SE-021`).
- **Una línea equivale a una instrucción.** Causa: se saltaron compilador y runtime; corrección: trazar representaciones intermedias (`SE-013`).
- **Un import pesado en el arranque** (`SE-109`).

## Límites y cuándo no aplica

El término se usa con matices (de lenguaje, de contenedores, de WebAssembly): conviene decir de cuál se habla. Las cifras de importación de `SE-109` son de un intérprete y un sistema concretos. Y el comportamiento del runtime puede cambiar entre versiones menores: declararlo y probar en cada una evita sorpresas.
