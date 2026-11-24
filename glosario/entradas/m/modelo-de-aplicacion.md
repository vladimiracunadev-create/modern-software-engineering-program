# Modelo de aplicación

[↑ Glosario](../../README.md) · [← Modelo de amenazas](./modelo-de-amenazas.md) · [Modelo de costo y pregunta →](./modelo-de-costo-y-pregunta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Un **modelo de aplicación** es el conjunto de reglas con que una plataforma crea, mantiene y termina el código en ejecución, y que reparte entre el sistema y el equipo las decisiones sobre proceso, ventanas e instancias. Es el sentido de [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) (modelos de aplicación móvil y de escritorio). No es un patrón de diseño ni un diagrama de dominio: es lo que la plataforma impone sobre cuándo y cómo existe tu código.

## Por qué importa

Fija qué entidades existen (proceso, ventana, instancia) y cuáles controla el sistema y cuáles el equipo. [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) distingue una restricción de diseño de un error de implementación: lo que decide el sistema (cuándo terminar un proceso, cuántas copias abrir) no se «arregla» con código; se diseña con ello.

## Cómo funciona

[SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) ofrece dos ejemplos:

- **Android.** La documentación describe que cada aplicación corre en su propio proceso con su propio usuario de sistema, que el sistema arranca el proceso cuando un componente lo necesita y que puede terminarlo cuando necesita memoria. El equipo no controla cuándo muere el proceso.
- **Escritorio con un marco como Electron.** Hay un proceso principal que gestiona ventanas y procesos de interfaz que las dibujan. Aquí el equipo controla más: puede permitir varias ventanas o varias instancias.

De ahí el método de la clase: una **tabla de supuestos** con una fila por modelo (teléfono, escritorio, ventana dividida) y una columna por supuesto (proceso permanente, copia única, ancho mínimo, estado en memoria). Cada celda es «se cumple», «no se cumple» o «depende», con su fuente (documentación de la plataforma o medición propia). Lo importante no es memorizar cada modelo, sino distinguir qué decide el equipo y qué decide el sistema.

## Ejemplo

El cliente de la plataforma de entregas es el caso conductor de la [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md). En [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) deja la tabla de supuestos que cada modelo rompe; [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) mide qué guardar en cada transición del ciclo de vida, [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) compara formas de construir, [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md) decide dónde vive el estado y [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) qué ocurre al editar sin conexión. Cambiar una sola decisión, permitir o prohibir la segunda instancia, obliga a revisar qué más se mueve.

## Errores y confusiones comunes

- **Suponer un proceso permanente** en un teléfono: el sistema puede terminarlo.
- **Tratar la terminación del proceso como un error del programa.**
- **Aplicar el modelo de escritorio al móvil** (estado solo en memoria, una segunda ventana inesperada).
- **Confundirlo con el enfoque de construcción:** el modelo es lo que la plataforma impone; el enfoque es cómo el equipo produce el cliente.

## Límites y cuándo no aplica

Las reglas son las de cada plataforma y versión, y cambian; la tabla de supuestos fecha su fuente. Para servicios de servidor el concepto se sustituye por el de ciclo de vida del proceso de despliegue. No sustituye medir el comportamiento real en el dispositivo.

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
