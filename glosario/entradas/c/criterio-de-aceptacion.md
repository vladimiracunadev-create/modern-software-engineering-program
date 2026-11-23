# Criterio de aceptación

[↑ Glosario](../../README.md) · [← Criterio de aborto](./criterio-de-aborto.md) · [Criterio de éxito →](./criterio-de-exito.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Un **criterio de aceptación** es una condición concreta, con un resultado observable, que debe cumplirse para que una historia o un entregable se acepte. El sentido central es el de [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) y [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md): condiciones binarias (se cumplen o no) que, si se cumplen, hacen que la historia se considere completa para quien la pidió. Las demás clases lo reutilizan con el mismo núcleo: [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md) lo aplica a un release («afirmación sobre el canal con una prueba ejecutable y un resultado esperado»), [SE-554](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md) a la salida de un modelo («condición verificable que la salida debe cumplir para aceptarse») y [SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) a un experimento de caos (el número de ensayos y la tolerancia de fallas, escritos antes de ejecutarlo).

## Por qué importa

Convierte la intención en condiciones que otra persona puede evaluar. Según [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), convierte «hecho» en una condición binaria; según [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), la intención en condiciones verificables que la usuaria o quien lleva el producto reconoce; según [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), «funciona» en pruebas con resultado. Sin ellos, la discusión sobre si algo está terminado ocurre al final, cuando es más cara.

## Cómo funciona

Según [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), un buen criterio es **binario**, **independiente de la implementación** y **comprobable por alguien que no escribió el código**. «La subida es rápida» no cumple; «un PDF de 10 MB se acepta y uno de 10,1 MB se rechaza con el mensaje que indica el límite» sí. [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) pide escribirlos como ejemplos o escenarios en el lenguaje del dominio («cuando la entrega llega a las 24 horas exactas, entonces se cuenta un día de retraso»), con una condición y un resultado observable.

Dos distinciones evitan confusiones. El criterio **no es la prueba**: es la promesa a la que la prueba se refiere ([SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)). Y la aceptación **no es lo mismo que el terminado**: lo segundo es calidad técnica; lo primero, el reconocimiento de que resuelve el problema ([SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md)).

## Ejemplo

En la plataforma de entregas de [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), el límite de subida se expresa con fronteras: un PDF de 10 MB se acepta y uno de 10,1 MB se rechaza con un mensaje que indica el límite. La clase añade además un registro de mutantes y una suite de pares para comprobar que los criterios detectan cambios, y propone cambiar una sola decisión (por ejemplo, el límite a 25 MB) y revisar qué escenarios deben reescribirse.

## Errores y confusiones comunes

- **Criterios vagos que se discuten al final.** «La pantalla debe ser intuitiva» invita a discutir; corrección ([SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md)): reescribir como ejemplos con condición y resultado observable.
- **Confundir criterio con prueba.** El criterio es la promesa; la prueba la comprueba ([SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)).
- **Confundir aceptación con terminado.** Una historia puede estar técnicamente terminada y no ser aceptada, y viceversa ([SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md)).

## Límites y cuándo no aplica

Un criterio escrito como ejemplo cubre los casos que se pensaron; [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) usa suites de pares y mutantes porque los ejemplos pueden ser insuficientes. Los criterios deben revisarse cuando cambia la decisión que los motivó: [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) propone justamente cambiar una decisión y comprobar qué escenarios deben reescribirse.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Condición](./condicion.md), [Ensayo](../e/ensayo.md), [Resultado](../r/resultado.md), [Cobertura combinatoria](./cobertura-combinatoria.md), [Correlación entre comprobaciones](./correlacion-entre-comprobaciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-108 — Proyecto: entorno de desarrollo autocontenido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.
- [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (152 clases más lo mencionan; las que más):

[SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md), [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), [SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Criterios de aceptación», «criterios de aceptación».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [North, «Introducing BDD»](https://dannorth.net/introducing-bdd/) — criterios de aceptación como escenarios; autoridad: autor de la práctica.
- [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — definición de terminado e incremento; autoridad: Scrum.org y Scrum Inc. (autores de la guía).
- [Jones, «Software defect-removal efficiency» (IEEE Computer, 1996)](https://doi.org/10.1109/2.488361) — eficiencia de eliminación de defectos por técnica; autoridad: IEEE Computer.
- [Fagan, «Design and code inspections to reduce errors in program development» (IBM Systems Journal, 1976)](https://doi.org/10.1147/sj.153.0182) — inspecciones formales de diseño y código; autoridad: IBM Systems Journal.
- [Agile Alliance: definition of done](https://www.agilealliance.org/glossary/definition-of-done/) — glosario de la práctica; autoridad: Agile Alliance.

---

[↑ Glosario](../../README.md) · [← Criterio de aborto](./criterio-de-aborto.md) · [Criterio de éxito →](./criterio-de-exito.md)
