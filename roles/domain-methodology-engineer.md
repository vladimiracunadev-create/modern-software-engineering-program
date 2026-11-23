# 📐 Domain & Methodology Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Metodolog%C3%ADa%20y%20dominio-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-semi--senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P06%20%C2%B7%20P12%20%C2%B7%20P13%20%C2%B7%20P25%20%C2%B7%20P27%20%C2%B7%20P35%20%C2%B7%20P45%20%C2%B7%20P47-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Convierte metodologías de desarrollo —TDD, BDD, ATDD, DDD, diseño por contrato y
> especificación guiada por spec— en prácticas de equipo con evidencia, sin tratarlas
> como rituales ni como etiquetas intercambiables.
>
> **Entrada habitual:** semi-senior/senior · **Foco:** prácticas de especificación y prueba
> · **Evidencia central:** ejemplos, contratos y modelo de dominio que detectan reglas mal entendidas

## 🧭 Qué es y por qué importa

Las metodologías responden a preguntas distintas. **TDD** usa una prueba que falla para
guiar el diseño en ciclos cortos. **BDD** y **ATDD** anclan el comportamiento en
ejemplos que negocio y desarrollo comprenden por igual, a menudo escritos en Gherkin.
**DDD** da un lenguaje ubicuo y contextos delimitados para que el modelo del código no
se desvíe del dominio. El **diseño por contrato** hace explícitas pre y poscondiciones
e invariantes. La **especificación guiada por spec (SDD)** convierte la intención en un
artefacto vivo del que se derivan código y pruebas, cada vez más importante cuando
quien implementa puede ser un agente.

Este rol decide **cuál práctica aplicar, dónde y con qué evidencia**, y la sostiene
como práctica de equipo: acuerdos, ejemplos revisables, pruebas que fallan por la
razón correcta y un glosario que el código realmente usa. No es un coach de ceremonias:
si un ciclo no reduce defectos de reglas ni acorta el feedback, se cambia.

## 🗓️ Un día en el puesto

- facilitar una conversación de ejemplos con negocio y convertir los acuerdos en
  escenarios verificables;
- revisar una prueba y comprobar que falla por la razón esperada antes de aceptar el
  código que la hace pasar;
- detectar un término del dominio usado con dos significados y proponer un contexto
  delimitado o un cambio de nombre;
- vincular una especificación con sus contratos y sus pruebas, y señalar la deriva;
- medir el tiempo de feedback del equipo y descartar prácticas que sólo añaden ritual.

## ✅ Responsabilidades y límites

- Responde por la coherencia entre intención, ejemplos, contratos, código y modelo.
- Elige la práctica por el tipo de incertidumbre (diseño, regla de negocio, integración),
  no por preferencia de escuela.
- No mide el éxito por cobertura de líneas ni por cantidad de escenarios.
- No impone una metodología a todo el sistema: un CRUD simple no necesita un modelo de
  dominio rico, y un algoritmo numérico se beneficia más de propiedades que de Gherkin.
- No sustituye al [QA / Test Automation Engineer](qa-test-engineer.md) ni al
  [Software Architect](software-architect.md): coordina prácticas y deja a cada rol su
  decisión de estrategia de prueba y de arquitectura.

## 🧠 Qué necesitas saber

Ciclo rojo-verde-refactor y sus límites; dobles de prueba y su coste de acoplamiento;
escritura de ejemplos y Gherkin sin convertirlo en scripts de interfaz; criterios de
aceptación y reglas; lenguaje ubicuo, contextos delimitados, agregados e invariantes;
pre y poscondiciones, pruebas de contrato y de propiedades; versionado de contratos;
especificaciones como fuente en proyectos con agentes; y cómo medir feedback y defectos
de regla sin gamificar la métrica.

## 📚 Tu ruta en el programa

1. [Parte 05 — Fundamentos de programación](../classes/part-05-fundamentos-de-programacion/README.md)
   para pruebas tempranas y diseño por ejemplos.
2. [Parte 12 — Ingeniería de requisitos](../classes/part-12-ingenieria-de-requisitos/README.md)
   y [Parte 13 — Especificaciones, contratos y modelos](../classes/part-13-especificaciones-contratos-y-modelos/README.md)
   para criterios de aceptación, BDD, contratos y spec-first.
3. Partes [25](../classes/part-25-diseno-patrones-y-refactorizacion/README.md), [27](../classes/part-27-arquitectura-de-software-y-dominio/README.md) y [35](../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md) para refactorización, dominio y pruebas.
4. La [Parte 45](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) (metodologías de TDD a ODD) y la 43 (patrones) ya están desarrolladas, a
   falta de revisión editorial humana independiente.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

