# Restricciones

[↑ Glosario](../../README.md) · [← Restricción única](./restriccion-unica.md) · [Restricciones y explicación →](./restricciones-y-explicacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Decisión ya tomada o condición externa que descarta alternativas sin discutirlas, con una fuente y un coste de levantarla.

Definición de trabajo de [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md): Condiciones impuestas fuera del equipo que limitan el diseño y no se negocian como requisitos.

## Por qué importa

En [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), el tema «Restricciones» importa porque reducen el espacio de alternativas antes de comparar.

En [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), el tema «Restricciones» importa porque limitan el espacio de diseño y no se negocian como un requisito.

En [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), el tema «Restricción» importa porque elimina opciones inviables

## Cómo funciona

Según [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), en la sección «Restricciones»:

Una **restricción** es una decisión que ya no está en discusión: «se despliega en la infraestructura de la universidad», «los datos de estudiantes no salen del país», «el equipo domina Python». Reduce el espacio de alternativas, y por eso es lo primero que se aplica. Dos errores típicos: tratar una preferencia como restricción («tiene que ser serverless») y tratar una restricción real como preferencia («ya veremos lo de los datos»). La regla práctica es anotar quién impuso la restricción, desde cuándo y qué costaría levantarla; una restricción sin esa información es una opinión.

Según [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), en la sección «Restricciones»:

Una restricción es una condición impuesta que el equipo no puede cambiar: debe usarse el servidor de identidad de la universidad, los datos no salen de un país, el sistema corre en una versión de navegador. Se separan de los requisitos porque su tratamiento es otro: no se prioriza, se cumple, y su origen es una decisión externa que hay que registrar. Una restricción mal identificada es un requisito negociable que nadie negocia o, peor, un requisito que se negoció cuando no se podía.

## Ejemplo

Ejemplo de [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma abre `drivers.md` con cuatro drivers (el pico de entrega no debe perder archivos; el servicio se apoya en seis personas; las notas deben ser consistentes; el servicio debe estar disponible en periodo de entregas), tres restricciones (infraestructura de la universidad, datos en el país, Python como lenguaje) y cinco escenarios medibles.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una restricción desaparece a mitad del proyecto** — causa: era una preferencia sin dueño. Corrección: registrar fuente, fecha y coste de levantarla. ([SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md))
- **Se pondera sin descartar** — causa: se comparan alternativas que una restricción ya excluía. Corrección: aplicar primero restricciones y dominancia y ponderar solo lo que queda. ([SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md))
- **Una restricción se discute como un requisito más** — causa: no se identificó su origen externo. Corrección: registrar origen, fecha y quién puede cambiarla. ([SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **restricción** es una decisión que ya no está en discusión: ([SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md))
- Una **restricción** excluye opciones dentro del alcance: una obligación legal, un límite físico, una fecha externa o compatibilidad contractual. ([SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Atributos de calidad](../a/atributos-de-calidad.md), [Compromisos entre atributos](../c/compromisos-entre-atributos.md), [Contingencia](../c/contingencia.md), [Escenario de calidad](../e/escenario-de-calidad.md), [Exposición](../e/exposicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (116 clases más lo mencionan; las que más):

[SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md), [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Restricción», «restricción».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — modelo de calidad del producto de software; autoridad: ISO.
- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — escenarios de calidad y árbol de utilidad; autoridad: Software Engineering Institute (Carnegie Mellon).
- [Google SRE, «Embracing Risk»](https://sre.google/sre-book/embracing-risk/) — disponibilidad como objetivo con coste; autoridad: Google SRE.
- [Python: `heapq`](https://docs.python.org/3/library/heapq.html) — cola de prioridad usada en la simulación; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Restricción única](./restriccion-unica.md) · [Restricciones y explicación →](./restricciones-y-explicacion.md)
