# Duplicación de conocimiento

[↑ Glosario](../../README.md) · [← Duplicación accidental](./duplicacion-accidental.md) · [Durabilidad →](./durabilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Misma regla mantenida en varios lugares.

Definición de trabajo de [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md).

## Por qué importa

La clase donde se define, [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md), existe con este propósito: la clase existe para evaluar legibilidad por el costo de comprender y cambiar, no por preferencias estéticas.

## Cómo funciona

Según [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md):

Duplicar una regla permite divergencia; extraerla prematuramente puede unir casos que cambian por razones distintas. Se elimina duplicación de conocimiento, no toda semejanza textual. Estructuras paralelas se presentan con forma y orden consistentes.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md):

La CLI diagnóstica adopta vocabulario del modelo de decisión diagnóstica en código y mensajes. El README define convenciones de unidades y errores. Cada refactor mantiene commits pequeños, pruebas verdes y una explicación de qué cambio futuro facilita.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md)) son:

- **nadie entiende una función de 50 líneas** — causa: mezcla varias responsabilidades en un solo nivel. Corrección: extraer por responsabilidad con nombres que cuenten la historia.
- **un booleano cambia el comportamiento de una función** — causa: función genérica con parámetro bandera. Corrección: dos funciones con nombre específico o un tipo del dominio.

Según [SE-070](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md): En el paquete no hay ventanas de cuatro líneas repetidas, pero «sin duplicación textual» no equivale a «sin duplicación de conocimiento»: la regla «un entero estricto» aparece en `_strict_int` una sola vez, y esa es la forma deseable.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se elimina duplicación de conocimiento, no toda semejanza textual. ([SE-070](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Regla](../r/regla.md), [Abstracción](../a/abstraccion.md), [Caracterización](../c/caracterizacion.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Efecto](../e/efecto.md).
- **Se confunde con:** En el paquete no hay ventanas de cuatro líneas repetidas, pero «sin duplicación textual» no equivale a «sin duplicación de conocimiento»: la regla «un entero estricto» aparece en `_strict_int` una sola vez, y esa es la forma deseable.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Duplicación accidental](./duplicacion-accidental.md) · [Durabilidad →](./durabilidad.md)
