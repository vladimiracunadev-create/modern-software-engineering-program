# Regla de tres

[↑ Glosario](../../README.md) · [← Regla de reserva](./regla-de-reserva.md) · [Regla decidible →](./regla-decidible.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Con \(n\) ejecuciones sin fallo, el límite superior del 95 % de la tasa de fallo es cercano a \(3/n\).

Definición de trabajo de [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md): Con n ensayos sin fallas, la tasa de fallas es menor que 3/n con 95 % de confianza.

## Por qué importa

La clase donde se define, [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), existe con este propósito: la clase existe para que diagnostiques las pruebas que fallan a veces: que calcules cuánto ruido produce una suite aunque cada prueba sea casi estable, que distingas una prueba inestable de un defecto intermitente real, que clasifiques la causa con evidencia y que mantengas la suite de modo que un fallo siga significando algo.

## Cómo funciona

Según [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md):

Un reintento arregla la apariencia: una prueba con 2 % de fallo espurio termina en verde el 97,92 % de las veces sin reintento, 99,96 % con uno y 100 % con dos o tres. Pero un defecto intermitente real que ocurre el 30 % de las ejecuciones termina en verde el 70,1 % sin reintento, 91,2 % con uno, 97,3 % con dos y 99,3 % con tres: el mismo mecanismo que silencia el ruido esconde la señal. Descartar con un 95 % de confianza una tasa de fallo de 1 % exige 299 ejecuciones sin fallos (regla de tres: \(\ln 0{,}05 / \ln(1-p)\)); para 2 %, 149; para 5 %, 59.

Según [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md):

Un ensayo es una repetición del evento (revocar una credencial y comprobar que deja de funcionar). Si el control tiene eficacia real p, la probabilidad de que n ensayos independientes salgan todos bien es `p^n`. Un control con eficacia de 95 % (falla una vez de cada veinte) pasa 5 ensayos con probabilidad 77 %, 20 ensayos con 36 % y 59 ensayos con solo 4,8 %. Eso fija la **regla de tres**: si n ensayos salen bien, con 95 % de confianza la tasa de fallas es menor que 3/n; con 59 ensayos, menor que 5 %. No es una peculiaridad: es la forma de pasar de «no vimos fallas» a «la tasa de fallas es menor que el límite con tal confianza».

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md):

El equipo de la plataforma guarda el historial de cada prueba (resultado, hora, carga, versión y pruebas anteriores del mismo trabajador) en una tabla y calcula cada semana la tasa de fallo espurio por prueba y por suite. Una prueba con más de 0,1 % de fallo espurio entra en cuarentena: sigue ejecutándose pero no bloquea, y tiene un responsable, una fecha de revisión a 14 días y un criterio de salida (300 ejecuciones sin fallo tras la corrección).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md)) son:

- **La suite casi nunca pasa limpia con pruebas «casi estables»** — causa: \((1-p)^N\) con \(N\) grande. Corrección: presupuesto de inestabilidad por prueba y por suite.
- **Un defecto real se descarta como «intermitente»** — causa: reintentos sin registro. Corrección: registrar cada reintento y revisar su tasa.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Descartar con un 95 % de confianza una tasa de fallo de 1 % exige 299 ejecuciones sin fallos (regla de tres: \(\ln 0{,}05 / \ln(1-p)\)); para 2 %, 149; para 5 %, 59. ([SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md), [SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Confianza](../c/confianza.md), [Ensayo](../e/ensayo.md), [Límite](../l/limite.md), [Caos de seguridad](../c/caos-de-seguridad.md), [Condición de carrera](../c/condicion-de-carrera.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), [SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md).

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

[↑ Glosario](../../README.md) · [← Regla de reserva](./regla-de-reserva.md) · [Regla decidible →](./regla-decidible.md)
