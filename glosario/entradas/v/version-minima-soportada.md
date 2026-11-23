# Versión mínima soportada

[↑ Glosario](../../README.md) · [← Versión etiquetada](./version-etiquetada.md) · [Versión optimista →](./version-optimista.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Versión más antigua que el servidor acepta; por debajo, el cliente debe actualizar.

Definición de trabajo de [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md): Versión más antigua desde la que se admite actualizar directamente.

## Por qué importa

La clase donde se define, [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md), existe con este propósito: la clase existe para que planifiques cómo llega una versión a los dispositivos (tiendas, actualización automática, distribución empresarial), cuántas versiones coexisten durante cuánto tiempo y cuándo es seguro retirar algo del servidor, con fechas que salgan de la adopción medida y no del calendario.

## Cómo funciona

Según [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md):

El equipo del cliente escribe un plan de lanzamiento: publicar al 5 % en el canal automático y observar errores durante dos días; subir a 25, 50 y 100 % si no hay regresión; declarar una versión mínima soportada con un anuncio dentro de la aplicación; y retirar un campo del servidor solo cuando la telemetría muestre que menos del 1 % de las peticiones lo usa durante 14 días seguidos. Para el canal empresarial, el plan incluye avisar al administrador con 60 días de antelación y publicar una guía de despliegue.

Según [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md):

En el servidor, todos los clientes usan la versión que despliegas. En los equipos de las personas, la distribución de versiones es una **cola larga**: unos actualizan el mismo día, otros cuando abren la aplicación, otros meses después o nunca. Con un lanzamiento cada 14 días y clientes que abren la aplicación cada 1, 2, 3, 7, 14, 30, 60 o 120 días, aparecen en seis meses 22 caminos de actualización distintos y una parte apreciable de los saltos cruza tres o más versiones. Cada camino ejercita migraciones (de configuración, de datos locales, de formatos de archivo) que tienen que haberse probado. Dos estrategias reducen el área:

## Ejemplo

Ejemplo de [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) (sección «Ejemplo profesional»):

El equipo del cliente escribe un plan de lanzamiento: publicar al 5 % en el canal automático y observar errores durante dos días; subir a 25, 50 y 100 % si no hay regresión; declarar una versión mínima soportada con un anuncio dentro de la aplicación; y retirar un campo del servidor solo cuando la telemetría muestre que menos del 1 % de las peticiones lo usa durante 14 días seguidos. Para el canal empresarial, el plan incluye avisar al administrador con 60 días de antelación y publicar una guía de despliegue.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Falla la actualización desde una versión antigua** — causa: ruta no probada. Corrección: tabla de rutas y versión mínima soportada. ([SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se publicó ninguna aplicación ni se midió ninguna base instalada: las probabilidades y el paquete son construcciones del autor. La siguiente clase pregunta qué ocurre cuando el cliente trabaja sin conexión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Versión](./version.md), [Activación](../a/activacion.md), [Adopción](../a/adopcion.md), [Auto-actualización](../a/auto-actualizacion.md), [Canal de distribución](../c/canal-de-distribucion.md), [Huella de bloque](../h/huella-de-bloque.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google Play Console Help, «Release app updates with staged rollouts»](https://support.google.com/googleplay/android-developer/answer/6346149) — lanzamiento escalonado en Google Play; autoridad: Google.
- [Apple Developer, «Release a version update in phases»](https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/) — lanzamiento en fases en App Store Connect; autoridad: Apple.
- [Microsoft, «What is MSIX?»](https://learn.microsoft.com/en-us/windows/msix/overview) — formato de empaquetado y actualización para aplicaciones de Windows; autoridad: Microsoft.
- [Electron, «autoUpdater»](https://www.electronjs.org/docs/latest/api/auto-updater) — actualización automática de una aplicación de escritorio; autoridad: OpenJS Foundation.
- [The Update Framework](https://theupdateframework.io/) — marco para proteger sistemas de actualización; autoridad: TUF / Linux Foundation.

---

[↑ Glosario](../../README.md) · [← Versión etiquetada](./version-etiquetada.md) · [Versión optimista →](./version-optimista.md)
