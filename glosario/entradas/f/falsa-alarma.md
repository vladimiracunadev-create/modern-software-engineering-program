# Falsa alarma

[↑ Glosario](../../README.md) · [← Fallo, enlaces y supervisión](./fallo-enlaces-y-supervision.md) · [Falsa denegación →](./falsa-denegacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Una **falsa alarma** es la activación de un aviso, regla o disparador cuando el problema que debía detectar no existe. El programa la usa con un núcleo común y matices por clase: en [SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), la activación de un disparador sin que el plan haya dejado de valer; en [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), el aviso de una función cuando la propiedad se cumple; en [SE-578](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md), el bloqueo de un cambio que no infringe la regla; en [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), el fallo de una suite sobre una configuración sana; en [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), el código que una regla señala y que, mirado en su contexto, no es un problema; en [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), la reversión de un canario sin defecto real.

## Por qué importa

Cada falsa alarma cuesta atención y credibilidad. Una regla que alarma casi siempre acaba ignorada, y entonces la alarma verdadera pasa desapercibida. Cambia el diseño de umbrales y ventanas: no se trata solo de detectar, sino de detectar sin alarmar de más.

## Cómo funciona

La causa estructural es el compromiso entre dos errores. [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) lo explica con el canario: el umbral fija el equilibrio entre ambos; **bajo, y se revierte sin defecto (falsa alarma); alto, y tarda más en declararse un defecto real**. Con ruido, el umbral decide cuántas falsas alarmas se producen.

La cuenta que sorprende es la de **evaluaciones repetidas**. En [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), sin ningún defecto (error del 0,5 % en ambas versiones), se evalúa la prueba cada segundo durante 30 minutos con un canario del 5 % y se cuenta cuántos de 200 episodios terminan en reversión según el umbral. Con un umbral del 5 % para una sola decisión, se revierte el 47 % de los episodios, porque se evalúa 1.800 veces. Las evaluaciones consecutivas están correlacionadas (no son 1.800 pruebas independientes), pero el efecto es grande. Es el mismo problema de mirar los resultados repetidamente.

[SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md) lo aplica a los disparadores: si cada semana hay una probabilidad independiente de 5 % de activarse sin motivo, en 20 semanas la probabilidad de al menos una falsa alarma es 1 − 0,95²⁰ ≈ 64 %. Las defensas son las mismas: exigir **avisos seguidos** (ventana), ampliar la ventana, subir el umbral y **medir las falsas alarmas** para ajustarlas.

## Ejemplo

Un canario del 5 % se evalúa cada segundo con un umbral del 5 % por decisión. Aunque las dos versiones sean idénticas, al cabo de 30 minutos casi la mitad de los episodios termina en reversión. Con un umbral más estricto y la exigencia de varias evaluaciones consecutivas, las reversiones innecesarias caen a una fracción pequeña, a costa de tardar más en detectar un defecto real. (Resultado de [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), expresado con las cifras de la clase.)

## Errores y confusiones comunes

- **Nadie reacciona a la alarma de replanificación**: regla sin ventana que alarma casi siempre; corrección: exigir avisos seguidos, ampliar la ventana y medir falsas alarmas.
- **Tratar cada falsa alarma como un fallo del equipo** en lugar de un parámetro de la regla.
- **Evaluar sin corregir por múltiples miradas.**
- **Confundirla con un falso positivo estadístico**: es el mismo concepto aplicado a una regla operativa.

## Límites y cuándo no aplica

Eliminar las falsas alarmas del todo exige dejar pasar defectos reales. El nivel aceptable depende del costo de actuar sin necesidad frente al de no actuar a tiempo. Las cifras de [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) son de una simulación con supuestos del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Activación](../a/activacion.md), [Bloqueo](../b/bloqueo.md), [Contextos](../c/contextos.md), [Disparador](../d/disparador.md), [Complejidad ciclomática](../c/complejidad-ciclomatica.md), [Duplicación accidental](../d/duplicacion-accidental.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-512 — Caos continuo: automatización en CI/CD y en producción](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.
- [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (52 clases más lo mencionan; las que más):

[SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), [SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «CanaryRelease»](https://martinfowler.com/bliki/CanaryRelease.html) — despliegue progresivo; autoridad: autor del texto.
- [Fowler, «BlueGreenDeployment»](https://martinfowler.com/bliki/BlueGreenDeployment.html) — dos entornos y cambio de tráfico; autoridad: autor del texto.
- [Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/) — diseño de un canario; autoridad: Google, libro de ingeniería de confiabilidad.
- [Fowler, «ParallelChange»](https://martinfowler.com/bliki/ParallelChange.html) — expandir, migrar y contraer; autoridad: autor del texto.
- [Google SRE: Release Engineering](https://sre.google/sre-book/release-engineering/) — entrega y retroceso; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Fallo, enlaces y supervisión](./fallo-enlaces-y-supervision.md) · [Falsa denegación →](./falsa-denegacion.md)
