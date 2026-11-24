# Incertidumbre

## Definición

La **incertidumbre** es la falta de conocimiento relevante para una decisión (`SE-059`). `SE-047` la precisa en diagnóstico: la parte relevante que la evidencia disponible no permite determinar. No es lo mismo que ignorancia total ni que error: es lo que queda sin saber después de usar lo que se sabe, y es parte de la decisión, no un defecto del informe.

## Por qué importa

Decidir sin reconocerla produce afirmaciones falsamente precisas; paralizarse por ella impide avanzar. `SE-006` lo plantea como criterio de ingeniería: reconocer la incertidumbre no es paralizarse, sino gobernar lo que todavía no se sabe, y la decisión incluye siempre señales de parada y revisión. Cambia qué se comunica (rangos en vez de cifras únicas) y cuánto se invierte en saber más.

## Cómo funciona

`SE-006` ofrece formas de expresarla: rangos, escenarios, sensibilidad o confianza argumentada. Una cifra con decimales no es más honesta si el método no permite esa precisión. La pregunta operativa es si cambiar un supuesto cambia la opción preferida (análisis de sensibilidad): si no la cambia, quizá investigar más no aporte valor; si invierte una decisión irreversible, la evidencia adicional puede ser esencial. Esa pregunta prioriza dónde reducir incertidumbre. `SE-006` distingue además la **observación** (qué ocurrió), la **inferencia** (qué se concluye) y la **hipótesis**, para no mezclar lo medido con lo supuesto. En diagnóstico (`SE-047`) se declara qué parte la evidencia no determina, y en producción de ML (`SE-604`) se trata como parte de lo que se monitorea.

## Ejemplo

Una estimación de «6 semanas» presentada sola oculta la incertidumbre. Mejor: «entre 5 y 9 semanas; la cola larga depende de si el proveedor cambia su contrato (disparador conocido)». Ilustración de sensibilidad:

```python
for supuesto in (0.6, 0.8, 1.0):
    print(supuesto, decidir(supuesto))   # si la opción no cambia, saber más vale poco
```

## Errores y confusiones comunes

- **Una métrica se presenta como conclusión.** Causa: se omitieron inferencia y supuestos; corrección: separar registro, interpretación y alternativa rival (`SE-006`).
- **Benchmark sin configuración.** Causa: se perdió trazabilidad; corrección: fijar datos, entorno, versiones, orden y múltiples corridas (`SE-006`).
- **Confundir significancia con importancia.** Un resultado poco probable sin efecto no dice que el efecto sea grande, importante ni causal (`SE-006`).

## Límites y cuándo no aplica

`SE-006` no es un curso de estadística: lo útil es preguntar qué incertidumbre queda y si cambia la decisión. Expresarla con rangos requiere un método que la sustente; un rango inventado es tan engañoso como una cifra falsa. Y algunas decisiones deben tomarse con la incertidumbre intacta: esperar más tiene su propio costo.
