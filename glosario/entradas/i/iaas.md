# IaaS

[↑ Glosario](../../README.md) · [← I/o y red](./i-o-y-red.md) · [Idempotencia →](./idempotencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Servicio que entrega cómputo, red y almacenamiento virtualizados sobre los que el cliente instala y opera su propio sistema operativo y software.

Definición de trabajo de [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md).

## Por qué importa

En [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), el tema «IaaS» importa porque entrega cómputo, red y almacenamiento virtualizados; el sistema operativo y todo lo que está encima es tuyo.

## Cómo funciona

Según [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), en la sección «IaaS»:

NIST define IaaS como la capacidad de aprovisionar procesamiento, almacenamiento y redes en las que el consumidor puede ejecutar software arbitrario, incluidos sistemas operativos y aplicaciones. El consumidor no gestiona la infraestructura subyacente, pero sí el sistema operativo, el almacenamiento y las aplicaciones desplegadas, y, de forma limitada, algunos componentes de red como los cortafuegos. En la práctica, una máquina virtual de un proveedor es una máquina que otra organización alimenta, refrigera y virtualiza, pero cuyo sistema operativo parcheas tú. La consecuencia es que la lista de parches pendientes no se reduce al pasar a IaaS: se queda con el cliente.

## Ejemplo

Ejemplo de [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) (sección «Ejemplo mínimo»):

Con estas cinco capas, el número baja de 5 a 5, 3 y 2: en IaaS no cambia porque el sistema operativo y el entorno de ejecución siguen siendo del cliente. Registra versión de Python, comando y salida, y completa el diccionario con las otras siete capas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md)) son:

- **Un depósito o un panel quedan abiertos tras migrar** — causa: se asumió que el proveedor configura lo que solo el cliente puede decidir. Corrección: asignar dueño y revisión a la celda «configuración del servicio».
- **Un tiempo de ejecución deja de recibir parches y nadie se entera** — causa: PaaS: el proveedor retira la versión y el equipo no sigue el calendario. Corrección: suscribirse a los avisos del proveedor y planificar el cambio de versión.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La consecuencia es que la lista de parches pendientes no se reduce al pasar a IaaS: se queda con el cliente. ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md))
- En el modelo, pasar de IaaS a SaaS recorta la exposición a un tercio y deja en pie casi el 61 % del resto; el efecto real depende de cuánto tarda cada proveedor y de cuántos ajustes mantienes. ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sistema operativo](../s/sistema-operativo.md), [Servicio](../s/servicio.md), [Sobre](../s/sobre.md), [PaaS](../p/paas.md), [Responsabilidad compartida](../r/responsabilidad-compartida.md), [SaaS](../s/saas.md).
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

[↑ Glosario](../../README.md) · [← I/o y red](./i-o-y-red.md) · [Idempotencia →](./idempotencia.md)
