# Resolución

[↑ Glosario](../../README.md) · [← Resiliencia demostrada](./resiliencia-demostrada.md) · [Resolución de un oráculo →](./resolucion-de-un-oraculo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

**Resolución** designa en el programa un proceso de «llegar a una respuesta concreta» con tres sentidos:

- **De dependencias** ([SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md)): el resolvedor busca una asignación de versiones que satisfaga las restricciones, retrocede ante un conflicto y aplica reglas del ecosistema.
- **De una ambigüedad o defecto** ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)): una decisión registrada, con responsable, que elimina el defecto o acepta el riesgo.
- **De rutas** ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)): el proceso de recorrer componentes, montajes y enlaces hasta el objeto real.

## Por qué importa

En dependencias, el resultado depende del orden de índices, versiones retiradas y plataforma: la misma lista puede resolver distinto. En requisitos, no resolver significa que la decisión la tomó el código. Cambia lo que se registra: la solución elegida y, en [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), quién y por qué.

## Cómo funciona

**Dependencias** ([SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md)): el resolvedor trata el problema como satisfacción de restricciones; puede existir más de una solución válida. Un manifiesto declara rangos; la resolución elige versiones concretas, que el archivo de bloqueo conserva para repetir la instalación ([SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)). Si hay conflicto, retrocede e intenta otra combinación.

**Requisitos** ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)): encontrar el defecto es la mitad; la otra mitad es decidir quién lo resuelve. Una pregunta va a quien tiene autoridad (producto para un comportamiento, privacidad para una retención), con las alternativas, sus consecuencias y una fecha. Resolver puede significar reescribir, eliminar un requisito, separar casos o aceptar el riesgo. Registrar la respuesta en el expediente evita preguntar otra vez.

**Rutas** ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)): resolver una ruta es seguir directorios, montajes y enlaces; dos rutas distintas pueden resolver al mismo objeto, y una resoluble puede estar prohibida por permisos.

## Ejemplo

```text
requisito: lib-a>=1.0, lib-b>=2.0 ; lib-b 2.0 exige lib-a<1.5
resolución: lib-a 1.4, lib-b 2.0  (única asignación compatible)
```

En requisitos: «el retraso de 30 minutos, ¿cuenta como tardío?» → decisión de producto, registrada con fecha y responsable.

## Errores y confusiones comunes

- **Un defecto reaparece tras un cambio.** Causa: la resolución no se registró o se repitió el análisis; corrección: guardar cada decisión con responsable y repetir las búsquedas tras cada cambio ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)).
- **Una actualización rompe otro proyecto.** Causa: alcance global sin control de resolución; corrección: aislar por proyecto y conservar manifiesto y bloqueo ([SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)).
- **Confundir resolver con descartar.** Aceptar el riesgo también es resolver, pero debe quedar escrito.

## Límites y cuándo no aplica

Un archivo de bloqueo conserva resoluciones para reproducibilidad, pero no garantiza disponibilidad futura, ausencia de vulnerabilidades ni equivalencia entre plataformas ([SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)). Y una resolución sin responsable ni fecha es una opinión: no cierra el defecto, solo lo oculta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Conflicto](../c/conflicto.md), [Montaje](../m/montaje.md), [Proceso](../p/proceso.md), [Alcance](../a/alcance.md), [Dependencia](../d/dependencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-111 — Resolución de dependencias y lockfiles](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.
- [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (83 clases más lo mencionan; las que más):

[SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md), [SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md), [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Apple Platform Deployment — File system basics](https://support.apple.com/guide/deployment/intro-to-file-system-apd0b895e8e1/web) — delimita el contrato técnico que debe cumplirse al razonar sobre identidad de archivos mediante rutas, enlaces, metadatos y resolución.
- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — Api pública, versiones, prereleases y compatibilidad declarada; autoridad: Semantic Versioning project.
- [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) — Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority.
- [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) — Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Argparse, importlib.metadata, subprocess y apis de automatización; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Resiliencia demostrada](./resiliencia-demostrada.md) · [Resolución de un oráculo →](./resolucion-de-un-oraculo.md)
