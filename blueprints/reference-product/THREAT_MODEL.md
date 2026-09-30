# Modelo de amenazas — EduProgress

## Activos

Identidad, matrículas, evidencias, progreso, auditoría, secretos, respaldos y telemetría.

## Amenazas prioritarias

| Amenaza | Control | Prueba |
| --- | --- | --- |
| acceso a otro estudiante | autorización por recurso | cambio de `studentId` devuelve 403 |
| docente fuera del curso | política curso–actor | prueba negativa con curso ajeno |
| doble creación | idempotencia persistente | reintento conserva identificador |
| manipulación de historial | eventos append-only y permisos | rol de aplicación no borra auditoría |
| fuga en logs | allowlist de campos | inspección automatizada de eventos |
| respaldo expuesto | cifrado y rol separado | restauración desde almacén restringido |
| dependencia comprometida | bloqueo, SBOM y revisión | pipeline bloquea hallazgo crítico |

## Riesgo residual

Errores en políticas y configuración siguen siendo posibles. Se requieren revisión, pruebas negativas, monitoreo y respuesta.
