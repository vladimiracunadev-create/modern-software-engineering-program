# Fallo espurio

[↑ Glosario](../../README.md) · [← Falla inyectada](./falla-inyectada.md) · [Fallo inyectado →](./fallo-inyectado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Fallo que no corresponde a un defecto del producto.

Definición de trabajo de [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md): Fallo de una prueba que no corresponde a un defecto del producto.

## Por qué importa

La clase donde se define, [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), existe con este propósito: la clase existe para que diagnostiques las pruebas que fallan a veces: que calcules cuánto ruido produce una suite aunque cada prueba sea casi estable, que distingas una prueba inestable de un defecto intermitente real, que clasifiques la causa con evidencia y que mantengas la suite de modo que un fallo siga significando algo.

## Cómo funciona

Según [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md):

Reintentar una prueba que falla es una decisión sobre qué errores se toleran. Para una prueba con 2 % de fallo espurio, un reintento la deja en verde el 99,96 % de las veces: el ruido desaparece. Pero un defecto real que ocurre en el 30 % de las ejecuciones también termina en verde el 91,2 % de las veces con un reintento y el 97,3 % con dos. El reintento no distingue entre los dos, y la diferencia importa: lo que se silencia puede ser el defecto que llegará a producción. Si se reintenta, se registra cada reintento y se revisa la tasa.

Según [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md):

El equipo de la plataforma guarda el historial de cada prueba (resultado, hora, carga, versión y pruebas anteriores del mismo trabajador) en una tabla y calcula cada semana la tasa de fallo espurio por prueba y por suite. Una prueba con más de 0,1 % de fallo espurio entra en cuarentena: sigue ejecutándose pero no bloquea, y tiene un responsable, una fecha de revisión a 14 días y un criterio de salida (300 ejecuciones sin fallo tras la corrección). Los reintentos están desactivados por defecto: se activan por prueba con un registro de cuántas veces se usaron, y la tasa de reintentos se publica.

## Ejemplo

Ejemplo de [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma guarda el historial de cada prueba (resultado, hora, carga, versión y pruebas anteriores del mismo trabajador) en una tabla y calcula cada semana la tasa de fallo espurio por prueba y por suite. Una prueba con más de 0,1 % de fallo espurio entra en cuarentena: sigue ejecutándose pero no bloquea, y tiene un responsable, una fecha de revisión a 14 días y un criterio de salida (300 ejecuciones sin fallo tras la corrección). Los reintentos están desactivados por defecto: se activan por prueba con un registro de cuántas veces se usaron, y la tasa de reintentos se publica.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La suite casi nunca está en verde sin cambios** — causa: demasiados pasos con fallo espurio pequeño. Corrección: calcular \((1-q)^k\) y acortar o dividir los recorridos. ([SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un reintento arregla la apariencia: una prueba con 2 % de fallo espurio termina en verde el 97,92 % de las veces sin reintento, 99,96 % con uno y 100 % con dos o tres. ([SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producto](../p/producto.md), [Aserción semántica](../a/asercion-semantica.md), [Condición de carrera](../c/condicion-de-carrera.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Cuarentena](../c/cuarentena.md), [Instantánea](../i/instantanea.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Luo et al., «An empirical analysis of flaky tests»](https://doi.org/10.1145/2635868.2635920) — causas de las pruebas inestables; autoridad: artículo revisado de FSE 2014.
- [Lam et al., «iDFlakies»](https://doi.org/10.1109/ICST.2019.00038) — detección de pruebas inestables; autoridad: artículo revisado de ICST 2019.
- [Google Testing Blog: Flaky Tests at Google and How We Mitigate Them](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html) — mitigación en una organización; autoridad: equipo de pruebas de Google.
- [Micco, «The State of Continuous Integration Testing @Google»](https://research.google/pubs/the-state-of-continuous-integration-testing-google/) — integración continua a gran escala; autoridad: Google Research.
- [Martin Fowler, «Eradicating Non-Determinism in Tests»](https://martinfowler.com/articles/nonDeterminism.html) — causas y tratamiento; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Falla inyectada](./falla-inyectada.md) · [Fallo inyectado →](./fallo-inyectado.md)
