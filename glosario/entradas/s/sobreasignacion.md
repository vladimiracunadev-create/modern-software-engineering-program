# Sobreasignación

[↑ Glosario](../../README.md) · [← Sobre](./sobre.md) · [Sobrecarga →](./sobrecarga.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

La **sobreasignación** (*overcommit*) es admitir peticiones de recursos por una suma mayor que la capacidad del nodo, apostando a que no se usarán todas a la vez ([SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md)). Es una práctica habitual de los orquestadores para aprovechar mejor el hardware.

## Por qué importa

Reservar recursos según lo que cada carga pide, sin margen, deja mucho hardware ocioso, porque el uso medio suele ser inferior a lo pedido. Sobreasignar baja el costo, pero cambia el modo de fallo: de «no cabe» a «se satura si coinciden». La decisión que cambia es cuánto riesgo se tolera por cada punto de uso medio ganado.

## Cómo funciona

[SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) razona así. Si todos los pods usaran siempre lo que piden, convendría que la suma de peticiones igualara la capacidad. Pero el uso medio suele ser inferior y **nunca coincide en el tiempo**, así que admitir más peticiones que capacidad aprovecha mejor el hardware. Los orquestadores de producción reutilizan los recursos reservados y no usados con esta idea.

El riesgo está en la **cola de la distribución**: cuando varios pods suben a la vez, el nodo se satura. La apuesta pierde a veces, y eso no se puede evitar, solo dimensionar. La clave de diseño es medir con qué probabilidad coinciden los picos. Si los usos son independientes, sumarlos con una media funciona bien; si están **correlacionados** (todos suben en la semana de cierre), la media engaña y la sobreasignación calculada con ella satura los nodos justo en el peor momento.

Por eso la corrección que da la clase es calcular el cociente de sobreasignación con el **pico** y con usos **correlacionados**, no con el uso medio. Se relaciona con las peticiones y límites de recursos, que son lo que el planificador usa para decidir dónde cabe cada carga, y con la reconciliación continua del orquestador.

## Ejemplo

Un nodo tiene 10 unidades de capacidad. Se admiten 15 unidades en peticiones, porque cada pod usa en promedio 6 de cada 10 pedidas. Normalmente cabe. En la semana de cierre todos los pods suben a la vez, la demanda supera la capacidad y los nodos se saturan. Un cociente calculado con el pico y la correlación habría sido menor. Escenario de [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) con datos sintéticos.

## Errores y confusiones comunes

- **Los nodos se saturan en la semana de cierre**: sobreasignación calculada con uso medio y no con picos; se corrige calculando el cociente con el pico y con usos correlacionados.
- **Suponer que los usos son independientes** sin comprobarlo.
- **Confundir petición con límite**: la petición reserva; el límite acota.
- **Sobreasignar todo por igual**: lo crítico se trata distinto.

## Límites y cuándo no aplica

[SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) precisa que no usó ningún orquestador real: las políticas son simplificaciones, el arranque de 7 s, los fallos y la distribución del uso son supuestos del autor, y el resultado no se extrapola a otra carga. No aplica a cargas que necesitan garantías estrictas de recursos (latencia crítica, tiempo real), ni a memoria sin margen, donde el exceso no se comparte con elegancia: un nodo sin memoria mata procesos.

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
