# LIMITES.md

[↑ Glosario](../../README.md) · [← Límites de lenguajes declarativos](./limites-de-lenguajes-declarativos.md) · [Limpieza y recuperación →](./limpieza-y-recuperacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Documento que declara lo no ejecutado, lo no medido y las suposiciones del autor.

Definición de trabajo de [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md).

## Por qué importa

La clase donde se define, [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), existe con este propósito: el proyecto final existe para que demuestres, con un producto pequeño pero completo, que sabes construir con agentes desde una especificación y que sabes decir con qué evidencia el producto está terminado.

## Cómo funciona

Según [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md):

La técnica de `SE-567` se aplica ahora a todo el producto. Para cada requisito se prepara una **variante defectuosa** del servicio que lo viola de una manera plausible (un agente que olvida registrar el último umbral, que guarda el estado en memoria, que compara «Silenciada» con distinción de mayúsculas) y se comprueba que la prueba del requisito falla con esa variante y pasa con el servicio correcto. Si una prueba no ha fallado nunca frente a una variante, no hay evidencia de que sea capaz de hacerlo; no se descarta que lo sea, pero la afirmación «este requisito está verificado» no está respaldada. El paquete debe decir, requisito por requisito, si hay variante y si la prueba la detecta.

Según [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo entrega el paquete de *Avisos*. La especificación tiene diez requisitos con identificador y criterio, tres principios de constitución y un registro de dos decisiones. El plan cita requisitos y el analizador de `SE-566` no encuentra incoherencias formales. El agente implementó con autoridad mínima: herramientas de lectura, escritura en el directorio del proyecto y ejecución de las pruebas, con un gancho previo que falla cerrado y un confinamiento de rutas probado con veinte intentos. Las herramientas de terceros están fijadas por huella y el agente en cuarentena es el único que lee notas de docentes. Las acciones irreversibles (enviar el primer lote real) tienen una solicitud con cinco datos y una pausa.

## Ejemplo

Ejemplo de [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo entrega el paquete de *Avisos*. La especificación tiene diez requisitos con identificador y criterio, tres principios de constitución y un registro de dos decisiones. El plan cita requisitos y el analizador de `SE-566` no encuentra incoherencias formales. El agente implementó con autoridad mínima: herramientas de lectura, escritura en el directorio del proyecto y ejecución de las pruebas, con un gancho previo que falla cerrado y un confinamiento de rutas probado con veinte intentos. Las herramientas de terceros están fijadas por huella y el agente en cuarentena es el único que lee notas de docentes.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`LIMITES.md` dice «nada que declarar»** — causa: no se pensó qué no se hizo. Corrección: listar lo no ejecutado, lo no medido y las suposiciones. ([SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los requisitos sin variante se declaran en `LIMITES.md`, y escribir una variante para cada uno es el trabajo pendiente. ([SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md))
- Si no usas ninguno, el proyecto sigue siendo válido como ejercicio de especificación, verificación y operación; declara en `LIMITES.md` que la autoría fue humana. ([SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Suposición](../s/suposicion.md), [Objetivo de punto de recuperación](../o/objetivo-de-punto-de-recuperacion.md), [Paquete de evidencia](../p/paquete-de-evidencia.md), [Producto operable](../p/producto-operable.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (15 clases más lo mencionan; las que más):

[SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jia y Harman](https://doi.org/10.1109/TSE.2010.62) — prueba de mutación; autoridad: IEEE Transactions on Software Engineering.
- [Google SRE: objetivos de nivel de servicio](https://sre.google/sre-book/service-level-objectives/) — indicadores y objetivos; autoridad: libro de Google SRE.

---

[↑ Glosario](../../README.md) · [← Límites de lenguajes declarativos](./limites-de-lenguajes-declarativos.md) · [Limpieza y recuperación →](./limpieza-y-recuperacion.md)
