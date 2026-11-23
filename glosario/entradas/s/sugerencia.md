# Sugerencia

[↑ Glosario](../../README.md) · [← Sucesos concurrentes](./sucesos-concurrentes.md) · [Suite adversaria →](./suite-adversaria.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Texto que propone una corrección sin ejecutarla.

Definición de trabajo de [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md).

## Por qué importa

En [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md), el tema «Abreviaturas y sugerencias» importa porque aceptar de más crea promesas implícitas; sugerir de más induce a error.

## Cómo funciona

Según [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md):

Un error de tecleo en un subcomando puede ayudarse con una sugerencia («¿quiso decir `exportar`?»). Con doce subcomandos del dominio de la herramienta y 294 erratas sintéticas de dos ediciones (borrar, insertar, sustituir o transponer una letra, dos veces), `difflib.get_close_matches` con **corte 0,6 acertó las 294**; con **corte 0,8 acertó 193 y no sugirió nada en 101**; con **0,9 acertó solo 23 y calló en 271**. Ninguno sugirió un comando equivocado ante una errata. Pero el criterio cambia con palabras que no son erratas: con 16 palabras ajenas (`borrar`, `delete`, `crear`, `list`, `export`…), el corte 0,6 produjo sugerencia para **6** —entre ellas `crear → revisar`, que no tiene relación— y el corte 0,8 para **3**.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md):

En la plataforma, `notas` documenta su contrato en un archivo corto: tabla de flags (nombre, tipo, valor por defecto, desde qué versión), tabla de códigos (0 éxito, 2 uso incorrecto, 65 datos inválidos, 75 fallo temporal), destino de cada flujo y política de deprecación. Las abreviaturas están desactivadas en todos los analizadores, incluidos los de subcomandos. Una prueba de contrato ejecuta la herramienta como lo haría un guion y comprueba código, flujo y presencia de ciertas cadenas en la ayuda; no compara el texto completo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La sugerencia convence al usuario de un comando equivocado** — causa: corte demasiado laxo. Corrección: subir el corte, limitar a una sugerencia y no ejecutarla. ([SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Pero el criterio cambia con palabras que no son erratas: con 16 palabras ajenas (`borrar`, `delete`, `crear`, `list`, `export`…), el corte 0,6 produjo sugerencia para **6** —entre ellas `crear → revisar`, que no tiene relación— y el corte 0,8 para **3**. ([SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Abreviatura de flag](../a/abreviatura-de-flag.md), [Contrato de línea de comandos](../c/contrato-de-linea-de-comandos.md), [Deprecación](../d/deprecacion.md), [Subcomando](./subcomando.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-556](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md), [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), [SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Command Line Interface Guidelines](https://clig.dev/) — principios de diseño de interfaces de línea de comandos; autoridad: guía de autores, de uso extendido.
- [POSIX: Utility Conventions](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html) — sintaxis de opciones y argumentos; autoridad: The Open Group.
- [GNU Coding Standards: Command-Line Interfaces](https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html) — `--help`, `--version` y opciones largas; autoridad: proyecto GNU.
- [Python: `argparse`](https://docs.python.org/3/library/argparse.html) — `allow_abbrev`, subanalizadores y código de salida 2; autoridad: documentación de Python.
- [Python: `difflib`](https://docs.python.org/3/library/difflib.html) — `get_close_matches` y su umbral de similitud; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Sucesos concurrentes](./sucesos-concurrentes.md) · [Suite adversaria →](./suite-adversaria.md)
