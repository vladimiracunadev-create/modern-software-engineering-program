# Daño, retiro y revisión

[↑ Glosario](../../README.md) · [← Daño](./dano.md) · [Dark pattern →](./dark-pattern.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Evaluación previa de los daños posibles, criterio para detener la actividad y revisión por una persona ajena al equipo.

Definición de trabajo de [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md).

## Por qué importa

En [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), el tema «Daño, retiro y revisión» importa porque la ética no termina en el consentimiento: hay que anticipar quién puede salir perjudicado y poder detenerse.

## Cómo funciona

Según [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), en la sección «Daño, retiro y revisión»:

Antes de empezar se pregunta qué daño puede causar la actividad (revelar una nota baja, exponer a alguien ante su docente, inducir una conducta) y a quién; qué grupos cargan con el riesgo y cuáles reciben el beneficio (justicia); y qué señal detiene la actividad. Una revisión por alguien ajeno al equipo detecta lo que el equipo no ve. La honestidad con los participantes —incluida la explicación posterior de pruebas como una puerta falsa o un mago de Oz (`SE-127`)— es parte del protocolo, no un adorno.

## Ejemplo

Caso medido en la sección «Daño, retiro y revisión» de [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md):

Antes de empezar se pregunta qué daño puede causar la actividad (revelar una nota baja, exponer a alguien ante su docente, inducir una conducta) y a quién; qué grupos cargan con el riesgo y cuáles reciben el beneficio (justicia); y qué señal detiene la actividad. Una revisión por alguien ajeno al equipo detecta lo que el equipo no ve. La honestidad con los participantes —incluida la explicación posterior de pruebas como una puerta falsa o un mago de Oz (`SE-127`)— es parte del protocolo, no un adorno.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md)) son:

- **Un revisor identifica a una persona en una tabla sin nombres** — causa: se combinaron cuasi-identificadores que la hacían única. Corrección: medir k mínimo, generalizar o suprimir y no publicar combinaciones con k menor que el umbral.
- **Los identificadores con hash se recuperan con un script corto** — causa: hash sin clave sobre un espacio pequeño. Corrección: usar HMAC con clave guardada aparte o identificadores aleatorios sin relación con el original.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2); los resultados fueron idénticos salvo los tiempos de hash, que se informan como medidas de un solo equipo. No se recogieron datos de personas, no se consultó a un comité ético ni a un especialista legal, y la normativa aplicable depende del lugar del proyecto. La siguiente clase define cuándo una investigación debe detenerse.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actividad](../a/actividad.md), [Daño](./dano.md), [Evaluación](../e/evaluacion.md), [Revisión](../r/revision.md), [Consentimiento y finalidad](../c/consentimiento-y-finalidad.md), [Identificabilidad](../i/identificabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Menlo Report (U.S. Department of Homeland Security)](https://www.dhs.gov/publication/menlo-report) — principios éticos para la investigación en tecnologías de la información; autoridad: U.S. Department of Homeland Security.
- [Reglamento (UE) 2016/679 (RGPD)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — minimización, limitación de la conservación, seudonimización y consentimiento; autoridad: Unión Europea.
- [U.S. eCFR, 45 CFR Part 46: Protection of Human Subjects](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-50) — normas federales de protección de sujetos humanos, incluido el consentimiento informado; autoridad: Electronic Code of Federal Regulations.
- [Sweeney: Simple Demographics Often Identify People Uniquely](https://dataprivacylab.org/projects/identifiability/paper1.pdf) — identificación única a partir de pocos atributos demográficos; autoridad: Data Privacy Lab, Carnegie Mellon University.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — marco para gestionar el riesgo de privacidad; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Daño](./dano.md) · [Dark pattern →](./dark-pattern.md)
