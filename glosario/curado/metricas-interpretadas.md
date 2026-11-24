# Métricas interpretadas

## Definición

Las **métricas interpretadas** son, en el proyecto de comparación de `SE-084`, las mediciones que se reportan **acompañadas de su contexto y de su lectura**, no como números sueltos. Se observan cuatro: la **superficie de cambio** (cuántos lugares hay que tocar ante un cambio), la **complejidad de la traza** (qué tan difícil es seguir lo que pasó en una ejecución), el **aislamiento de las pruebas** (cuánto de la realidad hay que montar para probar una pieza) y el **costo bajo una carga representativa**. «Interpretadas» expresa que cada cifra se presenta con qué mide, qué no mide y qué sesgos tiene.

## Por qué importa

Un número aislado seduce: «la solución B tiene 40 % menos líneas» o «tarda la mitad». Pero sin contexto, ese número puede ser irrelevante o engañoso: menos líneas puede significar más densidad ilegible; la mitad del tiempo puede deberse a que se excluyó la lectura de datos. La decisión que cambia es qué se acepta como evidencia en una comparación: una métrica solo cuenta si se sabe qué mide, bajo qué condiciones y con qué limitaciones. `SE-084` lo concreta: **líneas de código y tiempo bruto se presentan con contexto**.

## Cómo funciona

Cada métrica responde a una pregunta de mantenimiento o de ejecución:

- **Superficie de cambio:** se aplica un mismo cambio a cada solución y se cuenta qué se modifica; mide la dispersión de las decisiones.
- **Complejidad de traza:** cuántos pasos o saltos hay entre la entrada y la decisión; mide cuánto cuesta explicar un resultado.
- **Aislamiento de pruebas:** cuántas dependencias hay que simular para probar una regla; mide qué tan desacoplada está.
- **Costo bajo carga representativa:** tiempo o memoria con una carga que se parezca a la real.

La interpretación exige **no mezclar sesgos sin declararlos**: no se mezcla calentamiento (la primera ejecución paga costos de arranque) con ejecución estable, ni entrada y salida con cálculo, ni *runtimes* diferentes. Si se mezclan, se declara el sesgo. La causa de este cuidado es que la medición compara soluciones; cualquier diferencia ajena al diseño que entre en el número falsea la comparación.

## Ejemplo

Un fragmento de reporte con interpretación (ilustración, números inventados):

```text
superficie de cambio: A=1 archivo, B=3 archivos (cambio fijo: regla de empate).
   Lectura: en B la regla está repartida; no implica que B sea peor en otros cambios.
costo, 10 000 casos (mediana de 30 ejecuciones tras 5 de calentamiento, Python 3.12):
   A=18 ms, B=22 ms. Lectura: diferencia dentro del ruido (±4 ms); no concluyente.
comando: python -m bench --casos 10000 --reps 30
```

Un error documentado en la clase es el informe que afirma sin comando reproducible: se corrige añadiendo comando, versión y salida a cada afirmación. Otro: la suite pasa y hay defectos porque solo cubre el camino feliz; se derivan casos del contrato y de los mutantes.

## Errores y confusiones comunes

- **Reportar líneas de código como calidad.** Mide tamaño, no mantenibilidad.
- **Tiempo bruto sin contexto.** Mezcla calentamiento, entrada y salida, y máquinas distintas.
- **Concluir con diferencias dentro del ruido.** Sin repeticiones y dispersión, no hay conclusión.
- **Omitir el comando.** Nadie puede reproducir la cifra.

## Límites y cuándo no aplica

El proyecto demuestra equivalencia para el corpus y las propiedades declaradas, no para todas las entradas posibles ni para cargas de producción (`SE-084`). Las métricas de diseño (superficie de cambio) dependen del cambio elegido: con otro cambio, el orden puede invertirse. Y ninguna métrica sustituye observar el mantenimiento real del sistema a lo largo del tiempo; solo lo aproxima de forma controlada.
