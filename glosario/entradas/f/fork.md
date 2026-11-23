# Fork

[↑ Glosario](../../README.md) · [← Flujos estándar](./flujos-estandar.md) · [Formato columnar →](./formato-columnar.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Copia propia de un repositorio desde la que una persona sin permiso de escritura propone cambios.

Definición de trabajo de [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md).

## Por qué importa

La clase donde se define, [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), existe con este propósito: la clase existe para que abrir un proyecto a personas que no pertenecen al equipo sea una decisión con reglas visibles: cómo se contribuye, quién decide, qué pasa cuando alguien se va y cómo se mantiene al día una copia propia.

## Cómo funciona

Según [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md):

Quien no tiene permiso de escritura trabaja en una copia propia (fork) y propone cambios desde ella. La copia no se actualiza sola: cuando el original avanza, la rama de la persona queda por detrás y, cuanto más se aleja, más probable es que su cambio choque con lo nuevo. Sincronizar es traer los commits del original y rebasar o fusionar. Un proyecto acogedor responde a contribuciones rápido; uno realista asume que algunas necesitarán una actualización.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md):

La plataforma publica `CONTRIBUTING.md` con el entorno, el formato de ramas, la plantilla de PR, el tiempo objetivo de primera respuesta y lo que no se acepta. Una regla de decisión escrita: los cambios pequeños los aprueba una mantenedora; los que modifican una regla de negocio exigen dos aprobaciones y un plazo de 72 horas; los cambios de gobierno exigen consenso. Un indicador mensual muestra cuántas personas cubren la mitad de los commits y qué rutas solo conoce una, para planificar relevos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md)) son:

- **Las contribuciones externas se quedan sin respuesta** — causa: no hay tiempo objetivo ni responsable. Corrección: fijar un tiempo de primera respuesta y rotar quien lo cumple.
- **Los PR externos chocan al revisarse** — causa: la copia se quedó atrás. Corrección: pedir sincronización y ofrecer una guía para hacerla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Quien no tiene permiso de escritura trabaja en una copia propia (fork) y propone cambios desde ella. ([SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Permiso](../p/permiso.md), [Código de conducta](../c/codigo-de-conducta.md), [Concentración de conocimiento](../c/concentracion-de-conocimiento.md), [Consenso perezoso](../c/consenso-perezoso.md), [Regla de decisión](../r/regla-de-decision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: sincronizar un fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) — actualizar una copia con el original; autoridad: GitHub Docs.
- [Open Source Guides: liderazgo y gobernanza](https://opensource.guide/leadership-and-governance/) — estructuras de gobierno habituales; autoridad: Open Source Guides.
- [Apache: proceso de votación](https://www.apache.org/foundation/voting.html) — tipos de voto, consenso y periodos mínimos; autoridad: Apache Software Foundation.
- [PEP 13: modelo de gobierno de Python](https://peps.python.org/pep-0013/) — transición de un líder benevolente a un consejo; autoridad: Python Software Foundation.
- [Contributor Covenant](https://www.contributor-covenant.org/) — código de conducta para comunidades digitales; autoridad: Contributor Covenant.

---

[↑ Glosario](../../README.md) · [← Flujos estándar](./flujos-estandar.md) · [Formato columnar →](./formato-columnar.md)
