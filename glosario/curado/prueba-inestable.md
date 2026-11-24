# Prueba inestable

## Definición

Una **prueba inestable** (en inglés, *flaky test*) es una prueba que, **sin cambios en el código ni en los datos declarados, pasa o falla según la ejecución**. El programa usa el término con el mismo sentido en varias clases: `SE-069` la describe como una prueba con resultado no determinista sin cambio relevante; `SE-483` y `SE-527`, como una que pasa y falla sobre el mismo código sin que nada haya cambiado. La clase `SE-430` la trata a fondo y distingue la prueba inestable de un **defecto intermitente real**.

## Por qué importa

Una suite de pruebas vale por lo que significa su resultado: un rojo debe querer decir «algo se rompió». Las pruebas inestables destruyen esa señal. El efecto es multiplicativo: si cada prueba inestable falla con probabilidad *q*, una suite sana sale roja con probabilidad `1 − (1 − q)^m` con *m* pruebas inestables. Según `SE-430`, con 20 pruebas que fallan el 5 % de las veces, el **64 %** de los *commits* sanos se ven rojos. El rojo constante enseña a reejecutar sin leer, y entonces un fallo real pasa inadvertido.

## Cómo funciona

Las causas conocidas son esperas asíncronas (la prueba no espera lo suficiente a algo que tarda), dependencia del **orden de ejecución**, de la **hora**, de la **red** o de **datos compartidos** entre pruebas. En todas, la prueba depende de algo que no controla, y a veces ese algo es favorable y a veces no.

La respuesta habitual, **reintentar hasta que pase**, reduce los falsos rojos pero tiene un costo menos visible: un **defecto intermitente real** (una condición de carrera en el producto) también pasa en alguno de los reintentos, y la suite lo declara sano. Por eso `SE-527` desactiva los reintentos automáticos de integración durante la estabilización. El tratamiento que enseña el programa es:

1. **Medir:** ejecutar la suite muchas veces sobre un *commit* sano para identificar qué pruebas varían.
2. **Clasificar la causa con evidencia:** ¿es la prueba o el producto?
3. **Poner en cuarentena** las inestables con **dueño y plazo**, y corregir la causa.
4. **Mantener la suite** de modo que un fallo siga significando algo.

## Ejemplo

El taller de `SE-527` (escenario hipotético de la clase, sin datos reales): la suite se ejecuta cien veces sobre un *commit* sano y se identifican 7 pruebas inestables de 412; se ponen en cuarentena con dueño y plazo y se desactivan los reintentos automáticos. Una prueba inestable típica:

```python
def test_notifica():
    enviar_en_segundo_plano(caso)
    time.sleep(0.1)                 # asume que 100 ms bastan
    assert bandeja.contiene(caso)   # falla si el envío tarda más
```

La corrección es esperar una condición con plazo (`esperar_hasta(lambda: bandeja.contiene(caso), timeout=5)`), no un tiempo fijo.

## Errores y confusiones comunes

- **Reintentar hasta que pase.** Oculta defectos intermitentes reales.
- **Confundir inestable con intermitente.** La causa puede estar en la prueba o en el producto; hay que clasificar.
- **Ignorar el rojo.** El equipo aprende a reejecutar sin leer.
- **Cuarentena sin dueño ni plazo.** La prueba queda olvidada.

## Límites y cuándo no aplica

El cálculo del 64 % supone pruebas independientes con la misma probabilidad; en la práctica el fallo se concentra en pocas pruebas inestables y se correlaciona con la carga del entorno (`SE-430`). Es una cota del mecanismo, no una predicción de una suite real. La noción de inestabilidad tampoco aplica a pruebas deliberadamente aleatorias que fijan su semilla: si la semilla está fija, el resultado es reproducible.
