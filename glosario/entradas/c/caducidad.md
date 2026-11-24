# Caducidad

[↑ Glosario](../../README.md) · [← Cadencia de actualización](./cadencia-de-actualizacion.md) · [Caducidad de la evidencia →](./caducidad-de-la-evidencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

La **caducidad** es el momento a partir del cual un registro deja de valer o se borra. En [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) se aplica a la memoria de un agente; en [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), a las exclusiones de una estrategia de pruebas.

## Por qué importa

Lo que se guarda para siempre se vuelve obsoleto y, si son datos personales, un riesgo. Una memoria con datos personales necesita caducidad, borrado a petición y control de quién escribe ([SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md)). Es una decisión que ninguna otra estrategia de memoria ofrece: **olvidar a propósito**.

## Cómo funciona

Cada tipo de hecho persistente tiene clave, esquema, caducidad y quién puede escribirlo. El agente no escribe directamente: propone un registro con la cita del turno de donde lo sacó, y una validación de código comprueba el esquema y que quien solicita tenga permiso. La caducidad hace que lo almacenado deje de ser consultado cuando pierde vigencia.

## Ejemplo

[SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md): el equipo de *Avisos* define cuatro tipos de hecho persistente (silencios por curso, preferencias de canal, excepciones de plazo y contactos alternativos); un silencio caduca el día indicado.

## Errores y confusiones comunes

Guardar sin fecha de vencimiento; borrar al caducar sin comprobar que algo no depende del registro.

## Límites y cuándo no aplica

La caducidad reduce el volumen y el riesgo, pero no sustituye al borrado a petición ni a la validación del esquema.

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
