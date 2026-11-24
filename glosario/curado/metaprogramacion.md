# Metaprogramación

## Definición

La **metaprogramación** es escribir código que **modifica o genera otro código**, o que modifica el comportamiento de un programa desde el propio programa. `SE-116` enumera sus formas habituales: **decoradores**, **macros**, **reflexión** y **generación en tiempo de construcción**. Lo que las une es que el código opera sobre código (funciones, clases, texto fuente o estructuras del lenguaje) en lugar de operar sobre datos del dominio. No es un lenguaje ni una técnica única, sino una familia de mecanismos.

## Por qué importa

Reduce la repetición sistemática: un decorador evita escribir el mismo registro en veinte funciones; un generador produce los clientes de una API a partir de su descripción. La decisión que cambia es cuánta repetición se tolera frente a cuánta indirección se introduce. `SE-116` lo plantea con una advertencia: la metaprogramación **desplaza errores y herramientas**. El error ya no está en el código que se lee sino en el que se genera o se modifica, y los analizadores, depuradores y editores pueden no entenderlo.

## Cómo funciona

Cada forma actúa en un momento distinto:

- **Decorador:** una función que recibe otra y devuelve una versión modificada, aplicada al definirla.
- **Reflexión:** el programa inspecciona o altera sus propios objetos en ejecución (listar atributos, invocar por nombre).
- **Macro:** una transformación del código fuente en compilación (en lenguajes que las tienen).
- **Generación en construcción:** un script produce archivos de código a partir de una especificación y esos archivos se compilan o se importan.

La regla de `SE-116` es que **la expansión o el resultado debe poder inspeccionarse**: si no se puede ver el código generado, no se puede revisar ni depurar. Los fallos típicos de la generación se deben a que el generador no es determinista o a que se edita su producto. El primero: la integración continua marca diferencias en archivos generados que nadie tocó, porque el generador depende del reloj, del orden o de la ruta; se ordenan las entradas, se quitan marcas de tiempo y se usan rutas relativas. El segundo: alguien editó el archivo generado y se perdió al regenerar; se añade un encabezado «no editar», se regenera en integración continua y se usa `git diff --exit-code` para detectar discrepancias.

## Ejemplo

Un decorador que registra funciones como comandos:

```python
COMANDOS = {}

def comando(f):
    COMANDOS[f.__name__] = f
    return f

@comando
def listar(): ...

@comando
def borrar(): ...
```

Sin metaprogramación habría que mantener a mano un diccionario aparte, que es fácil olvidar actualizar. A cambio, quien lea `listar` no ve por sí solo que queda registrado; hay que conocer el decorador. En la generación en construcción, un script lee una descripción y escribe un archivo con el encabezado `# GENERADO: no editar`, y la integración continua lo regenera y falla si el resultado difiere del confirmado.

## Errores y confusiones comunes

- **Usarla para ahorrar unas líneas.** El costo de indirección supera el beneficio.
- **Generadores no deterministas.** Producen diferencias espurias en cada ejecución.
- **Editar archivos generados.** El cambio se pierde en la siguiente regeneración.
- **Ocultar la expansión.** Si no se puede ver lo generado, no se puede depurar.

## Límites y cuándo no aplica

La generación legalmente reutilizable depende de licencias y de la procedencia de las entradas y de las plantillas (`SE-116`): lo generado hereda las obligaciones de lo que lo originó. La metaprogramación pierde sentido cuando la repetición es pequeña o cuando el equipo no domina el mecanismo: el código claro y repetido puede ser más mantenible que el código ingenioso. Tampoco ayuda cuando el lenguaje ofrece una construcción directa para lo que se pretende.
