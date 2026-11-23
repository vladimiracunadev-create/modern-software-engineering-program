# Tipo

[↑ Glosario](../../README.md) · [← Timeout](./timeout.md) · [Tipo de programa →](./tipo-de-programa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Conjunto de valores y operaciones asociadas.

Definición de trabajo de [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md).

## Por qué importa

En [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md), el tema «valor» importa porque ¿qué representa y qué tipo tiene?

## Cómo funciona

Según [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md):

Un valor es información concreta interpretada según un tipo: `800`, `800.0` y `'800'` no son intercambiables. Enteros de Python tienen precisión arbitraria práctica limitada por memoria; `float` aproxima números binarios y no representa exactamente muchos decimales. Unidades y dominio no vienen incluidos en el tipo incorporado.

Según [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md):

Prueba el parser con `budget: true`. Predice el resultado antes de ejecutarlo, ejecútalo con `python -m diagnostic_cli` y observa `invalid_budget` y el código de salida 3. Después sustituye en una copia `type(value) is int` por `isinstance(value, int)` y repite: el JSON `true` pasa como presupuesto 1 y el informe sale con un estado que parece válido. La prueba `test_parse_rejects_boolean_budget_without_silent_integer_coercion` falla en la copia modificada; es el único guardián de esa regla. Registra la causa (`bool` es subtipo de `int`), la regla que debe permanecer (tipo exacto) y la prueba de regresión.

## Ejemplo

Ejemplo de [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md) (sección «Ejemplo mínimo»):

Evalúa `0.1 + 0.2`, `bool('false')`, `3 / 2`, `3 // 2` y `'3' * 2`. Antes de ejecutar predice valor y tipo; después explica qué interpretación sería peligrosa en la CLI diagnóstica.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md)) son:

- **`0.1 + 0.2 == 0.3` es `False`** — causa: los floats guardan aproximaciones binarias. Corrección: comparar con tolerancia (`math.isclose`) o trabajar con enteros/`Decimal`.
- **`--enabled false` queda activado** — causa: `bool('false')` es `True` (cadena no vacía). Corrección: parser explícito que acepte solo valores documentados.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Unidades y dominio no vienen incluidos en el tipo incorporado. ([SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Conjunto](../c/conjunto.md), [Operación](../o/operacion.md), [Valor](../v/valor.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Efecto](../e/efecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (364 clases más lo mencionan; las que más):

[SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md), [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Timeout](./timeout.md) · [Tipo de programa →](./tipo-de-programa.md)
