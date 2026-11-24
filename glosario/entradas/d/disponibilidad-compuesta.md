# Disponibilidad compuesta

[↑ Glosario](../../README.md) · [← Disponibilidad](./disponibilidad.md) · [Disponibilidad en cadena →](./disponibilidad-en-cadena.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

La **disponibilidad compuesta** es la disponibilidad de un sistema que depende de varios componentes, calculada combinando las de cada uno. En serie (hacen falta todos) es el producto de las disponibilidades; en paralelo (basta uno) la indisponibilidad es el producto de las indisponibilidades. [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) y [SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md) la enuncian para la cadena en serie y [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) desarrolla el cálculo completo.

## Por qué importa

La disponibilidad que se promete al cliente no es la de un componente sino la del conjunto. Sumar componentes fiables en serie reduce el total; duplicar un componente lo mejora, pero solo bajo condiciones. La decisión que cambia es dónde se invierte para subir la disponibilidad y qué se comprueba antes de creer una cifra de «nueves».

## Cómo funciona

[SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) da los tres cálculos que hay que distinguir:

1. **Paralelo con conmutación perfecta**: si dos componentes fallan de forma independiente y cualquiera basta, la indisponibilidad es el producto. Dos proveedores de 99,95 % dan 1 − 0,0005² = 99,99997 %.
2. **Serie**: si el servicio necesita a ambos a la vez, como una réplica síncrona, la disponibilidad es el producto de las disponibilidades: baja a 99,90 %.
3. **Techo de un componente compartido**: un componente en serie con el par, como el DNS que decide el destino, impone su propio techo: 99,95 % × 99,99997 % ≈ 99,95 %.

La lección de la clase es que la ganancia de un segundo proveedor existe solo si **la conmutación funciona, los fallos son independientes y nada común queda en el camino**. Los tres supuestos son las condiciones; fallar cualquiera anula el beneficio calculado. [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) y [SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md) aplican la misma aritmética a la cadena de dependencias de un producto y a un sistema que depende en serie de varios componentes.

## Ejemplo

Una plataforma usa dos proveedores de 99,95 % en paralelo y cree llegar a 99,99997 %. Pero ambos se resuelven por el mismo DNS, que está en serie con el par: el techo vuelve a ser 99,95 %. Además, si la conmutación nunca se ensayó y falla la mitad de las veces, el valor real queda lejos del calculado. Cálculo de [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) con proveedores ficticios.

## Errores y confusiones comunes

- **Dos proveedores y la misma caída anual**: un componente compartido en serie; se corrige dibujando las dependencias y eliminando o duplicando el común.
- **La conmutación falla cuando se necesita**: nunca se ensayó; se ensaya con regularidad y se mide su acierto.
- **Multiplicar disponibilidades de componentes correlacionados**: asume independencia que puede no existir.
- **Creer en el SLA de un proveedor como disponibilidad propia**: el crédito de servicio compensa, no restituye.

## Límites y cuándo no aplica

[SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) precisa que sus proveedores son ficticios y que no se midió ningún enlace real: la disponibilidad, la independencia, las probabilidades de oferta y el precio de salida son supuestos del autor. El modelo de producto asume independencia; los fallos correlacionados (un mismo despliegue, una misma región) empeoran el resultado. No describe degradación parcial ni latencia, solo si el servicio está arriba o abajo.

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