```mermaid
flowchart LR
    A["🎯 Intención"] --> B
    B["🧠 Ejemplo"] --> C
    C["🛠️ Contrato"] --> D
    D["🔎 Modelo de dominio"] --> E["📈 Evidencia"]
    classDef intent fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef work fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef proof fill:#dafbe1,stroke:#1a7f37,color:#24292f
    class A intent
    class B,C,D work
    class E proof
```

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **📐 Domain & Methodology Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Convierte metodologías de desarrollo —TDD, BDD, ATDD, DDD, diseño por contrato y especificación guiada por spec— en prácticas de equipo con evidencia, sin tratarlas como rituales ni como etiquetas intercambiables. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Metodología y dominio**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [🧪 QA / Test Automation Engineer](qa-test-engineer.md); [🏛️ Software Architect](software-architect.md); [🧾 Requirements Engineer / Business Systems Analyst](requirements-engineer.md);
- producto y personas usuarias cuando cambia una tarea o outcome;
- seguridad, privacidad, accesibilidad y operación según el riesgo;
- quienes mantendrán el sistema después de la entrega.

</td>
</tr>
</table>

El título no concede autoridad automática. El alcance real depende del equipo, la
industria y la criticidad. Esta guía describe un recorrido desde **semi-senior → principal**, pero una
vacante se evalúa por las decisiones que permite tomar, los sistemas que pone bajo
responsabilidad y la evidencia exigida, no por el nombre del cargo.

## 🧱 Partes y clases asociadas

La ruta distingue **parte** —unidad curricular con una capacidad acumulativa— de
**clase asociada** —punto concreto donde se estudia un mecanismo o una decisión. Las
clases siguientes forman el núcleo; no eliminan los prerrequisitos indicados en sus
propias páginas ni convierten en opcional la base común.

