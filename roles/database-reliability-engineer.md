# 🗄️ Database Reliability Engineer

> Mantiene servicios de datos correctos, disponibles, recuperables y comprensibles
> mientras cambian cargas, esquemas y dependencias.
>
> **Entrada habitual:** senior · **Foco:** operación de datos y automatización
> · **Evidencia central:** restauración ensayada y cambio compatible bajo carga

## 🧭 Qué es y por qué importa

Database Reliability Engineering aplica prácticas de software y SRE a bases de datos.
Equilibra corrección, disponibilidad, latencia y coste; automatiza operaciones sin
ocultar los límites de consistencia, replicación y recuperación.

## 🗓️ Un día en el puesto

- analizar contención, planes de consulta y saturación;
- revisar migraciones y capacidad antes de desplegar;
- comprobar réplica, backups y restauración;
- responder a degradación o corrupción;
- mejorar guardrails y autoservicio para equipos de producto.

## ✅ Responsabilidades y límites

- Responde por confiabilidad, recuperación y capacidad del servicio de datos.
- Exige RPO/RTO verificables, no backups “exitosos”.
- No es operador manual de tickets ni dueño del significado de todos los datos.
- No promete alta disponibilidad sin analizar modos de fallo comunes.

## 🧠 Qué necesitas saber

Transacciones, aislamiento, índices, locking, replicación, partición, consenso,
backups, PITR, migraciones, observabilidad, capacity planning, automatización,
seguridad, privacidad, incidentes y coste.

## 📚 Tu ruta en el programa

1. Partes 01–09 y 18 para sistemas, programación y automatización.
2. Partes 20 y 25 para consumidores, dominio y arquitectura.
3. [Parte 26](../classes/part-26-datos-persistencia-y-recuperacion/README.md) y partes 27–29.
4. Partes 31–36 para rendimiento, seguridad, entrega, SRE y modernización.

## 🧪 Evidencia de portafolio

- restauración cronometrada contra RPO/RTO;
- migración expand/contract bajo tráfico;
- diagnóstico de bloqueo o consulta lenta con evidencia;
- runbook de corrupción, failover y reconciliación.

## 📈 Progresión

DBA/Backend/SRE → DBRE → Senior/Staff DBRE → Data Platform Lead.

## ⚠️ Mitos frecuentes

- “Backup completado significa recuperación.” Solo una restauración lo demuestra.
- “La réplica es un backup.” Puede replicar corrupción y borrados.
- “El proveedor gestiona todo.” El cliente conserva datos, acceso y objetivos.

## 🚀 Siguientes pasos

1. Define pérdida y tiempo tolerables con el negocio.
2. Restaura en un entorno aislado y verifica consistencia.
3. Ejecuta una migración compatible y su reversión.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
