# Build reproducible

[↑ Glosario](../../README.md) · [← Build hermético](./build-hermetico.md) · [Builder →](./builder.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Construcción que, con las mismas entradas declaradas, produce artefactos idénticos bit a bit en cualquier máquina.

Definición de trabajo de [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md).

## Por qué importa

La clase donde se define, [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), existe con este propósito: la clase existe para que puedas responder, con evidencia y no con una promesa, a la pregunta «¿este binario sale de este código?».

## Cómo funciona

[SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md) (sección «Caso conductor»):

La API de entregas es el caso conductor de la [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md). Esta clase deja el primer artefacto del canal: un build reproducible con entradas declaradas. `SE-470` tratará cómo se almacena y se promueve ese artefacto sin reconstruirlo. Cambia después un solo dato, la versión de Python, y observa si el hash del release cambia: la respuesta decide si la versión del intérprete es una entrada que hay que declarar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md)) son:

- **Cada build produce un hash distinto** — causa: fechas, orden o rutas incrustadas. Corrección: normalizar tiempo y orden; eliminar rutas.
- **El hash cambia solo en otra máquina** — causa: campo del formato dependiente del sistema. Corrección: repetir en otro sistema y fijar el campo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con un árbol sintético de 42 archivos, uno de ellos con veinte entornos variados por semilla fija, en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3), con resultados idénticos una vez fijado el campo del sistema. No se construyó ningún proyecto real, no se usó compilador, contenedor ni herramienta de build reproducible, y no se probó macOS.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Build hermético](./build-hermetico.md), [Entrada no declarada](../e/entrada-no-declarada.md), [Huella](../h/huella.md), [Normalizar](../n/normalizar.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), [SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md), [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reproducible Builds: definición](https://reproducible-builds.org/docs/definition/) — qué es un build reproducible; autoridad: proyecto Reproducible Builds.
- [Reproducible Builds: SOURCE_DATE_EPOCH](https://reproducible-builds.org/docs/source-date-epoch/) — fecha fija para el build; autoridad: proyecto Reproducible Builds.
- [Lamb y Zacchiroli, «Reproducible Builds: Increasing the Integrity of Software Supply Chains»](https://doi.org/10.1109/MS.2021.3073045) — motivación y técnicas; autoridad: IEEE Software.
- [Thompson, «Reflections on trusting trust»](https://doi.org/10.1145/358198.358210) — compiladores comprometidos; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Build hermético](./build-hermetico.md) · [Builder →](./builder.md)
