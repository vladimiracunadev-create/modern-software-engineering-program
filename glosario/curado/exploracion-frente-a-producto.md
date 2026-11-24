# Exploración frente a producto

## Definición

**Exploración frente a producto** es la distinción que `SE-101` establece entre dos modos de trabajo con código: **explorar** (probar ideas, entender datos, descartar caminos) y **producir** (entregar algo que otros usarán y mantendrán). Explorar **tolera caminos muertos y visualización provisional**; un producto necesita **interfaz, pruebas y propietario** (*ownership*). La clase la usa para ubicar herramientas como el REPL y los cuadernos (*notebooks*): excelentes para explorar, insuficientes por sí solos para producir.

## Por qué importa

Confundir los modos produce dos fallos opuestos. Si se exige a una exploración el rigor de un producto, se frena el aprendizaje: nadie escribe pruebas para una idea que quizá se descarte en una hora. Si se entrega una exploración como producto, se despliega código sin interfaz definida, sin pruebas y con estado oculto, que nadie sabe mantener. La decisión que cambia es **cuándo y cómo se cruza la frontera**: `SE-101` pide un paso explícito, no desplegar el cuaderno sin revisión.

## Cómo funciona

Un cuaderno o una sesión interactiva guarda **estado oculto**: el orden en que se ejecutaron las celdas importa, y una variable definida y luego borrada sigue viva en memoria. Eso hace excelente la exploración (se prueba y se ajusta sin reiniciar) y frágil la reproducibilidad. Por eso `SE-101` documenta dos síntomas: el cuaderno da otro resultado en otra máquina por estado oculto del orden de ejecución, y se corrige **reiniciando y ejecutando todo** antes de compartir; y el *diff* es enorme con cambios mínimos porque se guardan salidas y metadatos en el archivo, y se corrige **limpiando las salidas** antes de confirmar.

El paso a producto consiste en **extraer**: las funciones útiles salen del cuaderno a módulos con interfaz definida; los datos se reducen a conjuntos pequeños y sintéticos para pruebas; el procedimiento se convierte en **un comando reproducible**; y alguien asume la propiedad (quién lo mantiene, quién responde).

## Ejemplo

Una persona explora un conjunto de registros en un cuaderno, prueba tres formas de limpiar fechas y se queda con una. Para llevarlo a producto:

```text
cuaderno.ipynb  ->  fechas.py        (funciones extraídas, con firma y errores)
                    test_fechas.py   (casos pequeños, sintéticos)
                    python -m fechas datos.csv   (comando reproducible)
```

El cuaderno puede quedarse como documentación de cómo se llegó a la decisión, con las salidas limpias. El criterio de paso es que otra persona, en otra máquina, obtenga el mismo resultado ejecutando el comando, no abriendo el cuaderno y corriendo celdas «en el orden correcto».

## Errores y confusiones comunes

- **Desplegar el cuaderno.** Lleva estado oculto, sin pruebas ni interfaz.
- **Compartir sin reiniciar y ejecutar todo.** El resultado depende del orden de celdas.
- **Versionar salidas y metadatos.** Producen *diffs* ilegibles y filtran datos.
- **Exigir rigor de producto a toda exploración.** Mata la velocidad con la que se aprende.

## Límites y cuándo no aplica

Un proceso limpio aún puede usar otra versión de *runtime* (`SE-101`): reproducir celdas en un entorno nuevo no basta si la instalación difiere; la clase siguiente fija instalación e intérprete. La frontera no siempre es nítida: un análisis puntual que no se repetirá puede quedarse como exploración sin migrar, y un cuaderno puede ser el producto cuando su público es analítico y el entorno está controlado. La pregunta es quién depende del resultado y con qué frecuencia lo reejecutará.
