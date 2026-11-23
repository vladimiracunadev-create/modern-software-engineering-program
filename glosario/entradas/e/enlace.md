# Enlace

[↑ Glosario](../../README.md) · [← Engineering Manager](./engineering-manager.md) · [Enlace de salto →](./enlace-de-salto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Asociación entre un nombre y un objeto.

Definición de trabajo de [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md): Objeto que resuelve las importaciones de un módulo con funciones del anfitrión.

## Por qué importa

La clase donde se define, [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md), existe con este propósito: la clase existe para explicar valores, tipos, expresiones y nombres por su semántica y ciclo de vida.

## Cómo funciona

Según [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md):

Una asignación enlaza un nombre a un objeto; no copia necesariamente el objeto. Reasignar un entero cambia el enlace; modificar una lista compartida cambia el objeto visto por todos sus alias. Llamar `timeout_seconds` al nombre hace visible una unidad que `t` oculta.

Según [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md):

Compilar una unidad no resuelve todas las dependencias. Enlace combina símbolos y artefactos; carga mapea código y datos, resuelve bibliotecas y prepara estado. Versiones, ABI y rutas pueden fallar aunque el fuente sea correcto. Empaquetado es parte del contrato.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md):

La CLI diagnóstica mantiene `duration_ms` como número no negativo y `outcome` como texto de un conjunto validado. La entrada textual se convierte una sola vez. El informe conserva la unidad en el nombre y en JSON para impedir que una persona trate 800 ms como 800 s.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **compilar = desplegar** — causa: enlace, carga y dependencias omitidos. Corrección: inventaría artefactos y runtime. ([SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md)) son: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas. Los tipos incorporados no expresan todas las reglas del dominio ni eliminan precisión finita. La siguiente clase usa condiciones para elegir comportamiento sin perder casos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Anfitrión](../a/anfitrion.md), [Artefacto](../a/artefacto.md), [Función](../f/funcion.md), [Importación](../i/importacion.md), [AOT](../a/aot.md), [AST](../a/ast.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (91 clases más lo mencionan; las que más):

[SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), [SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md), [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), [SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md).

**Aparece en los casos de estudio:** [Slack](../../../casos/exito/slack.md), [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Linker».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Engineering Manager](./engineering-manager.md) · [Enlace de salto →](./enlace-de-salto.md)
