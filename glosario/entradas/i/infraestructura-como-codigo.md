# Infraestructura como código

[↑ Glosario](../../README.md) · [← Informe y decisión](./informe-y-decision.md) · [Ingeniería →](./ingenieria.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Práctica de describir la infraestructura en archivos versionados que una herramienta aplica de forma repetible.

Definición de trabajo de [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md).

## Por qué importa

La clase donde se define, [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), existe con este propósito: la clase existe para que puedas declarar infraestructura como código y, sobre todo, entender el archivo que ese código necesita para funcionar: el estado.

## Cómo funciona

[SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. Cada herramienta usa estos términos con matices y debe contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md):

El equipo de la plataforma guarda el estado en un almacén remoto con bloqueo y cifrado, trata su acceso como el de un secreto y exige que todo cambio pase por un plan revisado por una persona distinta de quien lo escribió. Programa un plan solo de lectura cada noche para detectar deriva y abre una incidencia con cada diferencia; cuando la deriva es un arreglo de emergencia, el equipo lo incorpora al código o lo revierte de forma deliberada, no al pasar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)) son:

- **Un apply revierte un arreglo de emergencia** — causa: deriva no incorporada al código. Corrección: revisar las acciones que el código no editó y decidir cada una.
- **Un recurso se crea dos veces o falla por duplicado** — causa: escritura del estado perdida. Corrección: almacén remoto con bloqueo y versión.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada herramienta usa estos términos con matices y debe contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se ejecutó ninguna herramienta de infraestructura ni se tocó un proveedor: el diferenciador, la enumeración y el planificador son modelos del autor, las duraciones y el grafo son sintéticos y no se modelaron límites de tasa ni reemplazos forzados. La siguiente clase mira dónde se aplica todo esto: cuentas, entornos y separación de responsabilidades.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Práctica](../p/practica.md), [Versionado](../v/versionado.md), [Bloqueo del estado](../b/bloqueo-del-estado.md), [Camino crítico](../c/camino-critico.md), [Deriva](../d/deriva.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md), [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md).

**Aparece en los casos de estudio:** [TSB Bank](../../../casos/fallo/tsb.md).

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

[↑ Glosario](../../README.md) · [← Informe y decisión](./informe-y-decision.md) · [Ingeniería →](./ingenieria.md)
