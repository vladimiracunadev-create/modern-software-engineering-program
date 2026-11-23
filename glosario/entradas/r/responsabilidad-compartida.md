# Responsabilidad compartida

[↑ Glosario](../../README.md) · [← Responsabilidad](./responsabilidad.md) · [Restauración →](./restauracion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Reparto de qué seguridad y operación corresponde al proveedor y al cliente, que cambia con el tipo de servicio.

Definición de trabajo de [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md).

## Por qué importa

En [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), el tema «Responsabilidad compartida» importa porque fija quién responde por qué y qué evidencia sirve de prueba.

## Cómo funciona

Según [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), en la sección «Responsabilidad compartida»:

El modelo de responsabilidad compartida no es un reparto 50-50 sino una frontera que cambia con cada servicio. Los documentos de los proveedores coinciden en lo esencial: el proveedor responde de la seguridad **de** la nube (instalaciones, hardware, virtualización) y el cliente de la seguridad **en** la nube (datos, identidades, configuración). Entre ambos hay capas compartidas, como las copias de seguridad o el registro de eventos, donde el proveedor ofrece el mecanismo y el cliente decide si lo activa, qué conserva y quién lo mira. La utilidad práctica de la matriz es nombrar a una persona o un equipo para cada celda; una celda sin nombre es la que se incendia.

## Ejemplo

Caso medido en la sección «Responsabilidad compartida» de [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md):

El modelo de responsabilidad compartida no es un reparto 50-50 sino una frontera que cambia con cada servicio. Los documentos de los proveedores coinciden en lo esencial: el proveedor responde de la seguridad **de** la nube (instalaciones, hardware, virtualización) y el cliente de la seguridad **en** la nube (datos, identidades, configuración). Entre ambos hay capas compartidas, como las copias de seguridad o el registro de eventos, donde el proveedor ofrece el mecanismo y el cliente decide si lo activa, qué conserva y quién lo mira.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md)) son:

- **Un depósito o un panel quedan abiertos tras migrar** — causa: se asumió que el proveedor configura lo que solo el cliente puede decidir. Corrección: asignar dueño y revisión a la celda «configuración del servicio».
- **Un tiempo de ejecución deja de recibir parches y nadie se entera** — causa: PaaS: el proveedor retira la versión y el equipo no sigue el calendario. Corrección: suscribirse a los avisos del proveedor y planificar el cambio de versión.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El modelo de responsabilidad compartida no es un reparto 50-50 sino una frontera que cambia con cada servicio. ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md))

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
