# SE-210 — API docs, ejemplos y contratos publicados

> [!NOTE]
> Estado: **GUIDED**. Esta clase contiene explicación, práctica, ejercicios, evaluación y fuentes. No afirma ejecución automática; esa madurez requiere `EXECUTABLE` o superior.

## Ficha

| Campo | Valor |
| --- | --- |
| Etapa | C · Producto, requisitos y especificación |
| Parte | 17 · Documentación y conocimiento técnico |
| Modalidad | análisis guiado (`class`) |
| Propietario profundo | `suite` |
| Duración estimada | 4 horas |
| Producto de la clase | paquete de documentación mantenible |

## Prerrequisitos

- Haber completado o diagnosticado `SE-209` y poder explicar qué evidencia produjo.
- Manejar archivos de texto, rutas y control de versiones a nivel básico.
- Disponer de editor Markdown, Mermaid y verificador de enlaces.

## Problema auténtico

Un equipo que trabaja en una suite familiar privada debe decidir sobre **API docs, ejemplos y contratos publicados**. Tiene información incompleta, restricciones de tiempo y personas afectadas por una decisión incorrecta. El reto no es repetir definiciones: es convertir el tema en un resultado revisable, distinguir observación de supuesto y conservar evidencia para que otra persona pueda continuar o cuestionar el trabajo.

## Objetivos observables

Al terminar podrás:

1. explicar API y docs con un ejemplo y un contraejemplo;
2. comparar al menos dos opciones usando evidencia, riesgo, costo y reversibilidad;
3. producir el artefacto **paquete de documentación mantenible** para que otra persona pueda revisarlo;
4. diagnosticar el fallo «documentar una intención como si describiera el comportamiento actual» sin ocultar incertidumbre;
5. transferir la decisión a otra plataforma o dominio sin depender de una marca.

## Mapa conceptual

```mermaid
flowchart LR
    P["Problema: API docs, ejemplos y contratos publicados"] --> M["Modelo: API"]
    M --> D["Decisión: docs"]
    D --> E["Evidencia: ejemplos"]
    E --> R["Revisión: contratos"]
    R -->|nueva información| M
```

## Conceptos y decisiones

La documentación sirve a una audiencia y una tarea concreta; debe diferenciar tutorial, guía, explicación, referencia, arquitectura y registro histórico.

La pregunta rectora de esta parte es: **¿quién necesita tomar qué decisión con esta vista y cuándo dejaría de ser válida?** La respuesta debe
apoyarse en **prueba de recorrido, enlaces comprobados, owner, fecha y contraste con el comportamiento actual**.

### 1. Api

En **API docs, ejemplos y contratos publicados**, `API` se analiza dentro de esta base: La documentación sirve a una audiencia y una tarea concreta; debe diferenciar tutorial, guía, explicación, referencia, arquitectura y registro histórico. Para volverlo operativo, responde «¿quién necesita tomar qué decisión con esta vista y cuándo dejaría de ser válida?» y conserva prueba de recorrido, enlaces comprobados, owner, fecha y contraste con el comportamiento actual. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 2. Docs

En **API docs, ejemplos y contratos publicados**, `docs` se analiza dentro de esta base: La documentación sirve a una audiencia y una tarea concreta; debe diferenciar tutorial, guía, explicación, referencia, arquitectura y registro histórico. Para volverlo operativo, responde «¿quién necesita tomar qué decisión con esta vista y cuándo dejaría de ser válida?» y conserva prueba de recorrido, enlaces comprobados, owner, fecha y contraste con el comportamiento actual. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 3. Ejemplos

En **API docs, ejemplos y contratos publicados**, `ejemplos` se analiza dentro de esta base: La documentación sirve a una audiencia y una tarea concreta; debe diferenciar tutorial, guía, explicación, referencia, arquitectura y registro histórico. Para volverlo operativo, responde «¿quién necesita tomar qué decisión con esta vista y cuándo dejaría de ser válida?» y conserva prueba de recorrido, enlaces comprobados, owner, fecha y contraste con el comportamiento actual. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 4. Contratos

En **API docs, ejemplos y contratos publicados**, `contratos` se analiza dentro de esta base: La documentación sirve a una audiencia y una tarea concreta; debe diferenciar tutorial, guía, explicación, referencia, arquitectura y registro histórico. Para volverlo operativo, responde «¿quién necesita tomar qué decisión con esta vista y cuándo dejaría de ser válida?» y conserva prueba de recorrido, enlaces comprobados, owner, fecha y contraste con el comportamiento actual. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

La regla de trabajo es conservar trazabilidad: problema → supuesto → opción → decisión → evidencia → revisión. Una solución técnicamente posible puede seguir siendo inadecuada si excluye personas, desplaza riesgos o no puede mantenerse. La herramienta concreta se elige después de fijar el comportamiento y el criterio de aceptación.

## Ejemplo mínimo

Registra una sola decisión sobre **API docs, ejemplos y contratos publicados**:

| Elemento | Ejemplo contrastable |
| --- | --- |
| Contexto | el equipo necesita una decisión en una iteración y carece de una medición directa |
| Supuesto | la opción elegida reduce el riesgo principal sin crear uno mayor |
| Evidencia | ejemplo, medición o revisión que una segunda persona puede repetir |
| Límite | el resultado no representa producción ni todas las poblaciones usuarias |
| Próxima señal | un dato que confirmaría, refutaría o modificaría la decisión |

El valor del ejemplo no está en “tener razón”, sino en que el razonamiento pueda ser inspeccionado.

