# Regla

## Definición

Una **regla** es, en las clases de razonamiento (`SE-049`, `SE-050`), una proposición condicional que dice qué debe ser cierto: «si P entonces Q». Es lo que permite derivar conclusiones desde premisas. La palabra aparece con otros sentidos cercanos (regla de un verificador, `SE-483`; regla de prioridad entre instrucciones, `SE-560`), pero el núcleo es la implicación y lo que se hace con ella.

## Por qué importa

Una regla mal usada produce conclusiones falsas con apariencia de rigor. `SE-050` muestra la falacia más frecuente en un diagnóstico: de «si DNS falla, el nombre no resuelve» no se sigue «si el nombre no resuelve, DNS falla». El resolvedor local, una regla de red o un archivo `hosts` producen el mismo síntoma. Cambia cómo se razona: no se invierte una regla sin comprobar.

## Cómo funciona

`SE-050` presenta los dos patrones válidos y los dos errores frecuentes:

- **Modus ponens:** de P y P→Q se obtiene Q.
- **Modus tollens:** de P→Q y no Q se obtiene no P.
- **Error:** afirmar el consecuente (de Q concluir P).
- **Error:** negar el antecedente (de no P concluir no Q).

El modelo de decisión diagnóstica del curso almacena las premisas junto con su fuente y momento, porque una regla válida con una premisa obsoleta produce una conclusión inútil. Sus reglas no disparan acciones destructivas: una conclusión incluye las premisas usadas, su vigencia y su nivel de evidencia; si falta una premisa, propone una prueba; si dos reglas concluyen estados incompatibles, eleva el conflicto en lugar de escoger silenciosamente.

## Ejemplo

```python
# Regla: si todas las pruebas del conjunto pasan, se puede publicar.
pruebas = []
publicable = all(p.paso for p in pruebas)    # True: verdad vacía, no se ejecutó nada
```

La corrección de `SE-050`: comprobar que el conjunto no es vacío antes de afirmar.

## Errores y confusiones comunes

- **Una regla «todas pasan» se cumple sin ejecutar nada.** Causa: verdad vacía sobre un conjunto vacío; corrección: comprobar que el conjunto no es vacío (`SE-050`).
- **Debilitar una prueba para que pase.** Causa: se trata como obstáculo; corrección: revisar la regla o el modelo (`SE-060`, `SE-052`).
- **Invertir una implicación.** Afirmar el consecuente sin más.

## Límites y cuándo no aplica

La lógica proposicional de `SE-050` cubre dominios finitos y enumerables; no sustituye medir. Una regla es tan buena como sus premisas y su vigencia. Y entre reglas del programa (de diagnóstico, de un verificador, de prioridad entre instrucciones), el nombre es común pero el mecanismo cambia: hay que fijar a cuál se refiere.
