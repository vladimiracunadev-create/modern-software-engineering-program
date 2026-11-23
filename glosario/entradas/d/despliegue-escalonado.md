# Despliegue escalonado

[↑ Glosario](../../README.md) · [← Despliegue continuo](./despliegue-continuo.md) · [Despliegue por etapas →](./despliegue-por-etapas.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Entrega a fracciones crecientes de usuarios con una señal de salud entre cada una.

Definición de trabajo de [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md).

## Por qué importa

En [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md), el tema «Despliegue escalonado» importa porque limita el daño de un defecto antes de detectarlo.

## Cómo funciona

Según [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md):

Simulación con semilla 5: cada cliente que recibe la versión defectuosa se rompe con una probabilidad dada, y el despliegue escalonado (1 %, 5 %, 25 %, 100 %) se detiene si falla más del 1 % de los actualizados en un escalón. **Defecto de 0,2 %**: lanzar a todos rompió 20 clientes; el escalonado **no se detuvo** y rompió los mismos 20. **Defecto de 2 %**: a todos, **194**; escalonado, **3**, detenido en el escalón del 1 %. **Defecto de 10 %**: a todos, **1 002**; escalonado, **11**, detenido en el 1 %.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md):

La entrega de `notas` publica, para cada versión, un `notas-X.Y.Z.pyz`, un `SHA256SUMS` y su firma en un canal independiente. El cliente que se actualiza descarga a un temporal en el mismo directorio, comprueba la longitud, el SHA-256 contra una lista firmada y la compatibilidad mínima, y solo entonces reemplaza de forma atómica el archivo activo, conservando el anterior como `notas.anterior.pyz`. La versión se compara con tuplas y un formato desconocido es un error.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md)) son:

- **Se instala un archivo truncado** — causa: solo se comprobó su existencia. Corrección: descarga a temporal, longitud y SHA-256 antes de reemplazar.
- **Alguien sustituyó el archivo y su hash** — causa: el hash viaja por el mismo canal. Corrección: firma con clave pública conocida por otro camino.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): detecciones y simulaciones idénticas, velocidades y arranques distintos. No se firmó nada, no se verificó una firma real ni se probó un marco de actualización; los clientes, las tasas de defecto y el umbral son supuestos del autor. La siguiente clase pregunta cómo saber si un lanzamiento funciona sin vigilar a quien lo usa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Señal](../s/senal.md), [Artefacto](../a/artefacto.md), [Firma digital](../f/firma-digital.md), [Huella](../h/huella.md), [Retroceso](../r/retroceso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST FIPS 180-4: Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) — SHA-256 y SHA-512; autoridad: NIST.
- [Semantic Versioning 2.0.0](https://semver.org/) — orden y precedencia de versiones; autoridad: especificación de la comunidad.
- [The Update Framework](https://theupdateframework.io/) — amenazas y diseño de actualizaciones seguras; autoridad: proyecto de la Cloud Native Computing Foundation.
- [SLSA](https://slsa.dev/) — niveles de seguridad de la cadena de suministro; autoridad: OpenSSF.
- [Python: `zipapp`](https://docs.python.org/3/library/zipapp.html) — aplicaciones Python en un solo archivo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Despliegue continuo](./despliegue-continuo.md) · [Despliegue por etapas →](./despliegue-por-etapas.md)
