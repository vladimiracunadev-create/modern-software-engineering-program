# SaaS

[↑ Glosario](../../README.md) · [← Rutina de interrupción](../r/rutina-de-interrupcion.md) · [SaaS / Product Platform Engineer →](./saas-product-platform-engineer.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Aplicación completa operada por el proveedor, de la que el cliente solo configura, administra identidades y es dueño de sus datos.

Definición de trabajo de [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md): Producto operado por el proveedor, entregado de forma continua a muchos clientes y pagado por suscripción o consumo.

## Por qué importa

En [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), el tema «SaaS» importa porque entrega la aplicación completa; solo configuras, administras identidades y eres dueño de los datos.

## Cómo funciona

Según [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), en la sección «SaaS»:

En SaaS el consumidor usa una aplicación que corre en infraestructura del proveedor y solo controla configuraciones limitadas. Es el extremo en el que más cosas se delegan, y por eso es fácil olvidar lo que no: quién tiene acceso, qué datos se suben, cómo se exportan y qué pasa al terminar el contrato. Una plataforma educativa externa que guarda las entregas de los estudiantes sigue haciendo al equipo responsable de su tratamiento aunque no opere ni un servidor.

## Ejemplo

Ejemplo de [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma de entregas decide dónde alojar tres piezas: el servidor de la aplicación web, la base de datos y el servicio de correo de avisos a estudiantes. Para el servidor elige PaaS para no operar el sistema operativo; para la base de datos elige un servicio gestionado, y registra que las copias, el cifrado y los usuarios siguen siendo suyos aunque el motor y los parches no lo sean; para el correo elige SaaS y anota que debe configurar la autenticación del dominio remitente y decidir cuánto tiempo guardar los mensajes.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **«Pasamos a SaaS y ya no necesitamos seguridad»** — causa: se confunde delegar la operación con delegar la responsabilidad por los datos. Corrección: mantener revisión de accesos, exportación y retención. ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En SaaS el consumidor usa una aplicación que corre en infraestructura del proveedor y solo controla configuraciones limitadas. ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md))
- En el modelo, pasar de IaaS a SaaS recorta la exposición a un tercio y deja en pie casi el 61 % del resto; el efecto real depende de cuánto tarda cada proveedor y de cuántos ajustes mantienes. ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producto](../p/producto.md), [Suscripción](./suscripcion.md), [Baja](../b/baja.md), [CAC (costo de adquisición de cliente)](../c/cac-costo-de-adquisicion-de-cliente.md), [Expansión y contracción](../e/expansion-y-contraccion.md), [IaaS](../i/iaas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «software como servicio».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-145, «The NIST Definition of Cloud Computing»](https://csrc.nist.gov/pubs/sp/800/145/final) — definición de IaaS, PaaS y SaaS y de los modelos de despliegue; autoridad: NIST.
- [AWS, «Shared Responsibility Model»](https://aws.amazon.com/compliance/shared-responsibility-model/) — seguridad «de» la nube y «en» la nube; autoridad: documentación del proveedor.
- [Microsoft, «Shared responsibility in the cloud»](https://learn.microsoft.com/azure/security/fundamentals/shared-responsibility) — cómo cambia la responsabilidad por tipo de servicio; autoridad: documentación del proveedor.
- [Google Cloud, «Shared responsibility and shared fate»](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) — responsabilidad compartida y apoyo del proveedor a la configuración; autoridad: documentación del proveedor.
- [Python: random](https://docs.python.org/3/library/random.html) — generador y distribuciones usadas en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Rutina de interrupción](../r/rutina-de-interrupcion.md) · [SaaS / Product Platform Engineer →](./saas-product-platform-engineer.md)
