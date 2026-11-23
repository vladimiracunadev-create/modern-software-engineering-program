# Instancia

[↑ Glosario](../../README.md) · [← Instalación atómica](./instalacion-atomica.md) · [Instancia por petición →](./instancia-por-peticion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Copia de la aplicación en ejecución; un modelo puede permitir varias a la vez o una sola.

Definición de trabajo de [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md): Módulo con su memoria y sus importaciones ya enlazadas.

## Por qué importa

En [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), el tema «Instancia» importa porque permitir varias copias convierte cada archivo local en un recurso compartido con varios escritores.

## Cómo funciona

Según [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), en la sección «Instancia»:

Un escritorio permite abrir la misma aplicación varias veces salvo que se prohíba; un teléfono normalmente presenta una sola instancia. Cuando hay varias, el archivo del borrador tiene dos escritores que no se conocen. Las salidas son tres: aceptar la competencia y detectarla, coordinar con un bloqueo o impedir la segunda copia. Electron ofrece un mecanismo para obtener un bloqueo de instancia única, y cada solución añade una regla que hay que explicar a quien usa la aplicación.

## Ejemplo

Ejemplo de [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) (sección «Ejemplo profesional»):

El equipo del cliente de entregas escribe una tabla de supuestos con una fila por modelo (teléfono, escritorio, ventana dividida) y una columna por supuesto: proceso permanente, copia única, ancho mínimo, estado en memoria. Cada celda es «se cumple», «no se cumple» o «depende», con la fuente que lo respalda (la documentación de la plataforma o una medición propia). Las celdas «depende» se vuelven pruebas. La decisión de arquitectura nace de la tabla: guardar el borrador en el disco en cada pausa, impedir la segunda instancia en el escritorio y diseñar a 320 píxeles primero.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Dos ventanas guardan el borrador y una de las ediciones se pierde** — causa: dos escritores sin coordinación sobre el mismo archivo. Corrección: bloqueo, instancia única o fusión con detección de conflicto. ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md))
- **La aplicación se comporta bien en el equipo de desarrollo y mal en uso real** — causa: el equipo de desarrollo casi nunca recupera memoria ni abre varias copias. Corrección: forzar el arranque en frío y la segunda instancia en las pruebas. ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un escritorio permite abrir la misma aplicación varias veces salvo que se prohíba; un teléfono normalmente presenta una sola instancia. ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Importación](./importacion.md), [Modelo](../m/modelo.md), [Módulo](../m/modulo.md), [Arranque en frío](../a/arranque-en-frio.md), [Capacidad](../c/capacidad.md), [Combustible](../c/combustible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (63 clases más lo mencionan; las que más):

[SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Electron, «app» (instancia única)](https://www.electronjs.org/docs/latest/api/app) — bloqueo de instancia única de la aplicación; autoridad: OpenJS Foundation.
- [Android Developers, «Application fundamentals»](https://developer.android.com/guide/components/fundamentals) — procesos, sandbox y componentes de una aplicación Android; autoridad: Google.
- [Apple Developer, «Managing your app's life cycle»](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) — estados de una aplicación en iOS y qué hace el sistema entre ellos; autoridad: Apple.
- [Electron, «Process Model»](https://www.electronjs.org/docs/latest/tutorial/process-model) — proceso principal y procesos de interfaz de una aplicación de escritorio; autoridad: OpenJS Foundation.
- [Microsoft, «Windows app lifecycle»](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/applifecycle/applifecycle) — ciclo de vida de aplicaciones Windows con el SDK de aplicaciones; autoridad: Microsoft.

---

[↑ Glosario](../../README.md) · [← Instalación atómica](./instalacion-atomica.md) · [Instancia por petición →](./instancia-por-peticion.md)
