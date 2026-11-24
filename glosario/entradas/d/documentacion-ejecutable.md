# Documentación ejecutable

[↑ Glosario](../../README.md) · [← Documentación como código](./documentacion-como-codigo.md) · [Documentación viva →](./documentacion-viva.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

La **documentación ejecutable** es documentación cuyos **ejemplos se ejecutan y se comprueban automáticamente** ([SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md)). En [SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md), los ejemplos se prueban contra la **versión publicada** del producto y usan **datos sintéticos**. La idea es que un ejemplo que deja de funcionar haga fallar una verificación, y no que un lector lo descubra copiándolo. No es una herramienta concreta: pueden ser *doctests*, pruebas que extraen los bloques de código de los documentos, cuadernos ejecutados en integración continua o ejemplos mantenidos como pruebas.

## Por qué importa

Los ejemplos son lo primero que alguien copia. Un ejemplo roto por un cambio de versión cuesta más que su ausencia: el lector no sabe si se equivocó él o la documentación. [SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md) advierte además que copiar fragmentos sin sus *imports* o sin limpieza convierte la documentación en deuda. La decisión que cambia es cuándo se considera terminado un cambio de API: cuando además de la implementación, cambian los ejemplos y la verificación en verde confirma que los documentos siguen siendo ciertos.

## Cómo funciona

Para que funcione de verdad, la verificación sigue estas reglas:

- **Contra la versión publicada.** Un ejemplo que solo funciona con el código del repositorio no sirve a quien instaló el paquete; se prueba contra lo que se publica.
- **Datos sintéticos.** No dependen de datos reales, secretos ni servicios externos, de modo que son reproducibles y seguros de publicar.
- **Ejemplos completos.** Con sus *imports* y su limpieza, para que se puedan copiar y ejecutar tal cual.
- **Un tipo de documento por necesidad.** [SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md) distingue **tutorial** (aprender), **how-to** (resolver una tarea), **explicación** (entender por qué) y **referencia** (consultar detalles). Cada uno resuelve una necesidad distinta, y los ejemplos ejecutables sirven sobre todo a los dos primeros.

La integración continua ejecuta la verificación en cada cambio. [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) trata un caso emparentado: la generación asistida de pruebas, documentación y migraciones, donde la documentación producida también debe poder comprobarse.

## Ejemplo

Un SDK documenta su función `choose_next`. En lugar de un bloque de texto, el ejemplo se escribe de modo que pueda ejecutarse:

```python
>>> from engineering_sdk import choose_next
>>> casos = [{"id": 1, "prioridad": 2}, {"id": 2, "prioridad": 1}]
>>> choose_next(casos)["id"]
2
```

Un paso de integración continua ejecuta estos ejemplos (con `python -m doctest` o con una extensión que lea los bloques del documento) en un entorno donde se ha instalado la versión publicada. Si una versión nueva cambia el resultado, el ejemplo falla antes de que lo haga el lector. Los datos son inventados, así que el ejemplo no expone nada sensible.

## Errores y confusiones comunes

- **Ejemplos sin imports ni limpieza.** El lector no puede ejecutarlos y la documentación acumula deuda.
- **Probar contra el repositorio y no contra lo publicado.** Los ejemplos pasan, pero el paquete que se instala falla.
- **Una sola forma de documento.** Un tutorial no sustituye a la referencia, ni al revés.
- **Usar datos reales.** Complica la reproducción y puede filtrar información.

## Límites y cuándo no aplica

Ejecutar ejemplos garantiza que **funcionan**, no que se **entienden**: una documentación puede pasar todas las verificaciones y seguir siendo confusa. Una evaluación interna de la experiencia de desarrollo no sustituye investigación diversa ni soporte real ([SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md)). Hay contenido difícil de ejecutar automáticamente (flujos con servicios externos, interfaces gráficas), que exige otras formas de verificación. Y para documentación de decisiones o de conceptos sin código, el término no aplica.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Versión](../v/version.md), [Cuarentena](../c/cuarentena.md), [Diseño de errores](./diseno-de-errores.md), [Feedback, telemetría y privacidad](../f/feedback-telemetria-y-privacidad.md), [Journey de desarrollador](../j/journey-de-desarrollador.md), [Migración](../m/migracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-118 — Diseño de experiencia para desarrolladores](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.
- [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md).

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

[↑ Glosario](../../README.md) · [← Documentación como código](./documentacion-como-codigo.md) · [Documentación viva →](./documentacion-viva.md)
