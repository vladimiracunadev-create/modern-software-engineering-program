# Multi-cloud

[↑ Glosario](../../README.md) · [← Muestreo y saturación](./muestreo-y-saturacion.md) · [Multi-tenancy →](./multi-tenancy.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Uso de más de un proveedor de nube para una misma carga o plataforma.

Definición de trabajo de [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md).

## Por qué importa

La clase donde se define, [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), existe con este propósito: la clase existe para que, cuando alguien proponga «usar dos nubes por si una cae» o «no depender de un proveedor», puedas calcular qué se gana, qué se paga y bajo qué condiciones el argumento deja de sostenerse.

## Cómo funciona

Según [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md):

Multi-cloud significa usar más de un proveedor de nube; híbrido, combinar una instalación propia con la nube; portabilidad, poder cambiar de entorno sin reescribir. Son cosas distintas y se confunden porque comparten el discurso de «no depender de uno». La guía de Google sobre patrones híbridos y multi-cloud organiza los motivos: aprovechar funciones distintas, cumplir una regulación de ubicación de datos, reducir una dependencia, repartir riesgo, aprovechar inversiones existentes. Cada motivo se evalúa con su propio cálculo, y confundirlos produce arquitecturas caras que no resuelven ninguno.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md):

El equipo de la plataforma escribe el motivo antes de la solución: reducir el tiempo sin servicio de la recepción de entregas durante el cierre, no cumplir una regulación ni evitar un proveedor. Calcula que un segundo proveedor con conmutación del 90 % y un DNS compartido de 99,95 % no mejora lo suficiente para justificar su costo, y opta por una región adicional dentro del mismo proveedor, una cola que acepta entregas aunque el procesamiento esté caído y una exportación semanal de los datos en un formato abierto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md)) son:

- **Dos proveedores y la misma caída anual** — causa: un componente compartido en serie. Corrección: dibujar las dependencias y eliminar o duplicar el común.
- **La conmutación falla cuando se necesita** — causa: nunca se ensayó. Corrección: ensayar la conmutación con regularidad y medir su acierto.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Multi-cloud significa usar más de un proveedor de nube; híbrido, combinar una instalación propia con la nube; portabilidad, poder cambiar de entorno sin reescribir. ([SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Plataforma](../p/plataforma.md), [Disponibilidad compuesta](../d/disponibilidad-compuesta.md), [Gravedad de los datos](../g/gravedad-de-los-datos.md), [Mínimo común denominador](./minimo-comun-denominador.md), [Nube híbrida](../n/nube-hibrida.md), [Portabilidad](../p/portabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google Cloud: patrones híbridos y multi-cloud](https://cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices) — motivos y patrones; autoridad: documentación del proveedor.
- [OCI Image Specification](https://github.com/opencontainers/image-spec) — formato común de imágenes; autoridad: Open Container Initiative.
- [Kubernetes: controladores](https://kubernetes.io/docs/concepts/architecture/controller/) — orquestación declarativa; autoridad: documentación oficial de Kubernetes.
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — diseño para el fallo de componentes; autoridad: documentación del proveedor.
- [Python: random](https://docs.python.org/3/library/random.html) — generador usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Muestreo y saturación](./muestreo-y-saturacion.md) · [Multi-tenancy →](./multi-tenancy.md)
