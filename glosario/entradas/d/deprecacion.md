# Deprecación

[↑ Glosario](../../README.md) · [← Dependencias y distribución](./dependencias-y-distribucion.md) · [Deprecación y migración →](./deprecacion-y-migracion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Estado en que una opción sigue funcionando pero avisa de su retirada en una versión posterior.

Definición de trabajo de [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md).

## Por qué importa

La clase donde se define, [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md), existe con este propósito: la clase existe para diseñar una interfaz de línea de comandos como un contrato con dos lectores —una persona que escribe y un programa que invoca— de modo que cambiar un flag, un mensaje o un código no rompa ni a la persona que lo memorizó ni al guion que lo automatizó.

## Cómo funciona

Según [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md):

En la plataforma, `notas` documenta su contrato en un archivo corto: tabla de flags (nombre, tipo, valor por defecto, desde qué versión), tabla de códigos (0 éxito, 2 uso incorrecto, 65 datos inválidos, 75 fallo temporal), destino de cada flujo y política de deprecación. Las abreviaturas están desactivadas en todos los analizadores, incluidos los de subcomandos. Una prueba de contrato ejecuta la herramienta como lo haría un guion y comprueba código, flujo y presencia de ciertas cadenas en la ayuda; no compara el texto completo. Una segunda prueba falla si alguien añade un flag sin documentarlo.

## Ejemplo

Ejemplo de [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md) (sección «Ejemplo profesional»):

En la plataforma, `notas` documenta su contrato en un archivo corto: tabla de flags (nombre, tipo, valor por defecto, desde qué versión), tabla de códigos (0 éxito, 2 uso incorrecto, 65 datos inválidos, 75 fallo temporal), destino de cada flujo y política de deprecación. Las abreviaturas están desactivadas en todos los analizadores, incluidos los de subcomandos. Una prueba de contrato ejecuta la herramienta como lo haría un guion y comprueba código, flujo y presencia de ciertas cadenas en la ayuda; no compara el texto completo. Una segunda prueba falla si alguien añade un flag sin documentarlo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md)) son:

- **Un guion falla después de añadir un flag** — causa: dependía de una abreviatura. Corrección: desactivar abreviaturas en todos los analizadores y probar un prefijo.
- **`allow_abbrev=False` no surte efecto en un subcomando** — causa: la opción no se hereda en los subanalizadores. Corrección: pasarla en cada `add_parser`.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2), con resultados idénticos salvo el tamaño de un mensaje. No se usó ninguna herramienta real, no se midió a ninguna persona usando la ayuda y las erratas, los nombres de flags y los umbrales son supuestos del autor. La siguiente clase pregunta cómo entra y sale la información por la superficie que se acaba de definir.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Opción](../o/opcion.md), [Versión](../v/version.md), [Abreviatura de flag](../a/abreviatura-de-flag.md), [Contrato de línea de comandos](../c/contrato-de-linea-de-comandos.md), [Subcomando](../s/subcomando.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md).

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

[↑ Glosario](../../README.md) · [← Dependencias y distribución](./dependencias-y-distribucion.md) · [Deprecación y migración →](./deprecacion-y-migracion.md)
