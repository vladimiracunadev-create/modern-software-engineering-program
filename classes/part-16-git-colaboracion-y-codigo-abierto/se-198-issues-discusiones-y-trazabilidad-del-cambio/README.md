# SE-198 — Issues, discusiones y trazabilidad del cambio

> [!NOTE]
> Estado: **GUIDED**. Esta clase contiene explicación, práctica, ejercicios, evaluación y fuentes. No afirma ejecución automática; esa madurez requiere `EXECUTABLE` o superior.

## Ficha

| Campo | Valor |
| --- | --- |
| Etapa | C · Producto, requisitos y especificación |
| Parte | 16 · Git, colaboración y código abierto |
| Modalidad | análisis guiado (`class`) |
| Propietario profundo | `suite` |
| Duración estimada | 4 horas |
| Producto de la clase | cambio colaborativo recuperable |

## Prerrequisitos

- Haber completado o diagnosticado `SE-197` y poder explicar qué evidencia produjo.
- Manejar archivos de texto, rutas y control de versiones a nivel básico.
- Disponer de Git 2.40+ y alojamiento Git compatible.

## Problema auténtico

Un equipo que trabaja en una suite familiar privada debe decidir sobre **Issues, discusiones y trazabilidad del cambio**. Tiene información incompleta, restricciones de tiempo y personas afectadas por una decisión incorrecta. El reto no es repetir definiciones: es convertir el tema en un resultado revisable, distinguir observación de supuesto y conservar evidencia para que otra persona pueda continuar o cuestionar el trabajo.

## Objetivos observables

Al terminar podrás:

1. explicar Issues y discusiones con un ejemplo y un contraejemplo;
2. comparar al menos dos opciones usando evidencia, riesgo, costo y reversibilidad;
3. producir el artefacto **cambio colaborativo recuperable** para que otra persona pueda revisarlo;
4. diagnosticar el fallo «reescribir o publicar historia compartida sin evaluar a quién afecta» sin ocultar incertidumbre;
5. transferir la decisión a otra plataforma o dominio sin depender de una marca.

## Mapa conceptual

```mermaid
flowchart LR
    P["Problema: Issues, discusiones y trazabilidad del cambio"] --> M["Modelo: Issues"]
    M --> D["Decisión: discusiones"]
    D --> E["Evidencia: trazabilidad"]
    E --> R["Revisión: cambio"]
    R -->|nueva información| M
```

## Conceptos y decisiones

Git conserva un grafo de objetos y referencias; la colaboración añade revisión, integración, ownership y normas para cambiar historia compartida con seguridad.

La pregunta rectora de esta parte es: **¿qué cambio atómico se propone, quién puede verse afectado y cómo se recupera?** La respuesta debe
apoyarse en **diff enfocado, historial legible, revisión resuelta y estrategia de reversión**.

### 1. Issues

En **Issues, discusiones y trazabilidad del cambio**, `Issues` se analiza dentro de esta base: Git conserva un grafo de objetos y referencias; la colaboración añade revisión, integración, ownership y normas para cambiar historia compartida con seguridad. Para volverlo operativo, responde «¿qué cambio atómico se propone, quién puede verse afectado y cómo se recupera?» y conserva diff enfocado, historial legible, revisión resuelta y estrategia de reversión. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 2. Discusiones

En **Issues, discusiones y trazabilidad del cambio**, `discusiones` se analiza dentro de esta base: Git conserva un grafo de objetos y referencias; la colaboración añade revisión, integración, ownership y normas para cambiar historia compartida con seguridad. Para volverlo operativo, responde «¿qué cambio atómico se propone, quién puede verse afectado y cómo se recupera?» y conserva diff enfocado, historial legible, revisión resuelta y estrategia de reversión. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 3. Trazabilidad

En **Issues, discusiones y trazabilidad del cambio**, `trazabilidad` se analiza dentro de esta base: Git conserva un grafo de objetos y referencias; la colaboración añade revisión, integración, ownership y normas para cambiar historia compartida con seguridad. Para volverlo operativo, responde «¿qué cambio atómico se propone, quién puede verse afectado y cómo se recupera?» y conserva diff enfocado, historial legible, revisión resuelta y estrategia de reversión. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

### 4. Cambio

En **Issues, discusiones y trazabilidad del cambio**, `cambio` se analiza dentro de esta base: Git conserva un grafo de objetos y referencias; la colaboración añade revisión, integración, ownership y normas para cambiar historia compartida con seguridad. Para volverlo operativo, responde «¿qué cambio atómico se propone, quién puede verse afectado y cómo se recupera?» y conserva diff enfocado, historial legible, revisión resuelta y estrategia de reversión. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta.

La regla de trabajo es conservar trazabilidad: problema → supuesto → opción → decisión → evidencia → revisión. Una solución técnicamente posible puede seguir siendo inadecuada si excluye personas, desplaza riesgos o no puede mantenerse. La herramienta concreta se elige después de fijar el comportamiento y el criterio de aceptación.

