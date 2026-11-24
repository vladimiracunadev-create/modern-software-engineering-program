# Identificabilidad

[↑ Glosario](../../README.md) · [← Identidad federada](./identidad-federada.md) · [Identificador de correlación →](./identificador-de-correlacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

La **identificabilidad** es la posibilidad de distinguir a una persona de otras en un conjunto de datos, directamente o combinando atributos (cuasi-identificadores) ([SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md)). Un dato es identificable no solo si contiene un nombre o un número de documento, sino también si la combinación de sus atributos es lo bastante rara como para señalar a alguien.

## Por qué importa

Varios atributos inocuos, combinados, pueden identificar a una persona; **quitar el nombre no basta**. Cambia cómo se comparten, publican y analizan los datos: una tabla sin nombres puede seguir permitiendo reconocer a una persona a quien la conoce.

## Cómo funciona

[SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) define el **cuasi-identificador**: un atributo que no identifica por sí mismo pero sí junto con otros, como región, rango de edad, rol, dispositivo e idioma. El mecanismo es combinatorio: cada atributo parte el conjunto en grupos más pequeños, y con cuatro o cinco atributos muchos grupos quedan reducidos a una persona.

El **k-anonimato** mide esa propiedad: exige que cada combinación de cuasi-identificadores aparezca en al menos k personas. Si una combinación es única (k = 1), esa persona es reconocible por quien conozca esos atributos. La unicidad **crece rápidamente con el número de atributos** y depende del tamaño del grupo: en una población pequeña (un curso de 30 personas) se identifica con muy pocos atributos.

La defensa es medir y actuar: calcular el **k mínimo** del conjunto, **generalizar** (rangos de edad en lugar de edad exacta, región amplia en lugar de ciudad) o **suprimir** valores raros, y no publicar combinaciones con k menor que el umbral. [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) añade una trampa frecuente: los identificadores con hash se recuperan con un script corto cuando el hash no tiene clave y el espacio de posibles valores es pequeño (se prueban todos los valores y se comparan los hashes). La corrección es usar HMAC con una clave guardada aparte, o identificadores aleatorios sin relación con el original.

[SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) recuerda el mismo principio en contexto de privacidad en el producto: atributos inocuos por separado identifican en conjunto.

## Ejemplo

Una tabla de uso de la plataforma sin nombres con columnas `curso`, `rol`, `rango de edad` e `idioma`. Una fila es la única «docente, 50–59, inglés» del curso de Física. Cualquiera que sepa que hay una única docente de ese perfil la reconoce y ve todo lo demás de su fila. Medido k = 1, se generaliza el curso a «área» o se suprime la fila antes de compartir. (Ilustración del mecanismo de [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md).)

## Errores y confusiones comunes

- **Un revisor identifica a una persona en una tabla sin nombres**: se combinaron cuasi-identificadores; corrección: medir k mínimo, generalizar o suprimir.
- **Hash sin clave de un identificador** de espacio pequeño.
- **Creer que anonimizar es quitar el nombre.**
- **Medir k solo con los atributos publicados**: el atacante puede tener otras fuentes.

## Límites y cuándo no aplica

El k-anonimato no protege contra quien conoce atributos sensibles homogéneos dentro de un grupo ni contra el cruce con fuentes externas ricas. No sustituye una evaluación jurídica de qué es dato personal. Con grupos muy grandes y pocos atributos, el riesgo es menor, pero debe medirse.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cuasi-identificador](../c/cuasi-identificador.md), [Atributo](../a/atributo.md), [Conjunto](../c/conjunto.md), [Consentimiento](../c/consentimiento.md), [Consentimiento y finalidad](../c/consentimiento-y-finalidad.md), [Daño, retiro y revisión](../d/dano-retiro-y-revision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.
- [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md).

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

[↑ Glosario](../../README.md) · [← Identidad federada](./identidad-federada.md) · [Identificador de correlación →](./identificador-de-correlacion.md)
