# Costura

## Definición

Una **costura** (*seam*, de Feathers) es un lugar donde puede alterarse el comportamiento de un programa sin editar el código en ese lugar (`SE-519`). En `SE-422` se usa en un sentido práctico: el punto del código donde se puede reemplazar una dependencia sin editar la unidad.

## Por qué importa

Es lo que permite probar y refactorizar código heredado: sin costura, probar una función exige ejecutar su dependencia lenta o real. `SE-519` lo muestra con un síntoma concreto: la suite tarda minutos porque cada prueba paga la dependencia lenta; la corrección es crear una costura y sustituirla.

## Cómo funciona

Feathers distingue tres clases. En una **costura de objeto**, el comportamiento depende de un objeto o función que se puede sustituir (se pasa como argumento, se hereda, se reemplaza en una prueba); es la más usada. En una **costura de enlace** se cambia lo que se enlaza (otra biblioteca o módulo con el mismo nombre en el entorno de prueba). En una **costura de preprocesamiento** se transforma el texto antes de compilar.

## Ejemplo

`SE-519` (escenario hipotético): antes de refactorizar `nota_final`, el equipo añade un parámetro `leer_asistencia` con la consulta real como valor por defecto, una costura de objeto sin cambio de comportamiento. Luego genera 1 000 entradas con semilla fija y 14 casos de borde, guarda las salidas actuales y escribe una prueba que las exige.

```python
def nota_final(alumno, leer_asistencia=consultar_asistencia):
    return calcular(alumno, leer_asistencia(alumno))
```

## Errores y confusiones comunes

**La suite tarda minutos.** Cada prueba paga la dependencia lenta; crear una costura y sustituirla.

## Límites y cuándo no aplica

Una costura no mejora el diseño por sí sola: es un medio para fijar el comportamiento antes de refactorizar. Y no todos los lenguajes ofrecen las tres clases.