## Ejemplo mínimo

Registra una sola decisión sobre **Issues, discusiones y trazabilidad del cambio**:

| Elemento | Ejemplo contrastable |
| --- | --- |
| Contexto | el equipo necesita una decisión en una iteración y carece de una medición directa |
| Supuesto | la opción elegida reduce el riesgo principal sin crear uno mayor |
| Evidencia | ejemplo, medición o revisión que una segunda persona puede repetir |
| Límite | el resultado no representa producción ni todas las poblaciones usuarias |
| Próxima señal | un dato que confirmaría, refutaría o modificaría la decisión |

El valor del ejemplo no está en “tener razón”, sino en que el razonamiento pueda ser inspeccionado.

## Ejemplo profesional

En la suite familiar privada, el equipo prepara un cambio relacionado con **Issues, discusiones y trazabilidad del cambio**. Parte de esta pregunta: **¿qué cambio atómico se propone, quién puede verse afectado y cómo se recupera?** Antes de implementarlo, registra personas afectadas, estados normales y degradados, datos utilizados, costo de reversión y señales de éxito. Dos opciones se comparan con la misma tabla y se contrastan usando diff enfocado, historial legible, revisión resuelta y estrategia de reversión. La alternativa ganadora queda condicionada a una prueba pequeña. La revisión incluye a producto, ingeniería y una persona que no participó en la propuesta. El resultado se archiva como `change.md` y enlaza la evidencia, no solo la conclusión.

## Práctica guiada

1. Crea `work/SE-198/` sin copiar datos personales ni secretos.
2. Formula el problema en una frase que incluya actor, necesidad y consecuencia.
3. Separa en una tabla hechos observados, inferencias, incógnitas y restricciones.
4. Propón dos opciones y una opción de no actuar; explicita costos y riesgos.
5. Construye el cambio colaborativo recuperable con los archivos indicados abajo.
6. Introduce deliberadamente el fallo controlado y registra síntomas antes de corregirlo.
7. Pide una revisión: la otra persona debe reconstruir la decisión solo con el artefacto.
8. Actualiza la conclusión y anota qué evidencia cambiaría la decisión.

## Ejercicios

1. **Fundamental:** define Issues y discusiones con un ejemplo propio, un contraejemplo y un criterio que permita distinguirlos.
2. **Aplicado:** resuelve el caso de la suite familiar privada, compara tres opciones y entrega `change.md` con trazabilidad completa.
3. **Avanzado:** cambia una restricción crítica —plataforma, escala, conectividad, regulación o capacidad del equipo— y demuestra qué partes de la decisión se conservan y cuáles deben revisarse.

## Fallo controlado y diagnóstico

Provoca de forma segura este fallo: **reescribir o publicar historia compartida sin evaluar a quién afecta**. No lo ejecutes sobre producción ni datos reales. Captura la decisión inicial, el síntoma observable y la primera hipótesis. Después reduce el caso, busca evidencia que pueda refutar tu hipótesis y corrige la causa, no solo el síntoma. Cierra con una medida preventiva y un procedimiento de recuperación.

## Entorno y archivos clave

Entorno de referencia: Git 2.40+ y alojamiento Git compatible. La actividad es documental y portable; cualquier comando adicional debe declarar sistema operativo y versión.

```text
work/SE-198/
├── README.md
│   ├── change.md
│   ├── review-checklist.md
│   ├── recovery.md
├── activity.yaml
└── rubric.json
```

`README.md` explica cómo reproducir la actividad; `change.md` contiene el resultado principal; los demás archivos separan evidencia y revisión. `activity.yaml` y `rubric.json` son contratos generados junto a esta guía.

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

Entrega el directorio `work/SE-198/` y una reflexión de máximo 300 palabras. La rúbrica machine-readable está en `rubric.json`; no se aprueba solo por completar pasos.

## Fuentes

Fuentes verificadas el 2026-09-30:

- **Git documentation** — Git project. [https://git-scm.com/docs](https://git-scm.com/docs) — se usa para contrastar vocabulario, límites y criterios aplicables.
- **Collaborating with pull requests** — GitHub. [https://docs.github.com/pull-requests/collaborating-with-pull-requests](https://docs.github.com/pull-requests/collaborating-with-pull-requests) — se usa para contrastar vocabulario, límites y criterios aplicables.
- **ACM Code of Ethics and Professional Conduct** — ACM. [https://www.acm.org/code-of-ethics](https://www.acm.org/code-of-ethics) — se usa para contrastar vocabulario, límites y criterios aplicables.

## Límites y siguiente paso

Esta guía enseña a razonar y producir evidencia sobre **Issues, discusiones y trazabilidad del cambio**; no certifica dominio profesional ni valida una implementación productiva. El siguiente enlace curricular es `SE-199`. Si la actividad necesita código o infraestructura real, debe avanzar a `EXECUTABLE`, añadir pruebas y documentar versiones, limpieza y recuperación.
