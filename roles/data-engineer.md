# 🧱 Data Engineer

> Construye flujos y productos de datos confiables, trazables y evolutivos desde la
> captura hasta el consumo analítico u operacional.
>
> **Entrada habitual:** semi-senior · **Foco:** pipelines, contratos y calidad de datos
> · **Evidencia central:** flujo reproducible con lineage, controles y backfill probado

## 🧭 Qué es y por qué importa

Data engineering convierte eventos, tablas y archivos en datos utilizables sin perder
semántica. El reto central es conservar calidad, tiempo, privacidad y compatibilidad
cuando productores cambian y los consumidores toman decisiones con el resultado.

## 🗓️ Un día en el puesto

- revisar un contrato de datos con productor y consumidor;
- investigar retraso, duplicados o una dimensión inconsistente;
- diseñar ingestión batch, streaming o CDC;
- ejecutar backfill y reconciliar resultados;
- vigilar frescura, completitud, coste y acceso.

## ✅ Responsabilidades y límites

- Responde por contratos, lineage, calidad y operación del pipeline.
- Distingue dato faltante, tardío, incorrecto y semánticamente ambiguo.
- No crea un lago para posponer gobierno y modelado.
- No interpreta causalidad ni significado de dominio sin sus responsables.

## 🧠 Qué necesitas saber

Modelado relacional y analítico, OLTP/OLAP, SQL, archivos columnares, colas, streams,
CDC, partición, esquemas, orquestación, data quality, lineage, privacidad, IAM,
observabilidad, recuperación y costes.

## 📚 Tu ruta en el programa

1. Partes 01–09 para representación, programación y automatización.
2. Partes 10–13 para dominio, economía y contratos.
3. [Parte 26 — Datos, persistencia y recuperación](../classes/part-26-datos-persistencia-y-recuperacion/README.md).
4. Partes 27–29 para eventos, distribución y cloud.
5. Partes 30–35 para calidad, seguridad, supply chain y operación.

## 🧪 Evidencia de portafolio

- contrato versionado entre productor y consumidor;
- pipeline idempotente con datos tardíos y duplicados;
- backfill con reconciliación y rollback lógico;
- tablero de frescura, calidad, coste y lineage.

## 📈 Progresión

Data Engineer → Senior → Staff Data, Data Platform o Data Architect.

## ⚠️ Mitos frecuentes

- “ETL es mover datos.” También transforma significado y responsabilidad.
- “Streaming es más moderno.” Añade orden, tiempo y operación si no es necesario.
- “La calidad se limpia al final.” El contrato debe acercarla al origen.

## 🚀 Siguientes pasos

1. Define consumidores, semántica y SLO antes del pipeline.
2. Inyecta duplicados, retraso y cambio de esquema.
3. Ejecuta un backfill y reconcilia sin borrar evidencia.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
