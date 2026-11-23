# Sobreasignación

[↑ Glosario](../../README.md) · [← Sobre](./sobre.md) · [Sobrecarga →](./sobrecarga.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Admitir peticiones por una suma mayor que la capacidad del nodo, apostando a que no se usarán a la vez.

Definición de trabajo de [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md).

## Por qué importa

En [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), el tema «Sobreasignación» importa porque admitir más de lo que hay compra uso a cambio de riesgo.

## Cómo funciona

Según [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), en la sección «Sobreasignación»:

Si todos los pods usaran siempre lo que piden, convendría que la suma de peticiones igualara la capacidad. Pero el uso medio suele ser inferior y nunca coincide en el tiempo, así que admitir más peticiones que capacidad aprovecha mejor el hardware. El riesgo está en la cola: cuando varios pods suben a la vez, el nodo se satura. Los orquestadores de producción reutilizan los recursos reservados y no usados con esta idea; lo que no pueden evitar es que la apuesta pierda a veces. La pregunta de diseño es cuánto riesgo se tolera por cada punto de uso medio ganado.

## Ejemplo

Ejemplo de [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma de entregas define para cada servicio una petición cercana al uso medio medido y un límite algo mayor, y marca el corrector como de baja prioridad para que lo desplacen antes que a la aplicación web. Revisa el intervalo de lectura de su controlador con el tiempo de arranque de cada servicio y concluye que la aplicación web, con cuatro réplicas, no puede tolerar un hueco de un minuto, así que sube las réplicas a seis y mide el arranque.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los nodos se saturan en la semana de cierre** — causa: sobreasignación calculada con uso medio y no con picos. Corrección: calcular el cociente con el pico y con usos correlacionados. ([SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada orquestador usa estos términos con matices y debe contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún orquestador real ni se midió el tiempo de un clúster: las políticas son versiones simplificadas, el arranque de 7 s, los fallos y la distribución del uso son supuestos del autor y el resultado no se extrapola a otra carga.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Bucle de reconciliación](../b/bucle-de-reconciliacion.md), [Límite de recursos](../l/limite-de-recursos.md), [Petición de recursos](../p/peticion-de-recursos.md), [Planificador](../p/planificador.md), [Reconciliación](../r/reconciliacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kubernetes: kube-scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/) — filtrado y puntuación de nodos; autoridad: documentación oficial de Kubernetes.
- [Kubernetes: controladores](https://kubernetes.io/docs/concepts/architecture/controller/) — bucle de control entre estado actual y deseado; autoridad: documentación oficial de Kubernetes.
- [Kubernetes: ciclo de vida de un pod](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) — reinicios y retardo exponencial; autoridad: documentación oficial de Kubernetes.
- [Kubernetes: gestión de recursos de contenedores](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) — peticiones y límites; autoridad: documentación oficial de Kubernetes.
- [Large-scale cluster management at Google with Borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/) — orquestación de producción y reutilización de recursos; autoridad: artículo de Google (EuroSys 2015).

---

[↑ Glosario](../../README.md) · [← Sobre](./sobre.md) · [Sobrecarga →](./sobrecarga.md)
