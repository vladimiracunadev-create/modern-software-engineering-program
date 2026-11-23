# Disponibilidad compuesta

[↑ Glosario](../../README.md) · [← Disponibilidad](./disponibilidad.md) · [Disponibilidad en cadena →](./disponibilidad-en-cadena.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Disponibilidad de una cadena en serie, igual al producto de las disponibilidades.

Definición de trabajo de [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-535 — Compras, proveedores y evaluación técnica](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md): Disponibilidad de un sistema que depende en serie de varios componentes, igual al producto de las disponibilidades.

## Por qué importa

En [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), el tema «Disponibilidad compuesta» importa porque en paralelo mejora, en serie empeora y lo compartido la anula.

En [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), el tema «Disponibilidad compuesta» importa porque la cadena es peor que su peor eslabón.

## Cómo funciona

Según [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), en la sección «Disponibilidad compuesta»:

Si dos componentes fallan de forma independiente y cualquiera basta para servir, la indisponibilidad es el producto de las indisponibilidades: dos proveedores de 99,95 % dan 1 − 0,0005² = 99,99997 % si la conmutación es perfecta. Si el servicio necesita a ambos a la vez, como una réplica síncrona, la disponibilidad es el producto de las disponibilidades: baja a 99,90 %. Y un componente compartido en serie con el par, como el DNS que decide el destino, impone su propio techo: 99,95 % × 99,99997 % ≈ 99,95 %. La lección es que la ganancia de un segundo proveedor existe solo si la conmutación funciona, si los fallos son independientes y si nada común queda en el camino.

## Ejemplo

Ejemplo de [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) (sección «Ejemplo mínimo»):

Minutos permitidos, disponibilidad compuesta y crédito:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md)) son:

- **Dos proveedores y la misma caída anual** — causa: un componente compartido en serie. Corrección: dibujar las dependencias y eliminar o duplicar el común.
- **La conmutación falla cuando se necesita** — causa: nunca se ensayó. Corrección: ensayar la conmutación con regularidad y medir su acierto.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada proveedor y cada guía usan estos términos con matices y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Los proveedores son ficticios y no se midió ningún enlace ni proveedor real: la disponibilidad, la independencia de fallos, las probabilidades de oferta y el precio de salida son supuestos del autor. La siguiente clase mira cómo se ofrece todo esto a los equipos sin que cada uno lo reconstruya: plataformas internas y caminos dorados.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Disponibilidad](./disponibilidad.md), [Producto](../p/producto.md), [Crédito de servicio](../c/credito-de-servicio.md), [Gravedad de los datos](../g/gravedad-de-los-datos.md), [Mínimo común denominador](../m/minimo-comun-denominador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-535 — Compras, proveedores y evaluación técnica](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md).

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

[↑ Glosario](../../README.md) · [← Disponibilidad](./disponibilidad.md) · [Disponibilidad en cadena →](./disponibilidad-en-cadena.md)
