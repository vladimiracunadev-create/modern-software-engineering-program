# Requisitos — EduProgress

## Funcionales

- RF-01: un estudiante autenticado consulta solo su progreso.
- RF-02: un docente autorizado registra una evidencia para un estudiante de su curso.
- RF-03: repetir la creación con la misma clave idempotente no duplica evidencia.
- RF-04: el progreso se calcula desde evidencias vigentes y requisitos del curso.
- RF-05: cada cambio conserva actor, fecha y motivo.

## Calidad

- RQ-01: 95 % de consultas completas bajo 500 ms en el entorno objetivo.
- RQ-02: ninguna respuesta mezcla datos entre estudiantes.
- RQ-03: RPO máximo de 15 minutos y RTO de 60 minutos para el laboratorio avanzado.
- RQ-04: el flujo principal funciona con teclado y mensajes comprensibles.
- RQ-05: una versión del contrato mantiene compatibilidad durante la migración.

## Supuestos

La identidad es provista por un servicio externo confiable. Los datos del laboratorio son sintéticos. Los objetivos deben recalibrarse con mediciones reales antes de producción.
