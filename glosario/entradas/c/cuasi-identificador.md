# Cuasi-identificador

[↑ Glosario](../../README.md) · [← Cuarentena](./cuarentena.md) · [Cubeta de fichas →](./cubeta-de-fichas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Dato que no identifica por sí solo pero sí en combinación con otros.

Definición de trabajo de [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md): Atributo que no identifica por sí solo pero sí en combinación con otros (edad, sexo, código postal).
- En [SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md): Atributo que no identifica a una persona por sí solo y sí combinado con otros o con una fuente auxiliar.
- En [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md): Atributo que, combinado con otros, puede identificar a una persona.

## Por qué importa

En [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), el tema «Reidentificación» importa porque quitar el nombre no anonimiza; los cuasi-identificadores sí identifican.

## Cómo funciona

Según [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md):

Un **identificador directo** (nombre, correo) señala a una persona. Un **cuasi-identificador** es un dato que por sí solo no identifica pero que, combinado con otros, sí: fecha de nacimiento, código postal, género, curso. La investigación de Sweeney mostró que una gran parte de la población estadounidense era única por esos tres datos. En un **ataque de vinculación** se cruza el conjunto «anonimizado» con otra fuente que sí contiene nombres y los mismos cuasi-identificadores; donde la combinación es única en ambos, la identidad se recupera. La defensa técnica más sencilla es **generalizar** (año en lugar de fecha completa, tres dígitos del código postal) y **suprimir** los grupos pequeños, hasta que cada combinación corresponda a al menos *k* personas (k-anonimato).

Según [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** una persona ajena identifica a un estudiante en un entorno de revisión. **Hipótesis rivales:** (a) el enmascarado falló en algún campo; (b) alguien filtró el nombre; (c) la combinación de datos corrientes es única y permite la vinculación. **Prueba:** cuenta cuántos registros comparten cada combinación de cuasi-identificadores; si el 97,6 % es único y existe una lista externa con los mismos datos, la causa es la combinación. **Conclusión:** quitar el nombre no era anonimizar; la fecha completa, el código postal y el género identifican. **Regresión:** generaliza a año y tres dígitos, suprime los grupos de menos de cinco y añade una prueba que calcule la unicidad y falle si supera el 1 %.

## Ejemplo

Ejemplo de [SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md) (sección «Preguntas frecuentes»):

No: es una seudonimización parcial. Los cuasi-identificadores pueden identificar por combinación, y la unicidad medida lo muestra. Para considerar un conjunto desidentificado hay que seguir un método reconocido por la norma aplicable.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una persona es identificable en un entorno de pruebas** — causa: cuasi-identificadores sin generalizar. Corrección: medir la unicidad; generalizar y suprimir grupos pequeños. ([SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md))
- **Un conjunto sin nombre identifica a personas** — causa: cuasi-identificadores sin generalizar. Corrección: medir la unicidad y generalizar hasta una clase mínima declarada. ([SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md))
- **Se reidentifica un conjunto sin nombres** — causa: combinación de cuasi-identificadores única. Corrección: medir unicidad y generalizar o publicar agregados. ([SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **cuasi-identificador** es un dato que por sí solo no identifica pero que, combinado con otros, sí: fecha de nacimiento, código postal, género, curso. ([SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md))
- Traslada el análisis a otro contexto (por ejemplo, un entorno de formación con datos de clientes de una tienda): cambia los cuasi-identificadores disponibles y la lista externa posible, y conserva el procedimiento de medir la unicidad, generalizar hasta un umbral, elegir la técnica de enmascarado por la prueba que se hará y fijar la vida del entorno. ([SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md))

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
