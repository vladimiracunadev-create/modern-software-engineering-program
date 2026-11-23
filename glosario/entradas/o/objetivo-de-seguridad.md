# Objetivo de seguridad

[↑ Glosario](../../README.md) · [← Objetivo de punto de recuperación](./objetivo-de-punto-de-recuperacion.md) · [Objetivo táctil →](./objetivo-tactil.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Requisito de más alto nivel derivado de un peligro.

Definición de trabajo de [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md).

## Por qué importa

La clase donde se define, [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), existe con este propósito: la clase existe para que entiendas cómo el sector del automóvil convierte un análisis de peligros en un nivel de rigor de desarrollo y cómo se demuestra que los mecanismos de diagnóstico del producto cubren lo que dicen cubrir.

## Cómo funciona

Según [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md):

El análisis parte de situaciones concretas de uso («conducción en autopista a alta velocidad») y de fallos del sistema que las vuelven peligrosas («solicitud de par mucho mayor que el pedido»). Para cada combinación se juzgan tres ejes: cuán grave sería el daño, con qué frecuencia el vehículo está en esa situación y cuánto puede una persona conductora evitar el daño por su propia acción. De la combinación sale el nivel ASIL del **objetivo de seguridad**, una frase de alto nivel («evitar un par solicitado superior al pedido por la persona conductora»). La tabla exacta que asigna el nivel pertenece a la norma y no se reproduce; lo importante para el criterio profesional es que cada valoración lleve su razón escrita y que dos revisores puedan discutirla.

Según [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md):

Significa que el objetivo de seguridad que el sistema debe satisfacer tiene un riesgo asociado mayor y por tanto exige más rigor y más evidencia. No es una propiedad del producto: un sistema ASIL D mal verificado es menos seguro que uno ASIL B bien hecho.

## Ejemplo

Ejemplo de [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) (sección «Preguntas frecuentes»):

Significa que el objetivo de seguridad que el sistema debe satisfacer tiene un riesgo asociado mayor y por tanto exige más rigor y más evidencia. No es una propiedad del producto: un sistema ASIL D mal verificado es menos seguro que uno ASIL B bien hecho.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md)) son: Las tasas, las coberturas por componente y el cálculo de par son del autor; el modelo de fallos es de un bit; los valores de referencia de las métricas no se verificaron contra la norma de pago; no se reproduce ninguna tabla ni se afirma conformidad.

## Relación con otros conceptos

- **Prerrequisito:** [Peligro](../p/peligro.md).
- **Ver también:** [ASIL](../a/asil.md), [Cobertura de diagnóstico](../c/cobertura-de-diagnostico.md), [Descomposición](../d/descomposicion.md), [Fallo latente](../f/fallo-latente.md), [FIT](../f/fit.md), [QM](../q/qm.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Objetivo de punto de recuperación](./objetivo-de-punto-de-recuperacion.md) · [Objetivo táctil →](./objetivo-tactil.md)
