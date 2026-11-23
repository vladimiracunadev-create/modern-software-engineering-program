# Valor de referencia

[↑ Glosario](../../README.md) · [← Valor de frontera](./valor-de-frontera.md) · [Valor de Shapley →](./valor-de-shapley.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Medición que el verificador acepta como correcta, obtenida por un canal independiente.

Definición de trabajo de [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md).

## Por qué importa

En [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), el tema «Valores de referencia» importa porque sin ellos, la medición no significa nada.

## Cómo funciona

Según [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md):

Una medición es un número. Para que signifique algo, el verificador necesita saber *qué número esperar*, y ese valor debe venir de un canal independiente del atestador: el proceso de construcción que produce el binario (de ahí `SE-469` y `SE-472`, build reproducible y atestaciones de procedencia), firmado por quien publica. Si el servicio cambia en cada versión, cada versión tiene su medición, y el verificador debe tener una lista de valores aceptados con fechas y con un plan para retirar los de versiones vulnerables. Esa lista es una pieza de política: aceptar una versión antigua con una vulnerabilidad conocida es una decisión, no un descuido, y debe tener dueño.

Según [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md):

Contra el que tiene control del sistema operativo o del hipervisor, en lo que afecta a la memoria del TEE. No contra quien controla el código que se mide y se libera, ni contra quien controla los valores de referencia.

## Ejemplo

Ejemplo de [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) (sección «Preguntas frecuentes»):

Contra el que tiene control del sistema operativo o del hipervisor, en lo que afecta a la memoria del TEE. No contra quien controla el código que se mide y se libera, ni contra quien controla los valores de referencia.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El RFC 9334 distingue la *evidencia* que produce el atestador de los *valores de referencia* y *endosos* que aportan otros actores; la clase no los implementa, solo señala el lugar. ([SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md))
- Escribe quién tiene hoy acceso privilegiado a las máquinas, qué podrían ver de los datos en uso, qué cubriría un TEE y qué no, quién publicaría los valores de referencia, cómo se actualizaría el servicio sin perder el acceso a sus datos y qué control más simple podría cubrir la amenaza sin hardware especial. ([SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medición](../m/medicion.md), [Verificador](./verificador.md), [Extensión](../e/extension.md), [Raíz de confianza](../r/raiz-de-confianza.md), [Sellado](../s/sellado.md), [TEE](../t/tee.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md), [SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Valores de referencia».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Valor de frontera](./valor-de-frontera.md) · [Valor de Shapley →](./valor-de-shapley.md)
