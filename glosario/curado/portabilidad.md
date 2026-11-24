# Portabilidad

## Definición

La **portabilidad** es la capacidad de ejecutar el mismo software en otro entorno con el mismo resultado (`SE-441`). `SE-405` la formula para cargas en la nube: poder mover una carga entre entornos con un esfuerzo acotado y conocido. `SE-030` la acota con una cláusula honesta: el grado de funcionamiento demostrado dentro de una matriz definida. La portabilidad es, entonces, algo que se demuestra, no una propiedad declarada.

## Por qué importa

Decide cuánto cuesta cambiar de entorno (sistema operativo, proveedor de nube) y cuánto riesgo hay de que el cambio altere el resultado. `SE-405` advierte que se confunde con multi-cloud (usar más de un proveedor) y con híbrido (instalación propia más nube); comparten el discurso de «no depender de uno» pero son cosas distintas.

## Cómo funciona

Las diferencias entre entornos vienen sobre todo de los **valores por defecto** (`SE-441`):

- la codificación de texto cuando no se especifica;
- el fin de línea y el separador de ruta;
- si los nombres distinguen mayúsculas;
- caracteres y nombres prohibidos y la longitud máxima de ruta;
- qué ocurre al renombrar sobre un archivo existente o al borrar uno abierto;
- el rango de fechas del reloj y el método de creación de procesos.

Python esconde muchas diferencias y expone otras: las expuestas lanzan una excepción (`PermissionError`), las escondidas cambian el resultado. Por eso se escribe una matriz de soporte con lo realmente probado (`SE-030`) y se aíslan las diferencias en adaptadores.

Para la nube (`SE-405`), la guía de Google sobre patrones híbridos y multi-cloud organiza motivos: aprovechar funciones distintas, cumplir una regulación de ubicación de datos, reducir una dependencia, repartir riesgo, aprovechar inversiones existentes. Cada motivo se evalúa con su propio cálculo.

## Ejemplo

```python
open("datos.txt", "w", encoding="utf-8", newline="\n")   # fija lo que el entorno decidiría por defecto
```

Sin `encoding` ni `newline`, el mismo programa escribe bytes distintos en Windows y Linux.

## Errores y confusiones comunes

- **Dos proveedores y la misma caída anual.** Causa: un componente compartido en serie; corrección: dibujar las dependencias y eliminar o duplicar el común (`SE-405`).
- **La conmutación falla cuando se necesita.** Causa: nunca se ensayó; corrección: ensayarla con regularidad y medir su acierto (`SE-405`).
- **Declarar portable lo que solo se probó en un entorno.**

## Límites y cuándo no aplica

La portabilidad total es una ilusión de costo alto: normalmente se persigue una portabilidad acotada y probada. Multi-cloud sin motivo concreto produce arquitecturas caras que no resuelven ningún problema (`SE-405`). Y portable no significa idéntico en rendimiento: el resultado funcional puede igualar mientras el desempeño difiere.
