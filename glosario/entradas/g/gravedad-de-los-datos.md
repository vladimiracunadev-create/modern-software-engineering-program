# Gravedad de los datos

[↑ Glosario](../../README.md) · [← Gravedad](./gravedad.md) · [Green Software Engineer →](./green-software-engineer.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Tendencia de las aplicaciones a ubicarse donde están los datos, por el costo y el tiempo de moverlos.

Definición de trabajo de [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md).

## Por qué importa

En [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), el tema «Gravedad de los datos» importa porque los datos tardan y cuestan al moverse.

## Cómo funciona

Según [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), en la sección «Gravedad de los datos»:

Mover código es barato; mover datos no. Tardan según el tamaño y el ancho de banda, cuestan según la tarifa de salida y siguen atrayendo a las aplicaciones que los usan, porque ejecutar lejos de ellos añade latencia y más tráfico de salida. A esto se llama gravedad de los datos: cuanto más pesan, más condicionan dónde vive todo lo demás. Por eso la portabilidad de los datos se decide al diseñar, con formatos abiertos y exportaciones periódicas, y no el día que se quiere salir.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md):

El equipo de la plataforma escribe el motivo antes de la solución: reducir el tiempo sin servicio de la recepción de entregas durante el cierre, no cumplir una regulación ni evitar un proveedor. Calcula que un segundo proveedor con conmutación del 90 % y un DNS compartido de 99,95 % no mejora lo suficiente para justificar su costo, y opta por una región adicional dentro del mismo proveedor, una cola que acepta entregas aunque el procesamiento esté caído y una exportación semanal de los datos en un formato abierto.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md)) son:

- **Dos proveedores y la misma caída anual** — causa: un componente compartido en serie. Corrección: dibujar las dependencias y eliminar o duplicar el común.
- **La conmutación falla cuando se necesita** — causa: nunca se ensayó. Corrección: ensayar la conmutación con regularidad y medir su acierto.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada proveedor y cada guía usan estos términos con matices y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Los proveedores son ficticios y no se midió ningún enlace ni proveedor real: la disponibilidad, la independencia de fallos, las probabilidades de oferta y el precio de salida son supuestos del autor. La siguiente clase mira cómo se ofrece todo esto a los equipos sin que cada uno lo reconstruya: plataformas internas y caminos dorados.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Disponibilidad compuesta](../d/disponibilidad-compuesta.md), [Mínimo común denominador](../m/minimo-comun-denominador.md), [Multi-cloud](../m/multi-cloud.md), [Nube híbrida](../n/nube-hibrida.md), [Portabilidad](../p/portabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

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

[↑ Glosario](../../README.md) · [← Gravedad](./gravedad.md) · [Green Software Engineer →](./green-software-engineer.md)
