# Activo

[↑ Glosario](../../README.md) · [← Actividad](./actividad.md) · [Actor →](./actor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

En seguridad, un **activo** es un dato, capacidad o servicio cuyo daño importa a la organización o a las personas, como las calificaciones o la disponibilidad el día del cierre ([SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md)). Es el punto de partida del modelo de amenazas.

## Por qué importa

Un modelo de amenazas empieza por lo que se quiere conservar y no por lo que se teme. Sin activos definidos no se sabe qué proteger primero, y se terminan arreglando cosas graves que no importan o dejando abiertas las que sí.

## Cómo funciona

Cada activo se asocia a una propiedad que hay que proteger y a un atacante con una razón distinta. En la plataforma de [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md): las **calificaciones** (integridad: que nadie las altere), las **entregas** de cada estudiante (confidencialidad: que solo las lea quien debe), la **disponibilidad el día del cierre** y la **confianza de las familias**. Los atacantes concretan capacidad, paciencia y recursos: un estudiante que desea mejorar su nota conoce la plataforma por dentro y tiene una cuenta válida; un tercero que busca datos de menores parte de internet sin ninguna.

## Ejemplo

[SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) dibuja fronteras, enumera amenazas por elemento, calcula el camino más barato hasta el activo y lo recalcula tras cada decisión. Pide, como transferencia, repetirlo en otro dominio (un taller que gestiona citas): cambian activos y actores, no el procedimiento.

## Errores y confusiones comunes

- **Se arregla lo grave y nada mejora.** Se prioriza por gravedad, no por camino; calcular el camino más barato.
- **Una lista de 80 amenazas sin dueño.** Una fila por amenaza con elemento, respuesta y supuesto.
- **Confundir activo con sistema.** El activo es lo que importa dentro o a través del sistema.

## Límites y cuándo no aplica

Los activos de la clase pertenecen a una plataforma educativa concreta. En otro dominio la lista cambia, y un activo mal valorado desplaza todas las prioridades. Un activo no es sinónimo de «dato»: la disponibilidad y la confianza también lo son.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ventana de gracia](../v/ventana-de-gracia.md), [Capacidad](../c/capacidad.md), [Daño](../d/dano.md), [Disponibilidad](../d/disponibilidad.md), [Frontera de confianza](../f/frontera-de-confianza.md), [Grafo de ataque](../g/grafo-de-ataque.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (95 clases más lo mencionan; las que más):

[SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Saltzer y Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939) — principios de diseño de la protección; autoridad: Proceedings of the IEEE.
- [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) — valores y principios del modelado de amenazas; autoridad: comunidad de profesionales de seguridad.
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — proceso práctico de modelado; autoridad: OWASP.
- [Microsoft: amenazas STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) — categorías por elemento; autoridad: documentación de Microsoft.
- [Schneier, «Attack Trees»](https://www.schneier.com/academic/archives/1999/12/attack_trees/) — árboles de ataque con costos; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Actividad](./actividad.md) · [Actor →](./actor.md)
