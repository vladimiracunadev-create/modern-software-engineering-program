# Meseta

[↑ Glosario](../../README.md) · [← Merge --abort](./merge-abort.md) · [Meta-verificación →](./meta-verificacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Zona de la curva de ingreso donde cambiar el precio apenas cambia el ingreso.

Definición de trabajo de [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md).

## Por qué importa

La clase donde se define, [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md), existe con este propósito: la clase existe para que trates el precio y el empaquetado como una decisión de ingeniería de producto con consecuencias medibles, y no como un número que alguien pone al final.

## Cómo funciona

Según [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md):

Cerca del máximo, el ingreso varía poco: entre 90 y 150 queda dentro del 2 % del máximo (de 37 950 a 38 610). La consecuencia práctica es que discutir si el precio debe ser 99 o 119 es discutir poco; lo que vale la pena discutir es la forma del precio. En un producto real, la meseta es una invitación a elegir por otros criterios (simplicidad, percepción, competidores, margen mínimo) en lugar de optimizar la última unidad. El descenso hacia la derecha, en cambio, es abrupto: pasar de 150 a 230 cuesta un 24 % del ingreso. Es más barato equivocarse hacia la izquierda de la meseta que hacia la derecha.

## Ejemplo

Caso medido en la sección «La curva de ingreso tiene una meseta, y eso es una buena noticia» de [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md):

Cerca del máximo, el ingreso varía poco: entre 90 y 150 queda dentro del 2 % del máximo (de 37 950 a 38 610). La consecuencia práctica es que discutir si el precio debe ser 99 o 119 es discutir poco; lo que vale la pena discutir es la forma del precio. En un producto real, la meseta es una invitación a elegir por otros criterios (simplicidad, percepción, competidores, margen mínimo) en lugar de optimizar la última unidad. El descenso hacia la derecha, en cambio, es abrupto: pasar de 150 a 230 cuesta un 24 % del ingreso.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md)) son: Se simularon 1 000 clientes con semilla 34 y se compararon tres diseños de precio con parámetros del autor; no se midió ningún mercado, elasticidad ni competencia, y los parámetros se optimizaron sobre la misma población, lo que favorece a los diseños con más parámetros. Las cifras muestran un método, no un precio recomendable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Zona](../z/zona.md), [Disposición a pagar](../d/disposicion-a-pagar.md), [Empaquetado](../e/empaquetado.md), [Excedente del cliente](../e/excedente-del-cliente.md), [Grandfathering](../g/grandfathering.md), [Métrica de valor](./metrica-de-valor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Merge --abort](./merge-abort.md) · [Meta-verificación →](./meta-verificacion.md)
