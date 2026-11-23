# Compuerta

[↑ Glosario](../../README.md) · [← Compromisos entre atributos](./compromisos-entre-atributos.md) · [Compuerta de abandono →](./compuerta-de-abandono.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Una **compuerta** (*gate*) es una comprobación con veredicto de paso o fallo que un cambio debe superar para avanzar. Es una de las palabras más usadas del programa y no siempre con el mismo alcance, así que conviene precisar qué sentido usa cada clase:

- **El sentido central** ([SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), [SE-578](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md)): una comprobación automática cuyo resultado decide si un cambio puede integrarse o pasar de etapa. [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) pide que su criterio no dependa de opinión y que su veredicto sea reproducible: con el mismo cambio, el mismo resultado.
- **En integración continua** ([SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md)): el punto del flujo que bloquea o avisa según un umbral.
- **En una plataforma de datos** ([SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md)): el conjunto de reglas que decide si un conjunto de datos se publica.
- **Un uso más amplio** ([SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md)): una medida que reduce la probabilidad o el impacto de un riesgo, es decir, un control.

El glosario recoge el sentido central y señala los otros como matices del mismo núcleo: una condición que se comprueba antes de dejar pasar algo.

## Por qué importa

Una compuerta convierte una expectativa («esto debería compilar y pasar las pruebas») en un freno que no depende de la memoria ni de la buena voluntad de nadie. Es la pieza que hace posible delegar trabajo, a otras personas o a un agente, sin revisar cada paso: si el cambio pasa las compuertas, está dentro de lo que se verificó. [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) la presenta en el contexto de un agente que escribe código, donde la compuerta es lo que da confianza en un «pasa».

## Cómo funciona

[SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) describe el diseño de un conjunto de compuertas con cuatro decisiones:

1. **Criterio ejecutable.** «El código compila», «el linter no reporta problemas», «no hay cadenas con forma de secreto», «las pruebas pasan». Böckeler llama controles computacionales a los deterministas y baratos, y los distingue de los inferenciales (un modelo que revisa), más ricos y menos fiables.
2. **Menú único.** La persona, el agente y la integración continua ejecutan las mismas compuertas con el mismo comando. Si cada cual ejecuta un subconjunto, un cambio pasa en un lugar y falla en otro y se erosiona la confianza en «pasa». El menú es un script con un solo punto de entrada que lista las compuertas en orden, se detiene en la primera que falla, imprime su nombre y el motivo y devuelve un código de salida.
3. **Orden por costo.** Las compuertas baratas detectan muchos defectos con poco costo: en el experimento, la de estilo (de microsegundos a un milisegundo) atrapa 5 de los 11 defectos, y las pruebas, que tardan cientos de milisegundos, atrapan 2. Se ordena de barato a caro y se detiene en el primer fallo. [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) lo expresa como ordenar por razón de detección sobre costo: si el primer rojo tarda más de diez minutos, las etapas caras están primero.
4. **Meta-verificación.** Una compuerta que compara con la versión anterior detecta que las aserciones no bajen y que no aparezcan marcas de omisión sin justificación: no prueba el código, prueba que la prueba no se debilitó.

## Ejemplo

En el experimento de [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md), once defectos se evalúan contra un menú de compuertas. Solo dos (un error de sintaxis que rompe la importación y un error de lógica que una prueba ve) son atrapados por las pruebas; los demás (una importación sin usar, un `except` sin tipo, un argumento mutable, una impresión de depuración, un secreto literal) pasan las pruebas y los atrapa alguna compuerta barata. Dos defectos más consisten en debilitar la prueba, y los atrapa la compuerta de meta-verificación. Dos escapan: un error de lógica en una rama que ninguna prueba ejerce y una prueba que replica el error. La conclusión de la clase: «las pruebas pasan» es una compuerta, no la compuerta.

## Errores y confusiones comunes

- **El primer rojo tarda más de diez minutos.** Las etapas caras van primero; corrección ([SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md)): ordenar por razón de detección sobre costo.
- **El análisis de seguridad se ignora.** Bloquea por hallazgos sin corrección; hay que separar el bloqueo (críticos con corrección) del informe.
- **Las reglas se desactivan.** Muchas falsas alarmas; corrección: medir precisión y afinar con casos negativos.
- **Que cada cual ejecute un subconjunto.** Rompe la confianza en «pasa» ([SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md)).
- **Confundir la compuerta con la garantía.** Una compuerta verde dice que se verificó lo que se verificó, y no más.

## Límites y cuándo no aplica

[SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) declara que ningún menú lo ve todo y que declarar ese límite es parte del menú: una rama que ninguna prueba ejerce se mitiga con cobertura y pruebas basadas en propiedades; una prueba que replica el error exige una fuente independiente del oráculo (una especificación, una revisión humana, una evaluación de otro tipo). Un control inferencial (un modelo que revisa) es más rico y menos fiable que uno computacional, y su veredicto no es reproducible. Y los resultados cuantitativos (5 de 11, 2 de 11) son de un experimento de la clase con un módulo de siete líneas, no una proporción transferible.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Comprobación automática](./comprobacion-automatica.md), [Resultado](../r/resultado.md), [Ancla externa](../a/ancla-externa.md), [Bitácora encadenada](../b/bitacora-encadenada.md), [Criterio de aceptación](./criterio-de-aceptacion.md), [Exhaustividad](../e/exhaustividad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-483 — Tests, seguridad y políticas como gates](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (25 clases más lo mencionan; las que más):

[SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md), [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «gate».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub Actions: uso seguro](https://docs.github.com/en/actions/reference/security/secure-use) — acciones fijadas, permisos del token e inyección en scripts; autoridad: documentación de GitHub.
- [NIST SP 800-218 (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro; autoridad: NIST.
- [Open Policy Agent](https://www.openpolicyagent.org/docs) — políticas como código; autoridad: documentación del proyecto.
- [Luo et al., «An empirical analysis of flaky tests»](https://doi.org/10.1145/2635868.2635920) — causas de las pruebas inestables (FSE 2014); autoridad: artículo con DOI verificado en Crossref.
- [Google Testing Blog: flaky tests](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html) — gestión de pruebas inestables; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Compromisos entre atributos](./compromisos-entre-atributos.md) · [Compuerta de abandono →](./compuerta-de-abandono.md)
