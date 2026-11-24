# Responsabilidad compartida

[↑ Glosario](../../README.md) · [← Responsabilidad](./responsabilidad.md) · [Restauración →](./restauracion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

La **responsabilidad compartida** es el reparto de qué seguridad y operación corresponde al proveedor de nube y al cliente, y que cambia con el tipo de servicio ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md)). No es un reparto 50-50: es una frontera que se mueve según uses IaaS, PaaS o SaaS.

## Por qué importa

Migrar a la nube no traslada toda la responsabilidad al proveedor. Los incidentes más comunes aparecen en lo que el cliente asumió que otro hacía. La decisión que cambia es que cada tarea de seguridad y operación tiene un responsable nombrado, sabiendo en qué lado de la frontera cae según el servicio contratado.

## Cómo funciona

[SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) recoge lo que coinciden los documentos de los proveedores: el proveedor responde de la seguridad **de** la nube (instalaciones, hardware, virtualización) y el cliente de la seguridad **en** la nube (datos, identidades, configuración). Entre ambos hay **capas compartidas**, como las copias de seguridad o el registro de eventos, donde el proveedor ofrece el mecanismo y el cliente decide si lo activa, qué conserva y quién lo mira.

La frontera se desplaza según el servicio. En IaaS, el cliente mantiene el sistema operativo, el almacenamiento y las aplicaciones; en PaaS, el proveedor asume el sistema operativo y el tiempo de ejecución, y el cliente conserva el código y la configuración; en SaaS, el proveedor opera también la aplicación, y al cliente le quedan sus datos, sus usuarios y la configuración. La clase modela cuánta exposición queda según el tipo: pasar de IaaS a SaaS recorta la exposición a un tercio y deja en pie casi el 61 % del resto (valores del modelo de la clase).

La utilidad práctica es la **matriz**: una tabla de tareas por servicio con una persona o un equipo nombrado para cada celda. Una celda sin nombre es la que se incendia.

## Ejemplo

Una organización pasa un depósito de archivos a un servicio gestionado. El proveedor protege la infraestructura, pero la decisión de dejarlo público o privado es del cliente. En la matriz, la celda «configuración del servicio de almacenamiento» tiene un dueño y una revisión periódica; sin eso, un depósito queda abierto tras migrar. Caso de [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md).

## Errores y confusiones comunes

- **Un depósito o un panel quedan abiertos tras migrar**: se asumió que el proveedor configura lo que solo el cliente puede decidir; se corrige asignando dueño y revisión a la celda.
- **Un tiempo de ejecución deja de recibir parches y nadie se entera**: en PaaS, el proveedor retira la versión y el equipo no sigue el calendario.
- **Leerlo como 50-50**.
- **Asumir que la certificación del proveedor cubre al cliente**.

## Límites y cuándo no aplica

El modelo concreto varía por proveedor y por servicio: los documentos oficiales de cada uno mandan sobre cualquier resumen. [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) aclara que su modelo numérico usa supuestos del autor. En un sistema local, sin proveedor, no hay reparto: todo es del operador. Y la matriz es un punto de partida: debe revisarse al cambiar de servicio o de proveedor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Seguridad](../s/seguridad.md), [Servicio](../s/servicio.md), [Tipo](../t/tipo.md), [IaaS](../i/iaas.md), [PaaS](../p/paas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google Cloud, «Shared responsibility and shared fate»](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) — responsabilidad compartida y apoyo del proveedor a la configuración; autoridad: documentación del proveedor.
- [NIST SP 800-145, «The NIST Definition of Cloud Computing»](https://csrc.nist.gov/pubs/sp/800/145/final) — definición de IaaS, PaaS y SaaS y de los modelos de despliegue; autoridad: NIST.
- [AWS, «Shared Responsibility Model»](https://aws.amazon.com/compliance/shared-responsibility-model/) — seguridad «de» la nube y «en» la nube; autoridad: documentación del proveedor.
- [Microsoft, «Shared responsibility in the cloud»](https://learn.microsoft.com/azure/security/fundamentals/shared-responsibility) — cómo cambia la responsabilidad por tipo de servicio; autoridad: documentación del proveedor.
- [Python: random](https://docs.python.org/3/library/random.html) — generador y distribuciones usadas en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Responsabilidad](./responsabilidad.md) · [Restauración →](./restauracion.md)
