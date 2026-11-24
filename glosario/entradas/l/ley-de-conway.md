# Ley de Conway

[↑ Glosario](../../README.md) · [← Ley de Amdahl](./ley-de-amdahl.md) · [Ley de Fitts →](./ley-de-fitts.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

La **ley de Conway** es la observación de que la estructura de un sistema copia la estructura de comunicación de la organización que lo diseña ([SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md)). Melvin Conway la formuló en 1968. No es una ley en sentido estricto sino una regularidad observada: las organizaciones que diseñan sistemas producen diseños que son copias de su estructura de comunicación. El ejemplo clásico que cita la clase: si cuatro equipos trabajan en un compilador, saldrá un compilador de cuatro pasadas.

## Por qué importa

Cuando la arquitectura parece «mal diseñada», muchas veces refleja cómo se organizan y hablan los equipos, no una decisión técnica equivocada. La decisión que cambia es dónde se actúa: a veces la arquitectura solo se corrige reorganizando equipos o moviendo fronteras a donde los equipos ya se coordinan. Y sirve para anticipar: se puede predecir qué fronteras se erosionarán.

## Cómo funciona

[SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) explica la causa con un argumento práctico. Las fronteras técnicas que son fáciles de mantener coinciden con las fronteras entre grupos que se hablan poco: cada lado trabaja con su parte sin necesitar al otro. Las fronteras que **cruzan equipos** exigen coordinación continua, y con el tiempo el trabajo la evita: se saltan la API, se comparte una tabla, se añade una dependencia directa. Así la frontera se erosiona hasta coincidir con la que la organización sostiene.

La clase la usa para dos cosas: explicar por qué la arquitectura actual se parece al organigrama y anticipar qué fronteras se erosionarán. Y relaciona los síntomas con su causa: cada cambio de negocio que involucra varios equipos suele ser señal de equipos organizados por capa técnica; la corrección es reorganizar por flujo de valor o por comunidad de dependencias. Una frontera que se erosiona entre dos equipos indica que la frontera técnica cruza un límite que exige coordinación constante: hay que moverla o ponerla donde los equipos coinciden.

La consecuencia de diseño es la llamada maniobra inversa de Conway: moldear la organización para obtener la arquitectura deseada.

## Ejemplo

Una plataforma tiene un equipo de interfaz, otro de lógica y otro de datos. Cada nuevo requisito de negocio toca los tres, y las fronteras entre capas se saltan cuando hay prisa. Al reorganizarse en equipos por flujo de valor (entregas, calificaciones, avisos), cada equipo posee su porción completa y las fronteras técnicas coinciden con las de comunicación. Ilustración del razonamiento de [SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md).

## Errores y confusiones comunes

- **Cada cambio de negocio involucra varios equipos**: equipos organizados por capa técnica; se corrige reorganizando por flujo de valor.
- **La arquitectura se «erosiona» entre dos equipos**: la frontera técnica cruza un límite que exige coordinación constante.
- **Tratarla como una ley física**: es una tendencia, no una necesidad.
- **Querer arreglar la arquitectura sin mirar la organización**.

## Límites y cuándo no aplica

[SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) advierte que sus simulaciones usan modelos del autor (un grafo con cuatro comunidades, probabilidades de arista y colas M/M/1) y que no se observó ningún equipo ni repositorio real. La ley describe una tendencia fuerte, no una regla exacta: equipos con buena comunicación pueden mantener fronteras que cruzan sus límites, a costa de esfuerzo. Y en organizaciones muy pequeñas, donde todos hablan con todos, la estructura de comunicación casi no impone fronteras.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estructura](../e/estructura.md), [Observación](../o/observacion.md), [Organización](../o/organizacion.md), [Carga cognitiva de un equipo](../c/carga-cognitiva-de-un-equipo.md), [Factor de autobús](../f/factor-de-autobus.md), [Maniobra inversa de Conway](../m/maniobra-inversa-de-conway.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-334 — Arquitectura socio-técnica y límites de equipo](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Conway, «How Do Committees Invent?» (1968)](https://www.melconway.com/Home/Committees_Paper.html) — enunciado original de la ley; autoridad: Melvin Conway.
- [Fowler, «Conway's Law»](https://martinfowler.com/bliki/ConwaysLaw.html) — la ley y la maniobra inversa; autoridad: Martin Fowler.
- [Skelton y Pais, «Team Topologies»: conceptos clave](https://teamtopologies.com/key-concepts) — tipos de equipo, modos de interacción y carga cognitiva; autoridad: Team Topologies.
- [DORA, programa de investigación](https://dora.dev/research/) — capacidades técnicas y organizativas y rendimiento de la entrega; autoridad: DORA (Google Cloud).
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Ley de Amdahl](./ley-de-amdahl.md) · [Ley de Fitts →](./ley-de-fitts.md)
