# Exploración frente a producto

[↑ Glosario](../../README.md) · [← Exploración con semilla](./exploracion-con-semilla.md) · [Explosión de estados →](./explosion-de-estados.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

**Exploración frente a producto** es la distinción que [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md) establece entre dos modos de trabajo con código: **explorar** (probar ideas, entender datos, descartar caminos) y **producir** (entregar algo que otros usarán y mantendrán). Explorar **tolera caminos muertos y visualización provisional**; un producto necesita **interfaz, pruebas y propietario** (*ownership*). La clase la usa para ubicar herramientas como el REPL y los cuadernos (*notebooks*): excelentes para explorar, insuficientes por sí solos para producir.

## Por qué importa

Confundir los modos produce dos fallos opuestos. Si se exige a una exploración el rigor de un producto, se frena el aprendizaje: nadie escribe pruebas para una idea que quizá se descarte en una hora. Si se entrega una exploración como producto, se despliega código sin interfaz definida, sin pruebas y con estado oculto, que nadie sabe mantener. La decisión que cambia es **cuándo y cómo se cruza la frontera**: [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md) pide un paso explícito, no desplegar el cuaderno sin revisión.

## Cómo funciona

Un cuaderno o una sesión interactiva guarda **estado oculto**: el orden en que se ejecutaron las celdas importa, y una variable definida y luego borrada sigue viva en memoria. Eso hace excelente la exploración (se prueba y se ajusta sin reiniciar) y frágil la reproducibilidad. Por eso [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md) documenta dos síntomas: el cuaderno da otro resultado en otra máquina por estado oculto del orden de ejecución, y se corrige **reiniciando y ejecutando todo** antes de compartir; y el *diff* es enorme con cambios mínimos porque se guardan salidas y metadatos en el archivo, y se corrige **limpiando las salidas** antes de confirmar.

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

Un proceso limpio aún puede usar otra versión de *runtime* ([SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md)): reproducir celdas en un entorno nuevo no basta si la instalación difiere; la clase siguiente fija instalación e intérprete. La frontera no siempre es nítida: un análisis puntual que no se repetirá puede quedarse como exploración sin migrar, y un cuaderno puede ser el producto cuando su público es analítico y el entorno está controlado. La pregunta es quién depende del resultado y con qué frecuencia lo reejecutará.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Interfaz](../i/interfaz.md), [Ownership](../o/ownership.md), [Producto](../p/producto.md), [Narrativa y verificación](../n/narrativa-y-verificacion.md), [Notebook y grafo oculto](../n/notebook-y-grafo-oculto.md), [Proveniencia de datos](../p/proveniencia-de-datos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-101 — REPL, notebooks y desarrollo exploratorio](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) — Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft.
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) — Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Pdb, cprofile, timeit, tracemalloc y límites instrumentales; autoridad: Python Software Foundation.
- [Python venv](https://docs.python.org/3/library/venv.html) — Aislamiento de intérprete, scripts y entorno virtual; autoridad: Python Software Foundation.
- [Development Container Specification](https://containers.dev/implementors/spec/) — Configuración reproducible de herramientas y ciclo de vida del contenedor; autoridad: Dev Container Specification maintainers.

---

[↑ Glosario](../../README.md) · [← Exploración con semilla](./exploracion-con-semilla.md) · [Explosión de estados →](./explosion-de-estados.md)
