# Exposición

## Definición

La **exposición** a un riesgo es el producto de su probabilidad y su impacto (`SE-187`, siguiendo a Boehm); `SE-008` la presenta como la combinación razonada de probabilidad y consecuencia. `SE-432` la usa ponderada por la parte de los cambios que cae en un componente. `SE-187` advierte que su suma mide el retraso esperado, no su dispersión.

## Por qué importa

Permite ordenar riesgos y decidir a cuáles dedicar esfuerzo: Boehm propuso ordenarlos por exposición y revisar la lista de los principales cada vez. El valor de la lista, dice `SE-187`, es la conversación que obliga, no el número. Cambia la decisión de dónde se invierte atención, pruebas o contingencia.

## Cómo funciona

Cada riesgo se describe con causa, evento y efecto, se estima con probabilidad e impacto y se acompaña de un disparador, una respuesta y un responsable (`SE-187`). La exposición es `probabilidad × impacto`. `SE-432` la aplica a pruebas: el riesgo de un componente se pondera por la fracción de cambios que lo tocan, de modo que un componente muy modificado con impacto moderado puede merecer más atención que uno raro de impacto alto. En `SE-611` se calcula en horas y decisiones: 168 horas por 400 decisiones, más de 67 000 decisiones tomadas con la mitad del historial vacío, lo que da la magnitud de un incidente de datos.

Su límite estructural es que es un valor esperado: la media casi no se mueve cuando hay una cola de eventos grandes, por lo que la exposición esperada, sola, no avisa de la cola (`SE-187`).

## Ejemplo

Dos riesgos: A con probabilidad 0,5 e impacto de 2 días (exposición 1 día); B con probabilidad 0,1 e impacto de 20 días (exposición 2 días). Ilustración:

```python
riesgos = {"A": (0.5, 2), "B": (0.1, 20)}
orden = sorted(riesgos, key=lambda k: -riesgos[k][0] * riesgos[k][1])   # B, A
```

`SE-187` simula diez riesgos con y sin causa común y compara el percentil 85 con la exposición: con causa común, la exposición subestima el retraso.

## Errores y confusiones comunes

- **Sumar exposiciones como si fueran independientes.** Las causas comunes hacen que se materialicen juntos.
- **Tomar el número como predicción.** Ordena; no predice.
- **Confundirla con el riesgo mismo.** La exposición es una cifra; el riesgo es una cadena causal con respuesta (`SE-187`).

## Límites y cuándo no aplica

Las probabilidades e impactos son estimaciones. En seguridad funcional (`SE-008`, `SE-445`), el producto de números puede no bastar: la gravedad se trata con normas propias. Y una exposición baja no autoriza a ignorar un riesgo cuyo impacto es inaceptable.
