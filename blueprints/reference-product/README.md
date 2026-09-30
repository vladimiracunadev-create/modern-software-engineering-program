# Blueprint — EduProgress

Ejemplo de artefactos conectados para una capacidad educativa: un estudiante consulta su avance y un docente registra una evidencia.

El blueprint no es una aplicación terminada. Muestra trazabilidad entre producto, requisitos, contrato, arquitectura, datos, seguridad, pruebas y operación.

## Recorrido

1. `PRODUCT_BRIEF.md`: problema y resultado.
2. `REQUIREMENTS.md`: comportamiento y atributos.
3. `api/openapi.yaml`: contrato externo.
4. `ARCHITECTURE.md`: componentes y fallos.
5. `adr/ADR-001-modular-monolith.md`: decisión.
6. `TEST_STRATEGY.md`: confianza por riesgo.
7. `THREAT_MODEL.md`: activos y controles.
8. `runbooks/API_DEGRADED.md`: respuesta operativa.

## Extensión

Implementa el contrato mediante `framework-ecosystems-labs`, el modelo mediante `database-systems-labs` y las reglas en dos lenguajes mediante `polyglot-programming-labs`.