| Orden | Parte del programa | Estado | Clases clave | Por qué entra en esta ruta | Evidencia de transferencia |
| ---: | --- | --- | --- | --- | --- |
| 1 | [Parte 06 · Paradigmas de programación](../classes/part-06-paradigmas-de-programacion/README.md) | desarrollada | [SE-077 · Programación declarativa y basada en reglas](../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md)<br>[SE-078 · Programación lógica y resolución](../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md)<br>[SE-082 · Selección y combinación responsable de paradigmas](../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md)<br>[SE-083 · Taller: una regla de negocio en cinco paradigmas](../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md) | Profundiza **paradigmas y semánticas alternativas** desde la responsabilidad del rol. | Comparación razonada de implementaciones. |
| 2 | [Parte 12 · Ingeniería de requisitos](../classes/part-12-ingenieria-de-requisitos/README.md) | desarrollada | [SE-146 · Requisitos funcionales y reglas de negocio](../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)<br>[SE-148 · Casos de uso, historias y job stories](../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md)<br>[SE-149 · Criterios de aceptación y ejemplos](../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)<br>[SE-151 · Trazabilidad desde necesidad hasta evidencia](../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)<br>[SE-154 · Ambigüedad, contradicción e incompletitud](../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)<br>[SE-155 · Taller: reparar requisitos no verificables](../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) | Profundiza **requisitos, restricciones y trazabilidad** desde la responsabilidad del rol. | Baseline de requisitos revisable. |
| 3 | [Parte 13 · Especificaciones, contratos y modelos](../classes/part-13-especificaciones-contratos-y-modelos/README.md) | desarrollada | [SE-157 · Especificación informal, semiformal y formal](../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md)<br>[SE-158 · Specification by Example y BDD](../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md)<br>[SE-159 · Contratos, invariantes y diseño por contrato](../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md)<br>[SE-165 · Spec-first, spec-anchored y spec-as-source](../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md)<br>[SE-166 · Especificaciones ejecutables y pruebas contractuales](../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md)<br>[SE-167 · Taller: convertir intención en contrato comprobable](../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) | Profundiza **contratos, modelos e invariantes verificables** desde la responsabilidad del rol. | Especificación trazable. |
| 4 | [Parte 25 · Diseño, patrones y refactorización](../classes/part-25-diseno-patrones-y-refactorizacion/README.md) | desarrollada | [SE-301 · Cohesión, acoplamiento y encapsulación](../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)<br>[SE-307 · Refactorización segura apoyada por pruebas](../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md)<br>[SE-308 · Diseño para cambio, prueba y operación](../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md)<br>[SE-309 · Complejidad accidental y esencial](../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) | Profundiza **diseño, patrones y refactorización segura** desde la responsabilidad del rol. | Evolución compatible protegida por pruebas. |
| 5 | [Parte 27 · Arquitectura de software y dominio](../classes/part-27-arquitectura-de-software-y-dominio/README.md) | desarrollada | [SE-325 · Drivers, restricciones y atributos de arquitectura](../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md)<br>[SE-328 · Capas, hexagonal, clean y ports and adapters](../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md)<br>[SE-329 · Domain-Driven Design estratégico y táctico](../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md)<br>[SE-332 · Fitness functions y arquitectura evolutiva](../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md) | Profundiza **arquitectura, dominio y atributos de calidad** desde la responsabilidad del rol. | Arquitectura defendible con ADR. |
| 6 | [Parte 35 · Estrategia y técnicas de prueba](../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md) | desarrollada | [SE-421 · Calidad por riesgo y propósito de las pruebas](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md)<br>[SE-422 · Pruebas unitarias y diseño testable](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md)<br>[SE-423 · Integración, componentes y contratos](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)<br>[SE-425 · Pruebas basadas en propiedades y modelos](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md)<br>[SE-426 · Mutación, fuzzing y generación de casos](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)<br>[SE-431 · Taller: demostrar que una prueba detecta defectos](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) | Profundiza **estrategia de pruebas guiada por riesgo** desde la responsabilidad del rol. | Suite que demuestra detección de defectos. |
| 7 | [Parte 45 · Metodologías de desarrollo: de TDD a ODD](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) | desarrollada | [SE-541 · Mapa de metodologías: qué decide cada una y cómo elegir](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md)<br>[SE-542 · TDD: ciclo rojo-verde-refactor y diseño emergente](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md)<br>[SE-544 · BDD: ejemplos, conversación y lenguaje compartido](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md)<br>[SE-546 · DDD como lenguaje ubicuo y contexto para agentes](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md)<br>[SE-548 · SDD: spec-first, spec-anchored y spec-as-source](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md)<br>[SE-552 · Proyecto: política metodológica de equipo con evidencia](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md) | Profundiza **metodologías de desarrollo con evidencia de equipo** desde la responsabilidad del rol. | Política metodológica con evidencia. |
| 8 | [Parte 47 · SPEC, agentes y ciclo de vida agentic](../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md) | desarrollada | [SE-565 · De la intención a la especificación durable](../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)<br>[SE-566 · Constitución, specify, clarify, plan y tasks](../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md)<br>[SE-567 · Implementación, análisis y convergencia contra SPEC](../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md)<br>[SE-568 · Greenfield, brownfield, bug fixing e idea assessment](../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md) | Profundiza **SPEC, agentes, herramientas y guardrails** desde la responsabilidad del rol. | Flujo agentic controlado. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-052 · Invariantes, precondiciones y poscondiciones](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) | [Parte 04](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md) |
| [SE-057 · Modelado de estado, transiciones y eventos](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md) | [Parte 04](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md) |
| [SE-060 · Proyecto: especificación y solución contrastable](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md) | [Parte 04](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md) |
| [SE-069 · Pruebas tempranas y diseño por ejemplos](../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) | [Parte 05](../classes/part-05-fundamentos-de-programacion/README.md) |
| [SE-153 · Gestión de cambios y líneas base](../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) | [Parte 12](../classes/part-12-ingenieria-de-requisitos/README.md) |
| [SE-208 · ADRs, RFCs y registro de decisiones](../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) | [Parte 17](../classes/part-17-documentacion-y-conocimiento-tecnico/README.md) |
| [SE-543 · TDD en la práctica: escuelas de Londres y clásica, y sus límites](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md) | [Parte 45](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) |
| [SE-545 · ATDD y Specification by Example: aceptación ejecutable](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md) | [Parte 45](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) |
| [SE-547 · Diseño por contrato y pruebas de contrato como oráculo](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) | [Parte 45](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) |
| [SE-549 · EDD: evaluaciones como especificación y puerta de release](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) | [Parte 45](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) |
| [SE-550 · ODD: desarrollo orgánico y su contraste con SDD](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md) | [Parte 45](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) |
| [SE-551 · Taller: un mismo cambio con cinco metodologías](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md) | [Parte 45](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) |

