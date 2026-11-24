# Hipótesis rivales

[↑ Glosario](../../README.md) · [← Hipótesis rival](./hipotesis-rival.md) · [Histograma →](./histograma.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Las **hipótesis rivales** son, en el taller de [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), **al menos dos explicaciones** de un fallo, formuladas a la vez y con **predicciones distintas**: si la hipótesis A es cierta, una observación debería ser X; si lo es B, debería ser Y. Se formulan antes de experimentar y se contrastan entre sí. El nombre viene de la práctica científica de no quedarse con la primera explicación; en el programa se aplica al diagnóstico de software.

## Por qué importa

Cuando se tiene una sola explicación, cada observación tiende a interpretarse como confirmación. Es el sesgo de confirmación: se busca lo que la apoya y se pasa por alto lo que no encaja. Con dos o más explicaciones en competencia, cada experimento se diseña para **separarlas**, y una observación que descarta una deja más fuerte a la otra. La decisión que cambia es qué se hace con una corazonada: no se ejecuta ni se «prueba cambiando código», se formula con su alternativa y se decide qué medir para distinguirlas.

## Cómo funciona

El procedimiento tiene cuatro movimientos:

1. **Formular al menos dos explicaciones plausibles**, incluyendo la menos cómoda (por ejemplo, «el defecto está en mi código» frente a «el defecto está en la dependencia»).
2. **Derivar una predicción distinta de cada una:** qué se vería en cada caso que no se vería en el otro.
3. **Elegir el experimento que más separa**, es decir, aquel cuyo resultado cambia más la confianza entre las hipótesis; no el más fácil de ejecutar.
4. **Registrar el resultado y qué se descartó.** Las hipótesis descartadas se documentan para que nadie las repita.

[SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md) agrega dos advertencias: **confirmar solo la favorita genera sesgo**, y una hipótesis **que no puede refutarse** todavía no guía el diagnóstico, porque ninguna observación la distinguiría de otra. Una hipótesis útil dice qué observación la contradiría.

## Ejemplo

Un fallo intermitente en la biblioteca de estructuras y algoritmos. Dos hipótesis:

```text
H1: el fallo depende del orden de llegada de los casos (estado acumulado).
H2: el fallo depende del tamaño del lote (límite o desborde).

predicción H1: con el mismo tamaño y orden barajado, el fallo aparece o desaparece.
predicción H2: con orden fijo y tamaño pequeño, el fallo desaparece siempre.
experimento: ejecutar con tamaño 10 y orden original, y con tamaño grande y orden barajado.
```

Si con tamaño pequeño y orden original el fallo persiste, H2 queda debilitada; si desaparece solo al cambiar el orden, H1 gana. El registro conserva ambas hipótesis y el resultado. El error que [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md) documenta, el diagnóstico que se repite entre personas por falta de registro, se corrige escribiendo hipótesis, pruebas y descartes.

## Errores y confusiones comunes

- **Una sola hipótesis.** Todo se lee como confirmación.
- **Experimentos que no separan.** Si las dos hipótesis predicen lo mismo, el resultado no informa.
- **Hipótesis irrefutables.** «Es un problema de concurrencia» sin decir qué observación lo desmentiría.
- **Cambiar código antes de reproducir.** Se actúa sobre una impresión; primero se escribe la prueba determinista.

## Límites y cuándo no aplica

El taller produce un diagnóstico del caso dado; no demuestra que todo el equipo pueda recrearlo ([SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md)). Cuando el fallo es obvio y el costo de probar la corrección es mínimo, formalizar dos hipótesis es exceso. Y en sistemas donde el fallo no se puede reproducir ni observar, las hipótesis pueden quedar sin contrastar y el diagnóstico apoyarse en evidencia indirecta.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Explicación](../e/explicacion.md), [Predicción](../p/prediccion.md), [Causa, corrección y seguimiento](../c/causa-correccion-y-seguimiento.md), [Cronología y hechos](../c/cronologia-y-hechos.md), [Escalera de herramientas](../e/escalera-de-herramientas.md), [Triage y contención](../t/triage-y-contencion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-107 — Taller: diagnosticar un fallo desconocido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

**También se usa en** (437 clases más lo mencionan; las que más):

[SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) — Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft.
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) — Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Pdb, cprofile, timeit, tracemalloc y límites instrumentales; autoridad: Python Software Foundation.
- [Python venv](https://docs.python.org/3/library/venv.html) — Aislamiento de intérprete, scripts y entorno virtual; autoridad: Python Software Foundation.
- [Development Container Specification](https://containers.dev/implementors/spec/) — Configuración reproducible de herramientas y ciclo de vida del contenedor; autoridad: Dev Container Specification maintainers.

---

[↑ Glosario](../../README.md) · [← Hipótesis rival](./hipotesis-rival.md) · [Histograma →](./histograma.md)
