# Exposición

[↑ Glosario](../../README.md) · [← Explotación conocida](./explotacion-conocida.md) · [Expresión →](./expresion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Producto de la probabilidad y el impacto de un riesgo; su suma mide el retraso esperado, no su dispersión.

Definición de trabajo de [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md): Riesgo ponderado por la parte de los cambios que cae en un componente.
- En [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md): Combinación razonada de probabilidad y consecuencia.

## Por qué importa

En [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), el tema «Exposición» importa porque convierte retraso en decisiones erróneas.

## Cómo funciona

Según [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md):

**Diagnóstico paso a paso.** (1) Se consulta el historial de configuración de la validación: se bajó el umbral y se desactivó en un cambio sin revisión. (2) Se comprueba que el PSI descarta los nulos antes de comparar. (3) Se calcula la exposición: 168 horas por 400 decisiones, más de 67 000 decisiones con la mitad del historial vacío. (4) Se confirma que el AUC con etiquetas habría alertado a las 53 horas.

Según [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md):

Un riesgo es un evento incierto que, si ocurre, afecta al proyecto. Se describe con una causa, un evento y un efecto («si el proveedor de identidad cambia su contrato, la integración se retrasa»), se estima con probabilidad e impacto, y se acompaña de un disparador (la señal de que se está materializando), una respuesta (reducir, evitar, aceptar, transferir) y un responsable. Boehm propuso ordenarlos por exposición, es decir, por el producto de probabilidad y pérdida, y revisar la lista de los principales cada vez. El valor de la lista es la conversación que obliga, no el número.

## Ejemplo

Ejemplo de [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la exposición esperada de tres riesgos y la probabilidad de que ninguno ocurra. Antes de ejecutarlo, predice si la probabilidad de que no ocurra ninguno es mayor o menor que 50 %.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La media casi no se mueve, y por eso la exposición esperada, sola, no avisa de la cola. ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md))
- Simula los diez riesgos con y sin causa común y compara el percentil 85 con la exposición. ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](../c/combinacion.md), [Componente](../c/componente.md), [Consecuencia](../c/consecuencia.md), [Dispersión](../d/dispersion.md), [Contingencia](../c/contingencia.md), [Issue](../i/issue.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (38 clases más lo mencionan; las que más):

[SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), [SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [TSB Bank](../../../casos/fallo/tsb.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Boehm, «Software risk management: principles and practices» (IEEE Software, 1991)](https://doi.org/10.1109/52.62930) — identificación y priorización de riesgos de proyecto; autoridad: IEEE Software.
- [Nygard, «Documenting architecture decisions» (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registros breves de decisiones; autoridad: autor de la práctica.
- [Architectural Decision Records](https://adr.github.io/) — plantillas y vocabulario de registros de decisión; autoridad: comunidad ADR.
- [SEI: Software risk management](https://www.sei.cmu.edu/library/software-risk-management/) — recursos de gestión de riesgos de software; autoridad: Software Engineering Institute, Carnegie Mellon University.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Explotación conocida](./explotacion-conocida.md) · [Expresión →](./expresion.md)
