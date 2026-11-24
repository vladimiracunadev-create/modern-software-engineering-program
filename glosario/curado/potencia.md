# Potencia

## Definición

La **potencia** (estadística) es la probabilidad de detectar un efecto real (`SE-585`). El programa la formula con el mismo núcleo en varias clases: la probabilidad de que un experimento refute una hipótesis falsa con el efecto y la ventana dados (`SE-505`), de que un contraste detecte un efecto real de un tamaño dado (`SE-485`), de detectar una mejora real (`SE-597`) o de detectarlo con un procedimiento y un tamaño de muestra dados (`SE-190`). Es la otra cara del error de no detectar.

## Por qué importa

Un resultado «sin efecto» solo significa algo si el experimento podía haberlo visto. Sin potencia, «no se encontró nada» es compatible con «no se podía encontrar». `SE-505` lo traduce a decisiones: no confirmar una hipótesis con 2 % de potencia, y escribir el efecto mínimo detectable junto con la conclusión.

## Cómo funciona

La potencia depende del tamaño del efecto, de la variabilidad, del tamaño de muestra o ventana y del umbral de decisión. Aumentarla cuesta datos o tiempo. `SE-585` muestra el compromiso con una regla sobre discordancias: se cuentan las tareas en que solo una de dos versiones acierta; con *b* tareas en que solo B acierta y *c* en que solo A, se declara mejor a B si (*b* − *c*)/√(*b* + *c*) supera 1,96. Comparar el harness contra sí mismo declara «mejora» 2,1 %, 3,0 % y 3,0 % de las veces, cerca del 2,5 % de una prueba de una cola al 95 %. Esa regla controla el error de falsas mejoras y cobra su precio: la potencia, porque exige diferencias mayores para declararlas.

En despliegue (`SE-485`), el canario que dice «sin errores» puede carecer de tráfico suficiente para ver el cambio: hay que calcular la potencia y exigir un tráfico mínimo.

## Ejemplo

`SE-505`: un umbral de SLO parece detectar más (53 % con 5 s), pero lo consigue porque el indicador sano (96,5 %) ya está pegado al umbral (96 %) y refuta ventanas sanas con frecuencia: su «potencia» incluye las falsas alarmas. Moraleja: potencia sin tasa de falsas alarmas engaña. Ilustración de simulación:

```python
detecta = sum(prueba(simular(efecto=0.05, n=200)) for _ in range(5000)) / 5000
```

## Errores y confusiones comunes

- **La hipótesis nunca se refuta.** Causa: potencia baja (ventana corta o efecto pequeño); corrección: ampliar la ventana o repetir y declarar el efecto mínimo detectable (`SE-505`).
- **Confirmar con 2 % de potencia.** Causa: no se calculó lo que el experimento podía ver (`SE-505`).
- **El canario sin errores y producción que falla.** Causa: tráfico insuficiente; corrección: calcular la potencia (`SE-485`).

## Límites y cuándo no aplica

Las cifras son de simulaciones de las clases con datos sintéticos. La potencia se calcula para un efecto supuesto: si el efecto real es menor, la potencia real también. Y una potencia alta no valida el procedimiento por sí sola: hay que controlar también el error de falsa alarma.
