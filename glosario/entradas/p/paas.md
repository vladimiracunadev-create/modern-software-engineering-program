# PaaS

[↑ Glosario](../../README.md) · [← P95](./p95.md) · [Package URL →](./package-url.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Servicio que entrega un entorno de ejecución gestionado donde el cliente despliega código sin operar el sistema operativo.

Definición de trabajo de [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md).

## Por qué importa

En [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), el tema «PaaS» importa porque entrega además el entorno de ejecución; el código, los datos y la identidad siguen siendo tuyos.

## Cómo funciona

Según [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), en la sección «PaaS»:

En PaaS el consumidor despliega su propio código en una plataforma que ofrece lenguajes, bibliotecas y servicios soportados por el proveedor, sin gestionar el sistema operativo ni los servidores. El entorno de ejecución, con sus versiones y parches, pasa a ser del proveedor. Lo que se gana es que desaparece una familia de vulnerabilidades del lado del cliente; lo que se pierde es el control de la versión: el proveedor retira un tiempo de ejecución en una fecha que no eliges. La dependencia no es solo técnica sino de calendario, y por eso el contrato de versiones es parte del diseño.

## Ejemplo

Ejemplo de [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma de entregas decide dónde alojar tres piezas: el servidor de la aplicación web, la base de datos y el servicio de correo de avisos a estudiantes. Para el servidor elige PaaS para no operar el sistema operativo; para la base de datos elige un servicio gestionado, y registra que las copias, el cifrado y los usuarios siguen siendo suyos aunque el motor y los parches no lo sean; para el correo elige SaaS y anota que debe configurar la autenticación del dominio remitente y decidir cuánto tiempo guardar los mensajes.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un tiempo de ejecución deja de recibir parches y nadie se entera** — causa: PaaS: el proveedor retira la versión y el equipo no sigue el calendario. Corrección: suscribirse a los avisos del proveedor y planificar el cambio de versión. ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En PaaS el consumidor despliega su propio código en una plataforma que ofrece lenguajes, bibliotecas y servicios soportados por el proveedor, sin gestionar el sistema operativo ni los servidores. ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sistema operativo](../s/sistema-operativo.md), [Entorno](../e/entorno.md), [Servicio](../s/servicio.md), [IaaS](../i/iaas.md), [Responsabilidad compartida](../r/responsabilidad-compartida.md), [SaaS](../s/saas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-145, «The NIST Definition of Cloud Computing»](https://csrc.nist.gov/pubs/sp/800/145/final) — definición de IaaS, PaaS y SaaS y de los modelos de despliegue; autoridad: NIST.
- [AWS, «Shared Responsibility Model»](https://aws.amazon.com/compliance/shared-responsibility-model/) — seguridad «de» la nube y «en» la nube; autoridad: documentación del proveedor.
- [Microsoft, «Shared responsibility in the cloud»](https://learn.microsoft.com/azure/security/fundamentals/shared-responsibility) — cómo cambia la responsabilidad por tipo de servicio; autoridad: documentación del proveedor.
- [Google Cloud, «Shared responsibility and shared fate»](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) — responsabilidad compartida y apoyo del proveedor a la configuración; autoridad: documentación del proveedor.
- [Python: random](https://docs.python.org/3/library/random.html) — generador y distribuciones usadas en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← P95](./p95.md) · [Package URL →](./package-url.md)
