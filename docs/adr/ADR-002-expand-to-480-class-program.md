# ADR-002 — Expandir la suite a 40 partes y 480 clases

- Estado: aceptada
- Fecha: 2026-09-30
- Alcance: arquitectura curricular y de repositorio

## Contexto

La línea base 0.1 resume la disciplina en 17 documentos breves. Es útil como mapa,
pero no satisface el objetivo de un programa profesional comparable con los programas
hermanos ni proporciona ejemplos, ejercicios, entornos y evidencias por clase.

## Decisión

Adoptar ocho etapas, cuarenta partes y 480 clases. Cada parte tendrá diez clases
nucleares, un taller y un proyecto. El manifiesto generated `curriculum.yaml` será
validado en CI y todos sus contenidos comienzan como `PLANNED`.

Se preservan los documentos 00–16 existentes como línea base histórica hasta que una
fase posterior migre su contenido. No se presentarán como las 480 clases nuevas.

## Alternativas

- **Mantener 17 documentos:** insuficiente para la profundidad requerida.
- **Crear 51 clases:** mejora la granularidad, pero no cubre plataformas, operación,
  dominios e ingeniería con IA con práctica suficiente.
- **Crear un catálogo ilimitado:** imposible de verificar y mantener.
- **480 clases:** comparable con programas hermanos y permite cobertura sistemática
  con proyectos, sin alcanzar la escala extrema de 680 clases.

## Consecuencias

- La producción de contenido debe hacerse por incrementos y estados de madurez.
- Los conteos se generan; no se actualizan a mano.
- La suite crece, pero mantiene fronteras estrictas con los repositorios propietarios.
- La afirmación pública correcta durante esta fase es “480 clases especificadas”, no
  “480 clases construidas”.

## Criterios de aceptación de fase 1

- 40 partes y 480 IDs únicos en el manifiesto.
- Cobertura de cuerpo profesional, plataformas, SPEC, IA y agentes.
- Propiedad explícita por parte.
- Esquema y validación automatizada.
- Workflow multiplataforma con acciones fijadas a SHA.
- Documentación pública que distingue plan de implementación.
