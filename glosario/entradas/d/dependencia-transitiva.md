# Dependencia transitiva

[↑ Glosario](../../README.md) · [← Dependencia sin soporte](./dependencia-sin-soporte.md) · [Dependencias de proyecto y herramientas →](./dependencias-de-proyecto-y-herramientas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Paquete que un proyecto usa indirectamente a través de otro.

Definición de trabajo de [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md): Pieza que otra dependencia necesita, directa o indirectamente.
- En [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md): Componente requerido a través de otra dependencia.

## Por qué importa

En [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md), el tema «Dependencias transitivas» importa porque las obligaciones llegan por la cadena completa, no solo por lo que se declara.

## Cómo funciona

Según [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md), en la sección «Dependencias transitivas»:

Un proyecto usa unas decenas de paquetes directos que arrastran cientos. Cada uno tiene su licencia y las obligaciones se acumulan. Mirar solo las directas deja fuera casi todo. El inventario debe recorrer el grafo completo y registrar tres estados distintos: licencia reconocida y permitida, reconocida y no permitida, y no declarada o ilegible, que es un resultado que exige revisión y no una aprobación.

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

- **Prerrequisito:** las clases previas [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Dependencia](./dependencia.md), [Paquete](../p/paquete.md), [Alcance](../a/alcance.md), [Copyleft](../c/copyleft.md), [Expresión de licencia](../e/expresion-de-licencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Dependencias transitivas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SPDX: expresiones de licencia](https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/) — sintaxis de las expresiones; autoridad: especificación SPDX.
- [SPDX License List](https://spdx.org/licenses/) — identificadores y excepciones reconocidos; autoridad: proyecto SPDX.
- [REUSE specification](https://reuse.software/spec/) — declaración de licencias por archivo; autoridad: REUSE.
- [Open Source Definition](https://opensource.org/osd) — criterios de una licencia de código abierto; autoridad: Open Source Initiative.
- [Choose a License](https://choosealicense.com/) — comparación didáctica de licencias; autoridad: GitHub.

---

[↑ Glosario](../../README.md) · [← Dependencia sin soporte](./dependencia-sin-soporte.md) · [Dependencias de proyecto y herramientas →](./dependencias-de-proyecto-y-herramientas.md)
