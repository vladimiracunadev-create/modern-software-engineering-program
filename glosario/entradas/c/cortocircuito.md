# Cortocircuito

[↑ Glosario](../../README.md) · [← Corte vertical](./corte-vertical.md) · [Cosechar ahora, descifrar después →](./cosechar-ahora-descifrar-despues.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Evaluación que omite operandos innecesarios.

Definición de trabajo de [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md).

## Por qué importa

La clase donde se define, [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md), existe con este propósito: la clase existe para diseñar control de flujo desde decisiones del dominio y caminos verificables.

## Cómo funciona

Según [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md), en la sección «Cortocircuito»:

`and` deja de evaluar al encontrar falso y `or` al encontrar verdadero; además devuelven operandos, no siempre `bool`. El cortocircuito permite comprobar `value is not None and value >= 0`, pero no debe esconder una llamada con efectos en la segunda condición.

## Ejemplo

Caso medido en la sección «Cortocircuito» de [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md):

`and` deja de evaluar al encontrar falso y `or` al encontrar verdadero; además devuelven operandos, no siempre `bool`. El cortocircuito permite comprobar `value is not None and value >= 0`, pero no debe esconder una llamada con efectos en la segunda condición.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`AttributeError` solo con ciertos datos** — causa: guarda en orden inverso, sin cortocircuito protector. Corrección: poner primero la comprobación `is not None`. ([SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El cortocircuito permite comprobar `value is not None and value >= 0`, pero no debe esconder una llamada con efectos en la segunda condición. ([SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Evaluación](../e/evaluacion.md), [Operando](../o/operando.md), [Condición](./condicion.md), [Contrato](./contrato.md), [Control](./control.md), [Efecto](../e/efecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Corte vertical](./corte-vertical.md) · [Cosechar ahora, descifrar después →](./cosechar-ahora-descifrar-despues.md)
