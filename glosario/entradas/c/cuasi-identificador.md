# Cuasi-identificador

[↑ Glosario](../../README.md) · [← Cuarentena](./cuarentena.md) · [Cubeta de fichas →](./cubeta-de-fichas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Un **cuasi-identificador** es un dato que no identifica a una persona por sí solo pero sí en combinación con otros. Es la definición de [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) (entornos preview y datos seguros), con el mismo núcleo en [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md) (edad, sexo, código postal), [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) (combinado con otros o con una fuente auxiliar) y [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md). Se contrapone al **identificador directo** (nombre, correo), que señala a la persona por sí solo.

## Por qué importa

Quitar el nombre no anonimiza. Es la idea central de [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md): en un entorno de revisión con datos «enmascarados», los cuasi-identificadores siguen presentes y pueden devolver la identidad. Cambia la decisión de qué se copia a un entorno no productivo y qué se considera dato personal.

## Cómo funciona

[SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) lo explica con la investigación de Sweeney: una gran parte de la población estadounidense era única por fecha de nacimiento, código postal y género. El mecanismo es el **ataque de vinculación**:

1. El conjunto «anonimizado» conserva cuasi-identificadores (fecha de nacimiento, código postal, género, curso).
2. Otra fuente accesible contiene nombres y esos mismos atributos.
3. Se cruzan; donde la combinación es única en ambas, la identidad se recupera.

La defensa técnica más sencilla es **generalizar** (el año en lugar de la fecha completa; tres dígitos del código postal) y **suprimir** los grupos pequeños, hasta que cada combinación corresponda a al menos *k* personas, que es el k-anonimato. Para saber si hay riesgo, se cuenta cuántos registros comparten cada combinación de cuasi-identificadores.

## Ejemplo

En el caso de [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), una persona ajena identifica a un estudiante en un entorno de revisión. Hipótesis rivales: (a) falló el enmascarado de un campo; (b) alguien filtró el nombre; (c) la combinación de datos corrientes es única y permite la vinculación. Al contar registros por combinación, el 97,6 % es único; con una lista externa que tiene los mismos datos, la causa es (c), y la corrección es generalizar y suprimir, no enmascarar el nombre otra vez. El porcentaje es de los datos sintéticos de la clase.

## Errores y confusiones comunes

- **Creer que quitar nombre y correo anonimiza.**
- **Tratar cada columna por separado:** el riesgo está en la combinación, no en un campo.
- **Confundirlo con seudonimización:** esta reemplaza el identificador por otro valor, pero los cuasi-identificadores siguen vinculando.
- **Suponer que k-anonimato basta siempre:** [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) lo trata como una medida entre otras.

## Límites y cuándo no aplica

El riesgo depende de la fuente auxiliar que tenga el atacante, que no se conoce de antemano. Generalizar pierde precisión y puede inutilizar datos para análisis fino. El 97,6 % no es una cifra extrapolable a otra población. En conjuntos sin atributos combinables (agregados ya generalizados) el concepto pierde peso.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Combinación](./combinacion.md), [Dato personal](../d/dato-personal.md), [Fatiga de alarmas](../f/fatiga-de-alarmas.md), [Fusión errónea](../f/fusion-erronea.md), [HMAC](../h/hmac.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-188: de-identificación de conjuntos de datos](https://csrc.nist.gov/pubs/sp/800/188/final) — técnicas y riesgos de reidentificación; autoridad: NIST.
- [Sweeney, «k-anonymity: a model for protecting privacy»](https://doi.org/10.1142/S0218488502001648) — modelo de k-anonimato (International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 2002); autoridad: artículo con DOI verificado en Crossref.
- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — definición de seudonimización; autoridad: Unión Europea, EUR-Lex.
- [GitHub: despliegues y entornos](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) — entornos con protecciones y secretos propios; autoridad: documentación de GitHub.
- [Argo CD: ApplicationSet](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/) — generación de aplicaciones desde plantillas; autoridad: documentación de Argo CD.

---

[↑ Glosario](../../README.md) · [← Cuarentena](./cuarentena.md) · [Cubeta de fichas →](./cubeta-de-fichas.md)
