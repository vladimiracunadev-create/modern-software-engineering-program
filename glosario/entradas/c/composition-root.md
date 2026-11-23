# Composition root

[↑ Glosario](../../README.md) · [← Composite](./composite.md) · [Comprensión →](./comprension.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Punto donde se ensamblan colaboradores.

Definición de trabajo de [SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md).

## Por qué importa

La clase donde se define, [SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md), existe con este propósito: la clase existe para separar módulos por responsabilidades y contratos estables, no por tamaño de archivo.

## Cómo funciona

[SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md):

La CLI diagnóstica expone `choose_next` como interfaz de dominio, estable y sin efectos. La CLI convierte excepciones de frontera a códigos de salida. Los módulos no imprimen al importarse y el paquete puede ejecutarse con `python -m diagnostic_cli`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md)) son:

- **`ImportError: partially initialized module`** — causa: importación circular con `from … import`. Corrección: extraer lo común a un tercer módulo o invertir la dependencia.
- **`import json` ejecuta código propio** — causa: un archivo `json.py` local sombrea la biblioteca estándar. Corrección: renombrar el archivo y usar `python -I` en infraestructura.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md)) son: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas. Modularidad no garantiza buena API ni compatibilidad futura. La próxima clase usa ejemplos como pruebas tempranas para presionar el diseño.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Adaptador](../a/adaptador.md), [Contrato](./contrato.md), [Control](./control.md), [Dependencia](../d/dependencia.md), [Efecto](../e/efecto.md), [Interfaz](../i/interfaz.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial — Modules](https://docs.python.org/3/tutorial/modules.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Composite](./composite.md) · [Comprensión →](./comprension.md)
