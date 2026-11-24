# Evidencia

## Definición

**Evidencia** es un resultado concreto que sostiene una afirmación (`SE-450`). `SE-466` lo precisa para el cumplimiento: el resultado de una prueba o inspección con fecha, versión y huella que permite a otra persona verificar un control. No es una opinión ni un «confía en mí»: es algo que se puede mirar, repetir y atribuir a una versión.

## Por qué importa

Toda decisión de seguridad o de calidad es una afirmación («es aceptablemente seguro», «cumple») y sin evidencia es una creencia. La evidencia permite que alguien distinto del autor revise y desafíe. En sistemas críticos (`SE-450`), es el eslabón que convierte un argumento en un caso defendible.

## Cómo funciona

En un caso de seguridad, `SE-450` estructura tres preguntas: qué se afirma, por qué se cree (la estrategia de argumento) y con qué evidencia (resultados de pruebas, análisis, revisiones). Cada eslabón es visible y desafiable: quien lee puede preguntar «¿y si falla el sensor?» y hallar qué rama lo cubre. En la notación GSN, la evidencia es el nodo *solución*. `SE-466` añade requisitos para que la evidencia sea utilizable: **fecha**, **versión** del objeto probado y **huella** del resultado, para que no se confunda con evidencia de otra versión. Y separa lo demostrable de lo que decide una persona competente: la evidencia técnica no equivale a conformidad.

## Ejemplo

`SE-450`: un comité lee la afirmación «la puerta abierta corta la potencia» y su evidencia, una prueba funcional con el horno vacío. Pregunta qué pasa con la carga a 240 °C. El caso no responde: el contexto no menciona la carga térmica y la evidencia no la incluye. El equipo no estaba equivocado; el argumento no cubría un escenario real. La respuesta fue añadir el escenario como supuesto de contexto con una prueba, y registrar la contribución del comité. Ilustración de un registro:

```text
prueba: puerta_abierta_corta_potencia | version: 1.4.2 | fecha: 2026-03-04 | huella: ver artefacto
```

## Errores y confusiones comunes

- **La evidencia es de hace seis meses.** Causa: pruebas manuales y esporádicas; corrección: automatizar y guardar resultado con fecha y huella por versión (`SE-466`).
- **Declarar «cumple» sin revisión.** Causa: se confunde evidencia técnica con conformidad; corrección: separar lo demostrable de lo que decide una persona competente (`SE-466`).
- **Evidencia huérfana.** Resultados que no sostienen ninguna afirmación; `SE-450` usa un comprobador que detecta afirmaciones sin desarrollar y evidencias huérfanas.

## Límites y cuándo no aplica

La evidencia sostiene una afirmación acotada a un contexto y a una versión; no prueba lo que no cubre. Una gran cantidad de evidencia irrelevante no sustituye a la pertinente. Y el comprobador de `SE-450` verifica la estructura del argumento, no la calidad de la evidencia ni si el caso es suficiente.
