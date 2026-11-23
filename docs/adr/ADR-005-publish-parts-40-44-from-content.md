# ADR-005 — Publicar las Partes 40–44 desde el contenido, sin tocar la infraestructura

> [!NOTE]
> **Documento histórico.** Los identificadores `SE-nnn` y los números de parte de este texto usan la
> numeración vigente cuando se escribió (antes del 2026-11-23). Los enlaces apuntan a la clase migrada. Para
> traducir un identificador, consulta [`ID-MIGRATION.md`](../ID-MIGRATION.md) ([ADR-007](ADR-007-pedagogical-renumbering-and-new-parts.md)).

- Estado: aceptada el 2026-11-16.
- Contexto: [ADR-004](ADR-004-expand-to-540-class-scope.md) amplió el alcance a 540 clases
  (Partes 40–44, `SE-481`–`SE-540`) pero dejó `curriculum.yaml`, el catálogo, los
  generadores y los validadores fijos en 480 clases y 40 partes. Cada parte nueva habría
  exigido editar a mano una decena de constantes (`480`, `40`, `521`, rangos de IDs, tablas
  por parte), lo que es frágil y bloquea el trabajo en paralelo de varias sesiones.
- Decisión: el estado de cada parte se **deriva del contenido**, no de constantes.
  1. `scripts/program_state.py` es la única fuente del estado: una parte está
     **desarrollada** si y solo si existen `content/part-NN/README.md` y los doce
     `content/part-NN/SE-NNN.md` de su rango. Con solo parte de los archivos, la parte
     sigue planificada y `validate_repository.py` falla con un mensaje explícito.
  2. `scripts/build_program_blueprint.py` define las 45 partes y sus 540 títulos (la
     numeración `SE-001`–`SE-540` es fija) y emite en `curriculum.yaml` solo las partes
     desarrolladas en `parts`; el resto va en `planned_scope.unpublished_parts` con
     `status: planned`. `class_count` y `part_count` cuentan clases desarrolladas;
     `planned_scope` declara 45 partes, 540 clases y 2.430 horas.
  3. Los generadores (`build_phase2/3/4.py`, `build_role_guides.py`), los validadores y las
     pruebas calculan contadores, rangos y textos de estado desde ese módulo. El bloque de
     estado del `README.md` se regenera entre marcadores `<!-- state:… -->`.
  4. Los metadatos propios de una parte nueva (fuentes iniciales y fuentes nuevas) viven en
     `content/part-NN/part.json`, no en tablas compartidas.
  5. Los contadores dicen lo real: «N clases desarrolladas» y «M planificadas». Una parte
     planificada no tiene carpeta en `classes/`, ni página en `site/`, ni enlaces en las
     guías de rol.
- Consecuencias: añadir una parte exige solo sus archivos de contenido, figuras,
  experimentos, el registro en el tracker y el CHANGELOG, y marcar sus doce casillas en el
  plan maestro. Los archivos generados (índices, STATUS, portal, README de estado, guías)
  cambian al regenerar; en un rebase con otra parte en paralelo se resuelven regenerando.
  El procedimiento está en [`../ADDING-A-PART.md`](../ADDING-A-PART.md).
- Relación con otras decisiones: implementa ADR-004 y no cambia ADR-003 (sin renumerar,
  sin cuotas, sin inflar conteos).
