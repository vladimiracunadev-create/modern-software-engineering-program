# Disposición a pagar

[↑ Glosario](../../README.md) · [← Disposición](./disposicion.md) · [Dispositivo →](./dispositivo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Máximo que un cliente aceptaría pagar por algo.

Definición de trabajo de [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md).

## Por qué importa

La clase donde se define, [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md), existe con este propósito: la clase existe para que trates el precio y el empaquetado como una decisión de ingeniería de producto con consecuencias medibles, y no como un número que alguien pone al final.

## Cómo funciona

Según [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md):

La simulación genera 1 000 clientes cuyo número de puestos sigue una distribución con cola larga (mediana de 5, máximo de 70) y cuya disposición a pagar crece con el tamaño pero menos que proporcionalmente. Con un precio único, el ingreso sube mientras entran compradores y baja cuando los que se pierden pesan más que lo que se gana por cliente: el máximo está en 110 con 351 compradores y 38 610 de ingreso. A 50 el ingreso es 32 700 (más clientes, menos por cliente); a 230, 28 750 (pocos clientes, mucho por cliente). Los clientes grandes pagarían más y los pequeños no pagan nada: **un único precio obliga a elegir a quién dejar fuera o a quién regalarle valor**.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md)) son: Se simularon 1 000 clientes con semilla 34 y se compararon tres diseños de precio con parámetros del autor; no se midió ningún mercado, elasticidad ni competencia, y los parámetros se optimizaron sobre la misma población, lo que favorece a los diseños con más parámetros. Las cifras muestran un método, no un precio recomendable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Empaquetado](../e/empaquetado.md), [Excedente del cliente](../e/excedente-del-cliente.md), [Grandfathering](../g/grandfathering.md), [Meseta](../m/meseta.md), [Métrica de valor](../m/metrica-de-valor.md), [Valla](../v/valla.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Disposición](./disposicion.md) · [Dispositivo →](./dispositivo.md)
