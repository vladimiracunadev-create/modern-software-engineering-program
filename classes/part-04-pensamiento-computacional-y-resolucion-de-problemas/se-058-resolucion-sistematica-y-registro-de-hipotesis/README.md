# SE-058 — Resolución sistemática y registro de hipótesis

> [!NOTE]
> Estado: **GUIDED**. Esta clase contiene explicación, práctica, ejercicios, evaluación y fuentes. No afirma ejecución automática; esa madurez requiere `EXECUTABLE` o superior.

## Ficha

| Campo | Valor |
| --- | --- |
| Etapa | A · Fundamentos de la profesión |
| Parte | 04 · Pensamiento computacional y resolución de problemas |
| Modalidad | análisis guiado (`class`) |
| Propietario profundo | `polyglot-programming-labs` |
| Duración estimada | 4 horas |
| Producto de la clase | especificación contrastable de una solución |

## Prerrequisitos

- Haber completado o diagnosticado `SE-057` y poder explicar qué evidencia produjo.
- Manejar archivos de texto, rutas y control de versiones a nivel básico.
- Disponer de editor, Python opcional y diagramas Mermaid.

## Problema auténtico

Un equipo que trabaja en una comunidad social debe decidir sobre **Resolución sistemática y registro de hipótesis**. Tiene información incompleta, restricciones de tiempo y personas afectadas por una decisión incorrecta. El reto no es repetir definiciones: es convertir el tema en un resultado revisable, distinguir observación de supuesto y conservar evidencia para que otra persona pueda continuar o cuestionar el trabajo.

## Objetivos observables

Al terminar podrás:

1. explicar Resolución y sistemática con un ejemplo y un contraejemplo;
2. comparar al menos dos opciones usando evidencia, riesgo, costo y reversibilidad;
3. producir el artefacto **especificación contrastable de una solución** para que otra persona pueda revisarlo;
4. diagnosticar el fallo «resolver un ejemplo y asumir que la solución cubre todo el dominio» sin ocultar incertidumbre;
5. transferir la decisión a otra plataforma o dominio sin depender de una marca.

## Mapa conceptual

```mermaid
flowchart LR
    P["Problema: Resolución sistemática y registro de hipótesis"] --> M["Modelo: Resolución"]
    M --> D["Decisión: sistemática"]
    D --> E["Evidencia: registro"]
    E --> R["Revisión: hipótesis"]
    R -->|nueva información| M
```

## Conceptos y decisiones

Resolver un problema exige modelar entradas, salidas, estado, invariantes y costo; un ejemplo favorable no demuestra corrección para todo el dominio.

La pregunta rectora de esta parte es: **¿qué debe mantenerse verdadero y bajo qué conjunto de entradas?** La respuesta debe
apoyarse en **casos límite, contraejemplos, argumento de terminación y costo medido o acotado**.

### 1. Resolución

En **Resolución sistemática y registro de hipótesis**, `Resolución` se analiza dentro de esta base: Resolver un problema exige modelar entradas, salidas, estado, invariantes y costo; un ejemplo favorable no demuestra corrección para todo el dominio. Para volverlo operativo, responde «¿qué debe mantenerse verdadero y bajo qué conjunto de entradas?» y conserva casos límite, contraejemplos, argumento de terminación y costo medido o acotado. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 2. Sistemática

En **Resolución sistemática y registro de hipótesis**, `sistemática` se analiza dentro de esta base: Resolver un problema exige modelar entradas, salidas, estado, invariantes y costo; un ejemplo favorable no demuestra corrección para todo el dominio. Para volverlo operativo, responde «¿qué debe mantenerse verdadero y bajo qué conjunto de entradas?» y conserva casos límite, contraejemplos, argumento de terminación y costo medido o acotado. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 3. Registro

En **Resolución sistemática y registro de hipótesis**, `registro` se analiza dentro de esta base: Resolver un problema exige modelar entradas, salidas, estado, invariantes y costo; un ejemplo favorable no demuestra corrección para todo el dominio. Para volverlo operativo, responde «¿qué debe mantenerse verdadero y bajo qué conjunto de entradas?» y conserva casos límite, contraejemplos, argumento de terminación y costo medido o acotado. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 4. Hipótesis

En **Resolución sistemática y registro de hipótesis**, `hipótesis` se analiza dentro de esta base: Resolver un problema exige modelar entradas, salidas, estado, invariantes y costo; un ejemplo favorable no demuestra corrección para todo el dominio. Para volverlo operativo, responde «¿qué debe mantenerse verdadero y bajo qué conjunto de entradas?» y conserva casos límite, contraejemplos, argumento de terminación y costo medido o acotado. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

La regla de trabajo es conservar trazabilidad: problema → supuesto → opción → decisión → evidencia → revisión. Una solución técnicamente posible puede seguir siendo inadecuada si excluye personas, desplaza riesgos o no puede mantenerse. La herramienta concreta se elige después de fijar el comportamiento y el criterio de aceptación.

## Ejemplo mínimo

Registra una sola decisión sobre **Resolución sistemática y registro de hipótesis**:

| Elemento | Ejemplo contrastable |
| --- | --- |
| Contexto | el equipo necesita una decisión en una iteración y carece de una medición directa |
| Supuesto | la opción elegida reduce el riesgo principal sin crear uno mayor |
| Evidencia | ejemplo, medición o revisión que una segunda persona puede repetir |
| Límite | el resultado no representa producción ni todas las poblaciones usuarias |
| Próxima señal | un dato que confirmaría, refutaría o modificaría la decisión |

