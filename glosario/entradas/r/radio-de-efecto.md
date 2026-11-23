# Radio de efecto

[↑ Glosario](../../README.md) · [← Radio de daño](./radio-de-dano.md) · [Radio de explosión →](./radio-de-explosion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Recursos, personas o procesos que un cambio puede afectar.

Definición de trabajo de [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md).

## Por qué importa

En [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md), el tema «Cambio mínimo» importa porque limita variables y radio de efecto

## Cómo funciona

[SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md):

Una dependencia incompatible aparece después de corregir configuración. El equipo no deshace la primera conclusión: registra dos causas encadenadas, aísla la versión por proyecto y prueba ambos escenarios por separado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md)) son:

- **Se borra y reinstala al comienzo** — causa: se destruyó evidencia antes de formular hipótesis. Corrección: capturar y reproducir primero.
- **Varias cosas cambian a la vez** — causa: no puede atribuirse el resultado. Corrección: un cambio mínimo, medir y revertir si no explica.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md)) son: El escenario es local, deliberadamente controlado y no autoriza intervenir equipos de terceros. La clase final convierte el procedimiento en un producto pequeño: el kit de diagnóstico multiplataforma, con contrato, adaptadores, pruebas y entrega profesional.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Proceso](../p/proceso.md), [Recurso](./recurso.md), [Cambio mínimo](../c/cambio-minimo.md), [Estado inicial](../e/estado-inicial.md), [Hipótesis discriminante](../h/hipotesis-discriminante.md), [Hipótesis rival](../h/hipotesis-rival.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — Sysinternals documentation](https://learn.microsoft.com/sysinternals/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [systemd manual pages](https://www.freedesktop.org/software/systemd/man/latest/) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Python documentation — subprocess](https://docs.python.org/3/library/subprocess.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Radio de daño](./radio-de-dano.md) · [Radio de explosión →](./radio-de-explosion.md)
