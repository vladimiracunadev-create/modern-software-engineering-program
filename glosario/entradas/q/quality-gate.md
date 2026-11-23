# Quality gate

[↑ Glosario](../../README.md) · [← QM](./qm.md) · [Qubit →](./qubit.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Regla de decisión que decide, a partir de medidas del cambio, si este puede integrarse.

Definición de trabajo de [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md).

## Por qué importa

La clase donde se define, [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), existe con este propósito: la clase existe para que decidas qué comprobaciones automáticas y humanas debe pasar un cambio antes de integrarse, y para que sepas qué puede y qué no puede afirmar cada una.

## Cómo funciona

Según [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md):

Una **quality gate** es una regla de decisión sobre un conjunto de medidas: «el cambio entra si la cobertura de las líneas nuevas es al menos del 80 %, no hay alertas nuevas de severidad alta y la complejidad de las funciones tocadas no empeora». Tres decisiones de diseño importan más que el valor del umbral. La primera es **sobre qué se aplica**: el cambio, no el total, para que el umbral se mueva con lo que se evalúa. La segunda es **qué hace al fallar**: bloquear (el cambio no entra), avisar (entra con un comentario) o pedir una excepción registrada. Bloquear por todo enseña a saltarse la compuerta; avisar por todo la vuelve decoración.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md):

El equipo configura tres comprobaciones en el cambio: un analizador con las tres reglas y la excepción de prefijo, la cobertura de las líneas del cambio con umbral del 80 % y un comentario automático con la complejidad de las funciones tocadas. La regla de decisión dice: bloquea si hay alertas nuevas de las reglas de severidad alta o si la cobertura del cambio baja de 80 % en cambios de más de quince líneas; avisa en el resto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md)) son:

- **El pipeline está verde y el defecto llegó a producción** — causa: la regla no ve esa clase de defecto. Corrección: listar lo que no ve cada comprobación y cubrirlo con revisión o pruebas.
- **Las alertas del analizador se ignoran** — causa: precisión baja. Corrección: medir la precisión, afinar con datos y apartar las reglas ruidosas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md)) son: Las definiciones son operativas para el repositorio de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún proyecto real, ninguna herramienta comercial ni ninguna revisión humana; las funciones, los defectos sembrados, los cambios simulados, la calidad modelada y el 2 % de fallos propios son construcciones del autor, y las reglas se afinaron con los mismos casos que las evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla de decisión](../r/regla-de-decision.md), [Medida](../m/medida.md), [Regla](../r/regla.md), [Análisis estático](../a/analisis-estatico.md), [Cobertura del cambio](../c/cobertura-del-cambio.md), [Comprobación inestable](../c/comprobacion-inestable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SonarQube: quality gates](https://docs.sonarsource.com/sonarqube/latest/user-guide/quality-gates/) — ejemplo de compuerta sobre código nuevo; autoridad: documentación del producto.
- [Python: ast](https://docs.python.org/3/library/ast.html) — árbol sintáctico usado en las reglas; autoridad: documentación de Python.
- [Sadowski et al., «Lessons from building static analysis tools at Google»](https://doi.org/10.1145/3188720) — adopción de análisis estático y falsas alarmas; autoridad: Communications of the ACM, 2018.
- [Bacchelli y Bird, «Expectations, outcomes, and challenges of modern code review»](https://doi.org/10.1109/ICSE.2013.6606617) — qué aporta la revisión; autoridad: ICSE 2013.
- [Inozemtseva y Holmes, «Coverage is not strongly correlated with test suite effectiveness»](https://doi.org/10.1145/2568225.2568271) — límites de la cobertura; autoridad: ICSE 2014.

---

[↑ Glosario](../../README.md) · [← QM](./qm.md) · [Qubit →](./qubit.md)
