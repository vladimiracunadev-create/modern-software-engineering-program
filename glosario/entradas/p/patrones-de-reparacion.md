# Patrones de reparación

[↑ Glosario](../../README.md) · [← Patrón oscuro](./patron-oscuro.md) · [Pause →](./pause.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Los **patrones de reparación** son movimientos repetibles para volver verificable una frase de un requisito: cuantificar, acotar, condicionar y separar ([SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md)). Se aplican a requisitos con defectos de ambigüedad, vaguedad o compromiso múltiple.

## Por qué importa

Ofrecen movimientos repetibles para convertir adjetivos en criterios. «Rápido», «fácil» o «seguro» no se pueden probar; reparar la frase con uno o más movimientos la vuelve medible. Cambia la forma de revisar una especificación: no solo se señala el defecto, se propone un procedimiento para repararlo.

## Cómo funciona

[SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) describe **cuatro movimientos recurrentes**:

- **Cuantificar**: sustituir un adjetivo por un número con unidad («rápido» por «p95 ≤ 1.500 ms»).
- **Acotar**: decir bajo qué carga o entorno («con 200 usuarios concurrentes»).
- **Condicionar**: separar el estímulo de la respuesta («cuando la sesión expira…»).
- **Separar**: dividir una frase con varios compromisos en requisitos singulares («guardará y cifrará y avisará» son tres).

Aplicados juntos, «el sistema responderá rápido» pasa a «con 200 usuarios concurrentes, el 95 % de las peticiones de listado responde en 1.500 ms o menos». Los movimientos **no inventan el valor**: lo toman de una necesidad o una medición. Por eso, un número sin origen es un defecto nuevo. La corrección es registrar la necesidad o la medición de la que proviene y, si falta, marcarlo como **hipótesis**.

La reparación se acompaña de un **procedimiento de verificación** que dice cómo se comprobará, y de la decisión sobre lo que **no** se repara (qué se deja deliberadamente informal y por qué). Otro riesgo que la clase señala: la prueba pasa y las personas siguen quejándose porque la reparación mide un proxy de lo que importa; se valida con personas el umbral y se revisa si el proxy refleja la necesidad.

## Ejemplo

Requisito original: «La subida de archivos debe ser rápida y segura». Separar: dos requisitos. Cuantificar y acotar el primero: «con conexión de 10 Mbit/s, un PDF de 10 MB se sube en menos de 12 s en el 95 % de los intentos». Condicionar el segundo: «cuando el archivo tiene una extensión no permitida, el sistema lo rechaza con un mensaje que indica las extensiones aceptadas». Cada uno se puede probar. (Reparación ilustrativa con los movimientos de [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md).)

## Errores y confusiones comunes

- **Cifra sin origen**: nadie sabe de dónde salió; corrección: registrar la necesidad o la medición, o marcarla como hipótesis.
- **La prueba pasa y la gente se queja**: el proxy no refleja la necesidad.
- **Reparar solo la forma**: añadir un número arbitrario para parecer preciso.
- **Aplicar un solo movimiento** donde hacen falta varios.

## Límites y cuándo no aplica

No todo requisito debe cuantificarse: algunos se verifican con inspección o con una prueba con personas y un umbral. Un número impuesto sin respaldo da una falsa precisión. La reparación depende de saber qué importa; si no se conoce la necesidad, primero se investiga.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Acotar](../a/acotar.md), [Procedimientos de verificación](./procedimientos-de-verificacion.md), [Reformulación](../r/reformulacion.md), [Requisitos universales y negativos](../r/requisitos-universales-y-negativos.md), [Verificabilidad](../v/verificabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — características de un buen requisito, entre ellas ser verificable; autoridad: ISO, IEC e IEEE.
- [Mavin et al.: Easy Approach to Requirements Syntax, EARS (2009)](https://doi.org/10.1109/RE.2009.9) — plantillas de redacción; autoridad: IEEE International Requirements Engineering Conference.
- [Hanley y Lippman-Hand: If nothing goes wrong, is everything all right? (1983)](https://doi.org/10.1001/jama.1983.03330370053031) — regla de tres para cero fallos; autoridad: JAMA.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — objetivos con percentil, ventana y medición; autoridad: Google.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — verificación y validación de requisitos; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Patrón oscuro](./patron-oscuro.md) · [Pause →](./pause.md)
