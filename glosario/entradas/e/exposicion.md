# Exposición

[↑ Glosario](../../README.md) · [← Explotación conocida](./explotacion-conocida.md) · [Expresión →](./expresion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

La **exposición** a un riesgo es el producto de su probabilidad y su impacto ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), siguiendo a Boehm); [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md) la presenta como la combinación razonada de probabilidad y consecuencia. [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) la usa ponderada por la parte de los cambios que cae en un componente. [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) advierte que su suma mide el retraso esperado, no su dispersión.

## Por qué importa

Permite ordenar riesgos y decidir a cuáles dedicar esfuerzo: Boehm propuso ordenarlos por exposición y revisar la lista de los principales cada vez. El valor de la lista, dice [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), es la conversación que obliga, no el número. Cambia la decisión de dónde se invierte atención, pruebas o contingencia.

## Cómo funciona

Cada riesgo se describe con causa, evento y efecto, se estima con probabilidad e impacto y se acompaña de un disparador, una respuesta y un responsable ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md)). La exposición es `probabilidad × impacto`. [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) la aplica a pruebas: el riesgo de un componente se pondera por la fracción de cambios que lo tocan, de modo que un componente muy modificado con impacto moderado puede merecer más atención que uno raro de impacto alto. En [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) se calcula en horas y decisiones: 168 horas por 400 decisiones, más de 67 000 decisiones tomadas con la mitad del historial vacío, lo que da la magnitud de un incidente de datos.

Su límite estructural es que es un valor esperado: la media casi no se mueve cuando hay una cola de eventos grandes, por lo que la exposición esperada, sola, no avisa de la cola ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md)).

## Ejemplo

Dos riesgos: A con probabilidad 0,5 e impacto de 2 días (exposición 1 día); B con probabilidad 0,1 e impacto de 20 días (exposición 2 días). Ilustración:

```python
riesgos = {"A": (0.5, 2), "B": (0.1, 20)}
orden = sorted(riesgos, key=lambda k: -riesgos[k][0] * riesgos[k][1])   # B, A
```

[SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) simula diez riesgos con y sin causa común y compara el percentil 85 con la exposición: con causa común, la exposición subestima el retraso.

## Errores y confusiones comunes

- **Sumar exposiciones como si fueran independientes.** Las causas comunes hacen que se materialicen juntos.
- **Tomar el número como predicción.** Ordena; no predice.
- **Confundirla con el riesgo mismo.** La exposición es una cifra; el riesgo es una cadena causal con respuesta ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md)).

## Límites y cuándo no aplica

Las probabilidades e impactos son estimaciones. En seguridad funcional ([SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md)), el producto de números puede no bastar: la gravedad se trata con normas propias. Y una exposición baja no autoriza a ignorar un riesgo cuyo impacto es inaceptable.

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
