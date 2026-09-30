# SE-086 — Pilas, colas, deques y prioridades

> [!WARNING]
> Estado: **PLANNED · BORRADOR EN REVISIÓN**. El material es visible para auditoría,
> pero aún no supera el estándar pedagógico profundo y no debe presentarse como clase terminada.

## Ficha

| Campo | Valor |
| --- | --- |
| Etapa | B · Programación y construcción |
| Parte | 07 · Estructuras de datos y algoritmos |
| Modalidad | análisis guiado (`class`) |
| Dominio técnico principal | `polyglot-programming-labs` |
| Duración estimada | 4 horas |
| Producto de la clase | implementación medida con casos límite |

## Prerrequisitos

- Haber completado o diagnosticado `SE-085` y poder explicar qué evidencia produjo.
- Manejar archivos de texto, rutas y control de versiones a nivel básico.
- Disponer de Python 3.11+, unittest y temporizador monotónico.

## Problema auténtico

Un equipo que trabaja en una comercio responsable debe decidir sobre **Pilas, colas, deques y prioridades**. Tiene información incompleta, restricciones de tiempo y personas afectadas por una decisión incorrecta. El reto no es repetir definiciones: es convertir el tema en un resultado revisable, distinguir observación de supuesto y conservar evidencia para que otra persona pueda continuar o cuestionar el trabajo.

## Objetivos observables

Al terminar podrás:

1. explicar Pilas y colas con un ejemplo y un contraejemplo;
2. comparar al menos dos opciones usando evidencia, riesgo, costo y reversibilidad;
3. producir el artefacto **implementación medida con casos límite** para que otra persona pueda revisarlo;
4. diagnosticar el fallo «elegir una estructura por costumbre sin medir la carga relevante» sin ocultar incertidumbre;
5. transferir la decisión a otra plataforma o dominio sin depender de una marca.

## Mapa conceptual

```mermaid
flowchart LR
    P["Problema: Pilas, colas, deques y prioridades"] --> M["Modelo: Pilas"]
    M --> D["Decisión: colas"]
    D --> E["Evidencia: deques"]
    E --> R["Revisión: prioridades"]
    R -->|nueva información| M
```

## Conceptos y decisiones

Una estructura de datos define operaciones y costos; un algoritmo debe preservar invariantes, terminar y comportarse dentro de límites de tiempo y espacio adecuados a la carga.

La pregunta rectora de esta parte es: **¿qué operaciones dominan la carga y qué garantía necesita cada una?** La respuesta debe
apoyarse en **casos límite, pruebas de propiedades, complejidad y medición empírica**.

### 1. Pilas

En **Pilas, colas, deques y prioridades**, `Pilas` se analiza dentro de esta base: Una estructura de datos define operaciones y costos; un algoritmo debe preservar invariantes, terminar y comportarse dentro de límites de tiempo y espacio adecuados a la carga. Para volverlo operativo, responde «¿qué operaciones dominan la carga y qué garantía necesita cada una?» y conserva casos límite, pruebas de propiedades, complejidad y medición empírica. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 2. Colas

En **Pilas, colas, deques y prioridades**, `colas` se analiza dentro de esta base: Una estructura de datos define operaciones y costos; un algoritmo debe preservar invariantes, terminar y comportarse dentro de límites de tiempo y espacio adecuados a la carga. Para volverlo operativo, responde «¿qué operaciones dominan la carga y qué garantía necesita cada una?» y conserva casos límite, pruebas de propiedades, complejidad y medición empírica. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 3. Deques

En **Pilas, colas, deques y prioridades**, `deques` se analiza dentro de esta base: Una estructura de datos define operaciones y costos; un algoritmo debe preservar invariantes, terminar y comportarse dentro de límites de tiempo y espacio adecuados a la carga. Para volverlo operativo, responde «¿qué operaciones dominan la carga y qué garantía necesita cada una?» y conserva casos límite, pruebas de propiedades, complejidad y medición empírica. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 4. Prioridades

En **Pilas, colas, deques y prioridades**, `prioridades` se analiza dentro de esta base: Una estructura de datos define operaciones y costos; un algoritmo debe preservar invariantes, terminar y comportarse dentro de límites de tiempo y espacio adecuados a la carga. Para volverlo operativo, responde «¿qué operaciones dominan la carga y qué garantía necesita cada una?» y conserva casos límite, pruebas de propiedades, complejidad y medición empírica. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

La regla de trabajo es conservar trazabilidad: problema → supuesto → opción → decisión → evidencia → revisión. Una solución técnicamente posible puede seguir siendo inadecuada si excluye personas, desplaza riesgos o no puede mantenerse. La herramienta concreta se elige después de fijar el comportamiento y el criterio de aceptación.

## Ejemplo mínimo

Registra una sola decisión sobre **Pilas, colas, deques y prioridades**:

| Elemento | Ejemplo contrastable |
| --- | --- |
| Contexto | el equipo necesita una decisión en una iteración y carece de una medición directa |
| Supuesto | la opción elegida reduce el riesgo principal sin crear uno mayor |
| Evidencia | ejemplo, medición o revisión que una segunda persona puede repetir |
| Límite | el resultado no representa producción ni todas las poblaciones usuarias |
| Próxima señal | un dato que confirmaría, refutaría o modificaría la decisión |

El valor del ejemplo no está en “tener razón”, sino en que el razonamiento pueda ser inspeccionado.

## Ejemplo profesional

