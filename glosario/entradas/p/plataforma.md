# Plataforma

[↑ Glosario](../../README.md) · [← Plantillas y ast](./plantillas-y-ast.md) · [Plataforma como producto →](./plataforma-como-producto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Una **plataforma** combina capacidades, políticas, interfaces y operación para que otros construyan ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md)). No es solo un conjunto de librerías ni una marca. En el contexto de ejecución, [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) la define como la combinación relevante de hardware, sistema, versión, políticas y capacidades, no solo un nombre comercial. Son dos sentidos: plataforma como **producto interno o externo** para construir encima, y plataforma como **entorno de ejecución**.

## Por qué importa

Llamar «plataforma» a un conjunto de librerías sin responsables crea una expectativa que nadie cumple. Y tratar «Linux» como una plataforma uniforme esconde diferencias de kernel, distribución y espacio de usuario que cambian el comportamiento. Cambia qué se promete a quien construye encima y qué se prueba en cada entorno.

## Cómo funciona

**Como producto** ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md)): propiedad (*ownership*), SLO, autenticación, cuotas y soporte forman parte de su producto, junto con las capacidades. Una plataforma tiene una política de cambios y un responsable de operarla. Si no ofrece eso, es una biblioteca.

**Como entorno** ([SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md)): se registran kernel, distribución, versión y herramientas relevantes por separado. [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) mide que las diferencias entre plataformas importan: un intérprete limpio parte con 25 módulos en Windows y 23 en Linux, y el costo de importar `asyncio` es 9,0 veces el de `json` en Windows y 4,9 en Linux; por eso se comparan razones y no milisegundos.

## Ejemplo

Una «plataforma interna de datos» que ofrece pipelines, un catálogo, cuotas por equipo y un canal de soporte con SLO. Si en cambio publica solo un paquete de utilidades sin responsable ni SLO, es una biblioteca, y llamarla plataforma lleva a equipos a depender de algo sin garantías. Ilustración de ficha mínima:

```yaml
plataforma: datos
responsable: equipo-datos
slo: { disponibilidad: 99.5%, soporte: laborable }
cuotas: { consultas_por_equipo: 10000/día }
cambios: aviso de 2 versiones menores
```

## Errores y confusiones comunes

- **Se anuncia «plataforma» sin responsable ni SLO.** Causa: se confundió conjunto de librerías con plataforma; corrección: escribir propiedad, soporte, cuotas y política de cambios, o llamarlo biblioteca ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md)).
- **«Linux» como plataforma uniforme.** Causa: se confundió kernel con distribución y espacio de usuario; corrección: registrar cada capa por separado ([SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md)).
- **Comparar milisegundos entre plataformas.** Los tiempos absolutos varían; las razones son más estables ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md)).

## Límites y cuándo no aplica

Las cifras de [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) son de un intérprete concreto en dos sistemas y no se trasladan a otros sin medir. No toda organización necesita una plataforma interna: el costo de mantenerla (soporte, SLO) solo se justifica si hay varios equipos consumidores. Y el sentido de entorno no equivale al de producto: una plataforma de ejecución no promete soporte a nadie.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Combinación](../c/combinacion.md), [Interfaz](../i/interfaz.md), [Operación](../o/operacion.md), [ABI](../a/abi.md), [API](../a/api.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

**También se usa en** (502 clases más lo mencionan; las que más):

[SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

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

[↑ Glosario](../../README.md) · [← Plantillas y ast](./plantillas-y-ast.md) · [Plataforma como producto →](./plataforma-como-producto.md)
