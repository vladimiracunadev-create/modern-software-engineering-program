# Escenario de calidad

[↑ Glosario](../../README.md) · [← Escenario adverso](./escenario-adverso.md) · [Escenario de integración →](./escenario-de-integracion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Un **escenario de calidad** es la formulación estructurada de un atributo de calidad con seis partes: **fuente** del estímulo, **estímulo**, **artefacto**, **entorno**, **respuesta** y **medida de la respuesta** ([SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md)). [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md) lo resume como situación y respuesta medible. Convierte un adjetivo («rápido», «seguro») en una frase que puede probarse.

## Por qué importa

Un requisito como «el sistema debe ser seguro» no se puede probar ([SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md)). Sin escenario, dos personas creen cumplir lo mismo con sistemas distintos, y las decisiones de arquitectura se toman sin saber qué atributo importa y cuánto. Con escenarios, el equipo ordena qué atributos dominan el diseño y qué pruebas lo verifican ([SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md)).

## Cómo funciona

Cada parte elimina una ambigüedad ([SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md)):

- **fuente:** una persona, otro sistema, un fallo;
- **estímulo:** qué ocurre;
- **artefacto:** qué parte del sistema se ve afectada;
- **entorno:** en qué condiciones (carga, datos, modo de operación);
- **respuesta:** qué hace el sistema;
- **medida:** el estadístico, el umbral y la unidad que permiten decidir.

Sin entorno, «p95 ≤ 300 ms» se cumple con un usuario y se rompe con doscientos; sin estadístico, «300 ms» puede ser media o máximo; sin unidad, puede ser milisegundos o segundos. La medida es lo que hace al escenario falsable: si no se puede medir, aún no es un escenario.

## Ejemplo

[SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md): «Cuando una estudiante (fuente) abre su borrador (estímulo) en la aplicación web (artefacto) con 200 usuarios activos (entorno), el sistema lo muestra (respuesta) en menos de 1,5 s en el percentil 95 de las aperturas diarias (medida)». Se puede convertir directamente en una prueba de carga con ese entorno y ese umbral.

## Errores y confusiones comunes

- **El tablero está verde y la gente se queja.** Causa: el objetivo usa la media y la cola concentra el daño; corrección: fijar percentil y fracción de peticiones, y vigilar la cola ([SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)).
- **Se cumple el 99,9 % anual con un mes catastrófico.** Causa: la ventana anual diluye una caída larga; corrección: declarar la ventana (mensual) o añadir un tope de caída continua ([SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)).
- **Escribir seis partes de relleno.** Una medida vaga («rápido») invalida el escenario.

## Límites y cuándo no aplica

El formato de seis partes es una convención del programa, tomada del trabajo sobre arquitectura; no es la única forma de expresar atributos. Los números de [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) son de la plataforma de entregas (datos sintéticos): no se midió ningún sistema real. Un escenario sin entorno realista puede dar falsa seguridad, y demasiados escenarios sin prioridad paralizan el diseño.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida de la respuesta](../m/medida-de-la-respuesta.md), [Artefacto](../a/artefacto.md), [Atributo](../a/atributo.md), [Entorno](./entorno.md), [Atributos de calidad](../a/atributos-de-calidad.md), [Calidad del producto](../c/calidad-del-producto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-007 — Calidad interna, externa y calidad en uso](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Escenarios de calidad», «escenarios de calidad».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Bass, Clements y Kazman, «Software Architecture in Practice»](https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/) — escenarios de calidad y árbol de utilidad; autoridad: Software Engineering Institute.
- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — escenarios de calidad y árbol de utilidad; autoridad: Software Engineering Institute (Carnegie Mellon).
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — modelo de calidad del producto; autoridad: ISO e IEC.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos, percentiles y ventanas; autoridad: Google.
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — relación entre disponibilidad, riesgo y costo; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Escenario adverso](./escenario-adverso.md) · [Escenario de integración →](./escenario-de-integracion.md)
