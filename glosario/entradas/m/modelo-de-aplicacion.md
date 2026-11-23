# Modelo de aplicación

[↑ Glosario](../../README.md) · [← Modelo de amenazas](./modelo-de-amenazas.md) · [Modelo de costo y pregunta →](./modelo-de-costo-y-pregunta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Conjunto de reglas con que una plataforma crea, mantiene y termina el código en ejecución y reparte entre sistema y equipo las decisiones sobre proceso, ventanas e instancias.

Definición de trabajo de [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md).

## Por qué importa

En [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), el tema «Modelo de aplicación» importa porque fija qué entidades existen (proceso, ventana, instancia) y cuáles controla el sistema y cuáles el equipo.

## Cómo funciona

Según [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), en la sección «Modelo de aplicación»:

Un modelo de aplicación es el conjunto de reglas con que una plataforma crea, mantiene y termina el código en ejecución. En Android, la documentación describe que cada aplicación corre en su propio proceso con su propio usuario de sistema, que el sistema arranca el proceso cuando un componente lo necesita y que puede terminarlo cuando necesita memoria. En un escritorio con un marco como Electron hay un proceso principal que gestiona ventanas y procesos de interfaz que las dibujan. Lo importante no es memorizar cada modelo sino distinguir qué decide el equipo y qué decide el sistema: lo segundo es una restricción de diseño, no un error de implementación.

## Ejemplo

Ejemplo de [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) (sección «Caso conductor»):

El cliente de la plataforma de entregas de tareas es el caso conductor de la [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md). Esta clase deja el primer artefacto: la tabla de supuestos que cada modelo de aplicación rompe. `SE-254` mide qué hace falta guardar en cada transición del ciclo de vida, `SE-255` compara formas de construir el cliente, `SE-256` decide dónde vive el estado y `SE-260` qué ocurre cuando dos dispositivos editan sin conexión. Cambia después una sola decisión, permitir o prohibir la segunda instancia, y revisa qué artefactos hay que tocar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se afirma «funciona en móvil» tras ejecutar la versión web en un navegador estrecho** — causa: se confunde ancho de ventana con modelo de aplicación. Corrección: declarar qué supuestos del modelo móvil se probaron y cuáles no. ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún dispositivo, sistema operativo móvil ni persona: la recuperación de memoria, la geometría de la barra y la frecuencia de dos copias son construcciones del autor. La siguiente clase pregunta qué debe guardarse en cada transición del ciclo de vida.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Instancia](../i/instancia.md), [Plataforma](../p/plataforma.md), [Proceso](../p/proceso.md), [Arranque en frío](../a/arranque-en-frio.md), [Reflujo](../r/reflujo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Android Developers, «Application fundamentals»](https://developer.android.com/guide/components/fundamentals) — procesos, sandbox y componentes de una aplicación Android; autoridad: Google.
- [Apple Developer, «Managing your app's life cycle»](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) — estados de una aplicación en iOS y qué hace el sistema entre ellos; autoridad: Apple.
- [Electron, «Process Model»](https://www.electronjs.org/docs/latest/tutorial/process-model) — proceso principal y procesos de interfaz de una aplicación de escritorio; autoridad: OpenJS Foundation.
- [Electron, «app» (instancia única)](https://www.electronjs.org/docs/latest/api/app) — bloqueo de instancia única de la aplicación; autoridad: OpenJS Foundation.
- [Microsoft, «Windows app lifecycle»](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/applifecycle/applifecycle) — ciclo de vida de aplicaciones Windows con el SDK de aplicaciones; autoridad: Microsoft.

---

[↑ Glosario](../../README.md) · [← Modelo de amenazas](./modelo-de-amenazas.md) · [Modelo de costo y pregunta →](./modelo-de-costo-y-pregunta.md)
