# Promoción

[↑ Glosario](../../README.md) · [← Promesa declarada](./promesa-declarada.md) · [Pronóstico por simulación →](./pronostico-por-simulacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

**Promover** es avanzar un mismo artefacto de una etapa a la siguiente sin reconstruirlo ([SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md)). [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) lo usa en el contexto de entornos: el movimiento de un cambio ya probado de un entorno al siguiente por un proceso definido. La clave es «el mismo»: lo que se probó es lo que se despliega.

## Por qué importa

Una prueba es evidencia sobre un objeto concreto: si el objeto cambia, la evidencia no se traslada. Cuando cada entorno reconstruye el artefacto, aparece un hueco entre lo probado y lo desplegado. La decisión que cambia es dónde se construye: una sola vez, y de ahí en adelante se mueve ese resultado y se cambia solo la configuración.

## Cómo funciona

[SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) explica la razón lógica. El tamaño del hueco entre lo probado y lo desplegado es la probabilidad de que el *build* produzca un resultado distinto. Con una construcción reproducible, ese hueco se acerca a cero y la reconstrucción solo cuesta tiempo; con una que no lo es, es un riesgo que crece con cada etapa.

Lo que sí cambia entre entornos es la **configuración** (direcciones, credenciales, parámetros). Se inyecta en el despliegue y no se incrusta en el artefacto, porque un artefacto con la configuración dentro no se puede promover. Para asegurar que es el mismo objeto se usa su huella (digest), no una etiqueta que pueda moverse.

[SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) añade el efecto sobre la divergencia entre entornos: sin promoción, con una edición cada diez semanas, hay divergencia durante 38 de 52 semanas, y las diferencias se acumulan; promover periódicamente la configuración por la misma ruta a todos los entornos mantiene la paridad. El síntoma «preproducción pasa y producción falla» suele indicar configuraciones que divergieron; la corrección es promoción periódica y comparación semanal.

## Ejemplo

El artefacto se construye una vez, queda identificado por su huella y se despliega en preproducción con su configuración de ese entorno. Pasan las pruebas. Ese mismo artefacto (misma huella) se despliega en producción con la configuración de producción. Si en cambio se reconstruyera desde el código, la prueba de preproducción no probaría el artefacto de producción. Es el principio de [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md).

## Errores y confusiones comunes

- **Preproducción pasa y producción falla**: configuraciones que divergieron; se corrige con promoción periódica y comparación semanal.
- **Reconstruir en cada entorno** confiando en que «es el mismo código».
- **Incrustar la configuración en el artefacto**: lo vuelve no promovible.
- **Usar etiquetas mutables** en lugar de huellas para identificar el artefacto.

## Límites y cuándo no aplica

La promoción exige construir de forma reproducible y separar configuración de código; sin eso, no es aplicable de forma segura. Tiene sentido cuando hay varias etapas; en un flujo de una sola etapa no hay nada que promover. Y no sustituye la observación en producción: un artefacto bien promovido puede comportarse distinto con datos y carga reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Entorno](../e/entorno.md), [Proceso](./proceso.md), [Acceso de emergencia](../a/acceso-de-emergencia.md), [Etiqueta](../e/etiqueta.md), [Huella o digest](../h/huella-o-digest.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Release Engineering](https://sre.google/sre-book/release-engineering/) — builds herméticos y promoción; autoridad: Google, libro de ingeniería de confiabilidad.
- [Fowler, «DeploymentPipeline»](https://martinfowler.com/bliki/DeploymentPipeline.html) — artefacto único que avanza por etapas; autoridad: autor del texto.
- [OCI Image Specification: descriptores](https://github.com/opencontainers/image-spec/blob/main/descriptor.md) — identificación por resumen; autoridad: Open Container Initiative.
- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec) — referencias por etiqueta y por resumen; autoridad: Open Container Initiative.
- [PyPI: ayuda](https://pypi.org/help/) — inmutabilidad de los nombres de archivo publicados; autoridad: Python Packaging Authority.

---

[↑ Glosario](../../README.md) · [← Promesa declarada](./promesa-declarada.md) · [Pronóstico por simulación →](./pronostico-por-simulacion.md)
