# Archivo generado

[↑ Glosario](../../README.md) · [← Archivo de relevo](./archivo-de-relevo.md) · [Archivo huérfano →](./archivo-huerfano.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Código producido desde la especificación que no se edita a mano.

Definición de trabajo de [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md).

## Por qué importa

En [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md), el tema «Archivo generado editado a mano» importa porque sin una marca y una huella, se pierde en la siguiente regeneración.

## Cómo funciona

Según [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md):

Hay cuatro familias de comprobación posibles. La **estructura**: cada regla de la especificación tiene código y prueba que la citan, y nadie cita una regla que no existe. Los **valores declarados**: si la especificación dice que los umbrales son 72, 24 y 1, el código tiene exactamente esos valores. La **procedencia del cambio**: si el código cambió y la especificación no, alguien debe explicarlo. Y la **frescura de lo generado**: el archivo generado coincide con lo que produce hoy la especificación. Las cuatro son baratas y exactas, y no hablan del significado.

Según [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md):

El equipo elige el nivel por componente. Para las reglas de avisos, que fija un acuerdo con la plataforma y cambia poco, opta por spec-anchored: cada regla tiene identificador, el código y las pruebas lo citan, los umbrales viven en la especificación y se leen de ella, y la integración continua ejecuta el comprobador. Para el cliente web, que cambia cada semana, se queda en spec-first: una especificación breve por funcionalidad que se archiva al terminar. Para una tabla de textos traducidos, usa spec-as-source: un archivo de especificación y un generador, con la regla de que el archivo generado no se edita. Registra la decisión por componente y la revisa cada trimestre con los casos de deriva que encontró.

## Ejemplo

Ejemplo de [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) (sección «Ejemplo profesional»):

El equipo elige el nivel por componente. Para las reglas de avisos, que fija un acuerdo con la plataforma y cambia poco, opta por spec-anchored: cada regla tiene identificador, el código y las pruebas lo citan, los umbrales viven en la especificación y se leen de ella, y la integración continua ejecuta el comprobador. Para el cliente web, que cambia cada semana, se queda en spec-first: una especificación breve por funcionalidad que se archiva al terminar. Para una tabla de textos traducidos, usa spec-as-source: un archivo de especificación y un generador, con la regla de que el archivo generado no se edita.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Tampoco se comprueba que el texto de una regla haya cambiado de significado: el comprobador ve que el archivo generado quedó viejo (porque la huella cambió) pero no que la regla dice ahora lo contrario. ([SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Especificación](../e/especificacion.md).
- **Ver también:** [Anclaje](./anclaje.md), [Deriva](../d/deriva.md), [Huella](../h/huella.md), [SDD](../s/sdd.md), [Spec-anchored](../s/spec-anchored.md), [Spec-as-source](../s/spec-as-source.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-556](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md), [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Archivo de relevo](./archivo-de-relevo.md) · [Archivo huérfano →](./archivo-huerfano.md)
