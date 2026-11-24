# Valor esperado

[↑ Glosario](../../README.md) · [← Valor del aprendizaje](./valor-del-aprendizaje.md) · [Valor esperado de la información perfecta →](./valor-esperado-de-la-informacion-perfecta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

**Valor esperado** tiene dos sentidos en el programa, no relacionados entre sí. En [SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md) (gestión de riesgos) es la suma de los resultados posibles ponderados por su probabilidad. En [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) (cadena de suministro) es el dato (clave, constructor, repositorio, secuencia) que el verificador conoce *por fuera* del release que está comprobando.

## Por qué importa

En riesgos, ordenar por valor esperado evita mitigar lo que no pesa: [SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md) señala que una matriz con celdas que agrupan valores muy distintos hace elegir mal. En verificación de releases, que el valor esperado provenga de fuera es lo que da sentido a la comprobación.

## Cómo funciona

**Sentido de riesgos.** Se multiplica probabilidad por impacto y se ordenan los riesgos por ese producto, con rangos para no fingir precisión. La matriz de colores agrupa cosas muy distintas en una celda; el valor esperado conserva la magnitud.

**Sentido de releases.** El verificador compara el release con valores obtenidos de un canal independiente (el contrato, un archivo de configuración versionado), nunca del mismo documento que verifica. Si los valores esperados se toman del release, un atacante que lo manipula manipula también lo que se espera.

## Ejemplo

[SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md): el equipo de seguridad guarda clave pública, nombre del producto, constructor y repositorio en configuración versionada obtenida del contrato, y registra la secuencia más alta aceptada para rechazar un release antiguo. [SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md): se generan carteras de treinta riesgos y se cuenta en cuántas el riesgo de mayor valor esperado no está entre los cinco que elige la matriz.

## Errores y confusiones comunes

- **El verificador acepta un release de otro constructor.** Valores esperados tomados del documento; usar configuración independiente y fijada de antemano.
- **Se mitigan riesgos que no pesan.** Matriz con celdas muy heterogéneas; ordenar por valor esperado con rangos.

## Límites y cuándo no aplica

Probabilidades e impactos estimados son inciertos: el producto da una falsa precisión si no se acompaña de rangos. Un valor esperado bajo no cubre eventos raros de impacto catastrófico, que se tratan aparte.

## Relación con otros conceptos

- **Prerrequisito:** [Secuencia](../s/secuencia.md).
- **Ver también:** [Resultado](../r/resultado.md), [Verificador](./verificador.md), [Caso coherente](../c/caso-coherente.md), [Decisión reversible](../d/decision-reversible.md), [No verificable](../n/no-verificable.md), [Petición de decisión](../p/peticion-de-decision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-534 — Gestión de riesgos y decisiones ejecutivas](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SLSA v1.0: niveles](https://slsa.dev/spec/v1.0/levels) — garantías de la construcción y verificación de procedencia; autoridad: proyecto SLSA, OpenSSF.
- [in-toto: declaración (Statement)](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) — atestaciones ligadas a un sujeto; autoridad: proyecto in-toto.
- [Reproducible Builds: definición](https://reproducible-builds.org/docs/definition/) — reconstrucción independiente; autoridad: proyecto Reproducible Builds.
- [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro de software; autoridad: NIST.
- [Lamb y Zacchiroli, «Reproducible Builds»](https://doi.org/10.1109/MS.2021.3073045) — reconstrucción independiente como defensa; autoridad: IEEE Software.

---

[↑ Glosario](../../README.md) · [← Valor del aprendizaje](./valor-del-aprendizaje.md) · [Valor esperado de la información perfecta →](./valor-esperado-de-la-informacion-perfecta.md)
