# Cobertura del cambio

[↑ Glosario](../../README.md) · [← Cobertura de un nivel](./cobertura-de-un-nivel.md) · [Cobertura del verificador →](./cobertura-del-verificador.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Fracción de las líneas añadidas o modificadas que ejecutan las pruebas.

Definición de trabajo de [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md).

## Por qué importa

La clase donde se define, [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), existe con este propósito: la clase existe para que decidas qué comprobaciones automáticas y humanas debe pasar un cambio antes de integrarse, y para que sepas qué puede y qué no puede afirmar cada una.

## Cómo funciona

Según [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md):

Las métricas de código (cobertura, complejidad, duplicación) se pueden calcular sobre el repositorio entero o sobre el cambio. La diferencia no es cosmética. La cobertura total de un repositorio de cien mil líneas se mueve menos de una décima de punto con un cambio de cien líneas, de modo que una compuerta sobre el total no distingue el cambio con las pruebas al 100 % del cambio sin ninguna: ambos mantienen el total por encima del umbral. La cobertura del cambio (qué fracción de las líneas añadidas o modificadas ejecutan las pruebas) sí lo distingue, a costa de ser ruidosa en cambios pequeños: un cambio de cinco líneas con tres cubiertas da 60 %.

Según [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md):

El equipo configura tres comprobaciones en el cambio: un analizador con las tres reglas y la excepción de prefijo, la cobertura de las líneas del cambio con umbral del 80 % y un comentario automático con la complejidad de las funciones tocadas. La regla de decisión dice: bloquea si hay alertas nuevas de las reglas de severidad alta o si la cobertura del cambio baja de 80 % en cambios de más de quince líneas; avisa en el resto. Los cambios de quince líneas o menos solo avisan, porque la cobertura es ruidosa. Las excepciones se piden en el propio cambio con motivo y caducidad. Una vez al mes se cuenta cuántos defectos escaparon y de qué clase, y las reglas se ajustan con esa lista, no con opiniones.

## Ejemplo

Ejemplo de [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) (sección «Ejemplo profesional»):

El equipo configura tres comprobaciones en el cambio: un analizador con las tres reglas y la excepción de prefijo, la cobertura de las líneas del cambio con umbral del 80 % y un comentario automático con la complejidad de las funciones tocadas. La regla de decisión dice: bloquea si hay alertas nuevas de las reglas de severidad alta o si la cobertura del cambio baja de 80 % en cambios de más de quince líneas; avisa en el resto. Los cambios de quince líneas o menos solo avisan, porque la cobertura es ruidosa. Las excepciones se piden en el propio cambio con motivo y caducidad.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md)) son:

- **El pipeline está verde y el defecto llegó a producción** — causa: la regla no ve esa clase de defecto. Corrección: listar lo que no ve cada comprobación y cubrirlo con revisión o pruebas.
- **Las alertas del analizador se ignoran** — causa: precisión baja. Corrección: medir la precisión, afinar con datos y apartar las reglas ruidosas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se comparan tres compuertas: cobertura total mínima del 70 %, que la cobertura total no baje y cobertura del cambio de al menos 80 %. ([SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Análisis estático](../a/analisis-estatico.md), [Comprobación inestable](./comprobacion-inestable.md), [Falsa alarma](../f/falsa-alarma.md), [Quality gate](../q/quality-gate.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: ast](https://docs.python.org/3/library/ast.html) — árbol sintáctico usado en las reglas; autoridad: documentación de Python.
- [Sadowski et al., «Lessons from building static analysis tools at Google»](https://doi.org/10.1145/3188720) — adopción de análisis estático y falsas alarmas; autoridad: Communications of the ACM, 2018.
- [Bacchelli y Bird, «Expectations, outcomes, and challenges of modern code review»](https://doi.org/10.1109/ICSE.2013.6606617) — qué aporta la revisión; autoridad: ICSE 2013.
- [Inozemtseva y Holmes, «Coverage is not strongly correlated with test suite effectiveness»](https://doi.org/10.1145/2568225.2568271) — límites de la cobertura; autoridad: ICSE 2014.
- [SonarQube: quality gates](https://docs.sonarsource.com/sonarqube/latest/user-guide/quality-gates/) — ejemplo de compuerta sobre código nuevo; autoridad: documentación del producto.

---

[↑ Glosario](../../README.md) · [← Cobertura de un nivel](./cobertura-de-un-nivel.md) · [Cobertura del verificador →](./cobertura-del-verificador.md)
