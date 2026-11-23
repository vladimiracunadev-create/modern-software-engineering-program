# Dry-run

[↑ Glosario](../../README.md) · [← Driver arquitectónico](./driver-arquitectonico.md) · [Dunning →](./dunning.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Modo que valida y explica sin aplicar efectos.

Definición de trabajo de [SE-072 — Proyecto: herramienta de línea de comandos probada](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md).

## Por qué importa

La clase donde se define, [SE-072 — Proyecto: herramienta de línea de comandos probada](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md), existe con este propósito: la clase existe para integrar CLI, validación, archivos, pruebas y diagnóstico en una herramienta reproducible.

## Cómo funciona

Según [SE-072 — Proyecto: herramienta de línea de comandos probada](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md):

La CLI diagnóstica acepta un paquete del modelo de decisión diagnóstica, genera recomendación y explica cobertura/costo. `--dry-run` valida sin escribir; JSON va a stdout y diagnóstico a stderr. La entrega incluye 12+ pruebas, fixtures pequeños, README y evidencia reproducible en Windows y Unix o una matriz honesta de lo no ejecutado.

## Ejemplo

Ejemplo de [SE-072 — Proyecto: herramienta de línea de comandos probada](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md) (sección «Ejemplo profesional»):

La CLI diagnóstica acepta un paquete del modelo de decisión diagnóstica, genera recomendación y explica cobertura/costo. `--dry-run` valida sin escribir; JSON va a stdout y diagnóstico a stderr. La entrega incluye 12+ pruebas, fixtures pequeños, README y evidencia reproducible en Windows y Unix o una matriz honesta de lo no ejecutado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-072 — Proyecto: herramienta de línea de comandos probada](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md)) son:

- **el consumidor falla al leer stdout** — causa: mensajes de diagnóstico mezclados con los datos. Corrección: stdout solo datos; stderr solo diagnóstico.
- **un script no distingue un uso incorrecto de un rechazo del dominio** — causa: todos los fallos devuelven el mismo código. Corrección: códigos distintos y documentados.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-072 — Proyecto: herramienta de línea de comandos probada](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md)) son: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas. El proyecto demuestra fundamentos y un contrato local; no publica paquete, no ejecuta diagnósticos reales ni certifica seguridad productiva. La [Parte 6](../../../classes/part-06-paradigmas-de-programacion/README.md) comparará paradigmas para evolucionar el mismo comportamiento.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Efecto](../e/efecto.md), [CLI](../c/cli.md), [Código de salida](../c/codigo-de-salida.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Mantenimiento](../m/mantenimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-072 — Proyecto: herramienta de línea de comandos probada](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md), [SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python `argparse` documentation](https://docs.python.org/3/library/argparse.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python `unittest` documentation](https://docs.python.org/3/library/unittest.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python `json` documentation](https://docs.python.org/3/library/json.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python `pathlib` documentation](https://docs.python.org/3/library/pathlib.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Driver arquitectónico](./driver-arquitectonico.md) · [Dunning →](./dunning.md)
