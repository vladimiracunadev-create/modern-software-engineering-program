# Retrospectiva basada en evidencia

[↑ Glosario](../../README.md) · [← Retrospectiva](./retrospectiva.md) · [Retrospectiva sin culpa →](./retrospectiva-sin-culpa.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

La **retrospectiva basada en evidencia** es, en el taller de [SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md), la conclusión que **relaciona claridad, pruebas, diagnóstico y costo de cambio con artefactos concretos**: cada afirmación sobre qué paradigma resultó mejor apunta a algo que se puede revisar (un *diff*, una traza, una prueba, una medición). La palabra «retrospectiva» designa el cierre reflexivo del ejercicio. Se distingue de una retrospectiva de equipo ágil en que aquí el objeto es una comparación técnica y el criterio es la evidencia, no el sentir del grupo.

## Por qué importa

Después de implementar la misma regla en varios paradigmas, la conversación tiende a derivar a preferencias («me gustó más la versión funcional»). Las preferencias son legítimas, pero no son evidencia y no sirven para decidir qué mantener. La decisión que cambia es qué cuenta como argumento: [SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md) permite registrar «me gustó más» **como preferencia, no como evidencia**, y exige que las conclusiones sobre claridad o mantenibilidad se apoyen en artefactos. Así dos personas pueden discrepar sobre gustos y aun así acordar qué mostraron los datos.

## Cómo funciona

La retrospectiva organiza la evidencia en cuatro ejes y vincula cada uno a un artefacto:

- **Claridad:** qué tan fácil fue leer y explicar la regla (revisión por alguien ajeno, tiempo hasta entenderla), con ejemplos concretos de código.
- **Pruebas:** qué tan fácil fue probar la regla (cuántas dependencias hubo que simular, qué casos detectó el fixture común).
- **Diagnóstico:** qué tan fácil fue seguir una decisión errónea hasta su causa (la traza que cada versión produce).
- **Costo de cambio:** el *diff* del cambio dirigido en cada versión.

Hay una separación clave: **las diferencias del lenguaje y de las bibliotecas se separan de las del paradigma**. Una versión puede ser más corta porque el lenguaje en que se escribió tiene una función de biblioteca adecuada, no porque su paradigma sea superior. Si no se separan, se atribuye al modelo lo que es del ecosistema. Así la conclusión queda **acotada**: vale para esta regla, este lenguaje y este cambio.

## Ejemplo

Un fragmento de retrospectiva (ilustración, datos inventados):

```text
Costo de cambio:  tabla de reglas = 1 archivo; clases = 3 (cambio_dirigido.diff).
Diagnóstico:      traza funcional lista las reglas evaluadas; en objetos hay que
                  inspeccionar el estado (trazas/funcional.txt, trazas/objetos.txt).
Pruebas:          el fixture común detectó 2 divergencias en 'dato inválido'
                  (tests/fixture_semantico.py).
Preferencia (no evidencia): al autor le resultó más cómoda la versión de objetos.
Confusor: la versión funcional usa una biblioteca de tablas que las otras no.
```

Cada línea apunta a un archivo. Dos defectos documentados en la clase refuerzan la disciplina: las pruebas pasan pero un defecto plantado sobrevive porque falta el caso que ejercita esa regla (se añade el caso mínimo y se comprueba que el mutante falla), y dos versiones divergen solo con ciertos tipos porque el contrato no definía los inválidos.

## Errores y confusiones comunes

- **Presentar preferencias como hallazgos.** No son evidencia.
- **Atribuir al paradigma lo que es de la biblioteca.** Hay que separar las fuentes de diferencia.
- **Conclusiones sin artefacto.** Nadie puede verificarlas.
- **Generalizar.** Lo observado vale para esta regla y este cambio.

## Límites y cuándo no aplica

El taller compara un cambio y una carga pequeña, y no demuestra mantenibilidad a largo plazo ([SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md)). Una retrospectiva basada en un solo ejercicio tiene muestra mínima; el proyecto siguiente amplía pruebas, criterios y reporte para una comparación defendible. Y las preferencias de un equipo sí importan en la práctica (nadie mantiene bien lo que detesta), así que registrarlas aparte es lo correcto, no descartarlas.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Artefacto](../a/artefacto.md), [Costo](../c/costo.md), [Diagnóstico](../d/diagnostico.md), [Cambio dirigido](../c/cambio-dirigido.md), [Fixture semántico común](../f/fixture-semantico-comun.md), [Implementaciones idiomáticas](../i/implementaciones-idiomaticas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-083 — Taller: una regla de negocio en cinco paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Language Reference](https://docs.python.org/3/reference/) — Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project.
- [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) — Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project.
- [ReactiveX Observable Contract](https://reactivex.io/documentation/contract.html) — Notificaciones, terminación, errores y control de flujo observable; autoridad: ReactiveX project.
- [Erlang System Documentation: Processes](https://www.erlang.org/doc/system/ref_man_processes.html) — Procesos, buzones, envío de mensajes, enlaces y monitores; autoridad: Erlang/OTP project.

---

[↑ Glosario](../../README.md) · [← Retrospectiva](./retrospectiva.md) · [Retrospectiva sin culpa →](./retrospectiva-sin-culpa.md)
