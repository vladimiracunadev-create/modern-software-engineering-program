# Reformulación

[↑ Glosario](../../README.md) · [← Reflujo](./reflujo.md) · [Reformular como problema →](./reformular-como-problema.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Conversión de un requisito no verificable en un objetivo con revisión o en un riesgo aceptado con responsable.

Definición de trabajo de [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md).

## Por qué importa

La clase donde se define, [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), existe con este propósito: el taller existe para practicar el oficio central de la parte: tomar una frase que suena bien («fácil de usar», «nunca perderá un borrador») y devolver un requisito del que se pueda decir, con un procedimiento y un resultado, que se cumple o no, o reconocer que no se puede y reformularlo como objetivo o como riesgo.

## Cómo funciona

[SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) (sección «Caso conductor»):

La plataforma de entregas sigue siendo el caso de la parte. Esta clase añade al expediente diez requisitos reparados con procedimiento, una medición de percentil y la reformulación del «nunca perderá un borrador» como objetivo con tasa. La clase siguiente reúne todo en una especificación revisable (`SE-156`), donde estas reparaciones, el inventario de defectos y la trazabilidad se verifican juntos. Cambia después una sola decisión —por ejemplo, de 10 a 15 minutos en la prueba de uso— y revisa qué procedimientos deben repetirse.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md)) son:

- **Se repara una frase con una cifra y nadie sabe de dónde salió** — causa: el número no tiene origen. Corrección: registrar la necesidad o la medición de la que proviene y marcarlo como hipótesis si falta.
- **La prueba pasa y las personas siguen quejándose** — causa: la reparación mide un proxy de lo que importa. Corrección: validar con personas el umbral y revisar si el proxy refleja la necesidad.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): el cálculo y la regla con salidas idénticas y la medición de latencia con tiempos propios de cada sistema. Las frases, las reparaciones y las etiquetas son del autor, la regla se ajustó viendo los diez primeros enunciados, el servidor es trivial y no se probó con personas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [No verificable](../n/no-verificable.md), [Riesgo aceptado](./riesgo-aceptado.md), [Revisión](./revision.md), [Riesgo](./riesgo.md), [Patrones de reparación](../p/patrones-de-reparacion.md), [Procedimientos de verificación](../p/procedimientos-de-verificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md).

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

[↑ Glosario](../../README.md) · [← Reflujo](./reflujo.md) · [Reformular como problema →](./reformular-como-problema.md)
