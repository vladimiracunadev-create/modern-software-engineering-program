# Slice reusable

## Definición

Un **slice reusable** (porción reutilizable) es, en el taller de `SE-119`, la **capacidad pequeña** que se extrae de un sistema para empaquetarla y consumirla por separado, elegida porque tiene **entrada, salida, errores y dependencias claros**. «Slice» significa rebanada: no se empaqueta todo el sistema, sino una parte con una frontera nítida. El término es propio del programa; en otros contextos se habla de extraer un módulo o un componente.

## Por qué importa

La tentación al crear una biblioteca es extraer «todo lo que sirva». Pero `SE-119` advierte que **extraer todo el sistema crea una API extensa antes de entender a los consumidores**: cada función expuesta es una promesa que mantener, y se promete sin saber qué se usará. La decisión que cambia es el tamaño del primer paso: una capacidad pequeña, probada de punta a punta como paquete instalable, que enseña qué hace falta antes de ampliar. Es una forma de aprender barato.

## Cómo funciona

Un buen *slice* cumple cuatro condiciones:

- **Entrada y salida claras:** tipos y formatos conocidos, sin depender de estado global del producto original.
- **Errores definidos:** sabe fallar de forma que el consumidor lo entienda.
- **Dependencias acotadas:** pocas y declaradas, de modo que instalar el paquete no arrastre medio sistema.
- **Semántica conservada:** el comportamiento es el mismo que en el producto original; el paquete no «mejora» ni cambia reglas al extraerlo.

Lo que no es parte de la capacidad (acceso a la base de datos del producto, configuración específica, formato de archivos propio) se queda como **adaptadores en el producto original**: el producto llama al paquete a través de ellos. Así la dependencia va en una dirección (el producto depende del paquete) y el paquete no conoce al producto.

El *slice* se valida con el procedimiento del taller: construir sdist y wheel, instalarlos en un entorno limpio y probar desde fuera del repositorio con solo importaciones públicas. Dos defectos típicos aparecen aquí: el paquete instalado no encuentra su archivo de datos porque falta `package-data`, y `ModuleNotFoundError` solo en un entorno limpio porque una dependencia no está declarada.

## Ejemplo

Del motor de la biblioteca de estructuras y algoritmos se extrae solo la elección del siguiente caso:

```text
paquete:    engineering_sdk
capacidad:  choose_next(casos, politica) -> caso
entrada:    lista de casos con id, prioridad, dependencias, llegada
salida:     un caso o None si no hay elegible
errores:    ValueError si un caso no tiene id; CicloDeDependencias
dependencias: ninguna fuera de la biblioteca estándar
queda en el producto: lectura de archivos, formato de salida, configuración
```

Es pequeña, tiene frontera clara y se puede probar desde un directorio externo. No incluye el planificador completo, el formato de reportes ni la configuración, que seguirán en el producto y se extraerán, si hace falta, cuando se entiendan los consumidores.

## Errores y confusiones comunes

- **Extraer todo.** Se promete una API grande sin conocer su uso.
- **Arrastrar el estado global del producto.** El paquete queda acoplado a su origen.
- **Cambiar el comportamiento al extraer.** El producto original y el paquete divergen.
- **No declarar dependencias.** Falla en entorno limpio.

## Límites y cuándo no aplica

El taller verifica una versión y un entorno principal (`SE-119`); la compatibilidad entre versiones y plataformas la construye el proyecto siguiente. Si la capacidad solo se usa en un lugar, empaquetarla es esfuerzo sin retorno. Un *slice* demasiado pequeño (una función de tres líneas) cuesta más mantener como paquete que copiar. Y a veces la frontera no es nítida: si la capacidad está entrelazada con el resto, la primera tarea es separar, no empaquetar.
