# Fronteras entre repositorios

## Decisión

La suite es propietaria del ciclo de vida, la integración y la evidencia profesional.
Los repositorios especializados conservan la profundidad técnica. Cada clase puede
incluir un ejemplo mínimo autocontenido, pero no copiará cursos completos ajenos.

| Repositorio | Propiedad profunda | Lo que aporta a la suite |
| --- | --- | --- |
| `polyglot-programming-labs` | lenguajes, paradigmas, algoritmos y equivalencia | soluciones comparadas y pruebas comunes |
| `database-systems-labs` | modelado, motores, consultas y operación de datos | modelos, cargas, migraciones y recuperación |
| `framework-ecosystems-labs` | frameworks, UI, APIs y plataformas | adaptadores y fragmentos verticales |
| `software-engineering-learning-suite` | producto, requisitos, arquitectura, calidad, seguridad, entrega, operación, IA y liderazgo | contrato transversal y portafolio |

## Unidad de integración

1. La suite define necesidad, atributos, SPEC y aceptación.
2. El repositorio propietario implementa la profundidad especializada.
3. La integración consume un contrato versionado y una evidencia reproducible.
4. La suite registra la decisión, el resultado y los límites.

## Antiduplicación

- Un ejemplo local explica la decisión integradora, no reemplaza el laboratorio
  profundo.
- Un enlace sin práctica ni evidencia no cuenta como integración.
- Un cambio de contrato identifica consumidores, compatibilidad y migración.
- Las versiones verificadas se registran; no se usa `main` como contrato implícito.

## Cambios coordinados

Los cambios transversales deben incluir RFC o ADR, actualizar manifiestos, ejecutar
las validaciones de cada propietario afectado y conservar una ruta de adopción. Una
fase de esta suite puede avanzar con stubs explícitos, pero nunca declarar integrada
una capacidad que solo está planificada.
