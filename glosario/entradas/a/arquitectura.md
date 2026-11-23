# Arquitectura

[↑ Glosario](../../README.md) · [← ARP](./arp.md) · [Arquitectura de información →](./arquitectura-de-informacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Propiedades e interfaces visibles de un sistema.

Definición de trabajo de [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md).

## Por qué importa

La clase donde se define, [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), existe con este propósito: la clase existe para separar arquitectura física, ISA, sistema operativo y runtime antes de atribuir una propiedad a la máquina.

## Cómo funciona

Según [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md):

La arquitectura describe propiedades que un consumidor puede usar sin conocer toda la implementación. Una ISA especifica instrucciones, registros y efectos visibles para el software de bajo nivel. RISC-V, por ejemplo, separa deliberadamente la ISA de una microarquitectura particular. Dos procesadores pueden ejecutar el mismo binario y organizar internamente pipeline, cachés o unidades de ejecución de modo distinto.

Según [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md):

Porque informa la etiqueta que cada plataforma usa para nombrar la arquitectura. La misma familia de procesadores de 64 bits de Intel y AMD aparece como `AMD64` en Windows y como `x86_64` en Linux; los procesadores ARM de 64 bits aparecen como `arm64` en macOS y `aarch64` en Linux. La etiqueta ayuda a decidir compatibilidad aproximada de binarios, pero depende del sistema que la reporta, no de una norma común.

## Ejemplo

Ejemplo de [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) (sección «Preguntas frecuentes»):

Porque informa la etiqueta que cada plataforma usa para nombrar la arquitectura. La misma familia de procesadores de 64 bits de Intel y AMD aparece como `AMD64` en Windows y como `x86_64` en Linux; los procesadores ARM de 64 bits aparecen como `arm64` en macOS y `aarch64` en Linux. La etiqueta ayuda a decidir compatibilidad aproximada de binarios, pero depende del sistema que la reporta, no de una norma común.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **misma ISA implica mismo rendimiento** — causa: arquitectura confundida con implementación. Corrección: mide cada entorno y declara microarquitectura desconocida. ([SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La arquitectura describe propiedades que un consumidor puede usar sin conocer toda la implementación. ([SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Interfaz](../i/interfaz.md), [Propiedad](../p/propiedad.md), [ABI](./abi.md), [Dispositivo](../d/dispositivo.md), [Estado](../e/estado.md), [Firmware](../f/firmware.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (116 clases más lo mencionan; las que más):

[SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← ARP](./arp.md) · [Arquitectura de información →](./arquitectura-de-informacion.md)
