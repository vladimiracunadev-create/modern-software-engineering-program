# Plan

[↑ Glosario](../../README.md) · [← Pivote](./pivote.md) · [Plan adaptativo →](./plan-adaptativo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

En el sentido principal del programa ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)), un **plan** es el cálculo de las acciones necesarias para llevar lo existente a lo declarado, previo a aplicarlas: en infraestructura como código, la lista de cambios que una herramienta haría. El término es muy general y el programa lo usa con otros sentidos que esta entrada distingue:

- En [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md): la lista de acciones que la herramienta calcularía para llevar el estado registrado y el real al deseado (mismo sentido que [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)).
- En [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md): un paquete comercial con precio, ciclo y derechos (plan de suscripción).
- En [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md): el artefacto que decide cómo se construye (tecnología, arquitectura, restricciones) y que debe citar los requisitos que satisface.

Esta entrada desarrolla el de infraestructura.

## Por qué importa

Aplicar cambios de infraestructura sin verlos antes es actuar a ciegas. El plan separa «qué haría» de «hacerlo» y abre un punto de revisión humana. La decisión que cambia es que todo cambio pase por un plan revisado por una persona distinta de quien lo escribió, antes de aplicarse.

## Cómo funciona

La herramienta compara tres cosas: el **código** (lo declarado), el **estado** que guarda de lo que cree que existe, y la **realidad**. [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) introduce la **deriva**: la diferencia entre lo que el estado cree y lo que existe, nacida de un cambio hecho fuera del código (un arreglo de emergencia, una consola, otra herramienta). Un plan que solo compara el código con el estado no la ve; uno que antes refresca el estado con la realidad la ve y propone revertirla. Ninguna conducta es incorrecta: la primera es rápida y ciega; la segunda es exacta y puede deshacer un arreglo necesario. Lo importante es la decisión explícita: incorporar el cambio al código o revertirlo, tomada por una persona antes del `apply`.

El equipo de la clase guarda el estado en un almacén remoto con bloqueo y cifrado, programa un plan de solo lectura cada noche para detectar deriva y abre una incidencia con cada diferencia; divide la infraestructura en estados separados (red, datos, aplicación) para que un cambio en la aplicación no pueda destruir la base de datos.

## Ejemplo

Un cambio pequeño modifica un atributo de una base de datos. El plan muestra «destruir y recrear» porque ese atributo fuerza reemplazo. Al leerlo, la persona que revisa detiene el cambio y protege el recurso con datos. Sin plan, la base se habría destruido. Caso de [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md).

## Errores y confusiones comunes

- **Un cambio pequeño destruye una base de datos**: atributo que fuerza reemplazo; se corrige leyendo el plan y protegiendo los recursos con datos.
- **El plan propone crear algo que ya existe**: estado perdido o desactualizado; bloqueo y versionado del estado, e importar si falta ([SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md)).
- **La deriva se descubre semanas después**: sin comprobación periódica; plan sin aplicar cada pocas horas con responsable.
- **Mezclar sentidos**: un plan comercial no es un plan de infraestructura.

## Límites y cuándo no aplica

El plan refleja lo que la herramienta puede ver: no detecta lo que no gestiona. Un plan aprobado sin lectura real es una formalidad. Y «lo existente» depende de que el estado esté actualizado; con un estado perdido, el plan puede ser engañoso. Para entornos desechables de prueba, la revisión humana de cada plan puede ser innecesaria.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Arquitectura](../a/arquitectura.md), [Artefacto](../a/artefacto.md), [Ciclo](../c/ciclo.md), [Derecho](../d/derecho.md), [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Bloqueo del estado](../b/bloqueo-del-estado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (155 clases más lo mencionan; las que más):

[SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), [SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Terraform: estado](https://developer.hashicorp.com/terraform/language/state) — propósito del estado, datos sensibles y bloqueo; autoridad: documentación oficial de HashiCorp.
- [OpenTofu: documentación](https://opentofu.org/docs/) — bifurcación abierta con el mismo modelo declarativo; autoridad: proyecto OpenTofu.
- [Terraform: destroy](https://developer.hashicorp.com/terraform/cli/commands/destroy) — destrucción de los objetos gestionados; autoridad: documentación oficial de HashiCorp.
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — operaciones como código; autoridad: documentación del proveedor.
- [Python: itertools](https://docs.python.org/3/library/itertools.html) — permutaciones usadas para enumerar intercalaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Pivote](./pivote.md) · [Plan adaptativo →](./plan-adaptativo.md)
