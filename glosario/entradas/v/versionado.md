# Versionado

[↑ Glosario](../../README.md) · [← Versión optimista](./version-optimista.md) · [Versionado del protocolo →](./versionado-del-protocolo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

**Versionado** es la práctica de identificar y ordenar las versiones de un artefacto (un contrato, una API, un paquete, una página de documentación) para comunicar el alcance del cambio y gestionar la coexistencia entre versiones. El programa lo enseña en varios contextos: contratos de datos ([SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md)), portales de documentación ([SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md)) y paquetes con dependencias ([SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md)). El hilo común: cada versión debe ser coherente consigo misma y declarar qué pasa con los enlaces y la compatibilidad entre versiones.

## Por qué importa

Comunica el alcance del cambio. Un número o una etiqueta de versión es una promesa para quien consume: si el cambio es compatible, puede actualizar con confianza; si no lo es, debe revisar. Un versionado mal hecho produce roturas inesperadas, y uno que ordena mal las versiones puede instalar una anterior ([SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md)).

## Cómo funciona

El mecanismo tiene tres piezas. Primero, la **identidad**: cada versión tiene un identificador estable (una etiqueta, un número). Segundo, el **orden**: las versiones se pueden comparar. Aquí aparece un error típico que [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) señala: ordenar versiones como cadenas de texto pone «1.10» antes de «1.9»; hay que compararlas por componentes numéricos. Tercero, la **semántica**: qué comunica el cambio de número. El versionado semántico, por ejemplo, reserva el cambio de la versión mayor para los cambios incompatibles, el de la menor para añadidos compatibles y el del parche para correcciones.

En un contrato de datos ([SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md)), la versión acompaña a cinco declaraciones: el esquema, la semántica de cada campo, la calidad ofrecida, el nivel de servicio y la gobernanza (dueño, canal de contacto, política de cambios y retención). El contrato es un archivo versionado junto al código del productor, no una página de una wiki, y su verificación se ejecuta en cada cambio.

En un portal documental ([SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md)), el versionado se hace desde etiquetas del repositorio: cada versión de la documentación es coherente consigo misma (sus enlaces internos apuntan a su propia versión) y declara qué pasa con los enlaces entre versiones (redirecciones o avisos de retirada). La clase añade una política de retirada y propone trasladar la estructura a otro dominio para comprobar qué parte depende de la plataforma y qué parte es reutilizable.

## Ejemplo

El contrato de la API de entregas lleva la versión `2.3.0`. Un cambio que añade un campo opcional sube a `2.4.0`; uno que renombra un campo o elimina uno sube a `3.0.0` con aviso de retirada. Para decidir cuál de dos versiones es más reciente, se comparan sus componentes como números: `2.10.0` es posterior a `2.9.0`, aunque como texto sea anterior. (Ilustración de las reglas descritas.)

## Errores y confusiones comunes

- **Ordenar versiones como texto**: instala una anterior ([SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md)).
- **Versiones incoherentes**: enlaces internos que apuntan a otra versión.
- **Cambios incompatibles bajo un número menor**: rompen a los consumidores.
- **Contratos en una wiki en vez de en el repositorio**, sin verificación.

## Límites y cuándo no aplica

El versionado comunica intención, no la garantiza: un número no impide que un cambio «compatible» rompa a un cliente estricto. Para artefactos que nadie más consume, un esquema formal es excesivo. Mantener muchas versiones vivas tiene un costo; la política de retirada es parte del versionado, no un añadido.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Despliegue escalonado](../d/despliegue-escalonado.md), [Firma digital](../f/firma-digital.md), [Huella](../h/huella.md), [Informe de entrega](../i/informe-de-entrega.md), [Paquete reproducible](../p/paquete-reproducible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (61 clases más lo mencionan; las que más):

[SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [mike: versionado de documentación con MkDocs](https://github.com/jimporter/mike) — herramienta de ejemplo de versiones desde Git; autoridad: proyecto mike.
- [Semantic Versioning 2.0.0](https://semver.org/) — convención de versiones; autoridad: especificación SemVer.
- [Read the Docs: versiones](https://docs.readthedocs.com/platform/stable/versions.html) — publicación de varias versiones de documentación; autoridad: Read the Docs.
- [Keep a Changelog](https://keepachangelog.com/) — convención de registro de cambios; autoridad: proyecto Keep a Changelog.
- [GitHub Pages: documentación](https://docs.github.com/en/pages) — publicación de sitios estáticos desde un repositorio; autoridad: GitHub Docs.

---

[↑ Glosario](../../README.md) · [← Versión optimista](./version-optimista.md) · [Versionado del protocolo →](./versionado-del-protocolo.md)
