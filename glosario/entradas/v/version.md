# Versión

[↑ Glosario](../../README.md) · [← Verificador independiente](./verificador-independiente.md) · [Versión de esquema →](./version-de-esquema.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Marca que permite decidir qué valor de una clave es el vigente.

Definición de trabajo de [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md).

## Por qué importa

En [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), el tema «Almacén externo» importa porque escala y permite versión, a costa de un extractor.

## Cómo funciona

Según [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md):

La estrategia más simple es enviar toda la conversación mientras quepa. Cuando se llena, hay que descartar algo, y lo natural es descartar lo más antiguo. En el experimento, con un presupuesto de 2 000 tokens y 80 turnos, el sistema envía unos 1 973 tokens y recupera el 67,1 % de los hechos vigentes: lo que cayó fuera del presupuesto simplemente no está. El fallo es silencioso: el modelo no sabe que se descartó nada y contesta con lo que ve, que puede ser una versión intermedia de un hecho que cambió varias veces. Además, enviar 2 000 tokens en cada llamada cuesta aunque la pregunta sea sobre un dato.

Según [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md):

Para el contexto reciente, a menudo sí. Para compromisos que deben sobrevivir (una fecha de silencio), no: se guardan como hechos con clave y versión, no como prosa dentro de un resumen.

## Ejemplo

Ejemplo de [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) (sección «Ejemplo mínimo»):

Un almacén de hechos con versión y caducidad:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El fallo es silencioso: el modelo no sabe que se descartó nada y contesta con lo que ve, que puede ser una versión intermedia de un hecho que cambió varias veces. ([SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](./valor.md), [Caducidad](../c/caducidad.md), [Compactación](../c/compactacion.md), [Contexto de trabajo](../c/contexto-de-trabajo.md), [Extractor](../e/extractor.md), [Memoria de largo plazo](../m/memoria-de-largo-plazo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (550 clases más lo mencionan; las que más):

[SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md), [SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md), [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Verificador independiente](./verificador-independiente.md) · [Versión de esquema →](./version-de-esquema.md)