El valor del ejemplo no está en “tener razón”, sino en que el razonamiento pueda ser inspeccionado.

## Ejemplo profesional

En la comunidad social, el equipo prepara un cambio relacionado con **Resolución sistemática y registro de hipótesis**. Parte de esta pregunta: **¿qué debe mantenerse verdadero y bajo qué conjunto de entradas?** Antes de implementarlo, registra personas afectadas, estados normales y degradados, datos utilizados, costo de reversión y señales de éxito. Dos opciones se comparan con la misma tabla y se contrastan usando casos límite, contraejemplos, argumento de terminación y costo medido o acotado. La alternativa ganadora queda condicionada a una prueba pequeña. La revisión incluye a producto, ingeniería y una persona que no participó en la propuesta. El resultado se archiva como `problem.md` y enlaza la evidencia, no solo la conclusión.

## Práctica guiada

1. Crea `work/SE-058/` sin copiar datos personales ni secretos.
2. Formula el problema en una frase que incluya actor, necesidad y consecuencia.
3. Separa en una tabla hechos observados, inferencias, incógnitas y restricciones.
4. Propón dos opciones y una opción de no actuar; explicita costos y riesgos.
5. Construye el especificación contrastable de una solución con los archivos indicados abajo.
6. Introduce deliberadamente el fallo controlado y registra síntomas antes de corregirlo.
7. Pide una revisión: la otra persona debe reconstruir la decisión solo con el artefacto.
8. Actualiza la conclusión y anota qué evidencia cambiaría la decisión.

## Ejercicios

1. **Fundamental:** define Resolución y sistemática con un ejemplo propio, un contraejemplo y un criterio que permita distinguirlos.
2. **Aplicado:** resuelve el caso de la comunidad social, compara tres opciones y entrega `problem.md` con trazabilidad completa.
3. **Avanzado:** cambia una restricción crítica —plataforma, escala, conectividad, regulación o capacidad del equipo— y demuestra qué partes de la decisión se conservan y cuáles deben revisarse.

## Fallo controlado y diagnóstico

Provoca de forma segura este fallo: **resolver un ejemplo y asumir que la solución cubre todo el dominio**. No lo ejecutes sobre producción ni datos reales. Captura la decisión inicial, el síntoma observable y la primera hipótesis. Después reduce el caso, busca evidencia que pueda refutar tu hipótesis y corrige la causa, no solo el síntoma. Cierra con una medida preventiva y un procedimiento de recuperación.

## Entorno y archivos clave

Entorno de referencia: editor, Python opcional y diagramas Mermaid. La actividad es documental y portable; cualquier comando adicional debe declarar sistema operativo y versión.

```text
work/SE-058/
├── README.md
│   ├── problem.md
│   ├── model.md
│   ├── checks.md
├── activity.yaml
└── rubric.json
```

`README.md` explica cómo reproducir la actividad; `problem.md` contiene el resultado principal; los demás archivos separan evidencia y revisión. `activity.yaml` y `rubric.json` son contratos generados junto a esta guía.

## Seguridad, ética y accesibilidad

- usa datos sintéticos o anonimizados y aplica minimización;
- no incluyas tokens, rutas privadas ni información personal en evidencias;
- identifica personas que reciben beneficios, cargas o riesgo de exclusión;
- ofrece una alternativa textual a diagramas y no uses color como única señal;
- verifica navegación por teclado y lenguaje comprensible cuando exista interfaz;
- detén la práctica si requiere acceso no autorizado o puede afectar sistemas reales.

## Transferencia

Repite la decisión en un segundo contexto: cambia la comunidad social por otro de los dominios persistentes, o cambia Windows por Linux/macOS cuando aplique. Conserva problema, criterios y evidencia; modifica únicamente los supuestos dependientes del entorno. Explica por escrito qué conocimiento fue transferible y qué parte pertenecía a la herramienta.

## Evaluación y evidencia

| Criterio | Evidencia para aprobar |
| --- | --- |
| Comprensión | conceptos explicados con ejemplo, contraejemplo y límites |
| Decisión | opciones comparadas con criterios explícitos y alternativa de no actuar |
| Reproducibilidad | archivos, pasos y entorno permiten repetir la revisión |
| Diagnóstico | fallo controlado conserva síntomas, hipótesis, causa y recuperación |
| Responsabilidad | seguridad, privacidad, accesibilidad y personas afectadas fueron consideradas |

Entrega el directorio `work/SE-058/` y una reflexión de máximo 300 palabras. La rúbrica machine-readable está en `rubric.json`; no se aprueba solo por completar pasos.

## Fuentes

Fuentes verificadas el 2026-09-30:

- **Mathematics for Computer Science** — MIT OpenCourseWare. [https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — se usa para contrastar vocabulario, límites y criterios aplicables.
- **SWEBOK Guide v4.0a** — IEEE Computer Society. [https://www.computer.org/education/bodies-of-knowledge/software-engineering](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — se usa para contrastar vocabulario, límites y criterios aplicables.

## Límites y siguiente paso

Esta guía enseña a razonar y producir evidencia sobre **Resolución sistemática y registro de hipótesis**; no certifica dominio profesional ni valida una implementación productiva. El siguiente enlace curricular es `SE-059`. Si la actividad necesita código o infraestructura real, debe avanzar a `EXECUTABLE`, añadir pruebas y documentar versiones, limpieza y recuperación.
