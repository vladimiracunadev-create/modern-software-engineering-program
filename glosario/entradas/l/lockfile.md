# Lockfile

[↑ Glosario](../../README.md) · [← Localización](./localizacion.md) · [Log →](./log.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Un **lockfile** (archivo de bloqueo) es un registro de las resoluciones concretas de dependencias para poder repetir una instalación ([SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)). [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md) precisa su contenido: registra la selección concreta y, según el formato, hashes, fuente, marcadores y grupos. Distingue el manifiesto, que declara rangos aceptables, del lock, que dice qué versiones exactas se eligieron.

## Por qué importa

Sin lock, la misma lista de dependencias puede resolver a versiones distintas mañana y producir un fallo que no estaba en tu código. Con lock, el equipo y la integración continua instalan lo mismo. Pero [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md) y [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) advierten un matiz: mejora la repetibilidad dentro de su alcance; no congela runtime, sistema operativo ni disponibilidad del índice. Cambia qué se versiona y qué se revisa.

## Cómo funciona

El resolvedor lee el manifiesto (rangos), calcula un conjunto compatible, incluye las dependencias transitivas y escribe el resultado: nombre, versión, hashes del artefacto, fuente y, según el formato, marcadores de plataforma y grupos (principal, desarrollo). Al instalar desde el lock, el gestor no vuelve a resolver: usa lo registrado y puede verificar los hashes. Se actualiza **deliberadamente** (un comando explícito) y se revisa como cambio de código, porque un cambio en el lock es un cambio de lo que corre.

La causa de sus límites es que el lock describe artefactos, no entornos: se generó en una plataforma y un intérprete concretos. [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md) muestra el caso «CI pasa y producción rompe con la misma lista».

## Ejemplo

Ilustración con pip-tools y con npm:

```bash
pip-compile --generate-hashes requirements.in      # genera requirements.txt con versiones y hashes
npm ci                                              # instala exactamente lo que dice package-lock.json
```

Para una biblioteca que se publica, el lock del repositorio sirve para sus pruebas, pero no se transmite a quien la instale ([SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md)).

## Errores y confusiones comunes

- **CI pasa y producción rompe con la misma lista.** Causa: el lock se generó en otra plataforma o versión de Python; corrección: registrar plataforma e intérprete y probar en cada plataforma soportada ([SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md)).
- **Presentarlo como garantía total.** Causa: se ignoraron origen, runtime y plataforma; corrección: documentar qué fija y qué queda variable ([SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)).
- **Editarlo a mano o regenerarlo sin revisión.** El cambio de versiones queda sin examinar.

## Límites y cuándo no aplica

Para el consumidor de una biblioteca, el lockfile no se hereda: lo decide la aplicación ([SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md)). No protege si el índice retira un paquete, ni cubre el sistema operativo. Y fijar versiones no es actualizarlas: un lock viejo congela también las vulnerabilidades conocidas, por lo que requiere revisión periódica.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bloqueo](../b/bloqueo.md), [Registro](../r/registro.md), [Resolución](../r/resolucion.md), [Alcance](../a/alcance.md), [Dependencia](../d/dependencia.md), [Dependencia directa y transitiva](../d/dependencia-directa-y-transitiva.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-111 — Resolución de dependencias y lockfiles](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), [SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md).

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

[↑ Glosario](../../README.md) · [← Localización](./localizacion.md) · [Log →](./log.md)
