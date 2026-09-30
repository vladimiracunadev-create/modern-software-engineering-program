# Runbook — API degradada

## Señal

Latencia p95 sobre objetivo durante diez minutos o tasa de error superior al umbral del SLO.

## Primeros pasos

1. Confirma impacto desde la perspectiva del usuario.
2. Identifica versión, región y correlación temporal.
3. Revisa saturación de aplicación, conexiones y base.
4. Detén despliegues y cambios no esenciales.
5. Comunica alcance y próxima actualización.

## Mitigación

- revierte la última versión si existe correlación y rollback probado;
- limita funciones no críticas mediante bandera;
- reduce consultas costosas identificadas, sin desactivar autorización;
- no aumentes reintentos si la dependencia está saturada.

## Verificación

Comprueba flujo real, percentiles, errores, cola/outbox e integridad. Mantén observación después de recuperar.

## Después

Conserva línea temporal y evidencias, completa postmortem y convierte acciones en cambios con responsable y criterio verificable.
