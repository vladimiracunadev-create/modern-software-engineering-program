# Caducidad

[↑ Glosario](../../README.md) · [← Cadencia de actualización](./cadencia-de-actualizacion.md) · [Caducidad de la evidencia →](./caducidad-de-la-evidencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Momento a partir del cual un registro deja de valer o se borra.

Definición de trabajo de [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md).

## Por qué importa

La clase donde se define, [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), existe con este propósito: la clase existe para que trates la memoria de un agente como lo que es:

## Cómo funciona

Según [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md):

La tabla de costos muestra una paradoja útil: la estrategia que más recupera gasta menos tokens por pregunta. El almacén cuesta, sin embargo, en otro sitio: el extractor (una llamada o una regla por turno), la escritura, la consulta y el mantenimiento del esquema. Y hay una decisión que ninguna de las otras estrategias ofrece: **olvidar a propósito**. Una memoria con datos personales necesita caducidad (un silencio caduca el día indicado), borrado a petición y control de quién puede escribir. Una memoria que solo crece es un archivo de datos personales sin base legal. La política de olvido es parte del diseño y se prueba.

Según [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md):

El equipo de *Avisos* define cuatro tipos de hecho persistente: silencios por curso, preferencias de canal, excepciones de plazo y contactos alternativos. Cada tipo tiene clave, esquema, caducidad y quién puede escribirlo. El agente no escribe directamente: propone un registro con la cita del turno de donde lo sacó y una validación de código comprueba el esquema y que el solicitante tenga permiso sobre el curso. Las lecturas se hacen por clave antes de cada respuesta que dependa de un hecho y la respuesta cita el origen («según la instrucción de María del 3 de noviembre»). Cada mes se revisa una muestra de 50 registros contra la conversación original y se mide cuántos eran falsos o estaban obsoletos.

## Ejemplo

Ejemplo de [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) (sección «Ejemplo mínimo»):

Un almacén de hechos con versión y caducidad:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md)) son: Las conversaciones, la fracción de turnos con hechos, el acierto del extractor y la retención del resumen son parámetros del autor; no se midió ningún modelo ni ningún producto de memoria. El siguiente paso, `SE-594`, trata la lectura cuando no se conoce la clave: qué es un embedding, cómo se recupera por similitud y qué cambia cuando el agente decide cuándo y qué recuperar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](../r/registro.md), [Compactación](./compactacion.md), [Contexto de trabajo](./contexto-de-trabajo.md), [Extractor](../e/extractor.md), [Memoria de largo plazo](../m/memoria-de-largo-plazo.md), [Resumen con pérdida](../r/resumen-con-perdida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (32 clases más lo mencionan; las que más):

[SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md), [SE-231](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md), [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), [SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md), [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cadencia de actualización](./cadencia-de-actualizacion.md) · [Caducidad de la evidencia →](./caducidad-de-la-evidencia.md)
