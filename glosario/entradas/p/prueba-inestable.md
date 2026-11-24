# Prueba inestable

[↑ Glosario](../../README.md) · [← Prueba frágil](./prueba-fragil.md) · [Prueba metamórfica →](./prueba-metamorfica.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Una **prueba inestable** (en inglés, *flaky test*) es una prueba que, **sin cambios en el código ni en los datos declarados, pasa o falla según la ejecución**. El programa usa el término con el mismo sentido en varias clases: [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) la describe como una prueba con resultado no determinista sin cambio relevante; [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) y [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), como una que pasa y falla sobre el mismo código sin que nada haya cambiado. La clase [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) la trata a fondo y distingue la prueba inestable de un **defecto intermitente real**.

## Por qué importa

Una suite de pruebas vale por lo que significa su resultado: un rojo debe querer decir «algo se rompió». Las pruebas inestables destruyen esa señal. El efecto es multiplicativo: si cada prueba inestable falla con probabilidad *q*, una suite sana sale roja con probabilidad `1 − (1 − q)^m` con *m* pruebas inestables. Según [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), con 20 pruebas que fallan el 5 % de las veces, el **64 %** de los *commits* sanos se ven rojos. El rojo constante enseña a reejecutar sin leer, y entonces un fallo real pasa inadvertido.

## Cómo funciona

Las causas conocidas son esperas asíncronas (la prueba no espera lo suficiente a algo que tarda), dependencia del **orden de ejecución**, de la **hora**, de la **red** o de **datos compartidos** entre pruebas. En todas, la prueba depende de algo que no controla, y a veces ese algo es favorable y a veces no.

La respuesta habitual, **reintentar hasta que pase**, reduce los falsos rojos pero tiene un costo menos visible: un **defecto intermitente real** (una condición de carrera en el producto) también pasa en alguno de los reintentos, y la suite lo declara sano. Por eso [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) desactiva los reintentos automáticos de integración durante la estabilización. El tratamiento que enseña el programa es:

1. **Medir:** ejecutar la suite muchas veces sobre un *commit* sano para identificar qué pruebas varían.
2. **Clasificar la causa con evidencia:** ¿es la prueba o el producto?
3. **Poner en cuarentena** las inestables con **dueño y plazo**, y corregir la causa.
4. **Mantener la suite** de modo que un fallo siga significando algo.

## Ejemplo

El taller de [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) (escenario hipotético de la clase, sin datos reales): la suite se ejecuta cien veces sobre un *commit* sano y se identifican 7 pruebas inestables de 412; se ponen en cuarentena con dueño y plazo y se desactivan los reintentos automáticos. Una prueba inestable típica:

```python
def test_notifica():
    enviar_en_segundo_plano(caso)
    time.sleep(0.1)                 # asume que 100 ms bastan
    assert bandeja.contiene(caso)   # falla si el envío tarda más
```

La corrección es esperar una condición con plazo (`esperar_hasta(lambda: bandeja.contiene(caso), timeout=5)`), no un tiempo fijo.

## Errores y confusiones comunes

- **Reintentar hasta que pase.** Oculta defectos intermitentes reales.
- **Confundir inestable con intermitente.** La causa puede estar en la prueba o en el producto; hay que clasificar.
- **Ignorar el rojo.** El equipo aprende a reejecutar sin leer.
- **Cuarentena sin dueño ni plazo.** La prueba queda olvidada.

## Límites y cuándo no aplica

El cálculo del 64 % supone pruebas independientes con la misma probabilidad; en la práctica el fallo se concentra en pocas pruebas inestables y se correlaciona con la carga del entorno ([SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md)). Es una cota del mecanismo, no una predicción de una suite real. La noción de inestabilidad tampoco aplica a pruebas deliberadamente aleatorias que fijan su semilla: si la semilla está fija, el resultado es reproducible.

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
