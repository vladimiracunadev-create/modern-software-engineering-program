# Exhaustividad

[↑ Glosario](../../README.md) · [← Exclusión](./exclusion.md) · [Éxito y no éxito →](./exito-y-no-exito.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Fracción de los patrones reales que la regla detecta.

Definición de trabajo de [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-483 — Tests, seguridad y políticas como gates](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md): Fracción de los problemas reales que una regla avisa.

## Por qué importa

La clase donde se define, [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), existe con este propósito: el proyecto integra la parte en un entregable que un equipo puede mantener: un **catálogo de los patrones de un sistema** donde cada entrada responde por la fuerza que resuelve, dónde vive en el código, qué evidencia la sostiene, cuánto cuesta y bajo qué condición se retira.

## Cómo funciona

Según [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md):

El **detector por nombre** busca las palabras `Strategy`, `Observer`, `Decorator`, `Factory` y `Singleton` en los nombres de clase: obtiene 2 verdaderos positivos, **5 falsos positivos** y 6 falsos negativos, con **29 % de precisión** y **25 % de exhaustividad**. El **detector estructural** busca la forma con `ast`: una clase abstracta con al menos dos subclases, una subclase que guarda una instancia de su propia base, una lista de llamables con métodos que añaden y recorren, un diccionario de clases y un `__new__` que consulta un atributo de clase. Obtiene 6 verdaderos positivos, 1 falso positivo (el acumulador) y 2 falsos negativos (los dos patrones con diccionarios), con **86 % de precisión** y **75 % de exhaustividad**.

Según [SE-483 — Tests, seguridad y políticas como gates](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md):

Una **política como código** es una regla escrita en un lenguaje ejecutable que se evalúa sobre datos de entrada (la configuración de infraestructura, un archivo de flujo de trabajo, una lista de dependencias) y produce una decisión. Las reglas pueden basarse en **texto** (patrones que buscan cadenas) o en **estructura** (reglas sobre el árbol analizado del archivo). Las de texto son simples y producen falsas alarmas: un comentario que contiene una instrucción peligrosa, un nombre de paso que menciona un evento, un valor que parece un dato controlado por un tercero pero es un número. Se evalúan con tres medidas: **precisión** (de lo que avisa, qué parte es real), **exhaustividad** (de lo real, qué parte avisa) y falsos positivos por regla. Una regla ruidosa se vuelve una excepción permanente.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el corpus es pequeño, escrito por el autor, y el detector estructural se escribió conociéndolo; con código real, los patrones tienen más variantes y la precisión y la exhaustividad bajarían. ([SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Problemas](../p/problemas.md), [Regla](../r/regla.md), [ADR](../a/adr.md), [Candidato descartado](../c/candidato-descartado.md), [Catálogo de patrones de un sistema](../c/catalogo-de-patrones-de-un-sistema.md), [Compuerta](../c/compuerta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-483 — Tests, seguridad y políticas como gates](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub Actions: uso seguro](https://docs.github.com/en/actions/reference/security/secure-use) — acciones fijadas, permisos del token e inyección en scripts; autoridad: documentación de GitHub.
- [NIST SP 800-218 (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro; autoridad: NIST.
- [Open Policy Agent](https://www.openpolicyagent.org/docs) — políticas como código; autoridad: documentación del proyecto.
- [Luo et al., «An empirical analysis of flaky tests»](https://doi.org/10.1145/2635868.2635920) — causas de las pruebas inestables (FSE 2014); autoridad: artículo con DOI verificado en Crossref.
- [Google Testing Blog: flaky tests](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html) — gestión de pruebas inestables; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Exclusión](./exclusion.md) · [Éxito y no éxito →](./exito-y-no-exito.md)
