# Flujo

## Definición

Un **flujo** (*stream*) es una secuencia de elementos procesada de uno en uno (`SE-339`). El programa usa la palabra con matices:

- **En redes** (`SE-040`): una secuencia ordenada de octetos sin fronteras de mensaje (TCP) o un canal lógico ordenado dentro de una conexión QUIC.
- **En programación** (`SE-067`, `SE-248`): una secuencia de datos leída o escrita progresivamente, procesada por trozos sin retener el conjunto completo.
- **En estilos arquitectónicos** (`SE-339`): el contrato de las tuberías y filtros.

## Por qué importa

La memoria de una versión en flujo no depende del volumen de entrada; la de un procesamiento por lotes crece con él (`SE-339`). Con una entrada que se duplica, una versión por lotes puede quedarse sin memoria; una en flujo sigue funcionando. En redes, olvidar que un flujo de octetos no tiene fronteras de mensaje produce errores de lectura parcial.

## Cómo funciona

En el estilo de tuberías y filtros (`SE-339`), un filtro recibe un flujo de elementos y emite otro. Si todos comparten esa forma, se conectan en cualquier orden que tenga sentido y cada uno se prueba con una lista pequeña. En el laboratorio, cada filtro es un generador de Python: `f_validate` deja pasar las filas válidas, `f_due` las que vencen en 72 horas o menos, `f_enrich` añade una etiqueta y `f_format` produce el texto; la cadena es `f_format(f_enrich(f_due(f_validate(filas))))`. El contrato uniforme compra reuso y sustitución de pasos sin editar los vecinos.

## Ejemplo

El equipo de *Avisos* migra un volcado nocturno a filtros y descubre dos cosas: el paso de ordenar por urgencia, añadido al final, retiene todo el lote y es el único que escala con el volumen; y una fila con código de curso nulo detenía toda la cadena de madrugada. Solución: ordenar solo dentro de cada curso (estado de tamaño acotado) y entregar el orden global como una consulta aparte. Ilustración:

```python
def f_due(filas):
    for f in filas:
        if f["horas"] <= 72: yield f
```

## Errores y confusiones comunes

- **Un paso que acumula todo el flujo.** Ordenar o agrupar sin límite rompe la promesa de memoria acotada (`SE-339`).
- **Una fila inválida detiene todo.** Hace falta una política por elemento (descartar, registrar o apartar).
- **Suponer fronteras de mensaje en un flujo de octetos** (`SE-040`).

## Límites y cuándo no aplica

El estilo comparte la forma (pasos encadenados) pero no necesariamente el contrato: en una canalización de integración continua, cada paso suele recibir artefactos completos, no un flujo de elementos (`SE-339`). Los pasos con estado global (ordenar, agregar) obligan a retener datos y reintroducen el costo en memoria que el flujo evitaba.
