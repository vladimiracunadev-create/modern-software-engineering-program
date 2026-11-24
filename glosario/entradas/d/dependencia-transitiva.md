# Dependencia transitiva

[↑ Glosario](../../README.md) · [← Dependencia sin soporte](./dependencia-sin-soporte.md) · [Dependencias de proyecto y herramientas →](./dependencias-de-proyecto-y-herramientas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Una **dependencia transitiva** es un paquete o componente que un proyecto usa indirectamente, a través de otra dependencia ([SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)). [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) la formula como la pieza que otra dependencia necesita, directa o indirectamente. Si el proyecto declara `A` y `A` necesita `B`, entonces `B` es transitiva respecto del proyecto, aunque nadie la haya elegido.

## Por qué importa

Un proyecto usa unas decenas de paquetes directos que arrastran cientos ([SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md)). Lo que no se declara también se ejecuta, se licencia y se ataca. Por eso las decisiones de licencias, vulnerabilidades y reproducibilidad no pueden basarse solo en lo que el equipo escribió en su manifiesto: mirar solo las directas deja fuera casi todo.

## Cómo funciona

El gestor de paquetes resuelve el **grafo completo**: cada paquete declara rangos de versiones de sus dependencias y el resolvedor elige un conjunto compatible. Consecuencias que enseña el programa:

- **Licencias** ([SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md)): las obligaciones se acumulan. El inventario debe recorrer el grafo entero y registrar tres estados distintos: licencia reconocida y permitida, reconocida y no permitida, y no declarada o ilegible. Este último exige revisión; no es una aprobación.
- **Cadena de suministro** ([SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md)): una pieza comprometida o abandonada a cuatro niveles afecta igual que una directa, y el inventario de componentes (SBOM) existe para verlas.
- **Reproducibilidad** ([SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)): sin un archivo de bloqueo (`lockfile`), la resolución puede elegir otras versiones transitivas mañana.

## Ejemplo

[SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) analiza expresiones de licencia con sus operadores. Ilustración con npm:

```bash
npm ls --all        # muestra el árbol completo, directas y transitivas
npm ls left-pad     # ¿quién arrastra este paquete?
```

El equipo descubre que `left-pad` entra por un paquete de formato que usa una dependencia de segundo nivel.

## Errores y confusiones comunes

- **Rechazar dependencias válidas.** Causa: comparación literal de texto de la licencia; corrección: analizar la expresión con sus operadores ([SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md)).
- **Aprobar lo que no se entendió.** Causa: los avisos no se tratan como pendientes; corrección: que lo no reconocido exija revisión ([SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md)).
- **Fijar solo las directas.** Las versiones transitivas siguen moviéndose sin lockfile.

## Límites y cuándo no aplica

Las definiciones de [SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) son operativas para la plataforma de entregas: no se interpretó ninguna licencia ni se auditó ningún proyecto, y las decisiones con consecuencia jurídica requieren asesoría. Un grafo completo muestra qué está, no si es seguro. Y en proyectos con dependencias copiadas al repositorio (vendoring) la distinción directa/transitiva se difumina.

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
