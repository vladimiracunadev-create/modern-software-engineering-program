# ⚙️ Backend Engineer

> Diseña servicios, reglas de negocio, contratos y datos que siguen siendo confiables
> cuando aparecen concurrencia, fallos parciales y cambios de versión.
>
> **Entrada habitual:** junior/semi-senior · **Foco:** APIs, dominio, datos y operación
> · **Evidencia central:** servicio observable con contrato y recuperación probados

## 🧭 Qué es y por qué importa

Backend engineering construye las capacidades que viven detrás de una interfaz:
autorización, reglas, persistencia, integración y procesos asíncronos. El reto no es
solo responder HTTP; es conservar invariantes frente a duplicados, reintentos,
concurrencia, migraciones y dependencias degradadas.

## 🗓️ Un día en el puesto

- refinar una regla de negocio y convertirla en casos verificables;
- diseñar o evolucionar una API sin romper consumidores;
- investigar una consulta lenta, un timeout o un mensaje duplicado;
- revisar esquemas, migraciones y límites transaccionales;
- desplegar un cambio gradual y observar latencia, errores y saturación;
- coordinar con frontend, datos, seguridad, plataforma y producto.

## ✅ Responsabilidades y límites

- Responde por contratos, invariantes, datos y comportamiento bajo fallo.
- Debe comprender autenticación, autorización, privacidad y abuso.
- No convierte cada módulo en microservicio por defecto.
- No usa una cola para ocultar inconsistencias ni una caché para evitar modelar datos.
- No promete “exactly once” sin explicar el mecanismo y sus límites.

## 🧠 Qué necesitas saber

- estructuras de datos, concurrencia, procesos y redes;
- modelado de dominio, modularidad, errores e idempotencia;
- REST/RPC/GraphQL/gRPC, eventos, webhooks y contratos;
- transacciones, índices, caché, partición, réplica y migraciones;
- pruebas unitarias, integración, contrato, rendimiento y seguridad;
- logs estructurados, métricas, trazas, SLO y respuesta a incidentes.

## 📚 Tu ruta en el programa

1. Partes 00–09 para fundamentos y construcción.
2. Partes 10–13 para producto, requisitos, dominio y contratos.
3. [Parte 20 — Backend, APIs y procesamiento asíncrono](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md).
4. [Parte 24 — Diseño, patrones y refactorización](../classes/part-24-diseno-patrones-y-refactorizacion/README.md) y Parte 25.
5. Partes 26–28 para persistencia, eventos y distribución.
6. Partes 30–35 para pruebas, seguridad, entrega y operación.
7. Partes 36, 38 y 39 para evolución y trabajo asistido por agentes.

## 🧪 Evidencia de portafolio

- OpenAPI o contrato equivalente con ejemplos positivos y negativos;
- API idempotente con pruebas de duplicación y reintento;
- migración de esquema compatible con rollback;
- consumidor asíncrono que recupera poison messages;
- dashboard y runbook para una degradación de dependencia;
- ADR comparando monolito modular, servicio separado y alternativa comprada.

## 📈 Progresión

Backend Junior → Backend Engineer → Senior → Staff/Principal o especialización en
datos, distribución, seguridad, plataforma o arquitectura. El crecimiento consiste
en proteger más invariantes y coordinar más consumidores, no en sumar endpoints.

## ⚠️ Mitos frecuentes

- “Backend es CRUD.” El CRUD trivial termina donde empiezan reglas, concurrencia y fallos.
- “Microservicios escalan equipos.” También multiplican contratos y operación.
- “La base de datos resuelve consistencia.” Solo dentro de garantías bien entendidas.
- “Más caché siempre mejora.” Puede empeorar corrección, coste y diagnóstico.

## 🚀 Siguientes pasos

1. Construye un monolito modular pequeño antes de distribuirlo.
2. Define invariantes y pruebas contractuales antes de optimizar.
3. Introduce una falla de dependencia y demuestra recuperación.
4. Mide p50/p95/p99 y explica qué carga produjo esos datos.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
