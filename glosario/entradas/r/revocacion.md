# Revocación

[↑ Glosario](../../README.md) · [← Revisor de coherencia](./revisor-de-coherencia.md) · [RFC →](./rfc.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Retirada de un permiso concedido, normalmente desde los ajustes del sistema y sin que la aplicación participe.

Definición de trabajo de [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md): Declaración de que una clave ya no debe aceptarse.
- En [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md): Retirada de una clave o certificado para que el servidor deje de aceptarlo.

## Por qué importa

En [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md), el tema «Revocación y comprobación en el uso» importa porque un permiso comprobado una vez al iniciar la sesión puede dejar de valer a los diez minutos.

## Cómo funciona

Según [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md):

La revocación ocurre fuera de la aplicación y puede llegar en cualquier momento. Comprobar el permiso al iniciar la sesión y asumirlo después produce usos tras la revocación. Comprobar en cada uso lo evita y cuesta una consulta; comprobar periódicamente reduce el coste y deja una ventana. La tolerancia de esa ventana es una decisión de privacidad.

Según [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md):

Las claves se pierden, se filtran o caducan. La **rotación** es el cambio planificado de la clave; la **revocación**, la declaración de que una clave ya no debe usarse. Una rotación sólida se **declara antes de necesitarla**, firmada con la clave vigente, de modo que los clientes aprendan la clave nueva por la cadena de confianza anterior. Una revocación necesita llegar a los clientes, y entre el robo de la clave y la llegada de la revocación hay una ventana en la que el atacante puede firmar.

## Ejemplo

Ejemplo de [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) (sección «Ejemplo profesional»):

La API de entregas publica un manifiesto (`release.json`) con nombre, versión, número de secuencia y las huellas del artefacto, del SBOM y de la procedencia, firmado con Ed25519. El cliente de línea de órdenes incorpora la clave pública en cada versión que él mismo distribuye y recuerda la mayor secuencia vista; antes de instalar calcula la huella del archivo descargado, comprueba la firma del manifiesto con la clave incorporada, comprueba el nombre, rechaza una secuencia inferior a la recordada y falla cerrado ante cualquier discrepancia.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La cámara falla con un error críptico a mitad de la sesión** — causa: se comprobó el permiso solo al iniciar. Corrección: comprobar en el uso y manejar la revocación. ([SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md))
- **No se puede retirar una clave comprometida** — causa: sin revocación. Corrección: lista de revocación consultada por el servidor y rotación planificada. ([SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Y supone que la revocación se aplica de forma instantánea al consultar, algo que depende de la plataforma. ([SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md))

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
