# Contrato ejecutable

[↑ Glosario](../../README.md) · [← Contrato dirigido por el consumidor](./contrato-dirigido-por-el-consumidor.md) · [Contrato entre equipos →](./contrato-entre-equipos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Afirmación de un contrato escrita en código que puede comprobarse en ejecución o en pruebas.

Definición de trabajo de [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md).

## Por qué importa

La clase donde se define, [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), existe con este propósito: la clase existe para escribir lo que un componente promete y exige como afirmaciones que se ejecutan, de modo que una violación se detecte en el punto donde ocurre y no tres módulos más adelante.

## Cómo funciona

[SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md):

En la plataforma, cada operación pública de `Calificacion` documenta su contrato en el docstring (quién debe qué) y lo ejecuta con `assert` en pruebas. Los invariantes viven en un método `inv()` que cada operación llama al terminar. Un módulo de pruebas basadas en un conductor aleatorio ejecuta secuencias válidas y falla si algún contrato salta; un segundo conjunto ejecuta entradas ilegales y comprueba que la precondición correcta rechaza cada una. La política declara qué contratos se mantienen en producción (nota en rango, publicada con nota) y cuáles se retiran.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md)) son:

- **El invariante falla lejos de donde se corrompió el estado** — causa: se comprueba al final o cada muchas operaciones. Corrección: comprobar en la frontera de cada operación pública, al menos en pruebas.
- **Una subclase rompe a los clientes de la base pese a compilar** — causa: reforzó una precondición o debilitó una postcondición. Corrección: aplicar la regla: aceptar al menos lo mismo, garantizar al menos lo mismo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo los tiempos. No se usó ninguna biblioteca de contratos, los nueve defectos y la probabilidad de reparación son supuestos del autor y no se midió a ningún equipo. La siguiente clase pregunta qué estructura y qué comportamiento tienen las entidades cuyos contratos se acaban de escribir.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Contrato](./contrato.md), [Invariante](../i/invariante.md), [Invariante de clase](../i/invariante-de-clase.md), [Postcondición](../p/postcondicion.md), [Precondición](../p/precondicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Meyer, «Applying design by contract» (IEEE Computer, 1992)](https://doi.org/10.1109/2.161279) — formulación del diseño por contrato; autoridad: IEEE Computer.
- [Liskov y Wing, «A behavioral notion of subtyping» (TOPLAS, 1994)](https://doi.org/10.1145/197320.197383) — subtipado conductual y reglas de sustitución; autoridad: ACM TOPLAS.
- [Hoare, «An axiomatic basis for computer programming» (CACM, 1969)](https://doi.org/10.1145/363235.363259) — tripleta precondición–instrucción–postcondición; autoridad: Communications of the ACM.
- [Eiffel: Design by Contract](https://www.eiffel.com/values/design-by-contract/) — descripción del mecanismo en el lenguaje que lo introdujo; autoridad: Eiffel Software.
- [Python: sentencia `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) — semántica de `assert` y su desactivación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Contrato dirigido por el consumidor](./contrato-dirigido-por-el-consumidor.md) · [Contrato entre equipos →](./contrato-entre-equipos.md)
