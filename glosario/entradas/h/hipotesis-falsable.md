# Hipótesis falsable

[↑ Glosario](../../README.md) · [← Hipótesis discriminante](./hipotesis-discriminante.md) · [Hipótesis inductiva →](./hipotesis-inductiva.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Una **hipótesis falsable** es una afirmación sobre el mundo, con un umbral y una regla de decisión fijados antes de observar, que algún resultado posible refutaría ([SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)). [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) la usa en ingeniería del caos: la afirmación de que el estado estable se mantendrá bajo una condición, con una regla que dice qué observación la refuta.

## Por qué importa

Una hipótesis que ninguna observación puede contradecir no orienta ninguna decisión. La falsabilidad distingue una hipótesis de una esperanza. Cambia cómo se diseña una prueba de producto o un experimento: antes de mirar los datos se decide qué resultado haría cambiar de rumbo.

## Cómo funciona

[SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) contrasta dos frases. «Los estudiantes valoran la confirmación de entrega» **no puede fallar**: cualquier resultado se interpreta a favor. «Al menos 6 de cada 10 estudiantes que ven la confirmación no repiten la entrega en 48 horas» **sí puede fallar**: si menos de 6 de cada 10 no repiten, queda refutada. Tiene un **umbral** (6 de 10), una **medida observable** (no repetir en 48 horas) y una **ventana**.

Se completa con la **regla de decisión**: qué se hará si el resultado queda por debajo, por encima o en medio (por ejemplo, construir, descartar o seguir probando). Fijar umbral y regla **antes de observar** evita ajustar el criterio a lo que salió. Y se combina con la incertidumbre: con 4 de 20 y con 40 de 200 la tasa observada es la misma (20 %), pero la certeza no; la clase pide predecir el resultado de ambos con la regla fijada, y la muestra grande es la que permite concluir.

Hay dos errores típicos con su causa. Un piloto que «confirma» la idea y la ampliación no la confirma: la conclusión se sacó de una muestra pequeña sin fijar umbral ni confianza; se corrige declarando de antemano el tamaño, el umbral y la probabilidad exigida, y calculando la posterior. Y el equipo que mide el alcance durante semanas sin avanzar: contrastó el supuesto más cómodo y no el más sensible; se corrige calculando la oscilación de cada supuesto y contrastando primero el de mayor sensibilidad e incertidumbre.

En ingeniería del caos ([SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md)), la hipótesis dice que el estado estable se mantiene bajo una condición (una falla inyectada) y la regla define qué observación (una métrica fuera de rango) la refuta.

## Ejemplo

Hipótesis: «Con la confirmación de entrega visible, al menos el 60 % de las estudiantes no repite la entrega en 48 horas». Regla: con 200 observaciones, si el intervalo del 95 % queda por encima de 55 %, se construye; si queda por debajo de 55 %, se descarta; si lo atraviesa, se amplía la muestra. (Ilustración construida con el estilo de [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md).)

## Errores y confusiones comunes

- **Hipótesis que no puede fallar.**
- **Fijar el umbral después de ver los datos.**
- **Piloto pequeño tomado como confirmación.**
- **Contrastar lo cómodo y no lo sensible.**

## Límites y cuándo no aplica

Falsar una hipótesis no prueba su contraria ni dice por qué falló. En fases muy exploratorias, antes de saber qué medir, conviene primero investigar y luego formular. Un umbral mal elegido hace la hipótesis trivial o inalcanzable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla de decisión](../r/regla-de-decision.md), [Estado estable](../e/estado-estable.md), [Afirmación](../a/afirmacion.md), [Condición](../c/condicion.md), [Banda](../b/banda.md), [Evidencia y umbral](../e/evidencia-y-umbral.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.
- [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Stanford Encyclopedia of Philosophy: Karl Popper](https://plato.stanford.edu/entries/popper/) — falsabilidad como criterio de demarcación; autoridad: Stanford University.
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado y ciclo construir-medir-aprender; autoridad: Eric Ries (fuente del autor).
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — cuantificar la incertidumbre con rangos y valor de la información; autoridad: Hubbard Decision Research.
- [Product Talk: Opportunity Solution Tree](https://www.producttalk.org/opportunity-solution-tree/) — estructura para conectar resultados, oportunidades y experimentos; autoridad: Teresa Torres (fuente del autor).
- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — qué averiguar en una discovery y cómo compartir lo aprendido; autoridad: Government Digital Service.

---

[↑ Glosario](../../README.md) · [← Hipótesis discriminante](./hipotesis-discriminante.md) · [Hipótesis inductiva →](./hipotesis-inductiva.md)
