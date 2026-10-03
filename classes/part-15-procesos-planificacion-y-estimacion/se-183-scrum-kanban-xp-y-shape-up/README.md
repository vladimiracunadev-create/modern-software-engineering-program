# SE-183 — Scrum, Kanban, XP y Shape Up

[← SE-182 — Agile como principios y no como ceremonia](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md) · [↑ Parte 15](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-183.html) · [SE-184 — Lean, teoría de colas y límites de trabajo →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md)

> [!WARNING]
> Estado: **PLANNED · BORRADOR EN REVISIÓN**. El material es visible para auditoría,
> pero aún no supera el estándar pedagógico profundo y no debe presentarse como clase terminada.

## Prerrequisitos

- Haber completado o diagnosticado `SE-182` y poder explicar qué evidencia produjo.
- Manejar archivos de texto, rutas y control de versiones a nivel básico.
- Disponer de tablero reproducible en Markdown o herramienta equivalente.

## Problema auténtico

Un equipo que trabaja en una servicio financiero debe decidir sobre **Scrum, Kanban, XP y Shape Up**. Tiene información incompleta, restricciones de tiempo y personas afectadas por una decisión incorrecta. El reto no es repetir definiciones: es convertir el tema en un resultado revisable, distinguir observación de supuesto y conservar evidencia para que otra persona pueda continuar o cuestionar el trabajo.

## Objetivos observables

Al terminar podrás:

1. explicar Scrum y Kanban con un ejemplo y un contraejemplo;
2. comparar al menos dos opciones usando evidencia, riesgo, costo y reversibilidad;
3. producir el artefacto **plan adaptativo con riesgos y métricas de flujo** para que otra persona pueda revisarlo;
4. diagnosticar el fallo «convertir una estimación en compromiso sin rango ni supuestos» sin ocultar incertidumbre;
5. transferir la decisión a otra plataforma o dominio sin depender de una marca.

## Temas y por qué importan

| Tema | Función en la clase | Por qué importa |
| --- | --- | --- |
| Scrum | Modelo | Delimita qué entidad, estado o relación se estudia y qué queda fuera. |
| Kanban | Mecanismo | Explica la cadena causal: qué entrada cambia qué estado y mediante qué regla. |
| XP | Evidencia | Define la señal observable que permite contrastar el modelo sin confundir correlación con causa. |
| Shape | Decisión | Convierte el conocimiento en opciones comparables, límites, riesgos y condiciones de reversión. |

## Mapa conceptual

```mermaid
flowchart LR
    P["Problema: Scrum, Kanban, XP y Shape Up"] --> M["Modelo: Scrum"]
    M --> D["Decisión: Kanban"]
    D --> E["Evidencia: XP"]
    E --> R["Revisión: Shape"]
    R -->|nueva información| M
```

El diagrama se lee de izquierda a derecha: el problema obliga a construir un
modelo; el modelo permite decidir; la decisión solo se sostiene con evidencia; y
la revisión devuelve nueva información al modelo. No es una secuencia lineal de
entrega, sino un ciclo de aprendizaje aplicado a **Scrum, Kanban, XP y Shape Up**.

## Conceptos y decisiones

Un proceso de trabajo limita trabajo en curso, hace visible el flujo y crea ciclos de aprendizaje; un plan es una hipótesis actualizable, no una predicción exacta.

La pregunta rectora de esta parte es: **¿qué incertidumbre, dependencia o cuello de botella condiciona la siguiente entrega?** La respuesta debe
apoyarse en **políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos**.

### 1. Scrum: modelo

En esta clase, **Scrum** se estudia como modelo. Su función es delimita qué entidad, estado o relación se estudia y qué queda fuera. Debe conectarse con la pregunta «¿qué incertidumbre, dependencia o cuello de botella condiciona la siguiente entrega?» y demostrarse mediante políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos. Un tratamiento superficial solo lo nombraría; un tratamiento útil identifica precondiciones, transición, resultado observable y caso en que la explicación deja de sostenerse. Aplica esa secuencia a **Scrum, Kanban, XP y Shape Up**, registra los supuestos y explica qué decisión concreta cambia al comprenderla.

### 2. Kanban: mecanismo

En esta clase, **Kanban** se estudia como mecanismo. Su función es explica la cadena causal: qué entrada cambia qué estado y mediante qué regla. Debe conectarse con la pregunta «¿qué incertidumbre, dependencia o cuello de botella condiciona la siguiente entrega?» y demostrarse mediante políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos. Un tratamiento superficial solo lo nombraría; un tratamiento útil identifica precondiciones, transición, resultado observable y caso en que la explicación deja de sostenerse. Aplica esa secuencia a **Scrum, Kanban, XP y Shape Up**, registra los supuestos y explica qué decisión concreta cambia al comprenderla.

### 3. XP: evidencia

