# Comprobación inestable

[↑ Glosario](../../README.md) · [← Comprobación de forma](./comprobacion-de-forma.md) · [Comprobación previa de CORS →](./comprobacion-previa-de-cors.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Comprobación cuyo resultado varía sin que cambie el código.

Definición de trabajo de [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md).

## Por qué importa

La clase donde se define, [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), existe con este propósito: la clase existe para que decidas qué comprobaciones automáticas y humanas debe pasar un cambio antes de integrarse, y para que sepas qué puede y qué no puede afirmar cada una.

## Cómo funciona

[SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el repositorio de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md):

El equipo configura tres comprobaciones en el cambio: un analizador con las tres reglas y la excepción de prefijo, la cobertura de las líneas del cambio con umbral del 80 % y un comentario automático con la complejidad de las funciones tocadas. La regla de decisión dice: bloquea si hay alertas nuevas de las reglas de severidad alta o si la cobertura del cambio baja de 80 % en cambios de más de quince líneas; avisa en el resto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un cambio correcto se bloquea cuatro veces** — causa: comprobación inestable en la cadena. Corrección: hacerla determinista o apartarla del bloqueo. ([SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md)) son: Las definiciones son operativas para el repositorio de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún proyecto real, ninguna herramienta comercial ni ninguna revisión humana; las funciones, los defectos sembrados, los cambios simulados, la calidad modelada y el 2 % de fallos propios son construcciones del autor, y las reglas se afinaron con los mismos casos que las evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Análisis estático](../a/analisis-estatico.md), [Cobertura del cambio](./cobertura-del-cambio.md), [Falsa alarma](../f/falsa-alarma.md), [Quality gate](../q/quality-gate.md).
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

[↑ Glosario](../../README.md) · [← Comprobación de forma](./comprobacion-de-forma.md) · [Comprobación previa de CORS →](./comprobacion-previa-de-cors.md)
