# Valla

[↑ Glosario](../../README.md) · [← Validador de subida](./validador-de-subida.md) · [Valor →](./valor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Límite o función que separa un segmento de otro.

Definición de trabajo de [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md).

## Por qué importa

La clase donde se define, [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md), existe con este propósito: la clase existe para que trates el precio y el empaquetado como una decisión de ingeniería de producto con consecuencias medibles, y no como un número que alguien pone al final.

## Cómo funciona

Según [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md):

**Diagnóstico paso a paso.** (1) Se compara la conversión por cohorte: las cuentas nuevas posteriores al cambio convierten menos, las anteriores no cambian. (2) Se mide el momento de conversión histórico: el 63 % de las conversiones ocurría cuando la cuenta alcanzaba el límite de 2 proyectos. (3) Con 5 proyectos, las cuentas tardan más en llegar al límite y una parte nunca llega: el límite era la valla que provocaba la decisión. (4) El uso del producto sí subió (más proyectos creados) pero con proyectos de baja actividad. (5) Se prueba una alternativa que mantiene 2 proyectos activos y permite archivar sin límite, de modo que el cliente no pierde su trabajo pero la valla persiste; la conversión se recupera a 3,8 % en seis semanas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- (3) Con 5 proyectos, las cuentas tardan más en llegar al límite y una parte nunca llega: el límite era la valla que provocaba la decisión. ([SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Límite](../l/limite.md).
- **Ver también:** [Función](../f/funcion.md), [Segmento](../s/segmento.md), [Disposición a pagar](../d/disposicion-a-pagar.md), [Empaquetado](../e/empaquetado.md), [Excedente del cliente](../e/excedente-del-cliente.md), [Grandfathering](../g/grandfathering.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «fence».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Validador de subida](./validador-de-subida.md) · [Valor →](./valor.md)
