# Frescura

[↑ Glosario](../../README.md) · [← Frecuencia de despliegue](./frecuencia-de-despliegue.md) · [Frontend Engineer →](./frontend-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Edad del dato más reciente.

Definición de trabajo de [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md).

## Por qué importa

En [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), el tema «Frescura» importa porque detecta que algo dejó de llegar.

## Cómo funciona

Según [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md):

Volumen: ¿llegaron las filas esperadas? Unicidad: ¿hay claves repetidas? Nulos: ¿falta lo que debería estar? Integridad referencial: ¿cada clave extranjera apunta a algo? Frescura: ¿es reciente el dato más nuevo? Distribución: ¿se parecen los valores a lo habitual? En el laboratorio, una tabla de 5 000 pedidos recibió seis variantes defectuosas. La carga parcial falló el volumen; los duplicados fallaron volumen y unicidad; los nulos en el cliente, la comprobación de nulos; los clientes huérfanos, la integridad referencial; los datos atrasados, la frescura; los importes multiplicados por cien (un cambio de unidad) solo fallaron la distribución. La variante limpia no falló ninguna. Ninguna comprobación vio más de dos variantes: su ceguera es tan importante como su vista.

Según [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md):

El equipo de *Avisos* levanta una tabla con sus diez conjuntos de datos más consultados y, para cada uno, anota qué comprobaciones tiene. Encuentra que tres tienen solo validación de esquema. Prioriza por impacto: el hecho de lecturas recibe volumen, unicidad, nulos y frescura; el mart ejecutivo, distribución además de volumen. Define la política: unicidad y volumen detienen la publicación; la distribución publica con una marca. Fija una métrica del propio sistema: el porcentaje de alertas que terminaron en una acción (corregir, ajustar umbral, aceptar con anotación). A los dos meses, la métrica baja del 30 % al 12 % de acciones y el equipo recalibra la mediana por día de la semana en tres conjuntos antes de que alguien silencie el canal.

## Ejemplo

Ejemplo de [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* levanta una tabla con sus diez conjuntos de datos más consultados y, para cada uno, anota qué comprobaciones tiene. Encuentra que tres tienen solo validación de esquema. Prioriza por impacto: el hecho de lecturas recibe volumen, unicidad, nulos y frescura; el mart ejecutivo, distribución además de volumen. Define la política: unicidad y volumen detienen la publicación; la distribución publica con una marca. Fija una métrica del propio sistema: el porcentaje de alertas que terminaron en una acción (corregir, ajustar umbral, aceptar con anotación).

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La carga parcial falló el volumen; los duplicados fallaron volumen y unicidad; los nulos en el cliente, la comprobación de nulos; los clientes huérfanos, la integridad referencial; los datos atrasados, la frescura; los importes multiplicados por cien (un cambio de unidad) solo fallaron la distribución. ([SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Comprobación de calidad](../c/comprobacion-de-calidad.md), [Deriva de distribución](../d/deriva-de-distribucion.md), [Integridad referencial](../i/integridad-referencial.md), [MAD](../m/mad.md), [Observabilidad de datos](../o/observabilidad-de-datos.md), [Volumen](../v/volumen.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (23 clases más lo mencionan; las que más):

[SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md), [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Frecuencia de despliegue](./frecuencia-de-despliegue.md) · [Frontend Engineer →](./frontend-engineer.md)
