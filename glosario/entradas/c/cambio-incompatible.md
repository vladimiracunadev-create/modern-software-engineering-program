# Cambio incompatible

[↑ Glosario](../../README.md) · [← Cambio en paralelo](./cambio-en-paralelo.md) · [Cambio mínimo →](./cambio-minimo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Un **cambio incompatible** es el que puede hacer fallar o cambiar el resultado de un cliente que seguía el contrato ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md)).

## Por qué importa

Quien publica una biblioteca o una API promete a quien depende de ella; el versionado semántico es la forma de expresar esa promesa. Saber si un cambio es incompatible decide qué número de versión sube y cuánto aviso hay que dar.

## Cómo funciona

[SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md): el **versionado semántico** asigna significado a los tres números: el **mayor** sube cuando hay cambios incompatibles de la API pública, el **menor** cuando se añade funcionalidad compatible y el **parche** cuando se corrige un error sin cambiar la API. Quien depende puede escribir rangos (`>=1.4,<2`) y automatizar actualizaciones menores. Su debilidad: la compatibilidad se declara, no se comprueba, y un cambio de comportamiento con la firma intacta rompe clientes sin que el número lo anuncie.

## Ejemplo

Una función que antes devolvía una lista vacía ante «sin resultados» y ahora lanza una excepción mantiene su firma, pero rompe a los clientes que no la capturaban: es un cambio incompatible aunque el tipo no haya cambiado.

## Errores y confusiones comunes

- **Un cliente se rompe tras un cambio menor.** Cambio de comportamiento con la firma intacta; pruebas de contrato y revisión del comportamiento observable.
- **El número de versión no dice nada.** API pública no definida; declarar la API pública y lo que no se promete.

## Límites y cuándo no aplica

La compatibilidad es relativa a lo que el contrato promete; por eso hay que definir qué es API pública. El versionado semántico no se aplica igual a aplicaciones finales, que no tienen clientes programáticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](./contrato.md), [Resultado](../r/resultado.md), [API pública](../a/api-publica.md), [Obsolescencia](../o/obsolescencia.md), [Registro de cambios](../r/registro-de-cambios.md), [Versionado semántico](../v/versionado-semantico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/lang/es/) — significado de los componentes de la versión; autoridad: especificación de Tom Preston-Werner.
- [Keep a Changelog 1.1.0](https://keepachangelog.com/es-ES/1.1.0/) — registro de cambios para humanos; autoridad: proyecto Keep a Changelog.
- [PEP 440](https://peps.python.org/pep-0440/) — versiones en Python; autoridad: Python Enhancement Proposals.
- [PEP 387](https://peps.python.org/pep-0387/) — política de compatibilidad hacia atrás de Python; autoridad: Python Enhancement Proposals.
- [Hyrum's Law](https://www.hyrumslaw.com/) — dependencia de comportamientos no documentados; autoridad: autor de la formulación.

---

[↑ Glosario](../../README.md) · [← Cambio en paralelo](./cambio-en-paralelo.md) · [Cambio mínimo →](./cambio-minimo.md)
