# SDK

## Definición

Un **SDK** (*Software Development Kit*, kit de desarrollo de software) es, según `SE-109`, un conjunto que **reduce la fricción para integrar una capacidad**: incluye cliente, modelos de datos, autenticación, ejemplos, herramientas y documentación. Normalmente integra una **biblioteca** y puede añadir una CLI, pero su promesa no es el código sino una **experiencia coherente** de integración. Se distingue de la biblioteca (que ofrece funciones que se llaman) y del *framework* (que invierte el control) por su propósito: facilitar el uso de un servicio, una plataforma o una capacidad concreta.

## Por qué importa

Integrar un servicio remoto con solo su documentación obliga a cada consumidor a reescribir la autenticación, la serialización, los reintentos y la paginación. Un SDK lo hace una vez. Pero también concentra decisiones: **lo que el SDK decide por defecto lo hereda cada consumidor sin saberlo** (`SE-109`): el tiempo de espera, los reintentos, el formato de los errores. La decisión que cambia es cuánto confiar en esos valores por defecto y cuánto exigir que el SDK los haga visibles.

## Cómo funciona

Un SDK bien diseñado cumple varias condiciones:

- **Representa el contrato remoto sin ocultarlo.** Debe exponer, sin esconder, el *timeout*, la paginación y los errores del servicio; si los oculta, los consumidores no pueden razonar sobre fallos.
- **Tiene una superficie pública definida y versionada,** como cualquier API.
- **Es barato de importar.** Importarlo no debe abrir red ni leer credenciales.
- **Se clasifica por control y contrato, no por nombre.**

`SE-109` documenta tres defectos concretos. Clasificar «es un SDK porque se llama SDK» (se clasificó por marketing); la corrección es imprimir la pila desde una función de retorno y decidir por quién ocupa el fondo. `import mi_sdk` tarda 300 ms y carga más de 100 módulos porque el `__init__` importa un runtime completo aunque se use una función; se importa de forma perezosa o se divide en extras. Y `import mi_sdk` falla en integración continua sin credenciales porque el módulo lee variables de entorno o abre red al importarse; se mueven los efectos a `connect()` y se comprueba con un gancho de auditoría.

## Ejemplo

Un SDK que envuelve un servicio de casos, respetando el contrato remoto:

```python
from mi_sdk import Cliente

c = Cliente(token=leer_token(), timeout=10, reintentos=2)   # decisiones visibles
for pagina in c.casos.listar(pagina_tamano=100):             # paginación explícita
    for caso in pagina:
        procesar(caso)
```

El `timeout` y los reintentos son parámetros con valor por defecto documentado, no constantes ocultas. Importar `mi_sdk` no abre ninguna conexión: eso ocurre al construir `Cliente` o al llamar `connect()`. El SDK del programa (`engineering_sdk`) sigue esa estructura: expone `choose_next`, una CLI y un punto de extensión, con efectos fuera de la importación.

## Errores y confusiones comunes

- **Clasificar por nombre.** Lo que importa es quién ocupa el fondo de la pila y qué contrato ofrece.
- **Efectos al importar.** Falla en integración continua o en entornos sin credenciales.
- **Ocultar el *timeout* o los errores.** El consumidor no puede razonar sobre fallos.
- **Importar todo al cargar.** Cuesta tiempo y memoria aunque se use una función.

## Límites y cuándo no aplica

Un SDK es útil cuando hay una capacidad que muchos consumidores integran; para un servicio con un solo cliente interno, llamar a la API directamente puede ser más simple. Un SDK además tiene un costo de mantenimiento: debe versionarse, documentarse y mantenerse en cada lenguaje soportado, y retrasarse respecto del servicio crea una brecha. Y como hereda decisiones por defecto, un SDK mal calibrado las propaga a todos los consumidores a la vez.
