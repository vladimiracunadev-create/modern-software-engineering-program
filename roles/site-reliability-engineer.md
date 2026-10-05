# 📈 Site Reliability Engineer

> Aplica ingeniería de software a la confiabilidad: convierte expectativas de servicio
> en señales, automatización, límites de riesgo y aprendizaje operativo.
>
> **Entrada habitual:** semi-senior/senior · **Foco:** SLO, capacidad e incidentes ·
> **Evidencia central:** servicio que detecta, degrada y recupera de forma ensayada

## 🧭 Qué es y por qué importa

SRE gestiona la tensión entre velocidad de cambio y confiabilidad mediante objetivos
explícitos. Define SLI/SLO, usa error budgets, reduce toil con software y aprende de
incidentes sin buscar culpables. No promete disponibilidad infinita: acuerda qué nivel
de servicio importa y qué inversión lo sostiene.

## 🗓️ Un día en el puesto

- revisar alertas y distinguir síntoma accionable de ruido;
- analizar capacidad, saturación y tendencias;
- automatizar una operación manual repetitiva;
- participar en guardia, contención o postmortem;
- ajustar SLO con producto y equipos de servicio;
- ejecutar un game day o validar recuperación de backup.

## ✅ Responsabilidades y límites

- Responde por mecanismos y feedback de confiabilidad, no por absorber todo incidente.
- Comparte guardia y aprendizaje con quienes construyen el servicio.
- No convierte cada métrica en alerta.
- No usa error budgets como castigo ni SLO como SLA contractual sin acuerdo.
- No automatiza una operación que todavía no comprende.

## 🧠 Qué necesitas saber

- sistemas operativos, redes, concurrencia y sistemas distribuidos;
- latencia, throughput, percentiles y capacity planning;
- logs, métricas, trazas, profiling y OpenTelemetry;
- SLI, SLO, SLA, error budgets y toil;
- fault tolerance, backups, RTO/RPO y disaster recovery;
- incident command, runbooks, postmortems y chaos engineering.

## 📚 Tu ruta en el programa

1. Partes 02–03, 08 y 20 para sistemas, red, debugging y servicios.
2. Partes 26–29 para datos, eventos, distribución y cloud.
3. Parte 31 para rendimiento y resiliencia.
4. Parte 34 para entrega progresiva y rollback.
5. [Parte 35 — Observabilidad, SRE e incidentes](../classes/part-35-observabilidad-sre-e-incidentes/README.md).
6. Parte 36 para continuidad de sistemas legacy; partes 38–39 para agentes operativos controlados.

## 🧪 Evidencia de portafolio

- SLO derivado de una experiencia de usuario y SLI implementado;
- alertas por síntomas con runbook y prueba de escalado;
- dashboard que diferencia tráfico, errores, latencia y saturación;
- load/soak test con capacidad y límites declarados;
- restore ensayado con RTO/RPO observado;
- postmortem con timeline, factores contribuyentes y acciones verificables.

## 📈 Progresión

Software/Systems Engineer → SRE → Senior SRE → Staff Reliability / SRE Lead. También
puede transitar a plataforma, arquitectura distribuida o liderazgo de infraestructura.
La progresión reduce riesgo sistémico más allá de un servicio.

## ⚠️ Mitos frecuentes

- “SRE es operaciones con otro nombre.” Requiere ingeniería y objetivos explícitos.
- “Cinco nueves es siempre mejor.” Puede costar más que el valor que protege.
- “No hubo incidentes, somos confiables.” Quizá faltan tráfico o detección.
- “El postmortem sin culpa no tiene responsables.” Sí tiene ownership, sin simplificar causas.

## 🚀 Siguientes pasos

1. Define un SLO pequeño a partir de un recorrido de usuario.
2. Instrumenta la señal y prueba que detecta degradación.
3. Satura una dependencia en un entorno controlado.
4. Recupera, escribe el postmortem y verifica las acciones posteriores.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
