# Conflicto semántico

[↑ Glosario](../../README.md) · [← Conflicto de texto](./conflicto-de-texto.md) · [Conflicto textual →](./conflicto-textual.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Incompatibilidad entre dos cambios que se fusionan sin marcas de texto.

Definición de trabajo de [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md): Cambios compatibles para la fusión e incompatibles para el programa.
- En [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md): Combinación de dos cambios que no choca en el texto y rompe una suposición compartida.

## Por qué importa

En [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), el tema «Conflictos semánticos» importa porque un cambio puede combinarse sin marcas y romper el sistema.

## Cómo funciona

Según [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), en la sección «Conflictos semánticos»:

Dos cambios pueden fusionarse sin conflicto de texto y ser incompatibles: uno cambia la firma de una función y otro añade una llamada con la firma vieja. Git no ve esto porque no entiende el programa. La defensa es probar el resultado de la combinación antes de aceptar, no solo cada rama por separado: integración continua sobre el tronco y, con volumen alto, una cola de fusión que prueba cada cambio sobre el estado actual.

Según [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), en la sección «Conflicto semántico»:

En Git real, una rama invirtió el orden de los parámetros de `penalizar(nota, horas)` y actualizó `informe.py`; otra, desde la versión anterior, añadió `panel.py` con la llamada de orden antiguo. La segunda fusión terminó con **código de salida 0** (sin conflicto de texto) y `panel.py` imprimió **42** en lugar de **60**. Para estimar la frecuencia, se simularon 500 PR con una proporción de solapamiento y una probabilidad de incompatibilidad dada: con un 10 % de solapamiento, main se rompió 0,9 veces con una incompatibilidad del 2 %, 2,4 con el 5 % y 5,1 con el 10 %; con un 30 % de solapamiento, 3,0, 7,0 y 14,8 veces (media de 20 semillas).

**Cómo leer la figura.** Es un mapa de calor: cada fila es una proporción de PR que tocan lo mismo que otro abierto, cada columna una probabilidad de incompatibilidad y el color de cada recuadro, las veces que main queda roto. Mira primero la esquina oscura, con 30 % de solapamiento y 10 % de incompatibilidad, y cómo el color crece en ambos sentidos. **Dónde deja de valer:** ambas proporciones son supuestos del autor; el caso real prueba que ocurre, no con qué frecuencia, y en un proyecto el solapamiento se mide con los PR abiertos al mismo tiempo, que depende de cuánto tardan en integrarse.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md):

La plataforma de entregas se despliega varias veces al día y mantiene una sola versión publicada. El equipo adopta ramas de un día integradas por PR, pruebas de menos de diez minutos, indicadores de funcionalidad para lo no terminado y una cola de fusión. No mantiene rama de desarrollo ni de versión: una corrección se hace en el tronco y se despliega. Para una integración con un cliente que fija versión, mantiene una rama de versión de la API con correcciones portadas durante seis meses.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md)) son:

- **Cada integración exige un día de resolver conflictos** — causa: las ramas viven semanas. Corrección: dividir el trabajo, acortar ramas e integrar a diario.
- **Main queda roto tras dos PR verdes** — causa: no se probó la combinación. Corrección: probar el resultado de la fusión o usar una cola de fusión.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos. Las personas, la zona caliente y los solapamientos son supuestos del autor, los conflictos se miden sobre texto y no se midió el costo de resolverlos, ni productividad, ni ningún equipo. La siguiente clase pregunta cómo se ata cada cambio de este flujo a su motivo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cambio compatible](./cambio-compatible.md), [Combinación](./combinacion.md), [Fusión](../f/fusion.md), [Suposición](../s/suposicion.md), [Backport](../b/backport.md), [Bisección](../b/biseccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Conflictos semánticos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Trunk Based Development](https://trunkbaseddevelopment.com/) — descripción de la práctica; autoridad: sitio de la comunidad de la práctica.
- [Driessen, «A successful Git branching model»](https://nvie.com/posts/a-successful-git-branching-model/) — origen de GitFlow; autoridad: el autor del modelo.
- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — definición y prácticas; autoridad: martinfowler.com.
- [Fowler, «Feature Toggles»](https://martinfowler.com/articles/feature-toggles.html) — tipos y costos de los indicadores; autoridad: martinfowler.com.
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) — flujo de ramas cortas con PR; autoridad: GitHub Docs.

---

[↑ Glosario](../../README.md) · [← Conflicto de texto](./conflicto-de-texto.md) · [Conflicto textual →](./conflicto-textual.md)
