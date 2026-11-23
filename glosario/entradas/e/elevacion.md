# Elevación

[↑ Glosario](../../README.md) · [← Elemento semántico](./elemento-semantico.md) · [Elicitación →](./elicitacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Cambio a un contexto con más autoridad.

Definición de trabajo de [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md).

## Por qué importa

En [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md), el tema «Elevación» importa porque crea un contexto más poderoso

## Cómo funciona

Según [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md):

UAC separa el uso cotidiano de un token elevado; aceptar una elevación amplía la autoridad del proceso completo. La documentación de Access Control detalla el modelo. El kit de diagnóstico multiplataforma evita “traducir” ACL de Windows a permisos POSIX como si fueran equivalentes.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md):

Un servicio fue instalado por una cuenta administrativa y su configuración quedó inaccesible a la identidad de servicio. En vez de ejecutar el servicio como administrador, se asigna lectura al sujeto específico sobre el objeto específico y se valida que no obtuvo escritura ni acceso a otros secretos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md)) son:

- **“Funciona como administrador” se declara solución** — causa: se ocultó la regla que denegó acceso. Corrección: reproducir sin elevar e identificar capacidad mínima.
- **Se aplica acceso universal** — causa: se confunde disponibilidad con autorización. Corrección: definir quién necesita qué acción y limitar alcance.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- UAC separa el uso cotidiano de un token elevado; aceptar una elevación amplía la autoridad del proceso completo. ([SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [ACL](../a/acl.md), [Autenticación](../a/autenticacion.md), [Autorización](../a/autorizacion.md), [Mínimo privilegio](../m/minimo-privilegio.md), [Objeto](../o/objeto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Apple Platform Security](https://support.apple.com/guide/security/welcome/web) — delimita el contrato técnico que debe cumplirse al explicar autorización como evaluación de identidad, pertenencia, ACL y elevación.
- [The Open Group — File Access Permissions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_05) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Access Control](https://learn.microsoft.com/windows/win32/secauthz/access-control) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Microsoft Learn — How User Account Control works](https://learn.microsoft.com/windows/security/application-security/application-control/user-account-control/how-it-works) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.

---

[↑ Glosario](../../README.md) · [← Elemento semántico](./elemento-semantico.md) · [Elicitación →](./elicitacion.md)
