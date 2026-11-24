# Primera divergencia

## Definición

La **primera divergencia** es el primer punto donde un caso sano y uno afectado dejan de coincidir (`SE-047`, `SE-058`). `SE-105` precisa el método: se comparan trazas sana y afectada desde el mismo inicio y se localiza el primer estado distinto, no el último error. Es una técnica de diagnóstico, no un tipo de fallo.

## Por qué importa

El último error visible suele ser consecuencia, no causa. Buscar desde el final lleva a arreglar síntomas; buscar desde el primer punto en que algo difiere reduce las hipótesis causales. `SE-105` lo resume: las diferencias posteriores pueden ser consecuencias y no deben optimizarse primero. Cambia el orden en que se investiga y qué se corrige.

## Cómo funciona

El procedimiento (`SE-105`, `SE-047`):

1. Obtener una traza del caso **sano** y otra del **afectado**, con el mismo inicio y condiciones comparables.
2. Alinearlas paso a paso desde el principio.
3. Señalar la **primera fase o estado** donde difieren.
4. Formular hipótesis solo sobre ese punto y sus causas inmediatas.

La causa de que funcione es la causalidad temporal: lo que ocurre antes de la divergencia es idéntico en ambos casos, así que no puede explicar la diferencia; lo que ocurre después puede ser un efecto en cascada. En el laboratorio de `SE-047`, cada fila de la figura va de un escenario a su primera divergencia respecto del caso sano y a su resultado (correcto, fallido o recuperado). `SE-058` la usa para comparar dos recorridos de un algoritmo.

## Ejemplo

Traza sana: resolución DNS, conexión TCP, handshake TLS, petición, respuesta. Traza afectada: resolución DNS, conexión TCP, fallo del handshake TLS. La primera divergencia está en el handshake; el error final «no se pudo cargar la página» es solo el último eslabón. Ilustración:

```python
for i, (a, b) in enumerate(zip(traza_sana, traza_afectada)):
    if a != b:
        print("primera divergencia en el paso", i, a, b); break
```

## Errores y confusiones comunes

- **Informe con una lista de errores sin ordenar.** Causa: no se identificó la primera divergencia; corrección: comparar con el caso sano y señalar la primera fase que difiere (`SE-047`).
- **Optimizar las diferencias posteriores** (`SE-105`).
- **Comparar trazas con condiciones distintas.** La divergencia puede deberse a la entrada, no al fallo.

## Límites y cuándo no aplica

Requiere un caso sano comparable: si no existe, hay que construirlo o usar una referencia. En sistemas no deterministas, dos trazas sanas ya pueden diferir, y hay que descartar esas diferencias antes. Y el laboratorio de `SE-047` modela DNS, TLS y pérdida de forma determinista: demuestra el método, no el comportamiento de una red real.
