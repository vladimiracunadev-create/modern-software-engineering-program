# Matriz real

[↑ Glosario](../../README.md) · [← Matriz defecto por prueba](./matriz-defecto-por-prueba.md) · [Mayoría absoluta →](./mayoria-absoluta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Registro que diferencia diseñado, ejecutado, aprobado y no soportado.

Definición de trabajo de [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md).

## Por qué importa

La clase donde se define, [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), existe con este propósito: la clase existe para entregar un kit de diagnóstico multiplataforma que observe sin alterar innecesariamente.

## Cómo funciona

Según [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md):

Las pruebas específicas de plataforma se etiquetan. Un workflow que no ejecuta macOS no prueba macOS; el README muestra matriz real.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md):

Un equipo de soporte recibe un paquete diagnóstico de otra plataforma. La versión del esquema, procedencia de campos y límites le permiten revisar sin pedir el entorno completo. La matriz indica que macOS fue diseñado pero no ejecutado, evitando una promesa falsa.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md)) son:

- **El kit de diagnóstico multiplataforma se convierte en un script de cien comandos** — causa: no existe modelo ni contrato. Corrección: separar capacidades, adaptadores y decisiones.
- **El JSON cambia entre plataformas sin versión** — causa: se mezcló detalle con esquema común. Corrección: versionar esquema y aislar `platform_details`.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un workflow que no ejecuta macOS no prueba macOS; el README muestra matriz real. ([SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](../r/registro.md), [Adaptador](../a/adaptador.md), [Capacidad](../c/capacidad.md), [Contrato versionado](../c/contrato-versionado.md), [Degradación explícita](../d/degradacion-explicita.md), [Hallazgo](../h/hallazgo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — PowerShell documentation](https://learn.microsoft.com/powershell/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [GNU Bash Reference Manual 5.3](https://www.gnu.org/software/bash/manual/) — documenta parsing, expansión, quoting, pipelines y estado de salida en Bash.
- [Microsoft Learn — WSL documentation](https://learn.microsoft.com/windows/wsl/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [OWASP — Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — delimita el contrato técnico que debe cumplirse al entregar un kit de diagnóstico multiplataforma que observe sin alterar innecesariamente.

---

[↑ Glosario](../../README.md) · [← Matriz defecto por prueba](./matriz-defecto-por-prueba.md) · [Mayoría absoluta →](./mayoria-absoluta.md)
