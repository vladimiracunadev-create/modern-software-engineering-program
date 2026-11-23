# Problemas

[↑ Glosario](../../README.md) · [← Problema del oráculo](./problema-del-oraculo.md) · [Procedencia →](./procedencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Brecha entre lo que una persona intenta lograr y lo que logra, con una consecuencia observable y una causa que puede investigarse.

Definición de trabajo de [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md).

## Por qué importa

En [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), el tema «Problemas» importa porque un problema es una brecha con consecuencia observable y causa investigable; sin esos tres elementos es una opinión.

## Cómo funciona

Según [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), en la sección «Problemas»:

Un problema se enuncia con un actor, algo que intenta lograr, lo que se lo impide y la consecuencia: «los estudiantes pierden su avance cuando la sesión expira y no pueden recuperarlo». Es investigable cuando existe una observación que lo confirmaría o lo refutaría (por ejemplo, registros de sesiones expiradas con borrador sin guardar). «Los usuarios están insatisfechos» no es un problema sino un estado de ánimo sin actor concreto ni observable. La diferencia importa porque solo un enunciado investigable permite que otra persona llegue a la misma conclusión o la discuta con datos.

## Ejemplo

Ejemplo de [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) (sección «Caso conductor»):

La plataforma de entregas de tareas es el caso conductor de la [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md). Esta clase deja el primer artefacto: tickets sintéticos, causa más frecuente (la expiración de sesión), un enunciado de problema y un rango de oportunidad. Las clases siguientes preguntarán quiénes son las personas afectadas (`SE-122`), qué se sabe de ellas por entrevistas (`SE-123`) y qué hipótesis se pueden contrastar (`SE-124`). Cambia después una sola decisión —por ejemplo, fusionar dos causas— y revisa qué conclusiones del registro cambian.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La reunión discute «la solución» durante una hora sin acordar el problema** — causa: la petición original se aceptó como requisito. Corrección: reformular la petición como necesidad («necesito… para…») antes de proponer opciones. ([SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md))
- **Un enunciado de problema pasa el linter pero nadie lo reconoce como real** — causa: la regla comprueba forma, no existencia. Corrección: pedir a una segunda persona que cite un registro o una observación que confirme el enunciado. ([SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- «Los usuarios están insatisfechos» no es un problema sino un estado de ánimo sin actor concreto ni observable. ([SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Brecha](../b/brecha.md), [Consecuencia](../c/consecuencia.md), [Causa y evidencia](../c/causa-y-evidencia.md), [Necesidades](../n/necesidades.md), [Oportunidades](../o/oportunidades.md), [Síntomas y peticiones](../s/sintomas-y-peticiones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (611 clases más lo mencionan; las que más):

[SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — la discovery empieza reformulando una solución dada como problema por resolver; autoridad: Government Digital Service.
- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — marco oficial para investigar necesidades antes y durante el desarrollo; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) — formato de necesidad de usuario y criterios para validarla; autoridad: Government Digital Service.
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — propone observar el trabajo que la persona intenta hacer antes que sus características demográficas; autoridad: Harvard Business Review (artículo parcialmente de pago).
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — vocabulario para gestionar riesgo de privacidad al recoger datos de personas; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Problema del oráculo](./problema-del-oraculo.md) · [Procedencia →](./procedencia.md)
