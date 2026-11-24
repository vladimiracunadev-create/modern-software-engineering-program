# Evidencia trazable

[↑ Glosario](../../README.md) · [← Evidencia obsoleta](./evidencia-obsoleta.md) · [Evidencia y umbral →](./evidencia-y-umbral.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

La **evidencia trazable** es la relación verificable entre una afirmación del brief y uno o más registros (citas, datos, observaciones) que existen y la respaldan. Es el sentido de [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) (product brief respaldado por evidencia). La palabra «trazable» importa: no basta decir «los usuarios piden X»; debe poder seguirse el hilo hasta el registro.

## Por qué importa

Cambia qué se acepta como base de una decisión de producto. Según [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), cada afirmación debe poder rastrearse a una evidencia que exista, de más de una persona o fuente. Sin eso, una opinión del equipo se presenta como hallazgo y la decisión se apoya en aire.

## Cómo funciona

[SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) gradúa las afirmaciones por su respaldo: sin evidencia es una **hipótesis**; con una sola persona, una **pista**; con dos o más personas o con un registro, un **hallazgo con límites**. La trazabilidad se comprueba en dos planos. El mecánico: que el identificador de evidencia exista, que haya al menos dos participantes distintos o un registro, que no sea solo lo declarado. Un validador lo hace. El de lectura: que la evidencia diga lo que la afirmación dice. Eso lo hace una persona.

La separación importa porque un validador puede pasar un brief cuya cifra no coincide con la evidencia: solo comprueba estructura. La corrección de la clase es añadir una comparación de cifras con la fuente y una lectura humana antes de decidir. Y la decisión debe tener responsable y fecha, para que alguien responda por ella y pueda revisarse cuando llegue evidencia nueva.

## Ejemplo

En la plataforma de entregas, el brief se acompaña de un expediente: tickets y su agrupación, mapa de actores, transcripciones y códigos, mapa de hipótesis, propuesta, mapa de mercado, plan de experimento, registro de prioridad, protocolo ético, reglas de parada y petición descompuesta. El contrato es que `brief.md` remite a ellos por identificador, que cada afirmación declare sus evidencias y que la decisión indique responsable y fecha.

## Errores y confusiones comunes

- **El brief pasa el validador pero una cifra no coincide.** El validador solo comprueba estructura; añadir comparación con la fuente y lectura humana.
- **La decisión sin responsable ni fecha.** Se redactó como recomendación general; exigirlos en el formato.
- **Contar una persona como hallazgo.** Una sola persona es una pista.
- **Citar la evidencia sin que respalde la frase.** El enlace existe, el contenido no coincide.

## Límites y cuándo no aplica

Que haya evidencia trazable no hace verdadera la conclusión: dos personas pueden coincidir y estar equivocadas. Los experimentos de [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) usan evidencias y participantes sintéticos. Para decisiones reversibles y baratas, el costo de trazar todo puede superar el beneficio; la clase pide el rigor proporcional al costo de equivocarse.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Observación](../o/observacion.md), [Registro](../r/registro.md), [Relación](../r/relacion.md), [Abandono y límites](../a/abandono-y-limites.md), [Brief como contrato de evidencia](../b/brief-como-contrato-de-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — qué producir al terminar la discovery y cómo decidir si avanzar; autoridad: Government Digital Service.
- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — investigación con personas usuarias durante el desarrollo; autoridad: Government Digital Service.
- [Nielsen Norman Group: User Interviews 101](https://www.nngroup.com/articles/user-interviews/) — entrevista de usuario como método cualitativo; autoridad: Nielsen Norman Group.
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — rangos, incertidumbre y valor de la información; autoridad: Hubbard Decision Research.
- [The Menlo Report (U.S. Department of Homeland Security)](https://www.dhs.gov/publication/menlo-report) — principios éticos de la investigación en tecnologías de la información; autoridad: U.S. Department of Homeland Security.

---

[↑ Glosario](../../README.md) · [← Evidencia obsoleta](./evidencia-obsoleta.md) · [Evidencia y umbral →](./evidencia-y-umbral.md)
