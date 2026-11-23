# Huella de texto

[↑ Glosario](../../README.md) · [← Huella de segmentación](./huella-de-segmentacion.md) · [Huella de una falla →](./huella-de-una-falla.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Resumen criptográfico del texto normalizado de una licencia, sensible a cualquier cambio.

Definición de trabajo de [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md).

## Por qué importa

La clase donde se define, [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md), existe con este propósito: la clase existe para que una persona que usa, publica o recibe código de otras sepa qué licencia gobierna cada pieza, lo compruebe de forma repetible y reconozca cuándo la decisión ya no es técnica y requiere asesoría de alguien competente.

## Cómo funciona

[SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md):

En la plataforma, el `LICENSE` declara la licencia del proyecto, cada archivo de código lleva su etiqueta y un trabajo de integración continua construye el inventario de dependencias directas y transitivas, evalúa sus expresiones con un analizador y falla ante una licencia no permitida; ante una no reconocida o ilegible, abre una revisión con una persona designada. Las decisiones sobre licencias no permitidas pasan a asesoría y se registran con responsable y fecha.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md)) son:

- **Se rechazan dependencias válidas** — causa: comparación literal de texto. Corrección: analizar la expresión con sus operadores.
- **Se aprueban dependencias que no se entendieron** — causa: los avisos no se tratan como pendientes. Corrección: hacer que lo no reconocido exija revisión.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. La lista de identificadores, la política y la mezcla de licencias son del autor, el analizador cubre solo una parte de la gramática y no se interpretó ninguna licencia ni se auditó ningún proyecto; las decisiones con consecuencias jurídicas requieren asesoría.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Huella](./huella.md), [Copyleft](../c/copyleft.md), [Dependencia transitiva](../d/dependencia-transitiva.md), [Expresión de licencia](../e/expresion-de-licencia.md), [Licencia de software](../l/licencia-de-software.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SPDX: expresiones de licencia](https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/) — sintaxis de las expresiones; autoridad: especificación SPDX.
- [SPDX License List](https://spdx.org/licenses/) — identificadores y excepciones reconocidos; autoridad: proyecto SPDX.
- [REUSE specification](https://reuse.software/spec/) — declaración de licencias por archivo; autoridad: REUSE.
- [Open Source Definition](https://opensource.org/osd) — criterios de una licencia de código abierto; autoridad: Open Source Initiative.
- [Choose a License](https://choosealicense.com/) — comparación didáctica de licencias; autoridad: GitHub.

---

[↑ Glosario](../../README.md) · [← Huella de segmentación](./huella-de-segmentacion.md) · [Huella de una falla →](./huella-de-una-falla.md)
