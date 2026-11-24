# Revisión independiente

[↑ Glosario](../../README.md) · [← Revisión de la política](./revision-de-la-politica.md) · [Revisión por muestreo →](./revision-por-muestreo.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

La **revisión independiente** es una evaluación hecha sin autoría directa ni incentivo dominante ([SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md)). [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) la concreta como el examen de un paquete por una persona que no lo produjo, y [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) como la revisión por alguien que no desarrolló el sistema. «Independiente» no significa desconocedora ni neutral: significa menos comprometida con la autoría.

## Por qué importa

Quien construye algo ve lo que quiso hacer, no necesariamente lo que hizo. Una persona externa halla fallos que el autor no ve y cuestiona supuestos que el autor da por obvios. A mayor impacto e irreversibilidad, más importante es separar incentivos ([SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md)). Cambia quién puede aprobar un cambio, una evidencia de seguridad o un caso crítico.

## Cómo funciona

[SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md) establece las condiciones:

- La persona revisora necesita **contexto** (para entender) y **autoridad** (para cuestionar y detener).
- No significa desconocimiento ni neutralidad absoluta: aporta una perspectiva menos comprometida con la autoría.
- En equipos pequeños, si la misma persona propone y revisa, se **limita el alcance**, se buscan criterios automatizados o revisión externa y se **registra la limitación**.

En sistemas críticos ([SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md)), la revisión independiente de un caso de seguridad es parte de la práctica: la persona externa aporta escenarios de uso que el equipo desconoce (véase *evidencia*, donde un comité plantea qué ocurre con una carga térmica no considerada). En cumplimiento ([SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md)), el paquete de evidencia lo examina alguien que no lo produjo, para que «cumple» no sea la palabra del mismo equipo que lo declara.

La cantidad de personas no es lo importante: se necesitan las necesarias para cubrir competencia, autoridad y revisión independiente, no un número fijo; más personas sin interfaz clara añaden espera.

## Ejemplo

Un equipo de tres personas despliega un cambio de permisos. La autora propone; una compañera de otro equipo, con acceso al contexto y autoridad para bloquear, revisa el diff y las pruebas. Registro:

```text
Cambio: ampliar rol "docente" | Autor: A | Revisión: B (otro equipo) | Decisión: aprobado con 1 observación resuelta
```

## Errores y confusiones comunes

- **Todos son «responsables».** Se evitó declarar autoridad; corrección: nombrar quién acepta, detiene y escala cada decisión ([SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md)).
- **Revisión sin autoridad.** La persona revisora puede opinar pero no detener, y la revisión es decorativa.
- **Confundirla con una segunda firma automática.** Un clic de aprobación sin leer no es una revisión.

## Límites y cuándo no aplica

Para cambios de bajo impacto y fácilmente reversibles, una revisión independiente completa puede costar más de lo que protege; bastan criterios automatizados. En equipos muy pequeños puede no existir una persona independiente, y entonces el límite se declara. Y una revisión independiente no certifica ausencia de defectos: acota el sesgo de autoría, no el alcance de lo revisado.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evaluación](../e/evaluacion.md), [Paquete](../p/paquete.md), [Revisión](./revision.md), [Disparador de revisión](../d/disparador-de-revision.md), [Escalamiento](../e/escalamiento.md), [Especialidad](../e/especialidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-005 — Roles, especialidades y colaboración interdisciplinaria](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md).

**Aparece en los casos de estudio:** [TSB Bank](../../../casos/fallo/tsb.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) — requisitos de verificación; autoridad: OWASP.
- [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro; autoridad: NIST.
- [Reproducible Builds](https://reproducible-builds.org/) — verificación independiente; autoridad: proyecto Reproducible Builds.
- [OWASP SAMM](https://owaspsamm.org/) — madurez; autoridad: OWASP.
- [Jia y Harman, 2011](https://doi.org/10.1109/TSE.2010.62) — mutación; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Revisión de la política](./revision-de-la-politica.md) · [Revisión por muestreo →](./revision-por-muestreo.md)
