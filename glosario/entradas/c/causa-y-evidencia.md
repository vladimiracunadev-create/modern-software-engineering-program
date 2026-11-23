# Causa y evidencia

[↑ Glosario](../../README.md) · [← Causa común](./causa-comun.md) · [Causa, corrección y seguimiento →](./causa-correccion-y-seguimiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Explicación de por qué ocurre un conjunto de síntomas, sostenida por observaciones que otra persona puede revisar.

Definición de trabajo de [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md).

## Por qué importa

En [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), el tema «Causa y evidencia» importa porque agrupar síntomas por causa cambia el orden de prioridades, y solo la evidencia sostiene la agrupación.

## Cómo funciona

Según [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), en la sección «Causa y evidencia»:

Cada afirmación del tipo «estos cinco síntomas tienen la misma causa» es una hipótesis hasta que se observa algo que la distinga de las alternativas: un registro, una sesión observada, un contraejemplo. La regla de trabajo es separar tres columnas —hecho observado, inferencia, incógnita— y no mezclarlas. Cuando la causa se asigna por intuición y luego se usa como dato, el error se arrastra a las clases siguientes. Esta clase deja explícito qué parte de cada conclusión es observada y cuál es interpretación.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md):

En la plataforma de entregas, un ticket conserva identificador, fecha, texto original, canal y, cuando existe, una etiqueta de causa asignada por una persona identificada, con la fecha de asignación. El contrato del registro es que el texto original nunca se sobrescribe: la etiqueta de causa es una interpretación que puede cambiar, y el texto es el dato. Esa separación permite que un revisor vea cuántos síntomas se fusionaron y rehaga la agrupación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md)) son:

- **El tablero prioriza una falla que, al arreglarla, no reduce los tickets** — causa: se contó la frase y no la causa; varias redacciones de una causa quedaron dispersas. Corrección: etiquetar la causa por ticket (con quién y cuándo) y contar por causa, conservando el texto original.
- **La reunión discute «la solución» durante una hora sin acordar el problema** — causa: la petición original se aceptó como requisito. Corrección: reformular la petición como necesidad («necesito… para…») antes de proponer opciones.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se analizaron tickets reales, no se midió a ninguna persona y los rangos del dimensionamiento son supuestos. La siguiente clase pregunta quiénes son las personas detrás de los tickets y en qué contexto intentan hacer su trabajo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](./conjunto.md), [Explicación](../e/explicacion.md), [Observación](../o/observacion.md), [Necesidades](../n/necesidades.md), [Oportunidades](../o/oportunidades.md), [Problemas](../p/problemas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — marco oficial para investigar necesidades antes y durante el desarrollo; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) — formato de necesidad de usuario y criterios para validarla; autoridad: Government Digital Service.
- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — la discovery empieza reformulando una solución dada como problema por resolver; autoridad: Government Digital Service.
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — propone observar el trabajo que la persona intenta hacer antes que sus características demográficas; autoridad: Harvard Business Review (artículo parcialmente de pago).
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — vocabulario para gestionar riesgo de privacidad al recoger datos de personas; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Causa común](./causa-comun.md) · [Causa, corrección y seguimiento →](./causa-correccion-y-seguimiento.md)
