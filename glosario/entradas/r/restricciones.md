# Restricciones

[↑ Glosario](../../README.md) · [← Restricción única](./restriccion-unica.md) · [Restricciones y explicación →](./restricciones-y-explicacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Una **restricción** es una decisión ya tomada o una condición externa que descarta alternativas sin discutirlas, con una fuente y un coste de levantarla ([SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md)). [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) la precisa: una condición impuesta fuera del equipo que limita el diseño y no se negocia como requisito. [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md) la sitúa dentro del alcance: una obligación legal, un límite físico, una fecha externa o una compatibilidad contractual.

## Por qué importa

Es lo primero que se aplica al decidir: reduce el espacio de alternativas antes de ponderar. Mal identificada, produce los dos errores opuestos: tratar una preferencia como restricción («tiene que ser serverless») o una restricción real como preferencia («ya veremos lo de los datos»). El resultado es arquitectura rehecha a mitad de proyecto o incumplimientos tardíos.

## Cómo funciona

[SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) da ejemplos: «se despliega en la infraestructura de la universidad», «los datos de estudiantes no salen del país», «el equipo domina Python». Se distinguen de los requisitos porque su tratamiento es distinto ([SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)): un requisito se prioriza y se negocia; una restricción se cumple, y su origen es una decisión externa que hay que registrar. La regla práctica de [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md): anotar **quién** impuso la restricción, **desde cuándo** y **qué costaría levantarla**. Sin esa información es una opinión.

En el proceso de decisión, se aplican primero las restricciones y la dominancia (una alternativa peor en todo que otra), y se pondera solo lo que queda; ponderar sin descartar compara alternativas que una restricción ya excluía.

## Ejemplo

```text
R-03  Los datos de estudiantes no salen del país.
fuente: política de la universidad | desde: 2024-03 | costo de levantarla: aprobación del comité jurídico
efecto: descarta el proveedor X (única región fuera del país)
```

## Errores y confusiones comunes

- **Una restricción desaparece a mitad del proyecto.** Causa: era una preferencia sin dueño; corrección: registrar fuente, fecha y coste de levantarla ([SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md)).
- **Se pondera sin descartar.** Causa: se comparan alternativas que una restricción ya excluía; corrección: aplicar primero restricciones y dominancia ([SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md)).
- **Se discute como un requisito más.** Causa: no se identificó su origen externo; corrección: registrar origen, fecha y quién puede cambiarla ([SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)).

## Límites y cuándo no aplica

Una restricción no es eterna: su coste de levantarla puede ser aceptable si el beneficio es grande, y por eso hay que registrarlo. No toda limitación técnica es una restricción: la que se puede resolver con trabajo del equipo es un requisito de diseño. Y demasiadas restricciones sin revisar pueden dejar espacio de diseño vacío: entonces hay que renegociar alguna con su dueño.

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
