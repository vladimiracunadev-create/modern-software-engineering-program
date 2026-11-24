# Descubrimiento

[↑ Glosario](../../README.md) · [← Descripciones no confiables](./descripciones-no-confiables.md) · [Descubrimiento, formulación, automatización →](./descubrimiento-formulacion-automatizacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

En el contexto de plugins ([SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md)), el **descubrimiento** es el mecanismo por el que una aplicación **enumera los proveedores de extensión disponibles** junto con su metadata: por *entry points* (declaración en el paquete del plugin que la aplicación consulta) o por **registro explícito** (el plugin se inscribe en un registro conocido). [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) lo formula desde la arquitectura: define quién puede añadir un complemento y cómo se declara. Este término no es el «descubrimiento» de producto de la [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md); aquí designa la enumeración de extensiones.

## Por qué importa

Una aplicación extensible necesita saber qué extensiones existen sin conocerlas de antemano. Si lo hace mal, aparecen dos problemas: no se sabe de dónde viene cada plugin ni en qué orden se cargará, y el arranque se encarece con cada plugin instalado. La decisión que cambia es **qué hace el sistema con lo que encuentra**: [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md) separa explícitamente descubrir de activar. Que algo esté instalado no significa que deba ejecutarse; esa decisión la toma el usuario o una política.

## Cómo funciona

Hay dos formas habituales:

- **Entry points:** el paquete del plugin declara en sus metadatos un nombre que apunta a un objeto de su código. La aplicación lee los metadatos de todos los paquetes instalados y obtiene nombres y destinos **sin importar el código**. Python ofrece este mecanismo en `importlib.metadata`.
- **Registro explícito:** el plugin llama a una función de la aplicación para registrarse, o se lista en un archivo de configuración.

Las dos dejan **procedencia** (qué paquete trajo qué extensión). El escaneo de carpetas con importación automática, en cambio, mezcla procedencia y orden de carga y obliga a ejecutar código para saber qué hay. De ahí el principio de [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md): **descubrir no implica activar**. Se enumeran los nombres, se aplica la política (lista permitida, versión compatible) y solo entonces se carga lo solicitado. Eso resuelve dos fallos documentados: la aplicación que no arranca porque un plugin no se importa (carga ansiosa sin aislamiento, corregida cargando por plugin con `try/except` y registrando el fallo) y el arranque que tarda más cuanto más plugins hay (se cargan todos aunque se use uno; se corrige descubriendo los nombres y cargando solo el pedido).

## Ejemplo

El SDK+CLI de [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md) expone un punto de extensión. La CLI lista las extensiones sin cargarlas y carga la elegida:

```python
from importlib.metadata import entry_points

disponibles = {ep.name: ep for ep in entry_points(group="engineering_sdk.plugins")}
print(sorted(disponibles))           # descubrir: solo nombres
plugin = disponibles["mi-regla"].load()   # activar: solo el solicitado
```

Si `mi-regla` falla al importarse, se registra el error y el resto de la aplicación sigue funcionando.

## Errores y confusiones comunes

- **Cargar todo al arrancar.** El costo y el riesgo crecen con cada plugin instalado.
- **Escanear carpetas.** Mezcla procedencia y orden, y ejecuta código desconocido solo para listar.
- **Confundir descubrir con confiar.** Un plugin descubierto no está aprobado.
- **Sin aislamiento de fallos.** Un plugin roto derriba la aplicación entera.

## Límites y cuándo no aplica

Con dos o tres extensiones previsibles y un solo equipo, una interfaz y tres implementaciones en el mismo repositorio (el patrón Strategy de la [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)) dan la misma extensión sin descubrimiento, sin versión y sin aislamiento ([SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md)). El descubrimiento resuelve extensión por terceros; si nadie ajeno va a extender el sistema, es complejidad innecesaria. Tampoco ofrece seguridad por sí mismo: ejecutar plugins de terceros exige además permisos y verificación de origen.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Registro](../r/registro.md), [Adaptador de compatibilidad](../a/adaptador-de-compatibilidad.md), [Aislamiento](../a/aislamiento.md), [Capacidades y aislamiento](../c/capacidades-y-aislamiento.md), [Complemento](../c/complemento.md), [Contrato](../c/contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-115 — Plugins, extensiones y puntos de integración](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.
- [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (28 clases más lo mencionan; las que más):

[SE-544](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), [SE-595](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Slack](../../../casos/exito/slack.md), [Instagram](../../../casos/exito/instagram.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — Api pública, versiones, prereleases y compatibilidad declarada; autoridad: Semantic Versioning project.
- [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) — Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority.
- [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) — Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Argparse, importlib.metadata, subprocess y apis de automatización; autoridad: Python Software Foundation.
- [SPDX Specification 3.0](https://spdx.dev/use/specifications/) — Identificadores, sbom y procedencia legible por máquinas; autoridad: Linux Foundation.

---

[↑ Glosario](../../README.md) · [← Descripciones no confiables](./descripciones-no-confiables.md) · [Descubrimiento, formulación, automatización →](./descubrimiento-formulacion-automatizacion.md)
