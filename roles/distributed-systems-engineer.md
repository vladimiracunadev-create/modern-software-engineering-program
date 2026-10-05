# 🌐 Distributed Systems Engineer

> Diseña sistemas que conservan garantías explícitas pese a latencia, concurrencia,
> particiones, reintentos y fallos parciales.
>
> **Entrada habitual:** senior · **Foco:** coordinación, consistencia y resiliencia
> · **Evidencia central:** experimento de fallos que demuestra garantías y pérdidas

## 🧭 Qué es y por qué importa

Al distribuir estado, el sistema pierde un reloj y un destino universalmente fiables.
Este rol decide qué coordinar, qué aceptar como eventual, cómo detectar duplicados y
qué comportamiento ofrecer cuando una dependencia responde tarde o de forma incierta.

## 🗓️ Un día en el puesto

- precisar invariantes y modelo de consistencia;
- revisar timeout, retry, backoff e idempotencia;
- investigar un split-brain, duplicado o retraso;
- ejecutar pruebas de partición y reinicio;
- documentar trade-offs para producto y operación.

## ✅ Responsabilidades y límites

- Responde por garantías observables y comportamiento bajo fallo.
- Usa CAP/PACELC como marco, no como eslogan.
- No distribuye un monolito para resolver límites organizacionales vagos.
- No afirma exactly-once sin alcance, protocolo y evidencia.

## 🧠 Qué necesitas saber

Concurrencia, relojes, fallos parciales, consistencia, replicación, quorum, consenso,
leader election, idempotencia, sagas, event sourcing, partición, service discovery,
observabilidad y chaos engineering.

## 📚 Tu ruta en el programa

1. Partes 01–09, especialmente redes, algoritmos y debugging.
2. Partes 13, 20 y 24–27 para contratos, arquitectura, datos y eventos.
3. [Parte 28 — Concurrencia y sistemas distribuidos](../classes/part-28-concurrencia-y-sistemas-distribuidos/README.md).
4. Partes 29–35 para infraestructura, pruebas, resiliencia y operación.

## 🧪 Evidencia de portafolio

- modelo de invariantes y consistencia;
- servicio idempotente probado ante duplicación y timeout incierto;
- laboratorio de partición, reloj y reinicio;
- ADR que compare coordinación fuerte, compensación y rediseño.

## 📈 Progresión

Backend/Data/SRE Senior → Distributed Systems Engineer → Staff/Principal o Architect.

## ⚠️ Mitos frecuentes

- “La red es confiable en cloud.” Cambia el proveedor, no la física.
- “Eventual consistency significa datos incorrectos.” Requiere semántica temporal explícita.
- “Retries aumentan resiliencia.” Sin límites pueden amplificar una caída.

## 🚀 Siguientes pasos

1. Escribe invariantes antes de elegir protocolo.
2. Introduce latencia, pérdida y duplicación de forma controlada.
3. Explica qué garantía se conserva y cuál se sacrifica.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
