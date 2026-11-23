# Consentimiento y finalidad

[↑ Glosario](../../README.md) · [← Consentimiento informado](./consentimiento-informado.md) · [Consistencia eventual →](./consistencia-eventual.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Acuerdo informado y libre de una persona a participar, para fines declarados, con la posibilidad real de retirarse.

Definición de trabajo de [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md).

## Por qué importa

En [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), el tema «Consentimiento y finalidad» importa porque sin finalidad declarada y consentimiento revocable, la evidencia se obtiene de personas que no sabían para qué.

## Cómo funciona

Según [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), en la sección «Consentimiento y finalidad»:

Un consentimiento válido dice quién investiga, para qué, qué se recoge, cuánto tiempo se conserva, quién lo verá y cómo retirarse, en un lenguaje que la persona entienda y sin presión (la nota o el acceso a un servicio no pueden depender de participar). La finalidad limita: un dato recogido para entender plazos no se reutiliza para evaluar a la persona. Retirarse debe ser tan fácil como entrar y debe incluir el borrado de lo aportado cuando sea técnicamente posible. El consentimiento no es una casilla: es un proceso que se repite si la finalidad cambia.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md):

En la plataforma de entregas, el protocolo conserva: finalidad, datos recogidos con la decisión que justifica cada uno, base y forma de consentimiento, modo de retirarse, plazos de retención y borrado, quién accede a qué, técnica de seudonimización con ubicación de la clave, medida de unicidad del conjunto que se comparte y revisor externo. El contrato es que ninguna persona pasa a un conjunto compartido sin que el protocolo indique su k mínimo y que la clave de seudonimización se guarde separada de los datos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md)) son:

- **Un revisor identifica a una persona en una tabla sin nombres** — causa: se combinaron cuasi-identificadores que la hacían única. Corrección: medir k mínimo, generalizar o suprimir y no publicar combinaciones con k menor que el umbral.
- **Los identificadores con hash se recuperan con un script corto** — causa: hash sin clave sobre un espacio pequeño. Corrección: usar HMAC con clave guardada aparte o identificadores aleatorios sin relación con el original.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2); los resultados fueron idénticos salvo los tiempos de hash, que se informan como medidas de un solo equipo. No se recogieron datos de personas, no se consultó a un comité ético ni a un especialista legal, y la normativa aplicable depende del lugar del proyecto. La siguiente clase define cuándo una investigación debe detenerse.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Daño, retiro y revisión](../d/dano-retiro-y-revision.md), [Identificabilidad](../i/identificabilidad.md), [Minimización y retención](../m/minimizacion-y-retencion.md), [Seudonimización](../s/seudonimizacion.md).
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

[↑ Glosario](../../README.md) · [← Consentimiento informado](./consentimiento-informado.md) · [Consistencia eventual →](./consistencia-eventual.md)
