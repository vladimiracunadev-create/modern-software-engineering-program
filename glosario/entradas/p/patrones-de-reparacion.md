# Patrones de reparación

[↑ Glosario](../../README.md) · [← Patrón oscuro](./patron-oscuro.md) · [Pause →](./pause.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Movimientos repetibles para volver verificable una frase: cuantificar, acotar, condicionar y separar.

Definición de trabajo de [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md).

## Por qué importa

En [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), el tema «Patrones de reparación» importa porque ofrecen movimientos repetibles para convertir adjetivos en criterios.

## Cómo funciona

Según [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), en la sección «Patrones de reparación»:

Hay cuatro movimientos recurrentes. Cuantificar: sustituir un adjetivo por un número con unidad («rápido» por «p95 ≤ 1 500 ms»). Acotar: decir bajo qué carga o entorno («con 200 usuarios concurrentes»). Condicionar: separar el estímulo de la respuesta («cuando la sesión expira…»). Separar: dividir una frase con varios compromisos en requisitos singulares. Estos movimientos no inventan el valor: lo toman de una necesidad, una norma o una medición previa. Un número sin origen es una decisión que nadie tomó.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md):

La reparación de un requisito, con su procedimiento y la decisión sobre lo que no se repara:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md)) son:

- **Se repara una frase con una cifra y nadie sabe de dónde salió** — causa: el número no tiene origen. Corrección: registrar la necesidad o la medición de la que proviene y marcarlo como hipótesis si falta.
- **La prueba pasa y las personas siguen quejándose** — causa: la reparación mide un proxy de lo que importa. Corrección: validar con personas el umbral y revisar si el proxy refleja la necesidad.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): el cálculo y la regla con salidas idénticas y la medición de latencia con tiempos propios de cada sistema. Las frases, las reparaciones y las etiquetas son del autor, la regla se ajustó viendo los diez primeros enunciados, el servidor es trivial y no se probó con personas.

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
