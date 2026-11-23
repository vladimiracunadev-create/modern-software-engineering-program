# Escenario de calidad

[↑ Glosario](../../README.md) · [← Escenario adverso](./escenario-adverso.md) · [Escenario de integración →](./escenario-de-integracion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Formulación estructurada de un atributo con fuente, estímulo, artefacto, entorno, respuesta y medida.

Definición de trabajo de [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md): Descripción de un requisito de calidad con fuente, estímulo, artefacto, entorno, respuesta y medida.
- En [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md): Descripción de una fuente que produce un estímulo en un entorno sobre un artefacto y de la respuesta medible que se espera.
- En [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md): Situación con fuente, estímulo, artefacto, entorno, respuesta y medida de la respuesta.
- En [SE-007 — Calidad interna, externa y calidad en uso](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md): Situación y respuesta medible.

## Por qué importa

En [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), el tema «Escenarios de calidad» importa porque convierten un adjetivo en fuente, estímulo, entorno, respuesta y medida.

En [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), el tema «Escenarios de calidad» importa porque convierte «rápido» en una situación con medida que dos personas leen igual.

## Cómo funciona

Según [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), en la sección «Escenarios de calidad»:

Un escenario de calidad es una frase estructurada con seis partes: fuente del estímulo, estímulo, artefacto, entorno, respuesta y medida de la respuesta. «Cuando una estudiante (fuente) abre su borrador (estímulo) en la aplicación web (artefacto) con 200 usuarios activos (entorno), el sistema lo muestra (respuesta) en menos de 1,5 s en el percentil 95 de las aperturas diarias (medida)». Cada parte elimina una lectura: sin entorno no se sabe con qué carga; sin percentil no se sabe qué fracción de aperturas debe cumplir.

Según [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), en la sección «Escenarios de calidad»:

Un requisito como «el sistema debe ser seguro» no se puede probar. Un **escenario de calidad** lo vuelve comprobable con seis partes: la **fuente** del estímulo (una persona, otro sistema, un fallo), el **estímulo** (qué ocurre), el **artefacto** afectado (qué parte del sistema), el **entorno** (en qué condiciones: carga, datos, modo de operación), la **respuesta** esperada y la **medida de la respuesta**, que es lo que permite decidir. Cada parte elimina una ambigüedad: sin entorno, «p95 ≤ 300 ms» se cumple con un usuario y se rompe con doscientos; sin estadístico, «300 ms» puede significar media o máximo; sin unidad, el 300 puede ser milisegundos o segundos.

## Ejemplo

Ejemplo de [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) (sección «Ejemplo profesional»):

Tres escenarios de calidad del requisito conductor, escritos de forma verificable:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)) son:

- **El tablero está verde y la gente se queja** — causa: el objetivo usa la media y la cola concentra el daño. Corrección: fijar percentil y fracción de peticiones, y vigilar la cola.
- **Se cumple el 99,9 % anual con un mes catastrófico** — causa: la ventana anual diluye una caída larga. Corrección: declarar la ventana (mensual) o añadir un tope de caída continua.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): los dos primeros con salidas idénticas y el tercero con tiempos propios de cada equipo. No se midió ningún sistema real, la cola lenta y los incidentes son supuestos y el costo de PBKDF2 corresponde a una corrida. La siguiente clase cuenta los requisitos desde la perspectiva de quien los usa: casos de uso, historias y job stories.

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
