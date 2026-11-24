# Revocación

[↑ Glosario](../../README.md) · [← Revisor de coherencia](./revisor-de-coherencia.md) · [RFC →](./rfc.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

La **revocación** es la retirada de algo concedido. El sentido principal de [SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md) (permisos, sensores y capacidades del dispositivo) es la retirada de un permiso concedido, normalmente desde los ajustes del sistema y sin que la aplicación participe. En seguridad de claves ([SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md)) es la declaración de que una clave o certificado ya no debe aceptarse. Ambos sentidos comparten la estructura: concedido en el pasado, retirado después, y el que verifica debe enterarse.

## Por qué importa

Un permiso comprobado una vez al iniciar la sesión puede dejar de valer a los diez minutos ([SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md)). Y una clave filtrada sigue funcionando hasta que alguien la declara inválida. La decisión de diseño es cuándo y cómo se comprueba.

## Cómo funciona

**Permisos de dispositivo ([SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md)).** La revocación ocurre fuera de la aplicación y puede llegar en cualquier momento. Comprobar el permiso al iniciar la sesión y asumirlo después produce usos tras la revocación. Comprobar en cada uso lo evita y cuesta una consulta; comprobar periódicamente reduce el costo y deja una ventana. La tolerancia de esa ventana es una decisión de privacidad.

**Claves ([SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md)).** Las claves se pierden, se filtran o caducan. La *rotación* es el cambio planificado; la *revocación*, la declaración de que una clave ya no debe usarse. Una rotación sólida se **declara antes de necesitarla**, firmada con la clave vigente, de modo que los clientes aprendan la clave nueva por la cadena de confianza anterior. Una revocación necesita llegar a los clientes, y entre el robo de la clave y la llegada de la revocación hay una ventana en la que el atacante puede firmar. [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) la aplica a dispositivos: retirar una clave o certificado para que el servidor deje de aceptarlo.

## Ejemplo

Ilustración propia de permisos: una aplicación de entregas guarda la ubicación solo mientras la usa. La persona revoca el permiso desde los ajustes; en el siguiente uso, la comprobación devuelve «denegado» y la función ofrece alternativa en vez de fallar. De claves: un dispositivo robado se revoca en el servidor; mientras la lista de revocación no llega a los clientes, hay una ventana.

## Errores y confusiones comunes

- **Comprobar el permiso una vez y asumirlo.**
- **No definir qué hace la función al revocarse.**
- **Confundir revocación con caducidad:** la caducidad ocurre sola; la revocación es una acción.
- **Creer que revocar equivale a borrar los datos ya obtenidos.**

## Límites y cuándo no aplica

La revocación no deshace lo ya hecho: las firmas anteriores y los datos ya recogidos siguen existiendo. La ventana entre el compromiso y la revocación no se elimina, solo se acota. Para clientes sin conexión, la revocación no llega hasta que se reconectan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ajuste](../a/ajuste.md), [Certificado](../c/certificado.md), [Permiso](../p/permiso.md), [Capacidad](../c/capacidad.md), [Clave de flota](../c/clave-de-flota.md), [Derivación de claves](../d/derivacion-de-claves.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (14 clases más lo mencionan; las que más):

[SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), [SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md), [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md).

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

[↑ Glosario](../../README.md) · [← Revisor de coherencia](./revisor-de-coherencia.md) · [RFC →](./rfc.md)
