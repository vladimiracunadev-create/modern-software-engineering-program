# Extractor

[↑ Glosario](../../README.md) · [← Extracción](./extraccion.md) · [Extremo →](./extremo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Componente que detecta hechos en la conversación y los convierte en registros.

Definición de trabajo de [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md).

## Por qué importa

En [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), el tema «Almacén externo» importa porque escala y permite versión, a costa de un extractor.

## Cómo funciona

Según [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md):

El almacén guarda hechos como registros: clave (`silencio:curso7`), valor, instante, origen (qué turno o qué persona lo dijo) y versión. Un **extractor** detecta los hechos en la conversación y los escribe; la lectura es por clave (exacta) o por similitud (`SE-594`). En el experimento, con un extractor que acierta el 95 %, el almacén **con versión** (siempre gana el valor más reciente) recupera el 95,2 % con 80 tokens de memoria por pregunta, y el almacén **sin versión** (se conserva el primer valor escrito) recupera el 40,8 %. La diferencia entre las dos es una línea de código: qué ocurre cuando llega una clave que ya existe. Es el mismo problema que el de cualquier caché o réplica: sin una política de actualización, guarda el dato viejo.

Según [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md):

**Diagnóstico paso a paso.** (1) Se busca en el almacén la clave `silencio:curso7`: hay un registro con el día 12. (2) La conversación muestra que la corrección al 20 ocurrió tres días después. (3) El extractor sí detectó la segunda frase, pero la escritura usaba «insertar si no existe» y la ignoró. (4) Se confirma que el almacén no versionaba.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En el experimento, con un extractor que acierta el 95 %, el almacén **con versión** (siempre gana el valor más reciente) recupera el 95,2 % con 80 tokens de memoria por pregunta, y el almacén **sin versión** (se conserva el primer valor escrito) recupera el 40,8 %. ([SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Hecho](../h/hecho.md), [Registro](../r/registro.md), [Caducidad](../c/caducidad.md), [Compactación](../c/compactacion.md), [Contexto de trabajo](../c/contexto-de-trabajo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Extracción](./extraccion.md) · [Extremo →](./extremo.md)
