# Activación

[↑ Glosario](../../README.md) · [← Acotar](./acotar.md) · [Activación y ejecutable explícito →](./activacion-y-ejecutable-explicito.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Operación única que hace que el sistema use la versión nueva.

Definición de trabajo de [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md).

## Por qué importa

La clase donde se define, [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), existe con este propósito: la clase existe para que decidas cómo llega tu software al equipo de otra persona, qué ocurre cuando la instalación o la actualización se interrumpe y cuántas versiones distintas estarán en uso al mismo tiempo.

## Cómo funciona

Según [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md):

La verificación ocurre sobre el directorio preparado y antes de la activación: se calcula la huella de cada archivo y se compara con el manifiesto firmado (`SE-473`). Si algo no coincide (una descarga corrupta, un byte alterado), el directorio se descarta y la instalación actual no se ha tocado. Tras activar, la aplicación arranca una comprobación de humo; si falla, se vuelve a apuntar a la versión anterior, que se conserva hasta que la nueva ha funcionado durante un plazo. La migración de datos y configuración del usuario es el punto delicado: debe ser **reversible** o hacerse sobre una copia, porque una migración que reescribe el archivo de configuración con un formato que la versión anterior no lee impide el retroceso (el mismo problema de `SE-476`, ahora sin servidor).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md):

El procedimiento de actualización de `entregas-cli` descarga el paquete y su manifiesto firmado a un directorio temporal dentro de la misma partición que la instalación, verifica la firma con la clave incorporada y la secuencia, calcula la huella de cada archivo, descomprime en `versiones/2.0.0/`, ejecuta la migración de configuración sobre una copia y una comprobación de humo (`entregas --version` y una subida de prueba a un entorno de ensayo) y cambia el puntero `actual` con un renombrado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El programa no arranca tras una actualización interrumpida** — causa: archivos de dos versiones. Corrección: directorio nuevo y activación atómica. ([SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron cuatro experimentos: una inyección de fallos con archivos reales en un directorio temporal (resultado idéntico en Windows 11 con CPython 3.12.9 y en Ubuntu bajo WSL2 con 3.12.3) y una simulación de 20 000 clientes con semilla fija.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Versión](../v/version.md), [Auto-actualización](./auto-actualizacion.md), [Instalación atómica](../i/instalacion-atomica.md), [Sesgo de versiones](../s/sesgo-de-versiones.md), [Versión mínima soportada](../v/version-minima-soportada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [POSIX: rename()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html) — reemplazo atómico; autoridad: The Open Group.
- [Python: os.replace](https://docs.python.org/3/library/os.html#os.replace) — renombrado con reemplazo; autoridad: documentación de Python.
- [Microsoft: MoveFileExW](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefileexw) — reemplazo de archivos en Windows; autoridad: documentación de Microsoft.
- [The Update Framework](https://theupdateframework.io/specification/) — metadatos firmados con secuencia y caducidad; autoridad: proyecto TUF, CNCF.
- [PEP 427: wheel](https://peps.python.org/pep-0427/) — formato de distribución de paquetes de Python; autoridad: Python Enhancement Proposals.

---

[↑ Glosario](../../README.md) · [← Acotar](./acotar.md) · [Activación y ejecutable explícito →](./activacion-y-ejecutable-explicito.md)
