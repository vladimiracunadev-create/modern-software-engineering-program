# Lanzamiento por fases

[↑ Glosario](../../README.md) · [← Language server protocol](./language-server-protocol.md) · [Lápida →](./lapida.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Publicación de una versión a una fracción creciente de la base instalada para limitar el efecto de un error.

Definición de trabajo de [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md).

## Por qué importa

En [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md), el tema «Lanzamiento por fases» importa porque publicar a un porcentaje limita el daño de un error que se descubre tarde.

## Cómo funciona

Según [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md), en la sección «Lanzamiento por fases»:

Las tiendas permiten un lanzamiento escalonado: primero una fracción pequeña, luego más. Si la fracción pequeña revela un error grave, se detiene antes de llegar a todos. Es una red de seguridad, no una prueba: solo ve los fallos que aparecen en esa fracción y en el tiempo de espera. El lanzamiento por fases necesita una forma de detectar fallos, como errores y cierres inesperados por versión.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md):

El equipo del cliente escribe un plan de lanzamiento: publicar al 5 % en el canal automático y observar errores durante dos días; subir a 25, 50 y 100 % si no hay regresión; declarar una versión mínima soportada con un anuncio dentro de la aplicación; y retirar un campo del servidor solo cuando la telemetría muestre que menos del 1 % de las peticiones lo usa durante 14 días seguidos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un error se descubre tras llegar al 100 % de la base** — causa: lanzamiento sin fases ni métricas de parada. Corrección: lanzamiento por fases con errores y cierres por versión. ([SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se publicó ninguna aplicación ni se midió ninguna base instalada: las probabilidades y el paquete son construcciones del autor. La siguiente clase pregunta qué ocurre cuando el cliente trabaja sin conexión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Efecto](../e/efecto.md), [Versión](../v/version.md), [Adopción](../a/adopcion.md), [Canal de distribución](../c/canal-de-distribucion.md), [Huella de bloque](../h/huella-de-bloque.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

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

[↑ Glosario](../../README.md) · [← Language server protocol](./language-server-protocol.md) · [Lápida →](./lapida.md)
