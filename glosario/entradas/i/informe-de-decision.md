# Informe de decisión

[↑ Glosario](../../README.md) · [← Informativo](./informativo.md) · [Informe de entrega →](./informe-de-entrega.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Un **informe de decisión** es, en el proyecto de [SE-084](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md), el documento que cierra una comparación de paradigmas **conectando cuatro cosas: fuerza, observación, consecuencia y elección por contexto**. Parte de las fuerzas del problema, presenta lo que se observó al implementarlo y probarlo, deduce las consecuencias y recomienda una elección **para un contexto**, no una verdad general. Es un entregable propio del programa, cercano a un registro de decisión de arquitectura pero centrado en la comparación de modelos.

## Por qué importa

Comparar soluciones produce datos, y los datos sin conclusión no deciden nada. El informe es el puente entre la medición y la acción, y obliga a que cada recomendación tenga apoyo visible. La decisión que cambia es qué se entrega al terminar una comparación: no «esta solución me gusta más», sino una recomendación **trazable** hasta una fuerza del problema y una observación reproducible, y con la indicación de cuándo dejaría de ser válida.

## Cómo funciona

La estructura sigue la cadena de justificación:

1. **Fuerza:** la propiedad del problema que decide (auditabilidad, tasa de cambio, concurrencia).
2. **Observación:** qué se vio al implementar y probar, con datos, comando y versión.
3. **Consecuencia:** qué implica esa observación para mantener y evolucionar el sistema.
4. **Elección por contexto:** qué se recomienda **dado ese contexto**.

[SE-084](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md) ilustra que la recomendación puede ser **mixta**: reglas para la política y flujo reactivo para la telemetría, unidos por un adaptador pequeño. Y exige una cláusula honesta: el informe **declara cuándo esa combinación dejaría de ser adecuada**, es decir, qué cambio en las fuerzas invalidaría la elección. La causa de que esto importe es que las decisiones de diseño caducan cuando cambia el contexto, y sin esa cláusula nadie sabe cuándo revisarlas.

## Ejemplo

Un fragmento del informe del proyecto (ilustración, contenido inventado):

```text
Fuerza:        auditabilidad alta y reglas que cambian mensualmente.
Observación:   la versión de tabla de reglas cambió 1 archivo ante la regla nueva;
               la versión con clases tocó 3 (comando: pytest -k cambio_dirigido, v1.4.0).
Consecuencia:  la decisión de negocio vive en un solo lugar y es auditable.
Elección:      reglas como datos para la política; flujo reactivo para telemetría,
               unidos por un adaptador de 30 líneas.
Deja de valer: si las reglas pasan a depender de estado acumulado entre casos.
```

Dos errores documentados en la clase se evitan con este formato: el informe que afirma sin comando reproducible (se añade comando, versión y salida a cada afirmación) y la suite que pasa pero hay defectos, porque solo hay casos del camino feliz (se derivan casos del contrato y de los mutantes).

## Errores y confusiones comunes

- **Afirmaciones sin evidencia reproducible.** Nadie puede verificarlas.
- **Conclusiones universales.** «El paradigma X es mejor» en lugar de «para este contexto».
- **Omitir cuándo deja de valer.** La recomendación queda sin fecha de revisión.
- **Un informe que describe sin decidir.** Lista observaciones y no elige.

## Límites y cuándo no aplica

El proyecto demuestra equivalencia para el corpus y las propiedades declaradas, no para todas las entradas posibles ni para cargas de producción ([SE-084](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md)). Un informe no sustituye datos de mantenimiento reales, que solo llegan con el tiempo. Para decisiones pequeñas y reversibles, una nota breve en el cambio basta; el informe completo se justifica cuando la decisión es costosa de revertir.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Consecuencia](../c/consecuencia.md), [Contextos](../c/contextos.md), [Fuerza](../f/fuerza.md), [Observación](../o/observacion.md), [Contrato y corpus de comparación](../c/contrato-y-corpus-de-comparacion.md), [Métricas interpretadas](../m/metricas-interpretadas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-084 — Proyecto: comparación semántica con pruebas comunes](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md).

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

[↑ Glosario](../../README.md) · [← Informativo](./informativo.md) · [Informe de entrega →](./informe-de-entrega.md)
