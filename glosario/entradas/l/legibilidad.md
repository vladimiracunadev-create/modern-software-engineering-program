# Legibilidad

[↑ Glosario](../../README.md) · [← Legacy Modernization Engineer](./legacy-modernization-engineer.md) · [Lenguaje ubicuo →](./lenguaje-ubicuo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Facilidad para reconstruir intención y comportamiento.

Definición de trabajo de [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md).

## Por qué importa

La clase donde se define, [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md), existe con este propósito: la clase existe para evaluar legibilidad por el costo de comprender y cambiar, no por preferencias estéticas.

## Cómo funciona

Según [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md):

**Cómo leer la figura.** Compara cada fila entre «antes» y «después»; las tres últimas muestran que el comportamiento observable no cambió. **Dónde deja de valer:** el refactor se aplicó a una copia temporal y no se incluyó en el laboratorio; no se midió legibilidad con personas, solo métricas y pruebas. Que dos números bajen no prueba que el código sea más claro.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md):

La CLI diagnóstica adopta vocabulario del modelo de decisión diagnóstica en código y mensajes. El README define convenciones de unidades y errores. Cada refactor mantiene commits pequeños, pruebas verdes y una explicación de qué cambio futuro facilita.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md)) son:

- **nadie entiende una función de 50 líneas** — causa: mezcla varias responsabilidades en un solo nivel. Corrección: extraer por responsabilidad con nombres que cuenten la historia.
- **un booleano cambia el comportamiento de una función** — causa: función genérica con parámetro bandera. Corrección: dos funciones con nombre específico o un tipo del dominio.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el refactor se aplicó a una copia temporal y no se incluyó en el laboratorio; no se midió legibilidad con personas, solo métricas y pruebas. ([SE-070](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Intención](../i/intencion.md), [Abstracción](../a/abstraccion.md), [Caracterización](../c/caracterizacion.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Duplicación de conocimiento](../d/duplicacion-de-conocimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-071](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), [SE-106](../../../classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md), [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md), [SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Legacy Modernization Engineer](./legacy-modernization-engineer.md) · [Lenguaje ubicuo →](./lenguaje-ubicuo.md)
