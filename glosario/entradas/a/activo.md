# Activo

[↑ Glosario](../../README.md) · [← Actividad](./actividad.md) · [Actor →](./actor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Dato, capacidad o servicio cuyo daño importa a la organización o a las personas, como las calificaciones o la disponibilidad el día del cierre.

Definición de trabajo de [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md).

## Por qué importa

En [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), el tema «Activos, atacantes y supuestos» importa porque sin saber qué se protege y de quién, cada defensa se justifica por costumbre.

## Cómo funciona

Según [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md):

Un modelo de amenazas empieza por lo que se quiere conservar y no por lo que se teme. En la plataforma los activos son las calificaciones (integridad: que nadie las altere), las entregas de cada estudiante (confidencialidad: que solo las lea quien debe), la disponibilidad el día del cierre y la confianza de las familias. A cada activo le corresponde un atacante que lo quiere por una razón distinta: un estudiante que desea mejorar su nota, un tercero que busca datos de menores para venderlos, un compañero que quiere copiar una entrega, un exalumno con rencor. El atacante no es una abstracción: determina capacidad, paciencia y recursos. Un estudiante conoce la plataforma por dentro y tiene una cuenta válida; un tercero parte de internet sin ninguna.

Según [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md):

Traslada el análisis a otro dominio (por ejemplo, un taller que gestiona citas): cambia los activos y los actores y conserva el procedimiento de dibujar fronteras, enumerar por elemento, costear caminos y mantener el modelo. La transferencia está lograda cuando puedes decir qué frontera de ese dominio es la más barata de cruzar y qué evidencia la contradiría, no cuando el diagrama se parece al de la plataforma.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md):

El equipo de la plataforma dibuja el diagrama con cuatro procesos (API, servicio de calificación, trabajador de archivos y notificador), dos almacenes, tres actores y cinco fronteras. En el cruce navegador-API enumera por STRIDE nueve amenazas, descarta tres con razón escrita y deja seis; al ponerles costo descubre que la más barata es la elevación de privilegios por el campo de rol del registro.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md)) son:

- **Se arregla lo grave y nada mejora** — causa: se prioriza por gravedad, no por camino. Corrección: calcular el camino más barato y recalcularlo tras cada decisión.
- **El modelo es una lista de 80 amenazas sin dueño** — causa: se enumera sin descartar ni decidir. Corrección: una fila por amenaza con elemento, respuesta y supuesto.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En la plataforma los activos son las calificaciones (integridad: que nadie las altere), las entregas de cada estudiante (confidencialidad: que solo las lea quien debe), la disponibilidad el día del cierre y la confianza de las familias. ([SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md))

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
