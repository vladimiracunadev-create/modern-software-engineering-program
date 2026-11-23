# Dispositivo

[↑ Glosario](../../README.md) · [← Disposición a pagar](./disposicion-a-pagar.md) · [Distancia de color ΔE →](./distancia-de-color-e.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Componente que intercambia datos o señales con el sistema.

Definición de trabajo de [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md).

## Por qué importa

La clase donde se define, [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), existe con este propósito: la clase existe para separar arquitectura física, ISA, sistema operativo y runtime antes de atribuir una propiedad a la máquina.

## Cómo funciona

Según [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md):

La CPU obtiene y ejecuta instrucciones; los registros conservan estado inmediato; la memoria principal mantiene código y datos activos; el almacenamiento preserva datos; los dispositivos intercambian información. Interconexiones y controladores coordinan movimientos. Esta lista no explica por sí sola un programa: hay que seguir qué dato cambia, dónde vive y quién inicia la transición.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md):

Un servicio consume CPU baja y latencia alta. La traza muestra espera de red. Escalar frecuencia de CPU no ataca el mecanismo; reducir rondas, usar concurrencia controlada o mejorar la dependencia sí podrían hacerlo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md)) son:

- **una línea equivale a una instrucción** — causa: se saltaron compilador y runtime. Corrección: traza representaciones intermedias.
- **CPU y computador se usan como sinónimos** — causa: se omitieron memoria e I/O. Corrección: sigue dato y control por componentes.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- `os` y `resource` miran el sistema operativo y no revelan qué hizo el dispositivo después de aceptar una escritura. ([SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Componente](../c/componente.md), [ABI](../a/abi.md), [Arquitectura](../a/arquitectura.md), [Estado](../e/estado.md), [Firmware](../f/firmware.md), [ISA](../i/isa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (102 clases más lo mencionan; las que más):

[SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md), [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Disposición a pagar](./disposicion-a-pagar.md) · [Distancia de color ΔE →](./distancia-de-color-e.md)
