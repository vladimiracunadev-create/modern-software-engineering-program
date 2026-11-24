# Mínimo necesario

[↑ Glosario](../../README.md) · [← Mínimo común denominador](./minimo-comun-denominador.md) · [Mínimo privilegio →](./minimo-privilegio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

El **mínimo necesario** es el criterio de pedir solo la capacidad, con la precisión y el alcance más pequeños, sin los cuales una función falla. Es el sentido de [SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md) (permisos, sensores y capacidades del dispositivo); [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) lo aplica a la telemetría de herramientas: cada dato recogido es un riesgo que hay que justificar. Es el mismo espíritu del mínimo privilegio y de la minimización de datos, aplicado a lo que una aplicación solicita.

## Por qué importa

Cada capacidad que se pide es una superficie de ataque y una carga de confianza. Pedir menos reduce lo que puede filtrarse, abusarse o exigirse en una revisión de tienda, y aumenta la probabilidad de que la persona acepte.

## Cómo funciona

[SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md) propone una pregunta de control: **qué función falla sin la capacidad**, no qué dato podría ser útil. Dos formas de reducir:

- **Precisión:** si la función solo necesita saber que se entregó en la ciudad, la ubicación aproximada alcanza.
- **Alcance:** si solo adjunta una imagen, el selector del sistema puede evitar pedir acceso a toda la galería.

En [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), el principio se ve en la telemetría *opt-in*: se recoge solo lo que se puede justificar, con consentimiento y plazo de retención. Los pasos prácticos son enumerar las funciones, asignar a cada una la capacidad más estrecha, definir qué ocurre si se deniega o revoca, y decidir cuánto tiempo se guarda el dato.

## Ejemplo

El equipo del cliente escribe una tabla de capacidades con una fila por función ([SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md)): qué capacidad necesita, con qué precisión, cuándo la pide, qué hace si se deniega o revoca y cuánto tiempo guarda el dato. «Adjuntar foto» usa el selector del sistema o la cámara, y si se deniega, ofrece la galería. «Notificar vencimiento» usa notificaciones y, si se deniega, muestra un aviso dentro de la aplicación. «Registrar lugar de entrega» no existe: el equipo decidió que no lo necesitaba y no pidió ubicación.

## Errores y confusiones comunes

- **Pedir todos los permisos al inicio,** antes de que la función los necesite.
- **Pedir ubicación precisa cuando basta la aproximada.**
- **No definir qué ocurre al denegar:** la función se rompe en vez de degradarse.
- **Confundirlo con «pedir poco» sin criterio:** el criterio es lo que la función necesita para funcionar.

## Límites y cuándo no aplica

Una capacidad realmente necesaria no se evita: si la función es navegación, la ubicación precisa es parte del mínimo. Las reglas de permisos de cada plataforma cambian; la tabla de la clase refleja las de su fecha. Minimizar no reemplaza proteger bien los datos que sí se recogen.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Capacidad](../c/capacidad.md), [Función](../f/funcion.md), [Precisión](../p/precision.md), [Consentimiento](../c/consentimiento.md), [Identificabilidad](../i/identificabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-226 — Telemetría opt-in y privacidad en herramientas](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md), [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), [SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Android Developers, «Permissions on Android»](https://developer.android.com/guide/topics/permissions/overview) — modelo de permisos en tiempo de ejecución; autoridad: Google.
- [Android Developers, «Request location permissions»](https://developer.android.com/training/location/permissions) — ubicación aproximada y precisa; autoridad: Google.
- [Apple Developer, «Requesting access to protected resources»](https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy/requesting_access_to_protected_resources) — solicitud de acceso a recursos protegidos en iOS; autoridad: Apple.
- [W3C, «Permissions»](https://www.w3.org/TR/permissions/) — modelo de permisos de la plataforma web; autoridad: W3C.
- [OWASP, «MASVS»](https://mas.owasp.org/MASVS/) — requisitos de seguridad y privacidad para aplicaciones móviles; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Mínimo común denominador](./minimo-comun-denominador.md) · [Mínimo privilegio →](./minimo-privilegio.md)
