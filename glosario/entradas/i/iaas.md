# IaaS

[↑ Glosario](../../README.md) · [← I/o y red](./i-o-y-red.md) · [Idempotencia →](./idempotencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

**IaaS** (infraestructura como servicio) es el servicio que entrega cómputo, red y almacenamiento virtualizados sobre los que el cliente instala y opera su propio sistema operativo y software ([SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md)). La definición del programa sigue la de NIST: la capacidad de aprovisionar procesamiento, almacenamiento y redes en los que el consumidor puede ejecutar software arbitrario, incluidos sistemas operativos y aplicaciones.

## Por qué importa

Pasar a una nube no traslada todas las responsabilidades al proveedor. IaaS es el modelo que menos traslada: el proveedor aporta el hardware y la virtualización, y el cliente conserva lo que corre encima. La decisión que cambia es qué se espera del proveedor y qué sigue siendo propio, sobre todo en seguridad y operación.

## Cómo funciona

[SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) precisa el reparto. El consumidor no gestiona la infraestructura subyacente, pero sí el sistema operativo, el almacenamiento y las aplicaciones desplegadas y, de forma limitada, algunos componentes de red como los cortafuegos. En la práctica, una máquina virtual de un proveedor es una máquina que otra organización alimenta, refrigera y virtualiza, pero cuyo sistema operativo parcheas tú.

Por eso la clase llega a una consecuencia concreta: la lista de parches pendientes no se reduce al pasar a IaaS; se queda con el cliente. Frente a ello, PaaS traslada al proveedor el sistema operativo y el tiempo de ejecución, y SaaS traslada además la aplicación. En el modelo de exposición de la clase, pasar de IaaS a SaaS recorta la exposición a un tercio y deja en pie casi el 61 % del resto; el efecto real depende de cuánto tarda cada proveedor y de cuántos ajustes mantiene el cliente. Es la base de la **responsabilidad compartida**: el proveedor protege la nube, el cliente protege lo que pone en ella.

## Ejemplo

Una organización migra su servidor de aplicaciones a una máquina virtual de un proveedor. El proveedor se ocupa del hardware, la energía y la virtualización; la organización sigue aplicando parches al sistema operativo, configurando el cortafuegos y actualizando la aplicación. Si esperaba que el proveedor aplicara los parches, tiene una vulnerabilidad abierta. Ejemplo ilustrativo del reparto de [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md).

## Errores y confusiones comunes

- **Un depósito o un panel quedan abiertos tras migrar**: se asumió que el proveedor configura lo que solo el cliente puede decidir; se corrige asignando dueño y revisión a la configuración del servicio.
- **Creer que la nube elimina el trabajo de parches**: en IaaS se queda con el cliente.
- **Confundirlo con PaaS**: en PaaS el proveedor retira versiones y el equipo debe seguir su calendario, o el tiempo de ejecución deja de recibir parches sin aviso.
- **Tratar «la nube» como un único modelo de responsabilidad**.

## Límites y cuándo no aplica

[SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) presenta un modelo de exposición con supuestos del autor; no mide proveedores reales. IaaS da el máximo control y flexibilidad (cualquier sistema operativo, cualquier software), pero ese control es justo lo que se paga con trabajo operativo; si el equipo no puede asumirlo, un modelo más alto (PaaS o SaaS) puede ser más seguro aunque limite la configuración.

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
