# Capacidad

[↑ Glosario](../../README.md) · [← Capa de cascada](./capa-de-cascada.md) · [Capacidad de mejora →](./capacidad-de-mejora.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Función del dispositivo que el sistema protege (ubicación, cámara, notificaciones, archivos) y que exige una autorización.

Definición de trabajo de [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md): Resultado que un sistema produce bajo condiciones declaradas.
- En [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md): Operación cuya disponibilidad puede comprobarse sin asumirla por nombre.
- En [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md): Referencia no falsificable a un recurso (por ejemplo, un descriptor de directorio) que permite operar sobre él.
- En [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md): Operación comprobable que una plataforma ofrece al adaptador.

## Por qué importa

En [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md), el tema «Mínimo necesario» importa porque cada capacidad que se pide es una superficie de ataque y una carga de confianza.

## Cómo funciona

Según [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md):

Pedir menos reduce lo que puede filtrarse, abusarse o exigirse en una revisión de tienda. Si la función solo necesita saber que se entregó en la ciudad, la ubicación aproximada alcanza; si solo adjunta una imagen, el selector del sistema puede evitar pedir acceso a toda la galería. La pregunta es qué función falla sin la capacidad, no qué dato podría ser útil.

Según [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md):

El equipo del cliente escribe una tabla de capacidades con una fila por función: qué capacidad necesita, con qué precisión, cuándo la pide, qué hace si se deniega o revoca y cuánto tiempo guarda el dato. «Adjuntar foto» usa el selector del sistema o la cámara, y si se deniega, ofrece la galería. «Notificar vencimiento» usa notificaciones y, si se deniega, muestra un aviso dentro de la aplicación. «Registrar lugar de entrega» no existe: el equipo decidió que no lo necesitaba y no pidió ubicación. Cada fila tiene una prueba por estado del permiso.

## Ejemplo

Ejemplo de [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md) (sección «Ejemplo profesional»):

El equipo del cliente escribe una tabla de capacidades con una fila por función: qué capacidad necesita, con qué precisión, cuándo la pide, qué hace si se deniega o revoca y cuánto tiempo guarda el dato. «Adjuntar foto» usa el selector del sistema o la cámara, y si se deniega, ofrece la galería. «Notificar vencimiento» usa notificaciones y, si se deniega, muestra un aviso dentro de la aplicación. «Registrar lugar de entrega» no existe: el equipo decidió que no lo necesitaba y no pidió ubicación. Cada fila tiene una prueba por estado del permiso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La revisión de la tienda rechaza el permiso solicitado** — causa: se pidió una capacidad que ninguna función usa. Corrección: eliminar capacidades sin función que las necesite. ([SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md))
- **el objetivo dice “construir el portal”** — causa: se formuló una solución como necesidad. Corrección: reescribe capacidad, persona, condición de éxito y condición de fracaso. ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md))
- **El primer intento exige administrador** — causa: se trató el privilegio como comodidad. Corrección: observar primero sin elevación y justificar cada capacidad adicional. ([SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La pregunta es qué función falla sin la capacidad, no qué dato podría ser útil. ([SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md))
- Porque la persona decide sin contexto, se piden capacidades que quizá nunca se usen y cada una añade superficie. ([SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Adaptador](../a/adaptador.md), [Autorización](../a/autorizacion.md), [Candidato](./candidato.md), [Condición](./condicion.md), [ABI](../a/abi.md), [API](../a/api.md).
- **Se confunde con:** Aun así, una capacidad presente puede estar bloqueada por permisos o políticas; detectar no equivale a autorizar.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (254 clases más lo mencionan; las que más):

[SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md), [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md), [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

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

[↑ Glosario](../../README.md) · [← Capa de cascada](./capa-de-cascada.md) · [Capacidad de mejora →](./capacidad-de-mejora.md)
