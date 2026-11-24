# PaaS

[↑ Glosario](../../README.md) · [← P95](./p95.md) · [Package URL →](./package-url.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

**PaaS** (plataforma como servicio) es el servicio que entrega un entorno de ejecución gestionado donde el cliente despliega su propio código sin operar el sistema operativo ni los servidores ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md)). La plataforma ofrece lenguajes, bibliotecas y servicios soportados por el proveedor.

## Por qué importa

Entre alquilar máquinas (IaaS) y usar una aplicación ya hecha (SaaS) está el modelo en que el equipo escribe y despliega código, pero otro opera lo que hay debajo. La decisión que cambia es qué trabajo operativo se abandona y qué control se cede a cambio: se gana seguridad y velocidad, se pierde control sobre las versiones.

## Cómo funciona

En PaaS, el consumidor despliega su código y el proveedor se ocupa del entorno de ejecución, con sus versiones y parches. [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) señala el trueque con precisión:

- **Lo que se gana**: desaparece una familia de vulnerabilidades del lado del cliente, la de mantener al día el sistema operativo y el tiempo de ejecución.
- **Lo que se pierde**: el control de la versión. El proveedor retira un tiempo de ejecución en una fecha que no eliges.

Por eso la dependencia no es solo técnica sino de **calendario**, y el contrato de versiones es parte del diseño. Si el proveedor retira una versión y el equipo no sigue el calendario, el tiempo de ejecución deja de recibir parches y nadie se entera. La corrección que da la clase es suscribirse a los avisos del proveedor y planificar el cambio de versión.

En el reparto de responsabilidades, PaaS está entre IaaS (el cliente parchea el sistema operativo) y SaaS (el proveedor opera también la aplicación). Sigue siendo del cliente el código, sus dependencias y la configuración del servicio; un depósito o un panel quedan abiertos tras migrar si se asume que el proveedor configura lo que solo el cliente puede decidir.

## Ejemplo

Un equipo despliega una aplicación en un servicio PaaS con un tiempo de ejecución de cierta versión. Elimina la tarea de parchear servidores. Un año después el proveedor anuncia el retiro de esa versión; el equipo, suscrito a los avisos, planifica la actualización con meses de margen. Otro equipo, sin suscripción, descubre al retirarse la versión que su servicio ya no recibe parches. Ejemplo ilustrativo de lo que describe [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md).

## Errores y confusiones comunes

- **Un tiempo de ejecución deja de recibir parches y nadie se entera**: el proveedor retira la versión y el equipo no sigue el calendario; se corrige suscribiéndose a los avisos y planificando el cambio de versión.
- **Creer que el proveedor se hace cargo de todo**: el código y su configuración siguen siendo del cliente.
- **Confundirlo con IaaS o SaaS**: el límite lo marca quién opera el sistema operativo y quién la aplicación.
- **Ignorar el costo de salida** de usar servicios propios de la plataforma.

## Límites y cuándo no aplica

PaaS limita lo que se puede instalar y configurar: si la aplicación necesita un sistema operativo, un componente de red o una versión que la plataforma no ofrece, IaaS es la opción. [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) también advierte que su modelo de exposición usa supuestos del autor y que el efecto real depende de cuánto tarda cada proveedor y de cuántos ajustes mantiene el cliente.

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
