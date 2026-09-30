# ADR-001 — Monolito modular inicial

- Estado: aceptado para el laboratorio
- Fecha: 2026-08-19

## Contexto

El equipo es pequeño, el dominio evoluciona y la prioridad es validar el flujo con privacidad y trazabilidad. No existe evidencia de escala que exija despliegues independientes.

## Opciones

1. monolito sin módulos;
2. monolito modular;
3. microservicios por progreso, evidencia y auditoría.

## Decisión

Monolito modular con base relacional y worker de outbox. Los límites viven en código, pruebas y propiedad de datos lógica.

## Consecuencias

Menor costo operativo y transacciones simples. Exige disciplina para evitar acoplamiento. Una falla puede afectar todo el proceso y el escalado es conjunto.

## Revisión

Revisar si equipos necesitan despliegue autónomo, existen perfiles de carga incompatibles o los límites modulares no reducen interferencia. Antes de extraer, medir y ejecutar una migración reversible.