En esta clase, **XP** se estudia como evidencia. Su función es define la señal observable que permite contrastar el modelo sin confundir correlación con causa. Debe conectarse con la pregunta «¿qué incertidumbre, dependencia o cuello de botella condiciona la siguiente entrega?» y demostrarse mediante políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos. Un tratamiento superficial solo lo nombraría; un tratamiento útil identifica precondiciones, transición, resultado observable y caso en que la explicación deja de sostenerse. Aplica esa secuencia a **Scrum, Kanban, XP y Shape Up**, registra los supuestos y explica qué decisión concreta cambia al comprenderla.

### 4. Shape: decisión

En esta clase, **Shape** se estudia como decisión. Su función es convierte el conocimiento en opciones comparables, límites, riesgos y condiciones de reversión. Debe conectarse con la pregunta «¿qué incertidumbre, dependencia o cuello de botella condiciona la siguiente entrega?» y demostrarse mediante políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos. Un tratamiento superficial solo lo nombraría; un tratamiento útil identifica precondiciones, transición, resultado observable y caso en que la explicación deja de sostenerse. Aplica esa secuencia a **Scrum, Kanban, XP y Shape Up**, registra los supuestos y explica qué decisión concreta cambia al comprenderla.

La regla de trabajo es conservar trazabilidad: problema → supuesto → opción → decisión → evidencia → revisión. Una solución técnicamente posible puede seguir siendo inadecuada si excluye personas, desplaza riesgos o no puede mantenerse. La herramienta concreta se elige después de fijar el comportamiento y el criterio de aceptación.

## Definiciones de trabajo

- **Scrum:** concepto usado aquí como modelo; se acepta solo si puede observarse o justificarse mediante políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos.
- **Kanban:** concepto usado aquí como mecanismo; se acepta solo si puede observarse o justificarse mediante políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos.
- **XP:** concepto usado aquí como evidencia; se acepta solo si puede observarse o justificarse mediante políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos.
- **Shape:** concepto usado aquí como decisión; se acepta solo si puede observarse o justificarse mediante políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos.

Estas definiciones son operativas para el borrador: deberán sustituirse o
precisarse con terminología de las fuentes de la clase durante la revisión
cualitativa. No son un glosario normativo.

## Ejemplo mínimo

Registra una sola decisión sobre **Scrum, Kanban, XP y Shape Up**:

| Elemento | Ejemplo contrastable |
| --- | --- |
| Contexto | el equipo necesita una decisión en una iteración y carece de una medición directa |
| Supuesto | la opción elegida reduce el riesgo principal sin crear uno mayor |
| Evidencia | ejemplo, medición o revisión que una segunda persona puede repetir |
| Límite | el resultado no representa producción ni todas las poblaciones usuarias |
| Próxima señal | un dato que confirmaría, refutaría o modificaría la decisión |

El valor del ejemplo no está en “tener razón”, sino en que el razonamiento pueda ser inspeccionado.

## Ejemplo profesional

En la servicio financiero, el equipo prepara un cambio relacionado con **Scrum, Kanban, XP y Shape Up**. Parte de esta pregunta: **¿qué incertidumbre, dependencia o cuello de botella condiciona la siguiente entrega?** Antes de implementarlo, registra personas afectadas, estados normales y degradados, datos utilizados, costo de reversión y señales de éxito. Dos opciones se comparan con la misma tabla y se contrastan usando políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos. La alternativa ganadora queda condicionada a una prueba pequeña. La revisión incluye a producto, ingeniería y una persona que no participó en la propuesta. El resultado se archiva como `plan.md` y enlaza la evidencia, no solo la conclusión.

## Práctica guiada

1. Crea `work/SE-183/` sin copiar datos personales ni secretos.
2. Formula el problema en una frase que incluya actor, necesidad y consecuencia.
3. Separa en una tabla hechos observados, inferencias, incógnitas y restricciones.
4. Propón dos opciones y una opción de no actuar; explicita costos y riesgos.
5. Construye el plan adaptativo con riesgos y métricas de flujo con los archivos indicados abajo.
6. Introduce deliberadamente el fallo controlado y registra síntomas antes de corregirlo.
7. Pide una revisión: la otra persona debe reconstruir la decisión solo con el artefacto.
8. Actualiza la conclusión y anota qué evidencia cambiaría la decisión.

## Ejercicios

1. **Fundamental:** define Scrum y Kanban con un ejemplo propio, un contraejemplo y un criterio que permita distinguirlos.
2. **Aplicado:** resuelve el caso de la servicio financiero, compara tres opciones y entrega `plan.md` con trazabilidad completa.
3. **Avanzado:** cambia una restricción crítica —plataforma, escala, conectividad, regulación o capacidad del equipo— y demuestra qué partes de la decisión se conservan y cuáles deben revisarse.

## Reto verificable

