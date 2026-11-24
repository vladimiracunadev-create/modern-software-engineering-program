# Matriz de soporte

[↑ Glosario](../../README.md) · [← Matriz de pruebas](./matriz-de-pruebas.md) · [Matriz defecto por prueba →](./matriz-defecto-por-prueba.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Una **matriz de soporte** es la tabla de plataformas, versiones y escenarios realmente probados ([SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md)). [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md) precisa lo esencial: separa las plataformas **objetivo** de los escenarios **efectivamente probados**. La diferencia es la información útil: una plataforma puede ser «objetivo» sin que nadie la haya probado, y entonces el soporte es una intención.

## Por qué importa

«Compatible» sin evidencia es un adjetivo. Una matriz publicada dice a quien usa el producto qué puede esperar y dice al equipo dónde falta cobertura. [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) muestra el error contrario: llamar «compatible» a lo que solo inicia el shell, sin verificar las capacidades subyacentes. Cambia qué se promete y qué se prueba en integración continua.

## Cómo funciona

La matriz cruza ejes que importan al producto: sistema operativo, versión, arquitectura, intérprete o runtime, y escenarios (instalación limpia, actualización, política corporativa restrictiva). Cada celda tiene un estado con su evidencia: probada y pasa, probada y falla, no probada. En el proyecto de kit de diagnóstico multiplataforma ([SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md)), la matriz acompaña a los adaptadores: cada adaptador declara qué capacidades ofrece y la matriz registra en qué combinaciones se ejecutó la suite. La celda «no probada» es explícita: no se rellena por analogía.

La causa de que sea útil es que la compatibilidad no se hereda: que algo funcione en Linux no dice nada de Windows, ni de una versión distinta del intérprete.

## Ejemplo

```text
| Plataforma     | Intérprete | Instalación | Diagnóstico | Estado           |
| Ubuntu 24.04   | 3.12       | probada     | probada     | soportada        |
| Windows 11     | 3.12       | probada     | probada     | soportada        |
| macOS 14       | 3.12       | no probada  | no probada  | objetivo, sin evidencia |
```

La fila de macOS dice la verdad: es objetivo, pero no hay evidencia, por lo que no se anuncia como soportada.

## Errores y confusiones comunes

- **«Compatible» significa que el shell inicia.** Causa: no se verificaron las capacidades subyacentes; corrección: publicar y probar una matriz de soporte ([SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md)).
- **Copiar la matriz de otro producto.** Cada producto depende de capacidades distintas.
- **Matriz sin fecha ni versión.** Queda desactualizada y deja de ser una afirmación verificable.

## Límites y cuándo no aplica

Una matriz crece combinatoriamente: no se pueden probar todas las combinaciones, así que se escoge un subconjunto con criterio y se declara. Pasar en cada celda no prueba ausencia de defectos. Y [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) advierte que no busca cubrir toda la sintaxis ni producir scripts idénticos en cada shell: la matriz documenta lo probado, no lo que debería funcionar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Escenario](../e/escenario.md), [Plataforma](../p/plataforma.md), [Versión](../v/version.md), [Adaptador](../a/adaptador.md), [Capacidad](../c/capacidad.md), [Contrato](../c/contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GNU Bash Reference Manual 5.3](https://www.gnu.org/software/bash/manual/) — documenta parsing, expansión, quoting, pipelines y estado de salida en Bash.
- [Microsoft Learn — About PowerShell](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Microsoft Learn — about_Automatic_Variables](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_automatic_variables) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [The Open Group — Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.

---

[↑ Glosario](../../README.md) · [← Matriz de pruebas](./matriz-de-pruebas.md) · [Matriz defecto por prueba →](./matriz-defecto-por-prueba.md)
