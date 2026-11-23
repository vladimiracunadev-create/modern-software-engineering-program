# Reflexión

[↑ Glosario](../../README.md) · [← Referencia independiente](./referencia-independiente.md) · [Reflog →](./reflog.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Texto de retroalimentación sobre un intento fallido que se usa en el siguiente.

Definición de trabajo de [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md).

## Por qué importa

En [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md), el tema «Reflexión» importa porque una segunda oportunidad con una pista, si hay señal de fallo.

## Cómo funciona

Según [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md):

La reflexión (Shinn et al.) convierte el resultado de un intento fallido en un **texto de retroalimentación** («falló porque el estudiante 3 no tenía contacto; comprueba el contacto antes de enviar») que se añade al contexto del siguiente intento. Cuesta al menos dos llamadas más (reflexionar y volver a planificar) y solo ayuda si hay una **señal de fallo externa**: un código de error, un verificador, una prueba. Sin esa señal, el modelo reflexiona sobre su propia respuesta sin saber si falló, y es fácil que racionalice lo hecho.

Según [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md):

Sirve poco. Sin una señal externa, el modelo evalúa su propio resultado con los mismos sesgos con que lo produjo. Con un verificador, la reflexión recibe una falla concreta y puede mejorar.

## Ejemplo

Ejemplo de [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md) (sección «Preguntas frecuentes»):

Sirve poco. Sin una señal externa, el modelo evalúa su propio resultado con los mismos sesgos con que lo produjo. Con un verificador, la reflexión recibe una falla concreta y puede mejorar.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La reflexión (Shinn et al.) convierte el resultado de un intento fallido en un **texto de retroalimentación** («falló porque el estudiante 3 no tenía contacto; comprueba el contacto antes de enviar») que se añade al contexto del siguiente intento. ([SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Retroalimentación](./retroalimentacion.md), [Sobre](../s/sobre.md), [Plan-and-execute](../p/plan-and-execute.md), [ReAct](./react.md), [Replanificación](./replanificacion.md), [Señal de fallo](../s/senal-de-fallo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md), [SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md), [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md), [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md), [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Referencia independiente](./referencia-independiente.md) · [Reflog →](./reflog.md)
