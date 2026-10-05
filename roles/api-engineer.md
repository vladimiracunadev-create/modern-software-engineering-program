# 🔗 API Engineer

> Diseña contratos consumibles, compatibles y operables entre equipos, sistemas y
> organizaciones, cualquiera que sea su protocolo.
>
> **Entrada habitual:** semi-senior · **Foco:** contratos, experiencia y gobernanza
> · **Evidencia central:** API versionada con consumidores y fallos contractuales probados

## 🧭 Qué es y por qué importa

Una API es una promesa de comportamiento, no una lista de endpoints. API engineering
integra semántica, modelo de dominio, seguridad, compatibilidad, documentación y
operación para que productores y consumidores evolucionen sin coordinación perfecta.

## 🗓️ Un día en el puesto

- modelar un caso de uso y elegir REST, RPC, eventos o tiempo real;
- revisar OpenAPI/AsyncAPI y ejemplos de error;
- negociar compatibilidad y deprecación con consumidores;
- analizar abuso, cuotas, latencia e idempotencia;
- observar adopción y fallos por versión.

## ✅ Responsabilidades y límites

- Responde por contrato, ergonomía, seguridad y ciclo de vida de la interfaz.
- No convierte una preferencia de protocolo en arquitectura universal.
- No versiona para evitar comprender compatibilidad.
- No publica una API sin ownership, soporte y política de retirada.

## 🧠 Qué necesitas saber

HTTP y protocolos, REST/RPC/GraphQL/gRPC, WebSockets/SSE, eventos y webhooks;
modelado, esquemas, errores, paginación, idempotencia, authn/authz, rate limiting,
contract testing, SDK, observabilidad y developer experience.

## 📚 Tu ruta en el programa

1. Partes 03, 05–09 para red, programación y APIs internas.
2. Partes 10–13 y 17 para usuarios, contratos y documentación.
3. [Parte 20 — Backend y APIs](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md).
4. Partes 25–28 para límites, datos, eventos y distribución.
5. Partes 30–35 para pruebas, seguridad, gateways y operación.

## 🧪 Evidencia de portafolio

- contrato con casos positivos, negativos y ejemplos ejecutables;
- prueba proveedor-consumidor y detección de breaking change;
- política de versionado y deprecación aplicada;
- dashboard por operación, consumidor y versión.

## 📈 Progresión

Backend Engineer → API Engineer → Senior/Staff API → API Platform o Architect.

## ⚠️ Mitos frecuentes

- “REST es JSON sobre HTTP.” La semántica y el contrato importan más que el formato.
- “GraphQL elimina versionado.” Los cambios incompatibles siguen existiendo.
- “La documentación se genera sola.” Un esquema no explica intención ni decisiones.

## 🚀 Siguientes pasos

1. Diseña primero ejemplos y errores de un caso de uso.
2. Añade un consumidor real y rompe el contrato de forma controlada.
3. Practica deprecación, observación y retirada.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
