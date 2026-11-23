# Huella o digest

[↑ Glosario](../../README.md) · [← Huella del cuerpo](./huella-del-cuerpo.md) · [Huella reproducible →](./huella-reproducible.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Resultado de aplicar una función hash a los bytes de un artefacto.

Definición de trabajo de [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md).

## Por qué importa

La clase donde se define, [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), existe con este propósito: la clase existe para que decidas dónde vive un artefacto después de construirlo, cómo se le identifica sin ambigüedad y cómo avanza de un entorno a otro sin cambiar.

## Cómo funciona

[SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md):

El equipo define la canalización de la API de entregas. El build produce un artefacto y registra su huella; el repositorio acepta etiquetas de versión una sola vez. Integración y preproducción ejecutan sus pruebas contra esa huella y escriben un metadato por etapa (resultado, fecha, versión de las pruebas); la promoción a producción solo se permite si ambos metadatos existen. El despliegue recibe la huella y la configuración del entorno por separado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md)) son:

- **Un defecto aparece solo en producción** — causa: se reconstruyó o se movió una etiqueta. Corrección: desplegar por huella y promover sin reconstruir.
- **No se puede volver a la versión anterior** — causa: la limpieza borró la versión necesaria. Corrección: retención basada en la profundidad de los retrocesos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con semilla fija en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún registro real, no se midió ningún despliegue y la deriva del 1, 5 y 15 %, el 12 % de defectos escondidos, el repush del 2 y 10 %, el despliegue semanal y la cola geométrica de profundidad son supuestos del autor.

## Relación con otros conceptos

- **Prerrequisito:** [Huella](./huella.md).
- **Ver también:** [Artefacto](../a/artefacto.md), [Byte](../b/byte.md), [Función](../f/funcion.md), [Resultado](../r/resultado.md), [Etiqueta](../e/etiqueta.md), [Promoción](../p/promocion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «DeploymentPipeline»](https://martinfowler.com/bliki/DeploymentPipeline.html) — artefacto único que avanza por etapas; autoridad: autor del texto.
- [Google SRE: Release Engineering](https://sre.google/sre-book/release-engineering/) — builds herméticos y promoción; autoridad: Google, libro de ingeniería de confiabilidad.
- [OCI Image Specification: descriptores](https://github.com/opencontainers/image-spec/blob/main/descriptor.md) — identificación por resumen; autoridad: Open Container Initiative.
- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec) — referencias por etiqueta y por resumen; autoridad: Open Container Initiative.
- [PyPI: ayuda](https://pypi.org/help/) — inmutabilidad de los nombres de archivo publicados; autoridad: Python Packaging Authority.

---

[↑ Glosario](../../README.md) · [← Huella del cuerpo](./huella-del-cuerpo.md) · [Huella reproducible →](./huella-reproducible.md)
