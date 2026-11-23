# Canal de distribución

[↑ Glosario](../../README.md) · [← Canal de coordinación](./canal-de-coordinacion.md) · [Canario →](./canario.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Vía por la que una versión llega al dispositivo (tienda con actualización automática o manual, distribución empresarial o paquete propio) y que fija quién decide la fecha.

Definición de trabajo de [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md).

## Por qué importa

La clase donde se define, [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md), existe con este propósito: la clase existe para que planifiques cómo llega una versión a los dispositivos (tiendas, actualización automática, distribución empresarial), cuántas versiones coexisten durante cuánto tiempo y cuándo es seguro retirar algo del servidor, con fechas que salgan de la adopción medida y no del calendario.

## Cómo funciona

[SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md):

El equipo del cliente escribe un plan de lanzamiento: publicar al 5 % en el canal automático y observar errores durante dos días; subir a 25, 50 y 100 % si no hay regresión; declarar una versión mínima soportada con un anuncio dentro de la aplicación; y retirar un campo del servidor solo cuando la telemetría muestre que menos del 1 % de las peticiones lo usa durante 14 días seguidos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md)) son:

- **Un grupo no puede entregar tras retirar un campo** — causa: la fecha de retirada ignoró a quienes siguen en versiones viejas. Corrección: retirar por fracción de uso y versión mínima anunciada.
- **Una corrección urgente tarda semanas en llegar a la mayoría** — causa: el canal es lento y se supuso uno rápido. Corrección: medir la adopción por canal y planear en consecuencia.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se publicó ninguna aplicación ni se midió ninguna base instalada: las probabilidades y el paquete son construcciones del autor. La siguiente clase pregunta qué ocurre cuando el cliente trabaja sin conexión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Paquete](../p/paquete.md), [Versión](../v/version.md), [Adopción](../a/adopcion.md), [Huella de bloque](../h/huella-de-bloque.md), [Lanzamiento por fases](../l/lanzamiento-por-fases.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md).

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

[↑ Glosario](../../README.md) · [← Canal de coordinación](./canal-de-coordinacion.md) · [Canario →](./canario.md)
