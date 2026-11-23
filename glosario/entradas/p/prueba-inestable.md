# Prueba inestable

[↑ Glosario](../../README.md) · [← Prueba frágil](./prueba-fragil.md) · [Prueba metamórfica →](./prueba-metamorfica.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Prueba que, sin cambios en el código ni en los datos declarados, pasa o falla según la ejecución.

Definición de trabajo de [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md): Prueba que pasa y falla sobre el mismo código sin que nada cambie.
- En [SE-483 — Tests, seguridad y políticas como gates](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md): Prueba que pasa y falla sobre el mismo código sin que nada haya cambiado.
- En [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md): Prueba con resultado no determinista sin cambio relevante.

## Por qué importa

La clase donde se define, [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), existe con este propósito: la clase existe para que diagnostiques las pruebas que fallan a veces: que calcules cuánto ruido produce una suite aunque cada prueba sea casi estable, que distingas una prueba inestable de un defecto intermitente real, que clasifiques la causa con evidencia y que mantengas la suite de modo que un fallo siga significando algo.

## Cómo funciona

Según [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md):

**Cómo leer la figura.** El eje horizontal es el número de pruebas (escala logarítmica) y el vertical, el porcentaje de corridas sin ningún fallo espurio; cada curva fija la inestabilidad de cada prueba. Mira en qué tamaño cada curva se hunde. **Dónde deja de valer:** supone pruebas independientes con la misma probabilidad; en la práctica el fallo se concentra en pocas pruebas inestables y se correlaciona con la carga. La figura es una cota del mecanismo y no una predicción de una suite real.

Según [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md):

Una prueba **inestable** (flaky) pasa y falla con el mismo código. Sus causas conocidas son esperas asíncronas, dependencia del orden de ejecución, de la hora, de la red o de datos compartidos. El efecto sobre la suite es multiplicativo: si cada prueba inestable falla con probabilidad q, la suite sana sale roja con probabilidad 1 − (1 − q)^m con m pruebas inestables. Con 20 pruebas que fallan el 5 % de las veces, el 64 % de los commits sanos se ven rojos. El rojo constante enseña a reejecutar sin leer. La respuesta habitual, **reintentar hasta que pase**, reduce los falsos rojos y tiene un costo menos visible: un defecto intermitente real también pasa en alguno de los reintentos, y la suite lo declara sano.

## Ejemplo

Ejemplo de [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo ejecuta el taller en seis estaciones durante dos semanas. Estación 1: construye el artefacto dos veces en máquinas distintas, encuentra que las fechas del empaquetado lo impiden, las fija y vuelve a comparar. Estación 2: ejecuta la suite cien veces sobre un commit sano, identifica 7 pruebas inestables de 412 y las pone en cuarentena con dueño y plazo; desactiva los reintentos automáticos de la integración. Estación 3: carga las pruebas de caracterización de los tres puntos calientes del mapa de riesgo. Estación 4: despliega y revierte una versión en el entorno de ensayo, con cronómetro.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La suite sale roja y verde sin cambios** — causa: pruebas inestables. Corrección: cuarentena con dueño y plazo, y corregir la causa. ([SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** supone pruebas independientes con la misma probabilidad; en la práctica el fallo se concentra en pocas pruebas inestables y se correlaciona con la carga. ([SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Resultado](../r/resultado.md), [Sobre](../s/sobre.md), [Condición de carrera](../c/condicion-de-carrera.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Cuarentena](../c/cuarentena.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-483 — Tests, seguridad y políticas como gates](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «flaky».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Luo et al., «An empirical analysis of flaky tests»](https://doi.org/10.1145/2635868.2635920) — causas de las pruebas inestables; autoridad: artículo revisado de FSE 2014.
- [Lam et al., «iDFlakies»](https://doi.org/10.1109/ICST.2019.00038) — detección de pruebas inestables; autoridad: artículo revisado de ICST 2019.
- [Google Testing Blog: Flaky Tests at Google and How We Mitigate Them](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html) — mitigación en una organización; autoridad: equipo de pruebas de Google.
- [Micco, «The State of Continuous Integration Testing @Google»](https://research.google/pubs/the-state-of-continuous-integration-testing-google/) — integración continua a gran escala; autoridad: Google Research.
- [Martin Fowler, «Eradicating Non-Determinism in Tests»](https://martinfowler.com/articles/nonDeterminism.html) — causas y tratamiento; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Prueba frágil](./prueba-fragil.md) · [Prueba metamórfica →](./prueba-metamorfica.md)
