# 🔭 Observability Engineer

> Diseña señales, contexto y herramientas que permiten formular y responder preguntas
> sobre sistemas en producción sin convertir telemetría en ruido o vigilancia.
>
> **Entrada habitual:** senior · **Foco:** logs, métricas, trazas y diagnóstico
> · **Evidencia central:** recorrido de fallo correlacionado desde síntoma hasta causa

## 🧭 Qué es y por qué importa

Observabilidad es la capacidad práctica de inferir el estado interno a partir de
señales útiles. Este rol normaliza contexto, instrumentación y experiencia de consulta
para reducir tiempo de diagnóstico, coste y alertas sin dueño.

## 🗓️ Un día en el puesto

- diseñar convenciones de atributos y correlation IDs;
- revisar cardinalidad, muestreo y retención;
- instrumentar un recorrido distribuido con OpenTelemetry;
- mejorar dashboard, alerta o flujo de investigación;
- controlar acceso, datos sensibles y coste de telemetría.

## ✅ Responsabilidades y límites

- Responde por calidad, gobernanza y utilidad de señales compartidas.
- Conecta telemetría con preguntas, SLO y runbooks.
- No confunde almacenar muchos logs con comprender el sistema.
- No expone PII ni usa telemetría de ingeniería para vigilar individuos.

## 🧠 Qué necesitas saber

Logs estructurados, métricas, traces, profiling, OpenTelemetry, propagación de
contexto, sampling, cardinalidad, almacenamiento, consultas, SLO, alerting,
privacidad, seguridad, coste y experiencia de diagnóstico.

## 📚 Tu ruta en el programa

1. Partes 02–03 y 08 para sistemas, redes y debugging.
2. Partes 20 y 26–29 para instrumentar servicios y datos distribuidos.
3. Partes 31 y [35 — Observabilidad, SRE e incidentes](../classes/part-35-observabilidad-sre-e-incidentes/README.md).
4. Partes 34 y 37–39 para plataforma, ownership y agentes operativos.

## 🧪 Evidencia de portafolio

- convención de telemetría y modelo de ownership;
- traza correlacionada entre cliente, API, cola y base de datos;
- alerta basada en impacto con runbook;
- análisis de cardinalidad, privacidad, retención y coste.

## 📈 Progresión

SRE/Backend/Data Engineer → Observability Engineer → Staff Telemetry Platform.

## ⚠️ Mitos frecuentes

- “Tres pilares bastan.” Importa la pregunta que pueden responder juntos.
- “Más retención siempre ayuda.” También aumenta coste y exposición.
- “Un dashboard previene incidentes.” Sin acción y ownership es decoración.

## 🚀 Siguientes pasos

1. Formula una pregunta de diagnóstico antes de instrumentar.
2. Sigue una solicitud y un evento de extremo a extremo.
3. Retira una señal inútil y documenta el ahorro.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
