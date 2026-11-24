# Reproducibilidad

## Definición

La **reproducibilidad** es la capacidad de obtener el mismo resultado con el mismo código y los mismos datos (`SE-444`). `SE-006` la presenta como la posibilidad de repetir un método con información suficiente. Es una propiedad que se demuestra, no que se declara: se comprueba haciendo que otra persona, u otro entorno, repita el procedimiento y comparando el resultado.

## Por qué importa

Un resultado que no se puede reproducir no se puede auditar, depurar ni confiar en él. Las comparaciones entre versiones, los benchmarks y los informes dependen de ello. Cambia qué se registra al producir un artefacto: versiones, entradas, orden, codificación y entorno, no solo el código.

## Cómo funciona

La reproducibilidad exige controlar las fuentes de variación. `SE-444` clasifica ocho artefactos comparados: idénticos, diferentes por un defecto de escritura (corregible), diferentes por su naturaleza (por ejemplo, una fecha de generación) y diferentes por diseño. Al pasar de dos ejecuciones en el mismo sistema a Windows frente a Ubuntu, la parte idéntica se reduce: el entorno es una fuente de variación. La parte roja (defectos de escritura) se puede corregir, por ejemplo con escritura determinista.

`SE-504` indica prácticas concretas: serializar con claves ordenadas y UTF-8 y declarar las versiones, para que la huella no cambie entre sistemas por codificación, orden o versión no declarados. La causa de las diferencias suele ser un valor por defecto del entorno que nadie fijó.

## Ejemplo

```python
import json, hashlib
datos = {"b": 1, "a": 2}
s = json.dumps(datos, sort_keys=True, ensure_ascii=False).encode("utf-8")
print(hashlib.sha256(s).hexdigest())      # igual en Windows y en Linux
```

Sin `sort_keys` ni codificación explícita, la huella puede variar con el orden de inserción o la configuración regional.

## Errores y confusiones comunes

- **La huella cambia entre sistemas.** Causa: codificación, orden o versión no declarados; corrección: serializar con claves ordenadas y UTF-8 y declarar las versiones (`SE-504`).
- **El validador da 0 problemas y el ejercicio falla.** Causa: solo comprueba existencia y forma; corrección: añadir coincidencias de significado verificables (`SE-504`).
- **Confundirla con repetición o replicación.** `SE-289` los separa: repetir, reproducir y replicar fallan por razones distintas.

## Límites y cuándo no aplica

Los resultados de `SE-444` son de dos sistemas en un equipo, con una versión de Python en cada uno: otras versiones, sistemas de archivos o configuraciones regionales podrían cambiarlos. La reproducibilidad byte a byte de un informe con gráficos binarios exige controlar además fechas incrustadas y versiones de bibliotecas. Y no todo debe ser reproducible bit a bit: a veces basta una tolerancia declarada.
