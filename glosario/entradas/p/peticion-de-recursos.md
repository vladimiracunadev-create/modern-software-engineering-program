# Petición de recursos

[↑ Glosario](../../README.md) · [← Petición de decisión](./peticion-de-decision.md) · [PFD media →](./pfd-media.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Cantidad que una unidad reserva y que se usa para decidir dónde cabe.

Definición de trabajo de [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md).

## Por qué importa

La clase donde se define, [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), existe con este propósito: la clase existe para que entiendas qué hace un orquestador cuando decide dónde corre cada unidad y qué hace cuando una falla: es un bucle que compara lo que declaraste con lo que existe y actúa, y un algoritmo de ubicación que empaqueta lo que pides en lo que hay.

## Cómo funciona

[SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. Cada orquestador usa estos términos con matices y debe contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md):

El equipo de la plataforma de entregas define para cada servicio una petición cercana al uso medio medido y un límite algo mayor, y marca el corrector como de baja prioridad para que lo desplacen antes que a la aplicación web. Revisa el intervalo de lectura de su controlador con el tiempo de arranque de cada servicio y concluye que la aplicación web, con cuatro réplicas, no puede tolerar un hueco de un minuto, así que sube las réplicas a seis y mide el arranque.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md)) son:

- **Pods pendientes con CPU libre** — causa: fragmentación de memoria o de CPU entre nodos. Corrección: revisar el orden y los tamaños de pod y medir qué dimensión se agota.
- **Una réplica caída tarda minutos en volver** — causa: intervalo de revisión largo o arranque lento. Corrección: medir el tiempo de arranque y subir réplicas o acortar el intervalo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada orquestador usa estos términos con matices y debe contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún orquestador real ni se midió el tiempo de un clúster: las políticas son versiones simplificadas, el arranque de 7 s, los fallos y la distribución del uso son supuestos del autor y el resultado no se extrapola a otra carga.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Reserva](../r/reserva.md), [Bucle de reconciliación](../b/bucle-de-reconciliacion.md), [Límite de recursos](../l/limite-de-recursos.md), [Planificador](./planificador.md), [Reconciliación](../r/reconciliacion.md), [Sobreasignación](../s/sobreasignacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md).

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

[↑ Glosario](../../README.md) · [← Petición de decisión](./peticion-de-decision.md) · [PFD media →](./pfd-media.md)
