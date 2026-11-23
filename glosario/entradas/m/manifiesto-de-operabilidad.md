# Manifiesto de operabilidad

[↑ Glosario](../../README.md) · [← Manifiesto de aplicación web](./manifiesto-de-aplicacion-web.md) · [Manifiesto de respaldo →](./manifiesto-de-respaldo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Documento estructurado que declara las promesas operativas de una herramienta.

Definición de trabajo de [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md).

## Por qué importa

En [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md), el tema «Manifiesto de operabilidad» importa porque reúne las promesas para que otra persona las revise sin ejecutar.

## Cómo funciona

[SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md):

El paquete `operable-package/` contiene: `README.md` (qué es y cómo revisarlo en diez minutos), `notas.py`, `operability.json`, `tests/contract_suite.py`, `evidence/windows.txt` y `evidence/ubuntu.txt` (salida de la suite con versiones), `evidence/diferencias.md` (tabla de diferencias), `evidence/mutantes.md` (defectos inyectados y qué prueba los detecta), `evidence/humano.md` (decisiones abiertas: quién firma, qué ventana de soporte, qué se hace si el hash no coincide) y una huella SHA-256 de todos los archivos con el salto de línea fijado. Un validador comprueba el manifiesto y que cada fila observable remite a una prueba existente.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md)) son:

- **El manifiesto dice una cosa y la herramienta hace otra** — causa: el validador comprueba forma, no conducta. Corrección: remitir cada fila observable a una prueba que se ejecute.
- **La suite pasa en un sistema y falla en otro** — causa: solo se probó en el sistema de quien la escribió. Corrección: ejecutar y registrar en dos sistemas, con tabla de diferencias.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): la suite, los mutantes y el validador fueron idénticos; el hash con el modo de texto por defecto y los falsos fallos con tiempo difirieron.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Herramientas](../h/herramientas.md), [Decisión humana abierta](../d/decision-humana-abierta.md), [Prueba de contrato](../p/prueba-de-contrato.md), [Tabla de diferencias](../t/tabla-de-diferencias.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Command Line Interface Guidelines](https://clig.dev/) — prácticas de diseño de interfaces de línea de comandos; autoridad: guía de autores.
- [The Twelve-Factor App](https://12factor.net/config) — configuración, procesos y registros; autoridad: guía de autores, de uso extendido.
- [SLSA](https://slsa.dev/) — seguridad de la cadena de suministro; autoridad: OpenSSF.
- [Python: `unittest`](https://docs.python.org/3/library/unittest.html) — marco de pruebas; autoridad: documentación de Python.
- [Semantic Versioning 2.0.0](https://semver.org/) — versionado del contrato; autoridad: especificación de la comunidad.

---

[↑ Glosario](../../README.md) · [← Manifiesto de aplicación web](./manifiesto-de-aplicacion-web.md) · [Manifiesto de respaldo →](./manifiesto-de-respaldo.md)