En la comercio responsable, el equipo prepara un cambio relacionado con **Pilas, colas, deques y prioridades**. Parte de esta pregunta: **¿qué operaciones dominan la carga y qué garantía necesita cada una?** Antes de implementarlo, registra personas afectadas, estados normales y degradados, datos utilizados, costo de reversión y señales de éxito. Dos opciones se comparan con la misma tabla y se contrastan usando casos límite, pruebas de propiedades, complejidad y medición empírica. La alternativa ganadora queda condicionada a una prueba pequeña. La revisión incluye a producto, ingeniería y una persona que no participó en la propuesta. El resultado se archiva como `algorithm.py` y enlaza la evidencia, no solo la conclusión.

## Práctica guiada

1. Crea `work/SE-086/` sin copiar datos personales ni secretos.
2. Formula el problema en una frase que incluya actor, necesidad y consecuencia.
3. Separa en una tabla hechos observados, inferencias, incógnitas y restricciones.
4. Propón dos opciones y una opción de no actuar; explicita costos y riesgos.
5. Construye el implementación medida con casos límite con los archivos indicados abajo.
6. Introduce deliberadamente el fallo controlado y registra síntomas antes de corregirlo.
7. Pide una revisión: la otra persona debe reconstruir la decisión solo con el artefacto.
8. Actualiza la conclusión y anota qué evidencia cambiaría la decisión.

## Ejercicios

1. **Fundamental:** define Pilas y colas con un ejemplo propio, un contraejemplo y un criterio que permita distinguirlos.
2. **Aplicado:** resuelve el caso de la comercio responsable, compara tres opciones y entrega `algorithm.py` con trazabilidad completa.
3. **Avanzado:** cambia una restricción crítica —plataforma, escala, conectividad, regulación o capacidad del equipo— y demuestra qué partes de la decisión se conservan y cuáles deben revisarse.

## Fallo controlado y diagnóstico

Provoca de forma segura este fallo: **elegir una estructura por costumbre sin medir la carga relevante**. No lo ejecutes sobre producción ni datos reales. Captura la decisión inicial, el síntoma observable y la primera hipótesis. Después reduce el caso, busca evidencia que pueda refutar tu hipótesis y corrige la causa, no solo el síntoma. Cierra con una medida preventiva y un procedimiento de recuperación.

## Entorno y archivos clave

Entorno de referencia: Python 3.11+, unittest y temporizador monotónico. La actividad es documental y portable; cualquier comando adicional debe declarar sistema operativo y versión.

```text
work/SE-086/
├── README.md
│   ├── algorithm.py
│   ├── test_algorithm.py
│   ├── benchmark.md
├── activity.yaml
└── rubric.json
```

`README.md` explica cómo reproducir la actividad; `algorithm.py` contiene el resultado principal; los demás archivos separan evidencia y revisión. `activity.yaml` y `rubric.json` son contratos generados junto a esta guía.

## Seguridad, ética y accesibilidad

- usa datos sintéticos o anonimizados y aplica minimización;
- no incluyas tokens, rutas privadas ni información personal en evidencias;
- identifica personas que reciben beneficios, cargas o riesgo de exclusión;
- ofrece una alternativa textual a diagramas y no uses color como única señal;
- verifica navegación por teclado y lenguaje comprensible cuando exista interfaz;
- detén la práctica si requiere acceso no autorizado o puede afectar sistemas reales.

## Transferencia

Repite la decisión en un segundo contexto: cambia la comercio responsable por otro de los dominios persistentes, o cambia Windows por Linux/macOS cuando aplique. Conserva problema, criterios y evidencia; modifica únicamente los supuestos dependientes del entorno. Explica por escrito qué conocimiento fue transferible y qué parte pertenecía a la herramienta.

## Evaluación y evidencia

| Criterio | Evidencia para aprobar |
| --- | --- |
| Comprensión | conceptos explicados con ejemplo, contraejemplo y límites |
| Decisión | opciones comparadas con criterios explícitos y alternativa de no actuar |
| Reproducibilidad | archivos, pasos y entorno permiten repetir la revisión |
| Diagnóstico | fallo controlado conserva síntomas, hipótesis, causa y recuperación |
| Responsabilidad | seguridad, privacidad, accesibilidad y personas afectadas fueron consideradas |

Entrega el directorio `work/SE-086/` y una reflexión de máximo 300 palabras. La rúbrica machine-readable está en `rubric.json`; no se aprueba solo por completar pasos.

## Fuentes

Fuentes verificadas el 2026-09-30:

- **Mathematics for Computer Science** — MIT OpenCourseWare. [https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — se usa para contrastar vocabulario, límites y criterios aplicables.
- **Python 3 documentation** — Python Software Foundation. [https://docs.python.org/3/](https://docs.python.org/3/) — se usa para contrastar vocabulario, límites y criterios aplicables.
- **SWEBOK Guide v4.0a** — IEEE Computer Society. [https://www.computer.org/education/bodies-of-knowledge/software-engineering](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — se usa para contrastar vocabulario, límites y criterios aplicables.

## Límites y siguiente paso

Esta guía enseña a razonar y producir evidencia sobre **Pilas, colas, deques y prioridades**; no certifica dominio profesional ni valida una implementación productiva. El siguiente enlace curricular es `SE-087`. Si la actividad necesita código o infraestructura real, debe avanzar a `EXECUTABLE`, añadir pruebas y documentar versiones, limpieza y recuperación.
