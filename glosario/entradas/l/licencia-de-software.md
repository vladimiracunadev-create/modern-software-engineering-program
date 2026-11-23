# Licencia de software

[↑ Glosario](../../README.md) · [← Ley de Little](./ley-de-little.md) · [Lifecycle y caché →](./lifecycle-y-cache.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Autorización de su titular para usar, copiar, modificar o redistribuir una obra bajo ciertas condiciones.

Definición de trabajo de [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md): Permiso que concede el titular de los derechos para usar, modificar o distribuir un programa bajo condiciones.

## Por qué importa

La clase donde se define, [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md), existe con este propósito: la clase existe para que una persona que usa, publica o recibe código de otras sepa qué licencia gobierna cada pieza, lo compruebe de forma repetible y reconozca cuándo la decisión ya no es técnica y requiere asesoría de alguien competente.

## Cómo funciona

[SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md):

En la plataforma, el `LICENSE` declara la licencia del proyecto, cada archivo de código lleva su etiqueta y un trabajo de integración continua construye el inventario de dependencias directas y transitivas, evalúa sus expresiones con un analizador y falla ante una licencia no permitida; ante una no reconocida o ilegible, abre una revisión con una persona designada. Las decisiones sobre licencias no permitidas pasan a asesoría y se registran con responsable y fecha.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md)) son:

- **Se rechazan dependencias válidas** — causa: comparación literal de texto. Corrección: analizar la expresión con sus operadores.
- **Se aprueban dependencias que no se entendieron** — causa: los avisos no se tratan como pendientes. Corrección: hacer que lo no reconocido exija revisión.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. La lista de identificadores, la política y la mezcla de licencias son del autor, el analizador cubre solo una parte de la gramática y no se interpretó ninguna licencia ni se auditó ningún proyecto; las decisiones con consecuencias jurídicas requieren asesoría.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Autorización](../a/autorizacion.md), [Condición](../c/condicion.md), [Derecho](../d/derecho.md), [Permiso](../p/permiso.md), [Certificación de origen](../c/certificacion-de-origen.md), [Copyleft](../c/copyleft.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md).

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

[↑ Glosario](../../README.md) · [← Ley de Little](./ley-de-little.md) · [Lifecycle y caché →](./lifecycle-y-cache.md)
