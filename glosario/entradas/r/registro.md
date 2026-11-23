# Registro

[↑ Glosario](../../README.md) · [← Región](./region.md) · [Registro de auditoría →](./registro-de-auditoria.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Almacenamiento nombrado visible para la ISA.

Definición de trabajo de [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md): Diccionario de nombres a constructores que permite extender sin tocar la fábrica.

## Por qué importa

En [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), el tema «Registros y PC» importa porque conservan operandos y próxima instrucción

## Cómo funciona

Según [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

Una ISA define instrucciones, registros, formatos y efectos observables. La misma ISA puede tener implementaciones simples, segmentadas o fuera de orden. El software confía en el resultado arquitectónico, no en cada señal interna.

Según [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

Un segundo fallo controlado usa el simulador de la sección 7. Cambia `BEQZ` por una instrucción que salte cuando el registro *no* sea cero (`BNEZ`) sin ajustar la dirección de destino. **Síntoma:** el programa termina de inmediato con `r3 = 0` y la dirección 16 guarda 0 en lugar de 12. **Traza:** busca el primer paso en que el contador de programa difiere del original (el paso 5, donde ya salta al final con `r1 = 4`). **Causa:** la condición opuesta invierte el control del bucle. **Corrección:** invierte la condición *y* verifica el destino, y escribe una prueba con `r1 = 0` al inicio (cero vueltas) y con `r1 = 1`.

## Ejemplo

Ejemplo de [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* revisa sus cuatro puntos de creación con `criterio-de-patron.md`. Para los canales adopta un registro con un decorador que añade clases al diccionario, y los tres `if` desaparecen; para `Aviso` pasa a argumentos solo con nombre y un `validar()` que rechaza un SMS sin teléfono; para la configuración elimina el objeto global y crea una por proceso, que se entrega a los servicios en el arranque; y para la plantilla usa `deepcopy` con una prueba que añade un destinatario a un clon y comprueba que los demás no cambian.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **variable = registro** — causa: abstracciones mezcladas. Corrección: documenta decisiones de compilador/runtime. ([SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- `rs1` y `rs2` nombran los registros fuente (`x1` y `x2`) y `rd`, el destino (`x3`). ([SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md))
- Un **Factory Method** mueve la decisión a un método que las subclases redefinen; un **Abstract Factory** crea familias de objetos que deben ser coherentes entre sí (por ejemplo, el cliente HTTP y el serializador de un mismo proveedor); y un **registro** (un diccionario de nombres a constructores) permite añadir tipos sin tocar la fábrica. ([SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Builder](../b/builder.md), [Copia profunda](../c/copia-profunda.md), [Copia superficial](../c/copia-superficial.md), [Excepción](../e/excepcion.md), [Factory](../f/factory.md), [Instrucción](../i/instruccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (379 clases más lo mencionan; las que más):

[SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md), [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Región](./region.md) · [Registro de auditoría →](./registro-de-auditoria.md)