**Cómo recorrerla.** Empieza por [SE-077](../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md) para fijar el
primer mecanismo, usa [SE-325](../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) para integrar el
centro de la especialidad y llega a [SE-568](../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md) cuando ya
puedas explicar cómo detectar y recuperar un fallo. Una clase se considera estudiada
sólo cuando su concepto cambia una decisión y deja evidencia; abrir todos los enlaces
no constituye competencia.

> [!IMPORTANT]
> El mapa expresa el currículo vigente. Las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`) están
> desarrolladas, a falta de una revisión editorial humana independiente. Esta ruta no
> declara aprobadas esas clases ni reemplaza el [roadmap](../ROADMAP.md).

## ✅ Ampliación completada: todas las partes del alcance

> [!NOTE]
> Todas las partes del alcance ya están desarrolladas ([ADR-007](../docs/adr/ADR-007-pedagogical-renumbering-and-new-parts.md)); sus clases figuran en el núcleo y en las clases de apoyo de esta guía.


## ⚖️ Decisiones y trade-offs que debes defender

| Decisión recurrente | Criterio profesional | Evidencia mínima antes de defenderla |
| --- | --- | --- |
| **Prueba primero o prueba después** | Usar prueba primero cuando el diseño es incierto y el feedback rápido y después cuando un contrato ya fija el comportamiento. | Historial de ciclos rojo verde refactor con una prueba que falla por la razón correcta. |
| **Ejemplos ejecutables o especificación narrativa** | Elegir un lenguaje ejecutable cuando el ejemplo debe sobrevivir al cambio y ser leído por negocio. | Escenarios vinculados a automatización y a la regla que ilustran. |
| **Modelo de dominio rico o transaccional simple** | Invertir en límites y lenguaje ubicuo sólo donde la complejidad esencial lo justifica. | Mapa de contextos y pruebas de invariantes. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Prueba primero o prueba después**, **Ejemplos ejecutables o especificación narrativa**
y **Modelo de dominio rico o transaccional simple** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Escenarios verdes que no capturan la regla de negocio real

**Síntoma.** Las pruebas ejercen un camino feliz mientras negocio y desarrollo usan el mismo término con significados distintos. La respuesta madura evita convertir la primera
correlación en causa y conserva evidencia antes de modificar el sistema.

```mermaid
flowchart LR
    S["⚠️ Síntoma"] --> H["🔎 Hipótesis"]
    H --> C["🧯 Contención"]
    C --> D["🧠 Diagnóstico"]
    D --> R["🛠️ Recuperación"]
    R --> P["📚 Prevención"]
