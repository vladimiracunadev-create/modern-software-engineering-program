# Contrato versionado

[↑ Glosario](../../README.md) · [← Contrato público](./contrato-publico.md) · [Contrato y corpus de comparación →](./contrato-y-corpus-de-comparacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Interfaz observable cuya evolución se declara.

Definición de trabajo de [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md).

## Por qué importa

En [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), el tema «Contrato versionado» importa porque estabiliza entradas, salidas y estados

## Cómo funciona

[SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md):

Un equipo de soporte recibe un paquete diagnóstico de otra plataforma. La versión del esquema, procedencia de campos y límites le permiten revisar sin pedir el entorno completo. La matriz indica que macOS fue diseñado pero no ejecutado, evitando una promesa falsa.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md)) son:

- **El kit de diagnóstico multiplataforma se convierte en un script de cien comandos** — causa: no existe modelo ni contrato. Corrección: separar capacidades, adaptadores y decisiones.
- **El JSON cambia entre plataformas sin versión** — causa: se mezcló detalle con esquema común. Corrección: versionar esquema y aislar `platform_details`.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md)) son: El kit de diagnóstico multiplataforma es un kit educativo local, no un agente de soporte remoto, herramienta forense ni producto de seguridad certificado. No ejecuta reparaciones privilegiadas. La siguiente parte del programa utilizará este entorno reproducible para estudiar redes: nombres, direcciones, transporte y fallos entre procesos que ya no comparten una sola máquina.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interfaz](../i/interfaz.md), [Adaptador](../a/adaptador.md), [Capacidad](./capacidad.md), [Degradación explícita](../d/degradacion-explicita.md), [Hallazgo](../h/hallazgo.md), [Matriz de soporte](../m/matriz-de-soporte.md).
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

[↑ Glosario](../../README.md) · [← Contrato público](./contrato-publico.md) · [Contrato y corpus de comparación →](./contrato-y-corpus-de-comparacion.md)
