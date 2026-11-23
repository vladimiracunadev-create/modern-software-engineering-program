# Equivalencia semántica

[↑ Glosario](../../README.md) · [← Equivalencia funcional](./equivalencia-funcional.md) · [Ergonomía y carga →](./ergonomia-y-carga.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Mismo resultado observable dentro de límites declarados.

Definición de trabajo de [SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md).

## Por qué importa

La clase donde se define, [SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md), existe con este propósito: la clase existe para preservar intención al portar scripts entre PowerShell y Bash.

## Cómo funciona

[SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md):

Una herramienta corporativa necesita inventariar versión en tres sistemas. Cada adaptador consulta una fuente estable, normaliza una versión y reporta `unavailable` cuando la política bloquea acceso. El tablero no confunde desconocido con versión cero.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md)) son:

- **Se parsean columnas coloreadas** — causa: se confundió presentación humana con interfaz. Corrección: usar salida estructurada o API estable.
- **PowerShell y Bash “pasan” casos distintos** — causa: no existe contrato compartido. Corrección: definir fixtures y aserciones semánticas comunes.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md)) son: No buscamos cubrir toda la sintaxis ni producir scripts idénticos. Aún falta decidir cómo ambos adaptadores reciben configuración sin convertir el entorno o los logs en un almacén de secretos; ese es el foco siguiente.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Límite declarado](../l/limite-declarado.md), [Límite](../l/limite.md), [Resultado](../r/resultado.md), [Adaptador](../a/adaptador.md), [Contrato](../c/contrato.md), [Degradación](../d/degradacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GNU Bash Reference Manual 5.3](https://www.gnu.org/software/bash/manual/) — documenta parsing, expansión, quoting, pipelines y estado de salida en Bash.
- [Microsoft Learn — About PowerShell](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Microsoft Learn — about_Automatic_Variables](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_automatic_variables) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [The Open Group — Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.

---

[↑ Glosario](../../README.md) · [← Equivalencia funcional](./equivalencia-funcional.md) · [Ergonomía y carga →](./ergonomia-y-carga.md)
