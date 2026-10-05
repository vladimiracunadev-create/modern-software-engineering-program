# 🤖 AI-Augmented Software Engineer

> Usa copilots y agentes para acelerar trabajo verificable sin delegar especificación,
> seguridad, arquitectura ni responsabilidad profesional.
>
> **Entrada habitual:** después de fundamentos de ingeniería · **Foco:** contexto,
> herramientas, evals y guardrails · **Evidencia central:** cambio asistido reproducible

## 🧭 Qué es y por qué importa

No es un oficio separado de la ingeniería: es una forma aumentada de ejercerla. El rol
selecciona tareas apropiadas, prepara contexto, limita herramientas, exige comprobaciones
deterministas y revisa resultados. Puede coordinar coding agents, terminal agents y
flujos multiagente, pero nunca interpreta “el agente terminó” como “el software funciona”.

## 🗓️ Un día en el puesto

- convertir una necesidad en criterios de salida observables;
- preparar instrucciones, archivos y límites de herramientas;
- pedir alternativas y revisar supuestos del modelo;
- ejecutar tests, linters, análisis y benchmarks;
- investigar una regresión o API inventada;
- registrar coste, latencia, provenance y decisión humana.

## ✅ Responsabilidades y límites

- Mantiene el ciclo HUMANO ESPECIFICA → IA PROPONE → HERRAMIENTAS VERIFICAN →
  HUMANO REVISA → SISTEMA VALIDA.
- Protege secretos, licencias y datos sensibles.
- No permite cambios irreversibles sin autorización y límites.
- No acepta tests generados que solo confirman la implementación.
- No usa agentes para saltarse comprensión del repositorio.

## 🧠 Qué necesitas saber

- ingeniería de software suficiente para evaluar la salida;
- prompting, context engineering, tools, MCP, skills y memoria;
- repository instructions, permisos y sandboxing;
- evals, benchmarks, regression suites y deterministic checks;
- hallucinated APIs, dependencias falsas, drift y loops;
- coste, latencia, confiabilidad, reproducibilidad y revisión humana.

## 📚 Tu ruta en el programa

1. Parte 00, partes 05 y 08–09: criterio, programación, debugging y dependencias.
2. Partes 12–13 y 16–17: requisitos, SPEC, colaboración y documentación.
3. Partes 24 y 30–35: diseño, pruebas, seguridad, pipeline y operación.
4. [Parte 38 — Desarrollo de software asistido por IA](../classes/part-38-desarrollo-de-software-asistido-por-ia/README.md).
5. [Parte 39 — SPEC, agentes y ciclo de vida agentic](../classes/part-39-spec-agentes-y-ciclo-de-vida-agentic/README.md).

## 🧪 Evidencia de portafolio

- especificación y criterios antes de la generación;
- registro de herramientas, permisos y contexto entregado;
- comparación manual/asistida en calidad, coste y tiempo;
- eval que captura APIs falsas, regresiones o supuestos ocultos;
- cambio con tests independientes y revisión de seguridad/licencia;
- recuperación de un loop o acción fallida sin pérdida de estado.

## 📈 Progresión

La progresión sigue la ruta base —Junior, Senior, Staff— y añade capacidad de
orquestación. Un principiante no se vuelve senior por generar más código; necesita
reconocer fallos, operar el resultado y justificar decisiones.

## ⚠️ Mitos frecuentes

- “El modelo conoce el repositorio.” Solo conoce el contexto suministrado.
- “Más agentes producen mejor resultado.” También aumentan coordinación y coste.
- “Los tests generados verifican objetivamente.” Pueden repetir el mismo supuesto falso.
- “Autónomo significa sin supervisión.” La autonomía debe limitarse por riesgo.

## 🚀 Siguientes pasos

1. Elige una tarea pequeña con oráculo determinista.
2. Escribe criterios y límites antes de invocar el modelo.
3. Compara resultado manual y asistido con la misma suite.
4. Conserva fallos, coste y latencia; ajusta el flujo, no solo el prompt.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
