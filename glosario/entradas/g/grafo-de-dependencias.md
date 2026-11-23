# Grafo de dependencias

[↑ Glosario](../../README.md) · [← Grafo de ataque](./grafo-de-ataque.md) · [Grandfathering →](./grandfathering.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Dice qué recalcular y en qué orden.

Es uno de los temas de [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), donde se enseña como «Grafo de dependencias».

## Por qué importa

En [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), el tema «Grafo de dependencias» importa porque dice qué recalcular y en qué orden.

En [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), el tema «Grafo de dependencias» importa porque fija el orden y el paralelismo posible.

## Cómo funciona

Según [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md):

Elige una tabla que se cargue periódicamente en tu organización. Ejecuta su trabajo dos veces sobre una partición de prueba, anota si cambia el resultado y escribe, con el grafo de dependencias, qué habría que recalcular si se corrigiera el dato de hace tres semanas.

## Ejemplo

Caso medido en la sección «El grafo de dependencias dice qué recalcular» de [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md):

Las tareas forman un grafo acíclico dirigido: cada tarea depende de otras. El laboratorio tiene nueve tareas (dos crudas, dos intermedias, una dimensión, un hecho, dos marts y un informe). Un orden topológico válido es: `raw_customers`, `raw_orders`, `stg_customers`, `dim_customer`, `stg_orders`, `fact_sales`, `mart_city`, `mart_daily`, `report_exec`. Si cambia `raw_orders` hay que recalcular 5 tareas; si cambia `raw_customers`, 6; si cambia `fact_sales`, 3. Sin el grafo, la corrección se propaga a mano y se olvida un mart. Un ciclo no tiene orden y se rechaza: un orquestador que lo acepta no termina.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Ejecuta su trabajo dos veces sobre una partición de prueba, anota si cambia el resultado y escribe, con el grafo de dependencias, qué habría que recalcular si se corrigiera el dato de hace tres semanas. ([SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Backfill](../b/backfill.md), [Bloqueo del estado](../b/bloqueo-del-estado.md), [Camino crítico](../c/camino-critico.md), [Dato tardío](../d/dato-tardio.md), [Deriva](../d/deriva.md), [Determinismo](../d/determinismo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), [SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), [SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md).

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

[↑ Glosario](../../README.md) · [← Grafo de ataque](./grafo-de-ataque.md) · [Grandfathering →](./grandfathering.md)
