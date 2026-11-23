# Expresión

[↑ Glosario](../../README.md) · [← Exposición](./exposicion.md) · [Expresión de licencia →](./expresion-de-licencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Combinación evaluable que produce un valor.

Definición de trabajo de [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md).

## Por qué importa

La clase donde se define, [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md), existe con este propósito: la clase existe para explicar valores, tipos, expresiones y nombres por su semántica y ciclo de vida.

## Cómo funciona

Según [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md):

Una expresión combina literales, nombres, operadores y llamadas para producir un valor. Precedencia decide agrupación, pero paréntesis comunican intención. Operadores pueden tener semántica distinta por tipo: `+` suma números y concatena secuencias. Se evita depender de coerciones imaginadas.

## Ejemplo

Caso medido en la sección «Qué decide el tipo: expresiones ejecutadas» de [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md):

Un valor no lleva su significado escrito: lo decide el tipo del operando y la regla del lenguaje. Se ejecutaron siete expresiones en Python 3.12.9 (Windows 11) y 3.12.3 (Ubuntu 24.04 bajo WSL2) y dieron resultados idénticos. `0.1 + 0.2 == 0.3` es `False` porque un `float` guarda la fracción binaria más cercana, y 0.1 y 0.2 no son exactas en base 2; la suma da `0.30000000000000004`. `bool('false')` es `True` porque `bool` solo pregunta si la cadena está vacía, no qué dice.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md)) son:

- **`0.1 + 0.2 == 0.3` es `False`** — causa: los floats guardan aproximaciones binarias. Corrección: comparar con tolerancia (`math.isclose`) o trabajar con enteros/`Decimal`.
- **`--enabled false` queda activado** — causa: `bool('false')` es `True` (cadena no vacía). Corrección: parser explícito que acepte solo valores documentados.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md)) son: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas. Los tipos incorporados no expresan todas las reglas del dominio ni eliminan precisión finita. La siguiente clase usa condiciones para elegir comportamiento sin perder casos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Combinación](../c/combinacion.md), [Valor](../v/valor.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Efecto](./efecto.md), [Enlace](./enlace.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (81 clases más lo mencionan; las que más):

[SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md), [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md), [SE-536](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md), [SE-578](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md), [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), [SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md).

**Aparece en los casos de estudio:** [Cloudflare](../../../casos/exito/cloudflare.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Exposición](./exposicion.md) · [Expresión de licencia →](./expresion-de-licencia.md)
