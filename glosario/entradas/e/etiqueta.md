# Etiqueta

[↑ Glosario](../../README.md) · [← ETag](./etag.md) · [Etiqueta alternativa →](./etiqueta-alternativa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

El programa usa **etiqueta** con dos sentidos distintos. En la cadena de entrega ([SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md)), una etiqueta es un nombre legible que apunta a una huella y que normalmente se puede reasignar (por ejemplo, `api:1.4.0`). En aprendizaje automático ([SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md)), la etiqueta es el valor que el modelo debe predecir, con su fuente, su ventana y su retraso. Esta entrada desarrolla ambos y avisa de que no son lo mismo.

## Por qué importa

En entrega, confundir etiqueta con huella permite que «la misma versión» sea contenido distinto en dos momentos. En aprendizaje automático, una etiqueta sin su retraso invita a calcular métricas sobre decisiones que todavía no tienen respuesta y a presentarlas como resultados ([SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md)).

## Cómo funciona

**Sentido de entrega.** Un artefacto es la salida inmutable de un build; su huella es el resultado de aplicarle una función hash, de modo que un solo byte distinto produce otra huella. Un registro de contenedores permite referirse a una imagen por etiqueta (`api:1.4.0`) o por resumen (`api@sha256:…`); solo la segunda es inmutable. La etiqueta es un puntero que alguien puede mover.

**Sentido de datos.** La etiqueta tiene una fuente (de dónde sale la verdad), una ventana (en qué intervalo se observa) y un retraso (cuánto tarda en conocerse).

## Ejemplo

[SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md): el repositorio de la API de entregas acepta etiquetas de versión una sola vez; integración y preproducción prueban contra la huella, y el despliegue recibe la huella y la configuración por separado.

## Errores y confusiones comunes

- **Un defecto aparece solo en producción.** Se reconstruyó o se movió una etiqueta; corrección ([SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md)): desplegar por huella y promover sin reconstruir.
- **Métricas sobre etiquetas que aún no existen.** Se ignora el retraso de la etiqueta.

## Límites y cuándo no aplica

Una etiqueta inmutable por política (aceptada una sola vez) reduce el riesgo, pero la garantía fuerte sigue siendo la huella. En datos, ninguna etiqueta es verdad absoluta: tiene ruido y retraso de su fuente.

## Relación con otros conceptos

- **Prerrequisito:** [Huella](../h/huella.md).
- **Ver también:** [Modelo](../m/modelo.md), [Valor](../v/valor.md), [Ventana](../v/ventana.md), [Almacén de características](../a/almacen-de-caracteristicas.md), [Artefacto](../a/artefacto.md), [Característica](../c/caracteristica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (179 clases más lo mencionan; las que más):

[SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), [SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), [SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Slack](../../../casos/exito/slack.md), [Shopify](../../../casos/exito/shopify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec) — referencias por etiqueta y por resumen; autoridad: Open Container Initiative.
- [Fowler, «DeploymentPipeline»](https://martinfowler.com/bliki/DeploymentPipeline.html) — artefacto único que avanza por etapas; autoridad: autor del texto.
- [Google SRE: Release Engineering](https://sre.google/sre-book/release-engineering/) — builds herméticos y promoción; autoridad: Google, libro de ingeniería de confiabilidad.
- [OCI Image Specification: descriptores](https://github.com/opencontainers/image-spec/blob/main/descriptor.md) — identificación por resumen; autoridad: Open Container Initiative.
- [PyPI: ayuda](https://pypi.org/help/) — inmutabilidad de los nombres de archivo publicados; autoridad: Python Packaging Authority.

---

[↑ Glosario](../../README.md) · [← ETag](./etag.md) · [Etiqueta alternativa →](./etiqueta-alternativa.md)