```

1. **Detectar y delimitar:** identifica quién o qué está afectado, desde cuándo y qué
   cambió. Conserva timestamps, versiones, entradas y señales suficientes para no
   destruir la escena al intentar arreglarla.
2. **Investigar:** Contrastar ejemplos con la regla escrita y las conversaciones e identificar el término ambiguo y el contexto delimitado. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Corregir el lenguaje ubicuo reescribir los ejemplos en la frontera correcta y añadir una prueba de contrato que falle ante la regresión semántica. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Defectos de regla de negocio escapados** | Reglas mal entendidas que llegan a producción. | Usar la cobertura de líneas como sustituto. |
| **Estabilidad del lenguaje ubicuo** | Términos del dominio coincidentes entre código pruebas y conversaciones. | Contar glosarios que nadie usa. |
| **Tiempo de feedback de la práctica** | Minutos entre un cambio y una señal fiable de pruebas o contratos. | Ganar velocidad con pruebas frágiles. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Práctica de equipo verificable

**Propósito:** introducir una práctica que conecte ejemplos de negocio pruebas contratos y modelo de dominio en un flujo real de entrega. El resultado esperado es **acuerdo de equipo mapa de contextos ejemplos ejecutables pruebas de contrato SPEC trazable y métricas de feedback**.

Entrega un expediente revisable con estas piezas:

1. **Contexto y alcance:** usuario, sistema, restricción, supuestos, fuera de alcance y
   criterio de no éxito.
2. **Decisión:** al menos dos alternativas reales, trade-offs, coste de reversión y un
   ADR o memo que indique cuándo revisar la elección.
3. **Artefacto principal:** una implementación, modelo, flujo o política coherente con
   las clases núcleo; no una captura aislada ni una presentación sin mecanismo.
4. **Fallo controlado:** introduce una condición adversa relacionada con el escenario
   anterior y conserva el resultado observado, sin inventar una ejecución.
5. **Verificación:** prueba, rúbrica, revisión o medición que pueda fallar y que conecte
   directamente con el resultado profesional.
6. **Operación y salida:** telemetría, recuperación, mantenimiento, deprecación o retiro
   según corresponda; incluye límites y deuda residual.

**Criterio de aceptación:** otra persona puede reconstruir el razonamiento, reproducir
la comprobación y distinguir claramente qué quedó demostrado de lo que sólo se propone.
El proyecto no se aprueba por cantidad de archivos ni por utilizar una marca concreta.

## 📈 Dominio esperado por alcance

| Alcance | Qué resuelve | Qué evidencia su autonomía |
| --- | --- | --- |
| **Inicial** | ejecuta una tarea acotada con criterios y acompañamiento | reproduce el caso, pregunta por supuestos y entrega evidencia legible |
| **Intermedio** | decide dentro de un componente o flujo conocido | compara alternativas, prueba fallos previsibles y coordina dependencias |
| **Senior** | conduce problemas ambiguos que cruzan sistemas o equipos | hace explícito el riesgo, diseña recuperación y mejora el mecanismo de trabajo |
| **Staff / Lead** | cambia capacidades compartidas y decisiones de largo plazo | multiplica criterio, define guardrails, mide adopción y conserva opciones futuras |

Progresar no significa alejarse de la práctica. Significa aumentar ambigüedad, horizonte,
blast radius y responsabilidad por consecuencias. La persona senior todavía debe poder
explicar el mecanismo; la persona Staff además crea condiciones para que otros lo
operen sin depender de ella.

## 🗓️ Plan de práctica 30 · 60 · 90 días

- **Días 1–30 — comprender y reproducir.** Estudia las primeras clases de cada parte,
  reproduce un caso pequeño y escribe un mapa de responsabilidades. El entregable es
  una baseline con preguntas abiertas, no una transformación prematura.
- **Días 31–60 — intervenir y fallar con control.** Construye el artefacto central,
  introduce el escenario de fallo y mide el comportamiento. Revisa el trabajo con una
  persona de una ruta vecina para descubrir supuestos de frontera.
- **Días 61–90 — operar y transferir.** Ejecuta recuperación, corrige la causa, publica
  runbook o guía de uso y presenta la decisión con trade-offs. Termina con una
  retrospectiva que separe resultado, evidencia, límites y siguiente inversión.

Este plan es una secuencia de práctica, no una promesa de empleabilidad en noventa días.
La experiencia previa, el dominio y el acceso a sistemas reales cambian el tiempo
necesario.

## 🎤 Preguntas para revisión o entrevista

1. ¿En qué contexto elegirías **Prueba primero o prueba después** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Escenarios verdes que no capturan la regla de negocio real**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Práctica de equipo verificable** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — **IEEE Computer Society**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) — **Martin Fowler**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Introducing BDD](https://dannorth.net/introducing-bdd/) — **Dan North**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Gherkin reference](https://cucumber.io/docs/gherkin/reference/) — **Cucumber**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Specification by Example](https://gojko.net/books/specification-by-example/) — **Gojko Adzic**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Domain-Driven Design Reference](https://www.domainlanguage.com/ddd/reference/) — **Eric Evans / Domain Language**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Pact documentation: consumer-driven contract testing](https://docs.pact.io/) — **Pact Foundation**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- historial de ciclos TDD con pruebas que fallan por la razón correcta;
- conjunto de escenarios BDD ligado a reglas escritas y a pruebas automatizadas;
- mapa de contextos con glosario y términos ambiguos resueltos;
- contrato versionado con prueba de compatibilidad entre consumidor y proveedor;
- comparación del mismo cambio con dos prácticas y su efecto en feedback y defectos.

## 📈 Progresión

Software Engineer → Domain & Methodology Engineer → Staff / Technical Lead de prácticas
de ingeniería o Software Architect con foco en dominio.

## ⚠️ Mitos frecuentes

- “TDD garantiza buen diseño.” Guía el diseño sólo si el refactor ocurre y las
  pruebas describen comportamiento, no implementación.
- “BDD es automatizar con Gherkin.” Su valor está en la conversación y el ejemplo
  compartido; la automatización es una consecuencia.
- “DDD es usar agregados y repositorios.” Empieza por el lenguaje y los límites.
- “La especificación reemplaza a las pruebas.” Una spec sin comprobación ejecutable
  deriva.

## 🚀 Siguientes pasos

1. Elige una regla de negocio ambigua y redáctala con ejemplos que dos personas
   interpreten igual.
2. Escribe la prueba, confirma que falla por la razón esperada y refactoriza.
3. Registra qué término cambió de significado entre contextos y qué prueba lo protege.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
