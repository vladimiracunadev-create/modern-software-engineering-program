# Chaining

[↑ Glosario](../../README.md) · [← Certificado](./certificado.md) · [Chaos & Resilience Engineer →](./chaos-resilience-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Vínculo causal entre excepciones.

Definición de trabajo de [SE-065 — Errores, excepciones y resultados explícitos](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md).

## Por qué importa

La clase donde se define, [SE-065 — Errores, excepciones y resultados explícitos](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md), existe con este propósito: la clase existe para distinguir error esperado, excepción, resultado explícito y fallo irrecuperable.

## Cómo funciona

[SE-065 — Errores, excepciones y resultados explícitos](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-065 — Errores, excepciones y resultados explícitos](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md):

La CLI diagnóstica devuelve código 2 para uso inválido, 3 para archivo no accesible y 1 para diagnóstico con fallo, reservando 0 para ejecución válida. `stderr` explica el error; `stdout` conserva salida parseable. Los errores internos mantienen traceback en modo debug.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-065 — Errores, excepciones y resultados explícitos](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md)) son:

- **el programa no responde a Ctrl+C** — causa: `except:` o `except BaseException:` captura `KeyboardInterrupt`. Corrección: capturar clases concretas; `Exception` solo en el borde.
- **un error desaparece sin rastro** — causa: `except …: pass` o `return` dentro de `finally`. Corrección: manejar solo lo recuperable y registrar o relanzar.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-065 — Errores, excepciones y resultados explícitos](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md)) son: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas. La taxonomía no evita todos los defectos ni reemplaza logs seguros. La siguiente clase representa múltiples observaciones y sus transformaciones.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Excepción](../e/excepcion.md), [Contrato](./contrato.md), [Control](./control.md), [Efecto](../e/efecto.md), [Manejador](../m/manejador.md), [Mantenimiento](../m/mantenimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-065 — Errores, excepciones y resultados explícitos](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — documenta ownership, tipos de error, traits y concurrencia usados como contraste semántico.

---

[↑ Glosario](../../README.md) · [← Certificado](./certificado.md) · [Chaos & Resilience Engineer →](./chaos-resilience-engineer.md)
