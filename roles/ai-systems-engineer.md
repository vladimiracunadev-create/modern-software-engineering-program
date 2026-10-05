# 🧠 AI Systems Engineer

> Integra modelos en productos mediante datos, evaluaciones, guardrails y operación,
> sin confundir una demo probabilística con una capacidad confiable.
>
> **Entrada habitual:** semi-senior/senior · **Foco:** sistemas con modelos y evals
> · **Evidencia central:** capacidad de IA evaluada contra baseline, coste y riesgo

## 🧭 Qué es y por qué importa

Este rol construye el sistema alrededor del modelo: contrato, recuperación de contexto,
herramientas, seguridad, evaluación, fallback, observabilidad y revisión humana. No es
investigación de modelos fundacionales; integra capacidades probabilísticas en software.

## 🗓️ Un día en el puesto

- convertir un caso de uso en dataset y criterios de evaluación;
- comparar prompt, modelo, recuperación o herramienta;
- investigar alucinación, fuga de datos o regresión;
- revisar latencia, tokens, coste y fallback;
- desplegar un cambio controlado y analizar resultados.

## ✅ Responsabilidades y límites

- Responde por comportamiento del sistema completo, no sólo del modelo.
- Separa evaluación offline, online y revisión humana.
- No usa output del modelo como autorización o evidencia por sí solo.
- No promete determinismo donde el componente es probabilístico.

## 🧠 Qué necesitas saber

APIs y datos, prompts, embeddings y recuperación según caso, tool use, agentes, MCP,
datasets, evals, model grading con límites, seguridad, privacidad, provenance,
observabilidad, experimentación, coste, latencia y fallback.

## 📚 Tu ruta en el programa

1. Partes 00–13 para ingeniería, datos, contratos y evaluación de decisiones.
2. Partes 20 y 24–35 para integración, arquitectura, pruebas, seguridad y operación.
3. [Parte 38 — Desarrollo asistido por IA](../classes/part-38-desarrollo-de-software-asistido-por-ia/README.md).
4. [Parte 39 — SPEC y agentes](../classes/part-39-spec-agentes-y-ciclo-de-vida-agentic/README.md).

## 🧪 Evidencia de portafolio

- dataset versionado con criterios y casos adversos;
- baseline sin IA y comparación de calidad/coste/latencia;
- pruebas deterministas alrededor de herramientas y permisos;
- rollout, fallback y registro de revisión humana.

## 📈 Progresión

Software/Data Engineer → AI Systems Engineer → Senior/Staff AI Platform o Architect.

## ⚠️ Mitos frecuentes

- “Una demo buena demuestra producción.” No cubre distribución ni fallos reales.
- “El modelo grande resuelve contexto.” También puede amplificar coste y datos irrelevantes.
- “El agente terminó.” El sistema debe verificar artefactos y comportamiento.

## 🚀 Siguientes pasos

1. Define baseline, dataset y fallo inaceptable antes del prompt.
2. Encierra herramientas con permisos mínimos y salidas verificables.
3. Mide regresión, coste y latencia al cambiar cualquier componente.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
