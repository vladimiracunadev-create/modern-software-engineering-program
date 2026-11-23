# Tabla de diferencias

[↑ Glosario](../../README.md) · [← Tabla amenaza-mecanismo-prueba](./tabla-amenaza-mecanismo-prueba.md) · [Tablas de decisión →](./tablas-de-decision.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Registro de qué salidas cambian entre plataformas y por qué.

Definición de trabajo de [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md).

## Por qué importa

La clase donde se define, [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md), existe con este propósito: el proyecto existe para entregar una herramienta de línea de comandos con un paquete que otra persona pueda revisar sin ejecutar nada: contrato observable, configuración, códigos, ciclo de vida, entrega y privacidad declarados, con pruebas de contrato ejecutadas en dos sistemas y una lista honesta de lo que ningún manifiesto puede probar.

## Cómo funciona

Según [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md):

Ejecutar la suite en Windows y en Ubuntu y publicar solo «pasa» esconde lo interesante. Lo que se registra es una **tabla de diferencias**: qué salida cambió y por qué. En este proyecto, el hash de un archivo escrito con el modo de texto por defecto difirió (`a5b38bad23415ba9` en Windows y `9105e05b084e0394` en Ubuntu) porque Windows traduce los saltos de línea; con `newline` fijado a `\n` y la escritura en bytes, ambos dieron `9105e05b084e0394`. La tabla convierte una sorpresa de producción en una decisión de diseño documentada.

Según [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md):

El paquete `operable-package/` contiene: `README.md` (qué es y cómo revisarlo en diez minutos), `notas.py`, `operability.json`, `tests/contract_suite.py`, `evidence/windows.txt` y `evidence/ubuntu.txt` (salida de la suite con versiones), `evidence/diferencias.md` (tabla de diferencias), `evidence/mutantes.md` (defectos inyectados y qué prueba los detecta), `evidence/humano.md` (decisiones abiertas: quién firma, qué ventana de soporte, qué se hace si el hash no coincide) y una huella SHA-256 de todos los archivos con el salto de línea fijado. Un validador comprueba el manifiesto y que cada fila observable remite a una prueba existente.

## Ejemplo

Ejemplo de [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) (sección «Ejemplo profesional»):

El paquete `operable-package/` contiene: `README.md` (qué es y cómo revisarlo en diez minutos), `notas.py`, `operability.json`, `tests/contract_suite.py`, `evidence/windows.txt` y `evidence/ubuntu.txt` (salida de la suite con versiones), `evidence/diferencias.md` (tabla de diferencias), `evidence/mutantes.md` (defectos inyectados y qué prueba los detecta), `evidence/humano.md` (decisiones abiertas: quién firma, qué ventana de soporte, qué se hace si el hash no coincide) y una huella SHA-256 de todos los archivos con el salto de línea fijado. Un validador comprueba el manifiesto y que cada fila observable remite a una prueba existente.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La suite pasa en un sistema y falla en otro** — causa: solo se probó en el sistema de quien la escribió. Corrección: ejecutar y registrar en dos sistemas, con tabla de diferencias. ([SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): la suite, los mutantes y el validador fueron idénticos; el hash con el modo de texto por defecto y los falsos fallos con tiempo difirieron.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Plataforma](../p/plataforma.md), [Registro](../r/registro.md), [Decisión humana abierta](../d/decision-humana-abierta.md), [Manifiesto de operabilidad](../m/manifiesto-de-operabilidad.md), [Prueba de contrato](../p/prueba-de-contrato.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-071](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md), [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md).

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

[↑ Glosario](../../README.md) · [← Tabla amenaza-mecanismo-prueba](./tabla-amenaza-mecanismo-prueba.md) · [Tablas de decisión →](./tablas-de-decision.md)
