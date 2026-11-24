# Descomposición

## Definición

**Descomposición** es separar un todo en partes que se puedan tratar por separado. El programa usa la palabra con tres sentidos:

- **De un problema** (`SE-049`): separarlo en resultados coordinables.
- **De una métrica** (`SE-139`): repartir el cambio de una métrica entre los factores que la componen, con convención y orden declarados.
- **De un requisito de seguridad** (`SE-447`): satisfacerlo con elementos redundantes de nivel menor que sean independientes.

## Por qué importa

Un problema grande no se puede estimar, repartir ni verificar; uno partido en piezas sí. Y una métrica agregada que cambia sin explicación no sirve para decidir: hay que saber qué factor se movió. La decisión que cambia es qué criterio se usa para cortar, porque dos cortes distintos pueden ser ambos «razonables» y llevar a trabajos diferentes.

## Cómo funciona

- **Problemas** (`SE-049`): se declara un **criterio de descomposición** (por pregunta, no por herramienta) y se revisa el árbol contra él. Las partes deben ser coordinables: tener entradas y resultados claros.
- **Métricas** (`SE-139`): una métrica norte producto de factores (alcance × frecuencia × éxito) se descompone para saber qué factor explicó un cambio. Con logaritmos, la contribución de cada factor suma el cambio total sin depender del orden; con sustitución secuencial depende del orden y se informa un rango. Si el cambio total es pequeño, las participaciones son inestables y no se informan como porcentajes.
- **Seguridad** (`SE-447`): se cubre un requisito con elementos redundantes independientes de nivel menor; la independencia es lo que se comprueba.

## Ejemplo

`SE-139`: si el alcance sube un 10 % y el éxito baja un 5 %, el logaritmo reparte el cambio total en dos aportes que suman exactamente el total. Ilustración:

```python
import math
aporte = {k: math.log(nuevo[k]/viejo[k]) for k in viejo}
total = math.log(prod(nuevo.values())/prod(viejo.values()))   # == sum(aporte.values())
```

## Errores y confusiones comunes

- **Atribuir 90 % a un factor.** Causa: un solo orden de sustitución; corrección: logaritmos o informar el rango de órdenes (`SE-139`).
- **Dos árboles distintos, ambos «válidos».** Causa: falta criterio de descomposición; corrección: declararlo y revisar contra él (`SE-049`).
- **Creer que la descomposición explica el porqué.** Dice cuánto aportó cada factor, no por qué cambió.

## Límites y cuándo no aplica

Supone que la métrica es un producto exacto de los factores y que no hay interacciones fuera del producto (`SE-139`). En problemas muy acoplados, partir sin criterio ofrece una ilusión de orden. Y los tres sentidos no son intercambiables: descomponer un problema no es descomponer una métrica.
