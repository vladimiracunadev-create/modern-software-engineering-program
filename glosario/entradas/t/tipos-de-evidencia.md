# Tipos de evidencia

[↑ Glosario](../../README.md) · [← Tipo de programa](./tipo-de-programa.md) · [Tipos y flujo →](./tipos-y-flujo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Los **tipos de evidencia** son una clasificación de la evidencia según su origen (dijo, hizo, comprometió, registro), con una ponderación explícita y revisable ([SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md)). Se usan al escribir un brief de producto para declarar cuánto pesa cada tipo de respaldo.

## Por qué importa

Lo que alguien hizo o comprometió pesa distinto de lo que dijo, y el brief debe declarar el peso. Sin esa clasificación, diez frases entusiastas pueden parecer más sólidas que dos personas que entregaron un borrador real. Cambia cómo se leen las entrevistas y los datos: no todo respaldo vale lo mismo.

## Cómo funciona

[SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) ordena los tipos por fiabilidad:

- **Dijo**: lo que una persona afirma. Es el tipo **más barato y el menos fiable**.
- **Hizo**: lo que la persona hace (por ejemplo, copia su texto a un documento aparte para no perderlo). Es más fiable, porque es comportamiento observado.
- **Comprometió**: lo que la persona se compromete a hacer o entrega (reserva tiempo, entrega un borrador real). Es **el más fiable** de los tres, porque implica un costo.
- **Registro**: datos de uso o de tickets (42 tickets). Cuenta **frecuencia pero no motivos**.

Al **ponderar**, el orden de las opciones puede cambiar: si una opción acumula muchas frases y otra pocos compromisos, el peso decide cuál sube. Por eso el peso es **una decisión del brief, no un detalle interno**, y se muestra la comparación con distintos pesos, de modo que quien decide vea si la conclusión resiste al cambio.

El mecanismo se conecta con la evidencia trazable: cada afirmación del brief declara sus evidencias y su tipo, y el validador comprueba que el identificador exista y que haya al menos dos personas o un registro; que la evidencia diga lo que la afirmación dice lo comprueba una persona. Y con el experimento de demanda, que busca evidencia de tipo «hizo» y «comprometió» a bajo costo.

## Ejemplo

Afirmación: «los docentes necesitan ver quién no entregó». Evidencia: cinco docentes lo dijeron (dijo); dos copian a mano la lista de entregas a una hoja (hizo); una docente pidió acceso anticipado y reservó una hora para probarlo (comprometió); 42 tickets mensuales piden la lista (registro). La opinión de cinco pesa menos que el compromiso de una; el brief declara los pesos y muestra qué pasa si cambian. (Ilustración de la clasificación de [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md).)

## Errores y confusiones comunes

- **Contar frases como si fueran compromisos.**
- **El brief pasa el validador pero una cifra no coincide con la evidencia**: el validador solo comprueba estructura.
- **Decisión sin responsable ni fecha.**
- **Pesos fijados después de ver el resultado.**

## Límites y cuándo no aplica

La ordenación es una guía, no una ley: un registro bien medido puede ser más fiable que un compromiso aislado. Los pesos son una decisión y deben revisarse. Con muy poca evidencia, ponderar da una falsa precisión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Origen](../o/origen.md), [Registro](../r/registro.md), [Abandono y límites](../a/abandono-y-limites.md), [Brief como contrato de evidencia](../b/brief-como-contrato-de-evidencia.md), [Decisión con rangos](../d/decision-con-rangos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md), [SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md), [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md).

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

[↑ Glosario](../../README.md) · [← Tipo de programa](./tipo-de-programa.md) · [Tipos y flujo →](./tipos-y-flujo.md)
