# Promoción

[↑ Glosario](../../README.md) · [← Promesa declarada](./promesa-declarada.md) · [Pronóstico por simulación →](./pronostico-por-simulacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Avance de un mismo artefacto a la siguiente etapa sin reconstruirlo.

Definición de trabajo de [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md): Movimiento de un cambio ya probado de un entorno al siguiente por un proceso definido.

## Por qué importa

En [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), el tema «Promoción» importa porque reconstruir para cada entorno rompe la cadena de evidencia.

## Cómo funciona

Según [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), en la sección «Promoción»:

**Promover** es avanzar un mismo artefacto de una etapa a la siguiente sin reconstruirlo. La razón es lógica: una prueba es evidencia sobre un objeto concreto; si el objeto cambia, la evidencia no se traslada. Cuando cada entorno reconstruye, aparece un hueco entre lo probado y lo desplegado cuyo tamaño es la probabilidad de que el build produzca un resultado distinto. Con un build reproducible ese hueco se acerca a cero, y entonces la reconstrucción solo cuesta tiempo; con uno que no lo es, es un riesgo que crece con cada etapa. Lo que sí cambia entre entornos es la **configuración** (direcciones, credenciales, parámetros), que se inyecta en el despliegue y no se incrusta en el artefacto, porque un artefacto con la configuración dentro no se puede promover.

## Ejemplo

Ejemplo de [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) (sección «Ejemplo profesional»):

El equipo define la canalización de la API de entregas. El build produce un artefacto y registra su huella; el repositorio acepta etiquetas de versión una sola vez. Integración y preproducción ejecutan sus pruebas contra esa huella y escriben un metadato por etapa (resultado, fecha, versión de las pruebas); la promoción a producción solo se permite si ambos metadatos existen. El despliegue recibe la huella y la configuración del entorno por separado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Preproducción pasa y producción falla** — causa: configuraciones que divergieron. Corrección: promoción periódica y comparación semanal. ([SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Sin promoción, con una edición cada diez semanas, hay divergencia durante 38 de 52 semanas, y las diferencias se acumulan. ([SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md))
- Traslada el análisis a otro dominio (por ejemplo, una tienda con pagos y un panel de administración): cambia los recursos y conserva el procedimiento de medir el alcance de un error por estructura de cuentas, medir la divergencia con y sin promoción, escribir los pares incompatibles y calcular su incidencia. ([SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md))

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