## Ejemplo profesional

En la suite familiar privada, el equipo prepara un cambio relacionado con **API docs, ejemplos y contratos publicados**. Parte de esta pregunta: **¿quién necesita tomar qué decisión con esta vista y cuándo dejaría de ser válida?** Antes de implementarlo, registra personas afectadas, estados normales y degradados, datos utilizados, costo de reversión y señales de éxito. Dos opciones se comparan con la misma tabla y se contrastan usando prueba de recorrido, enlaces comprobados, owner, fecha y contraste con el comportamiento actual. La alternativa ganadora queda condicionada a una prueba pequeña. La revisión incluye a producto, ingeniería y una persona que no participó en la propuesta. El resultado se archiva como `README.md` y enlaza la evidencia, no solo la conclusión.

## Práctica guiada

1. Crea `work/SE-210/` sin copiar datos personales ni secretos.
2. Formula el problema en una frase que incluya actor, necesidad y consecuencia.
3. Separa en una tabla hechos observados, inferencias, incógnitas y restricciones.
4. Propón dos opciones y una opción de no actuar; explicita costos y riesgos.
5. Construye el paquete de documentación mantenible con los archivos indicados abajo.
6. Introduce deliberadamente el fallo controlado y registra síntomas antes de corregirlo.
7. Pide una revisión: la otra persona debe reconstruir la decisión solo con el artefacto.
8. Actualiza la conclusión y anota qué evidencia cambiaría la decisión.

## Ejercicios

1. **Fundamental:** define API y docs con un ejemplo propio, un contraejemplo y un criterio que permita distinguirlos.
2. **Aplicado:** resuelve el caso de la suite familiar privada, compara tres opciones y entrega `README.md` con trazabilidad completa.
3. **Avanzado:** cambia una restricción crítica —plataforma, escala, conectividad, regulación o capacidad del equipo— y demuestra qué partes de la decisión se conservan y cuáles deben revisarse.

## Fallo controlado y diagnóstico

Provoca de forma segura este fallo: **documentar una intención como si describiera el comportamiento actual**. No lo ejecutes sobre producción ni datos reales. Captura la decisión inicial, el síntoma observable y la primera hipótesis. Después reduce el caso, busca evidencia que pueda refutar tu hipótesis y corrige la causa, no solo el síntoma. Cierra con una medida preventiva y un procedimiento de recuperación.

## Entorno y archivos clave

Entorno de referencia: editor Markdown, Mermaid y verificador de enlaces. La actividad es documental y portable; cualquier comando adicional debe declarar sistema operativo y versión.

```text
work/SE-210/
├── README.md
│   ├── README.md
│   ├── architecture.md
│   ├── decision-record.md
├── activity.yaml
└── rubric.json
```

`README.md` explica cómo reproducir la actividad; `README.md` contiene el resultado principal; los demás archivos separan evidencia y revisión. `activity.yaml` y `rubric.json` son contratos generados junto a esta guía.

## Seguridad, ética y accesibilidad

- usa datos sintéticos o anonimizados y aplica minimización;
- no incluyas tokens, rutas privadas ni información personal en evidencias;
- identifica personas que reciben beneficios, cargas o riesgo de exclusión;
- ofrece una alternativa textual a diagramas y no uses color como única señal;
- verifica navegación por teclado y lenguaje comprensible cuando exista interfaz;
- detén la práctica si requiere acceso no autorizado o puede afectar sistemas reales.

## Transferencia

Repite la decisión en un segundo contexto: cambia la suite familiar privada por otro de los dominios persistentes, o cambia Windows por Linux/macOS cuando aplique. Conserva problema, criterios y evidencia; modifica únicamente los supuestos dependientes del entorno. Explica por escrito qué conocimiento fue transferible y qué parte pertenecía a la herramienta.

## Evaluación y evidencia

| Criterio | Evidencia para aprobar |
| --- | --- |
| Comprensión | conceptos explicados con ejemplo, contraejemplo y límites |
| Decisión | opciones comparadas con criterios explícitos y alternativa de no actuar |
| Reproducibilidad | archivos, pasos y entorno permiten repetir la revisión |
| Diagnóstico | fallo controlado conserva síntomas, hipótesis, causa y recuperación |
| Responsabilidad | seguridad, privacidad, accesibilidad y personas afectadas fueron consideradas |

Entrega el directorio `work/SE-210/` y una reflexión de máximo 300 palabras. La rúbrica machine-readable está en `rubric.json`; no se aprueba solo por completar pasos.

## Fuentes

Fuentes verificadas el 2026-09-30:

- **Diátaxis documentation framework** — Diátaxis project. [https://diataxis.fr/](https://diataxis.fr/) — se usa para contrastar vocabulario, límites y criterios aplicables.
- **C4 model** — C4 model project. [https://c4model.com/](https://c4model.com/) — se usa para contrastar vocabulario, límites y criterios aplicables.
- **SWEBOK Guide v4.0a** — IEEE Computer Society. [https://www.computer.org/education/bodies-of-knowledge/software-engineering](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — se usa para contrastar vocabulario, límites y criterios aplicables.

## Límites y siguiente paso

Esta guía enseña a razonar y producir evidencia sobre **API docs, ejemplos y contratos publicados**; no certifica dominio profesional ni valida una implementación productiva. El siguiente enlace curricular es `SE-211`. Si la actividad necesita código o infraestructura real, debe avanzar a `EXECUTABLE`, añadir pruebas y documentar versiones, limpieza y recuperación.
