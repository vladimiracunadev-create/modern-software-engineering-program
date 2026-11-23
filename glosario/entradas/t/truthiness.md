# Truthiness

[↑ Glosario](../../README.md) · [← Trunk-based development](./trunk-based-development.md) · [Tubería →](./tuberia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Regla que convierte valores a contexto booleano.

Definición de trabajo de [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md).

## Por qué importa

La clase donde se define, [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md), existe con este propósito: la clase existe para diseñar control de flujo desde decisiones del dominio y caminos verificables.

## Cómo funciona

Según [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md):

`if` evalúa truthiness, que considera falsos `0`, `None` y colecciones vacías. Esa conveniencia puede mezclar ausencia, cero válido y lista sin elementos. En reglas de dominio se prefieren comparaciones explícitas para que el lector sepa qué caso se trata.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md):

La CLI diagnóstica separa validación de clasificación. Una duración inválida genera `INPUT_INVALID`; un fallo de protocolo conserva su categoría; solo resultados `ok` se comparan con presupuesto. Así las métricas no cuentan errores de datos como degradación real.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md)) son:

- **clases mal asignadas justo en el límite** — causa: `<=` y `<` intercambiados, sin prueba de frontera. Corrección: probar ambos lados de cada umbral.
- **`if budget:` responde igual con 0 y con `None`** — causa: verdad de Python mezcla ausencia y cero. Corrección: comparar con `is None` y con 0 por separado.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md)) son: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas. Las ramas secuenciales no modelan bien procesos largos ni estados concurrentes. La siguiente clase repite transformaciones sobre colecciones y estructuras.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Contextos](../c/contextos.md), [Regla](../r/regla.md), [Valor](../v/valor.md), [Condición](../c/condicion.md), [Contrato](../c/contrato.md), [Control](../c/control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Trunk-based development](./trunk-based-development.md) · [Tubería →](./tuberia.md)
