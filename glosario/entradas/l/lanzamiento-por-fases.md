# Lanzamiento por fases

[↑ Glosario](../../README.md) · [← Language server protocol](./language-server-protocol.md) · [Lápida →](./lapida.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

El **lanzamiento por fases** (*phased* o *staged release*) es la publicación de una versión a una fracción creciente de la base instalada para limitar el efecto de un error. Es el sentido de [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) (actualizaciones, tiendas y distribución empresarial), donde las tiendas de aplicaciones lo ofrecen como lanzamiento escalonado. Es el mismo principio que el despliegue por etapas de flotas de dispositivos, aplicado al canal de una tienda.

## Por qué importa

Publicar a un porcentaje limita el daño de un error que se descubre tarde. En aplicaciones de cliente no se puede «volver atrás» una versión ya instalada con un botón, así que reducir cuántas personas la reciben antes de saber si funciona es la protección principal.

## Cómo funciona

Las tiendas permiten primero una fracción pequeña y luego más. Si la fracción pequeña revela un error grave, se detiene antes de llegar a todos. [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) precisa su naturaleza: es una **red de seguridad, no una prueba**. Solo ve los fallos que aparecen en esa fracción y en el tiempo de espera.

Y necesita una forma de detectar fallos: errores y cierres inesperados por versión. Sin esa señal, la fase siguiente avanza a ciegas. Las condiciones de avance (porcentaje, tiempo de observación, métrica que debe mantenerse) se escriben antes de publicar.

## Ejemplo

El plan de lanzamiento del cliente en [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md): publicar al 5 % en el canal automático y observar errores durante dos días; subir a 25, 50 y 100 % si no hay regresión; declarar una versión mínima soportada con un anuncio dentro de la aplicación; y retirar un campo del servidor solo cuando la telemetría muestre que menos del 1 % de las peticiones lo usa durante 14 días seguidos.

## Errores y confusiones comunes

- **Descubrir un error tras llegar al 100 % de la base:** el lanzamiento no tenía fases ni métricas de parada; la corrección es lanzar por fases con errores y cierres por versión ([SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md)).
- **Creer que el 5 % equivale a probar:** solo ve lo que ocurre en esa fracción durante ese tiempo.
- **Avanzar por calendario** sin mirar las métricas.
- **Confundirlo con una bandera de funcionalidad:** el lanzamiento por fases controla quién *recibe la versión*; la bandera, quién *ve la función* ya instalada.

## Límites y cuándo no aplica

No ayuda con defectos que dependen de un subconjunto no representado en la fracción (un dispositivo o región) ni con errores que tardan en aparecer. Las personas que reciben la versión primero no son una muestra aleatoria si el canal es de adopción rápida. Una corrección urgente de seguridad puede obligar a acelerar las fases. La retirada de campos del servidor, como en el ejemplo, depende de que la versión mínima soportada esté definida.

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
