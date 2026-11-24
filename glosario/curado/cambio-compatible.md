# Cambio compatible

## Definición

Un **cambio compatible** es una modificación del proveedor de una interfaz que **no rompe ningún contrato de un consumidor existente** (`SE-423`). En el taller de empaquetado de `SE-119` el ejemplo es agregar una opción sin romper al consumidor anterior: el código antiguo sigue funcionando sin tocarse, y se ejecutan ambas pruebas (la del consumidor antiguo y la que usa la opción nueva) para demostrarlo. Es el caso que justifica subir una versión **menor** en versionado semántico, mientras que un cambio incompatible exige subir la mayor.

## Por qué importa

La compatibilidad permite que proveedores y consumidores evolucionen a ritmos distintos. Si cada cambio obliga a coordinar con todos, el costo de mejorar el producto crece con el número de consumidores. La decisión profesional que cambia es **cómo se clasifica un cambio antes de numerarlo**: `SE-119` lo dice así, «el número se decide después de clasificar el cambio», no antes. Clasificar mal produce versiones que mienten: un parche que rompe, o una versión mayor que alarma sin motivo.

## Cómo funciona

Un cambio es compatible respecto de un contrato concreto. Se razona sobre qué puede depender el consumidor:

- **Añadir** una opción con valor por defecto, un campo opcional en la respuesta o una función nueva suele ser compatible: el consumidor antiguo no la usa.
- **Quitar o renombrar** algo público, **cambiar el tipo** de un valor, **endurecer** una validación (rechazar lo que antes se aceptaba) o **cambiar el orden o el formato** prometidos suele ser incompatible.
- **Ablandar** requisitos de entrada y **endurecer** garantías de salida son compatibles; lo contrario no.

El razonamiento es de sustitución: el consumidor antiguo debe poder usar la versión nueva sin enterarse. Para comprobarlo, `SE-119` pide ejecutar la prueba antigua contra el código nuevo, revisar el changelog y, si hace falta, la guía de migración. Un comparador de API detecta firmas, y las pruebas de contrato escritas desde el consumidor detectan comportamiento.

## Ejemplo

El taller de `SE-119` agrega una opción a la API del paquete reutilizable. El consumidor anterior llama sin la opción y obtiene el comportamiento previo, porque el valor por defecto lo conserva:

```python
# versión 1.2: salida = procesar(datos)
# versión 1.3: salida = procesar(datos, estricto=False)  # nuevo, por defecto igual al anterior
```

Se ejecutan las dos pruebas: la que invoca `procesar(datos)` debe seguir verde y la nueva debe cubrir `estricto=True`. Como la API declarada solo añade, la versión propuesta es la menor (1.3.0) y el changelog lo anota. En `SE-423`, la misma idea aparece en componentes: un proveedor que cambia sin romper ningún contrato de consumidor hace un cambio compatible, y el consumidor puede actualizar cuando quiera.

## Errores y confusiones comunes

- **Creer que «solo añadir» siempre es compatible.** Añadir un valor a una enumeración que los consumidores recorren con `switch` exhaustivo puede romperlos.
- **Medir por la firma y no por el comportamiento.** Mantener la firma pero cambiar el orden de los resultados o la excepción lanzada rompe a quien dependía de ellos.
- **Numerar primero y clasificar después.** Se acaba justificando el número en lugar de describir el cambio.
- **No probar con el consumidor antiguo.** Solo la prueba antigua contra el código nuevo demuestra la compatibilidad.

## Límites y cuándo no aplica

La compatibilidad se define frente a los consumidores conocidos y a la API declarada: no puede garantizarse frente a quien dependa de comportamiento no documentado. El taller verifica una versión y un entorno principal (`SE-119`); la compatibilidad entre versiones de dependencias y plataformas pide una matriz de compatibilidad. En sistemas donde el proveedor controla a todos los consumidores y los despliega juntos, la distinción pierde peso porque se puede cambiar ambos a la vez.