Entrega el **plan adaptativo con riesgos y métricas de flujo** de forma que una persona que no participó en
la clase pueda reconstruir problema, supuestos, opciones, decisión y evidencia.
El reto se acepta únicamente si esa persona puede señalar una condición concreta
que cambiaría la decisión y reproducir al menos una comprobación sin pedir contexto
oral adicional.

## Fallo controlado y diagnóstico

Provoca de forma segura este fallo: **convertir una estimación en compromiso sin rango ni supuestos**. No lo ejecutes sobre producción ni datos reales. Captura la decisión inicial, el síntoma observable y la primera hipótesis. Después reduce el caso, busca evidencia que pueda refutar tu hipótesis y corrige la causa, no solo el síntoma. Cierra con una medida preventiva y un procedimiento de recuperación.

## Entorno y archivos clave

Entorno de referencia: tablero reproducible en Markdown o herramienta equivalente. La actividad es documental y portable; cualquier comando adicional debe declarar sistema operativo y versión.

```text
work/SE-183/
├── README.md
│   ├── plan.md
│   ├── risks.md
│   ├── flow.csv
├── activity.yaml
└── rubric.json
```

`README.md` explica cómo reproducir la actividad; `plan.md` contiene el resultado principal; los demás archivos separan evidencia y revisión. `activity.yaml` y `rubric.json` son contratos generados junto a esta guía.

## Seguridad, ética y accesibilidad

- usa datos sintéticos o anonimizados y aplica minimización;
- no incluyas tokens, rutas privadas ni información personal en evidencias;
- identifica personas que reciben beneficios, cargas o riesgo de exclusión;
- ofrece una alternativa textual a diagramas y no uses color como única señal;
- verifica navegación por teclado y lenguaje comprensible cuando exista interfaz;
- detén la práctica si requiere acceso no autorizado o puede afectar sistemas reales.

## Transferencia

Repite la decisión en un segundo contexto: cambia la servicio financiero por otro de los dominios persistentes, o cambia Windows por Linux/macOS cuando aplique. Conserva problema, criterios y evidencia; modifica únicamente los supuestos dependientes del entorno. Explica por escrito qué conocimiento fue transferible y qué parte pertenecía a la herramienta.

## Evaluación y evidencia

| Criterio | Evidencia para aprobar |
| --- | --- |
| Comprensión | conceptos explicados con ejemplo, contraejemplo y límites |
| Decisión | opciones comparadas con criterios explícitos y alternativa de no actuar |
| Reproducibilidad | archivos, pasos y entorno permiten repetir la revisión |
| Diagnóstico | fallo controlado conserva síntomas, hipótesis, causa y recuperación |
| Responsabilidad | seguridad, privacidad, accesibilidad y personas afectadas fueron consideradas |

Entrega el directorio `work/SE-183/` y una reflexión de máximo 300 palabras. La rúbrica machine-readable está en `rubric.json`; no se aprueba solo por completar pasos.

## Fuentes

Fuentes verificadas el 2026-09-30:

- **The Scrum Guide** — Scrum Guide authors. [https://scrumguides.org/scrum-guide.html](https://scrumguides.org/scrum-guide.html) — se usa para contrastar vocabulario, límites y criterios aplicables.
- **The Kanban Guide** — Kanban Guides. [https://kanbanguides.org/english/](https://kanbanguides.org/english/) — se usa para contrastar vocabulario, límites y criterios aplicables.
- **SWEBOK Guide v4.0a** — IEEE Computer Society. [https://www.computer.org/education/bodies-of-knowledge/software-engineering](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — se usa para contrastar vocabulario, límites y criterios aplicables.

## Preguntas frecuentes

### ¿Basta con definir los términos del título?

No. Debes mostrar cómo se relacionan, qué mecanismo explican, qué evidencia los
contrasta y qué decisión profesional cambia gracias a esa comprensión.

### ¿La herramienta recomendada es obligatoria?

No. El entorno de referencia hace reproducible la práctica, pero puedes usar otro
si documentas equivalencias, versiones, diferencias y procedimiento de recuperación.

### ¿Completar los archivos aprueba automáticamente la clase?

No. Los archivos son contenedores de evidencia. La aprobación depende de la calidad
del razonamiento, la reproducibilidad, el diagnóstico y la revisión contra las fuentes.

## Límites y siguiente paso

Esta guía enseña a razonar y producir evidencia sobre **Scrum, Kanban, XP y Shape Up**; no certifica dominio profesional ni valida una implementación productiva. El siguiente enlace curricular es `SE-184`. Si la actividad necesita código o infraestructura real, debe avanzar a `EXECUTABLE`, añadir pruebas y documentar versiones, limpieza y recuperación.

---

[← SE-182 — Agile como principios y no como ceremonia](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md) · [↑ Parte 15](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-183.html) · [SE-184 — Lean, teoría de colas y límites de trabajo →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md)
